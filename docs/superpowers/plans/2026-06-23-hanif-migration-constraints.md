# Database Migration Constraints Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Resolve all MySQL column constraints, date format boundaries, enum conversions, duplicate entries, and unique key violations in Fase 3 and Fase 4 migration scripts.

**Architecture:** Modifies the patching script `config.gemini/apply_migration_updates.py` to inject robust text fallbacks, enum normalization, sequential uniqueness generators, and date logic into Jupyter Notebooks. Then executes the notebooks and validates the pickles/databases.

**Tech Stack:** Python, Pandas, Regex, JSON, MySQL

---

### Task 1: Update Fase 3 Patch Transformations in `apply_migration_updates.py`

**Files:**
- Modify: `config.gemini/apply_migration_updates.py:59-431`

- [ ] **Step 1: Replace helper block in `patch_fase_3()`**
  Inject a manual gender map dictionary and normalization helpers inside the `new_helpers` string variable.
  
  ```python
  # ponytail: gender manual lookup table for NULLs
  GENDER_MAP = {
      'ditari@leapsurabaya.sch.id': 'Perempuan',
      'safitriintan801@gmail.com': 'Perempuan',
      'ddoanda@gmail.com': 'Laki laki',
      'raputri.rap@gmail.com': 'Perempuan',
      'gistara.azzahra@gmail.com': 'Perempuan',
      'tedialvianto062@gmail.com': 'Laki laki',
      'nimasbuwana@gmail.com': 'Perempuan',
      'erfiadyntahzanin@gmail.com': 'Perempuan',
      'bryantfrederico@gmail.com': 'Laki laki',
      'ficcaayu@gmail.com': 'Perempuan',
      'graciela@leapsurabaya.sch.id': 'Perempuan',
      '09putrirahayu@gmail.com': 'Perempuan',
      'shaniafebrianaa@gmail.com': 'Perempuan',
      'bibah@gmail.com': 'Perempuan',
      'admin@gmail.com': 'Perempuan',
      'mochamadsaifulr15@gmail.com': 'Laki laki',
      'akin@email.com': 'Laki laki',
      'staffhrd@leapsurabaya.sch.id': 'Laki laki',
      'rini.rahayu@leapsurabaya.sch.id': 'Perempuan',
      'cantikaswasti76@gmail.com': 'Perempuan',
      'hartatik@leapsurabaya.sch.id': 'Perempuan',
      'nisrina.dea@leapsurabaya.sch.id': 'Perempuan',
      'miekepuspita@leapsurabaya.sch.id': 'Perempuan',
      'agung.wijayanto@leapsurabaya.sch.id': 'Laki laki',
      'qorin.rahmaniah@leapsurabaya.sch.id': 'Perempuan',
      'miftakhul.jannah@leapsurabaya.sch.id': 'Perempuan',
      'vivi.wulandari@leapsurabaya.sch.id': 'Perempuan',
      'eka.wahyuni@leapsurabaya.sch.id': 'Perempuan',
      'siti.uswatun@leapsurabaya.sch.id': 'Perempuan',
      'ericasusanto@leapsurabaya.sch.id': 'Perempuan',
      'getari@leapsurabaya.sch.id': 'Perempuan',
      'generalaffair@gmail.com': 'Laki laki'
  }
  ```

- [ ] **Step 2: Replace `pelamar` transformation block**
  Apply gender mapping normalization and fill all `NaN` values in `NOT NULL` columns.
  
  ```python
  # 3. pelamar -> pelamar
  if 'pelamar' in raw_data:
      df_pel = pd.DataFrame(raw_data['pelamar'])
      df_pel['tempat_lahir'] = df_pel['ttl'].apply(extract_place)
      df_pel['tanggal_lahir'] = df_pel['ttl'].apply(extract_date).apply(parse_date)
      
      def map_nikah(x):
          val = str(x).strip().lower()
          if val in ['menikah', 'nikah', 'kawin']: return 'Menikah'
          return 'Belum Menikah'
      
      df_pel['status_pernikahan'] = df_pel['statusnikah'].apply(map_nikah)
      df_pel['penggunaan_laptop'] = df_pel['gunalaptop'].apply(lambda x: 'Pernah' if str(x).strip().lower() in ['pernah', 'ya, pernah', 'ya'] else 'Tidak Pernah')
      df_pel['gaji'] = df_pel['gaji'].apply(clean_currency)
      
      # ponytail: clean and normalize gender
      def clean_gender(row):
          email = str(row.get('email', '')).strip().lower()
          jk = row.get('jk')
          if pd.notna(jk) and str(jk).strip():
              val = str(jk).strip().lower()
              if 'perempuan' in val or val == 'p': return 'Perempuan'
              if 'laki' in val or val == 'l': return 'Laki laki'
          return GENDER_MAP.get(email, 'Laki laki')
      df_pel['jenis_kelamin'] = df_pel.apply(clean_gender, axis=1)
      
      cursor_old.execute("SELECT idusers, email, nama FROM users")
      df_users = pd.DataFrame(cursor_old.fetchall())
      cursor_old.execute("SELECT idpelamar, idusers FROM pelamar_users")
      df_pu = pd.DataFrame(cursor_old.fetchall())
      
      cursor_old.execute("SELECT DISTINCT idusers FROM pekerjaan")
      df_pekerjaan_users = pd.DataFrame(cursor_old.fetchall())
      cursor_old.execute("SELECT DISTINCT idusers FROM pendidikan")
      df_pendidikan_users = pd.DataFrame(cursor_old.fetchall())
      cursor_old.execute("SELECT DISTINCT idusers FROM kursus")
      df_kursus_users = pd.DataFrame(cursor_old.fetchall())
      
      child_users = set(df_pekerjaan_users['idusers']).union(
          set(df_pendidikan_users['idusers'])
      ).union(
          set(df_kursus_users['idusers'])
      )
      
      def clean_str(s):
          if pd.isna(s): return ""
          return str(s).strip().lower()
          
      df_users['email_clean'] = df_users['email'].apply(clean_str)
      df_users['name_clean'] = df_users['nama'].apply(clean_name_without_titles)
      
      df_pel['email_clean'] = df_pel['email'].apply(clean_str)
      df_pel['name_clean'] = df_pel['nama'].apply(clean_name_without_titles)
      
      pu_map = dict(zip(df_pu['idusers'], df_pu['idpelamar']))
      email_to_pelamar = {}
      for _, row in df_pel.iterrows():
          email = row['email_clean']
          if email and email not in email_to_pelamar:
              email_to_pelamar[email] = row['idpelamar']
              
      name_to_pelamar = {}
      for _, row in df_pel.iterrows():
          name = row['name_clean']
          if name and name not in name_to_pelamar:
              name_to_pelamar[name] = row['idpelamar']
              
      user_to_pelamar_id = {}
      unmatched_users = []
      
      for u_id in child_users:
          u_rows = df_users[df_users['idusers'] == u_id]
          if u_rows.empty:
              unmatched_users.append((u_id, "User not in users table", ""))
              continue
          u_row = u_rows.iloc[0]
          u_email = u_row['email_clean']
          u_name = u_row['name_clean']
          
          p_id = pu_map.get(u_id)
          if p_id:
              user_to_pelamar_id[u_id] = p_id
              continue
              
          p_id = email_to_pelamar.get(u_email)
          if p_id:
              user_to_pelamar_id[u_id] = p_id
              continue
              
          p_id = name_to_pelamar.get(u_name)
          if p_id:
              user_to_pelamar_id[u_id] = p_id
              continue
              
          unmatched_users.append((u_id, u_row['nama'], u_row['email']))
          
      df_pel_extended = df_pel.copy()
      for u_id, name, email in unmatched_users:
          # ponytail: fill missing user info
          cleaned_name = name if pd.notna(name) else '-'
          new_row = {
              'idpelamar': u_id,
              'nama': cleaned_name,
              'email': email,
              'idpengajuan': None,
              'jenis_kelamin': GENDER_MAP.get(email, 'Laki laki')
          }
          df_pel_extended = pd.concat([df_pel_extended, pd.DataFrame([new_row])], ignore_index=True)
          
      df_pel_extended['id_pelamar_new'] = df_pel_extended.index + 1
      pelamar_id_map = dict(zip(df_pel_extended['idpelamar'], df_pel_extended['id_pelamar_new']))
      
      final_user_to_pelamar_id = {}
      for u_id in child_users:
          old_p_id = user_to_pelamar_id.get(u_id)
          if old_p_id:
              final_user_to_pelamar_id[u_id] = pelamar_id_map.get(old_p_id)
          else:
              final_user_to_pelamar_id[u_id] = pelamar_id_map.get(u_id)
              
      df_pel_extended['id_pelamar'] = df_pel_extended['id_pelamar_new']
      df_pel_extended['id_pengajuan'] = df_pel_extended['idpengajuan'].astype('Int64')
      
      # ponytail: fill missing NOT NULL columns in pelamar
      df_pel_extended['nama'] = df_pel_extended['nama'].fillna('-')
      df_pel_extended['panggilan'] = df_pel_extended['panggilan'].fillna('-')
      df_pel_extended['tempat_lahir'] = df_pel_extended['tempat_lahir'].fillna('-')
      df_pel_extended['tanggal_lahir'] = df_pel_extended['tanggal_lahir'].fillna(pd.to_datetime('1970-01-01').date())
      df_pel_extended['status_pernikahan'] = df_pel_extended['status_pernikahan'].fillna('Belum Menikah')
      df_pel_extended['penggunaan_laptop'] = df_pel_extended['penggunaan_laptop'].fillna('Tidak Pernah')
      df_pel_extended['gaji'] = df_pel_extended['gaji'].fillna(0)
      
      for text_col in ['alamat', 'domisili', 'wa', 'ig', 'fb', 'sosmed', 'laptop', 'internet', 'kegiatan', 'rencana', 'mobilitas', 'info', 'wfo', 'jenis', 'work', 'ppdk', 'pengalaman', 'wawasan', 'sehat', 'ajar', 'app', 'apps', 'link', 'resign', 'piciq', 'picminat', 'picpribadi']:
          df_pel_extended[text_col] = df_pel_extended[text_col].fillna('-')
      for int_col in ['toefl', 'hasiliq']:
          df_pel_extended[int_col] = df_pel_extended[int_col].fillna(0)
      df_pel_extended['bergabung'] = df_pel_extended['bergabung'].fillna(pd.to_datetime('1970-01-01').date())
      
      mapping = {
          'id_pelamar': 'id_pelamar', 'id_pengajuan': 'id_pengajuan', 'email': 'email_pelamar',
          'nama': 'nama_lengkap', 'panggilan': 'nama_panggilan', 'jenis_kelamin': 'jenis_kelamin',
          'tempat_lahir': 'tempat_lahir', 'tanggal_lahir': 'tanggal_lahir',
          'alamat': 'alamat_ktp', 'domisili': 'alamat_domisili', 'wa': 'nomor_wa',
          'linkedin': 'akun_linkedin', 'ig': 'akun_instagram', 'fb': 'akun_facebook', 
          'sosmed': 'sosmed_lain', 'laptop': 'spesifikasi_laptop', 'internet': 'internet',
          'kegiatan': 'kegiatan_sekarang', 'rencana': 'rencana_karir', 'mobilitas': 'mobilitas',
          'info': 'sumber_info', 'wfo': 'siap_wfo', 'bergabung': 'tanggal_bergabung',
          'jenis': 'kategori_pelamar', 'work': 'riwayat_kerja', 'ppdk': 'riwayat_pendidikan',
          'pengalaman': 'pengalaman_bidang', 'wawasan': 'wawasan', 'sehat': 'riwayat_kesehatan',
          'status_pernikahan': 'status_pernikahan', 'ajar': 'kemampuan_ajar', 'app': 'penguasaan_aplikasi', 
          'apps': 'aplikasi_lainnya', 'penggunaan_laptop': 'penggunaan_laptop', 'toefl': 'skor_toefl',
          'gaji': 'ekspektasi_gaji', 'link': 'tautan_berkas', 'resign': 'alasan_resign',
          'hasiliq': 'skor_iq', 'piciq': 'foto_iq', 'picminat': 'foto_minat', 
          'picpribadi': 'foto_kepribadian', 'created_at': 'created_at'
      }
      transformed_dfs['pelamar'] = df_pel_extended.rename(columns=mapping).reindex(columns=list(mapping.values()))
  ```

- [ ] **Step 3: Replace `pelamar_sekolah`, `pelamar_kursus`, and `progres_pelamar` blocks**
  Fill all missing columns with defaults (`2000` for `tahun_lulus`, `0.0` for `ipk`, `'-'` for strings).
  
  ```python
  # 5. pendidikan -> pelamar_sekolah
  if 'pendidikan' in raw_data:
      df = pd.DataFrame(raw_data['pendidikan'])
      df['tahun'] = df['tahun'].apply(extract_latest_year).fillna(2000).astype(int)
      df['ipk'] = df['ipk'].apply(clean_ipk).fillna(0.0)
      df['id_pelamar'] = df['idusers'].map(final_user_to_pelamar_id).astype('Int64')
      df['id_pelamar_sekolah'] = df['idpendidikan'].apply(extract_int).astype('Int64')
      
      for col in ['sekolah', 'jenjang', 'prodi', 'organisasi']:
          df[col] = df[col].fillna('-')
          
      mapping = {
          'id_pelamar_sekolah': 'id_pelamar_sekolah', 'id_pelamar': 'id_pelamar',
          'sekolah': 'nama_sekolah', 'jenjang': 'jenjang', 'prodi': 'prodi',
          'tahun': 'tahun_lulus', 'ipk': 'ipk', 'organisasi': 'organisasi'
      }
      transformed_dfs['pelamar_sekolah'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

  # 6. kursus -> pelamar_kursus
  if 'kursus' in raw_data:
      df = pd.DataFrame(raw_data['kursus'])
      df['tanggal'] = df['tanggal'].apply(parse_date).fillna(pd.to_datetime('1970-01-01').date())
      df['id_pelamar'] = df['idusers'].map(final_user_to_pelamar_id).astype('Int64')
      df['id_pelamar_kursus'] = df['idkursus'].astype('Int64')
      
      for col in ['nama', 'deskripsi', 'lokasi', 'nosertifikat']:
          df[col] = df[col].fillna('-')
          
      mapping = {
          'id_pelamar_kursus': 'id_pelamar_kursus', 'id_pelamar': 'id_pelamar',
          'nama': 'nama_kursus', 'tanggal': 'tanggal', 'deskripsi': 'deskripsi',
          'lokasi': 'lokasi', 'nosertifikat': 'nomor_sertifikat'
      }
      transformed_dfs['pelamar_kursus'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

  # 7. pelamar_note -> progres_pelamar
  if 'pelamar_note' in raw_data:
      df = pd.DataFrame(raw_data['pelamar_note'])
      df['status'] = df['status'].replace('baru', 'Baru')
      df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
      df['id_progres_pelamar'] = df['idnote'].astype('Int64')
      df['id_user'] = df['idusers']
      
      for col in ['note', 'link', 'pertanyaan']:
          df[col] = df[col].fillna('-')
          
      mapping = {
          'id_progres_pelamar': 'id_progres_pelamar', 'id_pelamar': 'id_pelamar',
          'id_user': 'id_user', 'status': 'status_progres_pelamar',
          'note': 'catatan', 'link': 'tautan_file', 'pertanyaan': 'pertanyaan',
          'created_at': 'created_at'
      }
      transformed_dfs['progres_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
  ```

---

### Task 2: Update Fase 4 Patch Transformations in `apply_migration_updates.py`

**Files:**
- Modify: `config.gemini/apply_migration_updates.py:432-872`

- [ ] **Step 1: Replace `siswa` gender normalization & `tanggal_registrasi` checks**
  Clean `'jkel'` string values and extract registration dates using registration numbers.
  
  ```python
      # 1. siswa -> siswa
      if 'siswa' in raw_data:
          df = pd.DataFrame(raw_data['siswa'])
          df['id_siswa_clean'] = df['idsiswa'].apply(extract_int).astype('Int64')
          df['id_mitra_clean'] = df['idmitra'].apply(extract_int).astype('Int64')
          
          # ponytail: normalize gender enum
          def clean_siswa_gender(x):
              if pd.isna(x): return None
              val = str(x).strip().lower()
              if 'perempuan' in val or val == 'p': return 'Perempuan'
              if 'laki' in val or val == 'l': return 'Laki laki'
              return None
          df['jkel'] = df['jkel'].apply(clean_siswa_gender)
          
          # ponytail: smart extract date from no_induk
          def clean_tgl_daftar(row):
              t = row['tgl_daftar']
              if pd.notna(t) and str(t).strip() not in ('', '-', 'NaT', 'None'):
                  return parse_date_f4(t)
              no_induk = str(row['no_induk']).strip()
              if len(no_induk) >= 4 and no_induk[:4].isdigit():
                  year = int(no_induk[:4])
                  if 2000 <= year <= 2026:
                      # Check if remaining part has non-zero digits
                      remaining = no_induk[4:].replace('0', '').strip()
                      if remaining:
                          return pd.to_datetime(f"{year}-07-01").date()
              return pd.to_datetime("1970-01-01").date()
          df['tgl_daftar'] = df.apply(clean_tgl_daftar, axis=1)
  ```

- [ ] **Step 2: Replace `kursus_siswa` deduplication logic**
  Implement Pandas `groupby().first()` deduplication.
  
  ```python
      # Build kursus_siswa dynamically
      # ... (same SQL query selection code) ...
      df_ks_raw = pd.DataFrame(cursor_old.fetchall())
      
      if not df_ks_raw.empty:
          df_ks_raw['id_siswa'] = df_ks_raw['idsiswa'].apply(extract_int).astype('Int64')
          
          # Redefine parse_date for Fase 4
          def parse_date_f4(date_str):
              if pd.isna(date_str) or not str(date_str).strip(): return None
              s = str(date_str).strip()
              formats = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y']
              for fmt in formats:
                  try: return pd.to_datetime(s, format=fmt).date()
                  except: continue
              try: return pd.to_datetime(s, errors='coerce').date()
              except: return None
              
          df_ks_raw['tanggal_mulai'] = df_ks_raw['tanggal_mulai'].apply(parse_date_f4)
          
          def map_metode(x):
              if pd.isna(x): return 'Offline'
              val = str(x).strip().capitalize()
              if val in ['Online', 'Offline', 'Hybrid']: return val
              return 'Offline'
          df_ks_raw['metode_belajar'] = df_ks_raw['metode_belajar'].apply(map_metode)
          df_ks_raw['status_lulus'] = df_ks_raw['lulus'].apply(lambda x: 1 if pd.notna(x) and float(x) == 1.0 else 0).astype('Int64')
          df_ks_raw['catatan'] = None
          
          # ponytail: group by student & course, taking first non-null properties to fill missing info
          df_ks_raw = df_ks_raw.groupby(['id_siswa', 'id_kursus'], as_index=False).first()
          df_ks_raw = df_ks_raw.reset_index(drop=True)
          df_ks_raw['id_kursus_siswa'] = df_ks_raw.index + 1
          
          transformed_dfs['kursus_siswa'] = df_ks_raw[['id_kursus_siswa', 'id_siswa', 'id_kursus', 'tanggal_mulai', 'metode_belajar', 'status_lulus', 'catatan']]
      else:
          transformed_dfs['kursus_siswa'] = pd.DataFrame(columns=['id_kursus_siswa', 'id_siswa', 'id_kursus', 'tanggal_mulai', 'metode_belajar', 'status_lulus', 'catatan'])
  ```

- [ ] **Step 3: Replace `mitra` sequential uniqueness logic**
  Sort by `created_at` and generate unique codes based on student prefix occurrences.
  
  ```python
      # 4. mitra -> mitra
      if 'mitra' in raw_data:
          df = pd.DataFrame(raw_data['mitra'])
          df['id_mitra_new'] = df['idmitra'].apply(extract_int).astype('Int64')
          
          # ponytail: sorting ascending by created_at and idmitra
          df['_sort_key'] = df['created_at'].fillna(pd.to_datetime('2020-01-01'))
          df = df.sort_values(by=['_sort_key', 'idmitra']).reset_index(drop=True)
          
          # ponytail: extract letters from student numbers, map sequentially to make unique
          prefix_count = {}
          new_kodes = []
          for idx, row in df.iterrows():
              idmitra = row['idmitra']
              cursor_old.execute("SELECT no_induk FROM siswa WHERE idmitra = %s AND no_induk IS NOT NULL AND no_induk != ''", (idmitra,))
              students = cursor_old.fetchall()
              prefixes = []
              for s in students:
                  prefix = re.sub(r'[0-9#-/\s]', '', s['no_induk'])
                  if prefix:
                      prefixes.append(prefix)
              unique_prefixes = list(set(prefixes))
              prefix = unique_prefixes[0] if unique_prefixes else 'M'
              
              count = prefix_count.get(prefix, 0)
              if count == 0:
                  kode = prefix
              else:
                  kode = f"{prefix}{count}"
              prefix_count[prefix] = count + 1
              new_kodes.append(kode)
              
          df['kode_mitra'] = new_kodes
          
          # ponytail: fill missing NOT NULL columns of mitra
          for text_col in ['visimisi', 'program', 'sdm', 'weakness', 'rekomen']:
              df[text_col] = df[text_col].fillna('-')
              
          df['provinsi_id'] = df['provinsi'].map(prov_map).astype('Int64')
          df['kabupaten_id'] = df['kotkab'].map(kab_map).astype('Int64')
          
          bool_cols = ['leapverse', 'kemitraan', 'elsa', 'classin', 'mitraleap']
          for col in bool_cols:
              df[col] = df[col].apply(convert_ya_tidak)
              
          mapping = {
              'id_mitra_new': 'id_mitra', 'nama': 'nama_mitra', 'instansi': 'nama_instansi',
              'namasekolah': 'nama_sekolah', 'lokasi': 'alamat_mitra', 'kepsek': 'nama_pimpinan',
              'cp': 'kontak_mitra', 'status': 'status_mitra', 'visimisi': 'visi_misi',
              'program': 'program_mitra', 'sdm': 'info_sdm', 'weakness': 'info_kelemahan',
              'rekomen': 'rekomendasi_program', 'jenis': 'jenis_mitra', 'provinsi_id': 'provinsi_id',
              'kabupaten_id': 'kabupaten_id', 'jml': 'jumlah_siswa_mitra', 'bidang': 'bidang_usaha',
              'leapverse': 'is_leapverse', 'kemitraan': 'status_kemitraan', 'tahun': 'tahun_bergabung',
              'jeniskemitraan': 'tipe_kerjasama', 'elsa': 'is_elsa', 'classin': 'is_classin',
              'mitraleap': 'is_mitra_leap', 'created_at': 'created_at', 'kode_mitra': 'kode_mitra'
          }
          transformed_dfs['mitra'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
  ```

- [ ] **Step 4: Replace `mitra_progres` mapping**
  Use the generated dictionary to map `id_mitra` correctly.
  
  ```python
      # 5. mitra_note -> mitra_progres
      if 'mitra_note' in raw_data:
          df_note = pd.DataFrame(raw_data['mitra_note'])
          mapping = {
              'id_progres_mitra': 'id_progres_mitra', 'id_mitra': 'id_mitra',
              'catatan_progres_mitra': 'catatan_progres_mitra', 'id_user': 'id_user', 'status_progres_mitra': 'status_progres_mitra',
              'kemitraan_mulai': 'kemitraan_mulai', 'kemitraan_berakhir': 'kemitraan_berakhir', 'created_at': 'created_at'
          }
          if not df_note.empty:
              # ponytail: join using our newly generated map to avoid letter stripping discrepancies
              old_id_to_kode = dict(zip(df['idmitra'], df['kode_mitra']))
              cursor_new.execute("SELECT id_mitra, kode_mitra FROM mitra")
              _mitra_rows = cursor_new.fetchall()
              _mitra_map = {row['kode_mitra']: int(row['id_mitra']) for row in _mitra_rows}
              
              df_note['id_mitra'] = df_note['idmitra'].map(old_id_to_kode).map(_mitra_map).astype('Int64')
              df_note['id_progres_pelamar'] = df_note['idmnote'].apply(extract_int).astype('Int64')
              df_note['id_progres_mitra'] = df_note['id_progres_pelamar']
              df_note['catatan_progres_mitra'] = df_note['note']
              df_note['id_user'] = df_note['idusers']
              
              def map_status_mitra(val):
                  if pd.isna(val): return 'On-going'
                  s = str(val).strip().lower()
                  if s == 'on-going': return 'On-going'
                  if s == 'transfer': return 'Transfer'
                  if s == 'connect': return 'Connect'
                  if s == 'done': return 'Done'
                  return 'On-going'
              df_note['status_progres_mitra'] = df_note['status'].apply(map_status_mitra)
              
              df_note['kemitraan_mulai'] = df_note.apply(
                  lambda r: pd.to_datetime(r['startdate']).date() if pd.notna(r['startdate']) and r['startdate'] is not None
                  else (pd.to_datetime(r['created_at']).date() if pd.notna(r['created_at']) else pd.to_datetime('2023-01-01').date()),
                  axis=1
              )
              df_note['kemitraan_berakhir'] = df_note.apply(
                  lambda r: pd.to_datetime(r['enddate']).date() if pd.notna(r['enddate']) and r['enddate'] is not None
                  else (pd.to_datetime(r['kemitraan_mulai']) + pd.DateOffset(years=1)).date(),
                  axis=1
              )
              transformed_dfs['mitra_progres'] = df_note[list(mapping.values())]
          else:
              transformed_dfs['mitra_progres'] = pd.DataFrame(columns=list(mapping.values()))
  ```

---

### Task 3: Patch Notebooks and Execute Pipeline

**Files:**
- Modify: `fase_3/script_hanif.ipynb` (run)
- Modify: `fase_4/script_hanif.ipynb` (run)

- [ ] **Step 1: Execute patching script**
  Apply changes to the JSON of the notebooks.
  Run: `venv\Scripts\python config.gemini/apply_migration_updates.py`
  Expected: Prints "OK: Fase 3 notebook patched successfully!" and "OK: patch_fase_4 - ..."

- [ ] **Step 2: Run notebooks to regenerate Pickles and CSVs**
  Run the update runner to execute the notebooks in place.
  Run: `venv\Scripts\python update_notebooks.py`
  Expected: Complete run without errors, printing "Update notebooks finished."

---

### Task 4: Run Database Import and Verify Insertion Counts

**Files:**
- Verify: `config.gemini/scratch/check_db_new_counts.py`

- [ ] **Step 1: Re-import clean database schema**
  Restore the migration database to its blank state.
  Run: `venv\Scripts\python config.gemini/import_sql_dump.py`
  Expected: Prints "Database restored successfully!"

- [ ] **Step 2: Run insert handlers to import pickles into database**
  Execute the insert handlers for Fase 3 and Fase 4.
  Run: `venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_3/insert_handler.ipynb`
  Run: `venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_4/insert_handler.ipynb`
  Expected: Complete execution with zero skipped rows due to constraints.

- [ ] **Step 3: Verify counts**
  Verify the final table counts in the target database.
  Run: `$env:PYTHONPATH="."; venv\Scripts\python config.gemini/scratch/check_db_new_counts.py`
  Expected:
  - `pelamar`: 192
  - `pelamar_sekolah`: 53
  - `pelamar_kursus`: 50
  - `progres_pelamar`: 403
  - `rekrutmen_pelamar`: 281
  - `siswa`: 1469
  - `siswa_keluar`: 556
  - `mitra`: 22
