transformed_dfs = {}

# --- HELPER FUNCTIONS ---
def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\d+', str(s))
    return int(nums[0]) if nums else None

def extract_chars(s):
    if pd.isna(s) or not str(s).strip(): return None
    return re.sub(r'\d+', '', str(s)).strip()

def convert_ya_tidak(s):
    if pd.isna(s): return 0
    val = str(s).strip().lower()
    return 1 if val == 'ya' else 0

# --- TRANSFORMATION ---

# 1. siswa -> siswa
# ponytail: normalized gender and fixed dates, resolved duplicate nomor_induk and filled missing NOT NULL columns
if 'siswa' in raw_data:
    # Define parse_date_f4 at the start of the siswa block
    def parse_date_f4(date_str):
        if pd.isna(date_str) or not str(date_str).strip(): return None
        s = str(date_str).strip()
        # Common formats
        formats = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y']
        for fmt in formats:
            try: return pd.to_datetime(s, format=fmt).date()
            except: continue
        try: return pd.to_datetime(s, errors='coerce').date()
        except: return None

    # ponytail: clean WA number, handle slash and limit to 15 characters (digits/plus)
    def clean_wa_number(x):
        if pd.isna(x) or str(x).strip() == '':
            return '-'
        s = str(x).strip()
        if '/' in s:
            s = s.split('/')[0].strip()
        cleaned = ''.join([c for c in s if c.isdigit() or c == '+'])
        if not cleaned:
            return '-'
        return cleaned[:15]

    # ponytail: clean domisili at the first comma and cap at 100 characters
    def clean_domisili(x):
        if pd.isna(x) or str(x).strip() == '':
            return '-'
        s = str(x).strip()
        if ',' in s:
            s = s.split(',')[0].strip()
        return s[:100]

    df = pd.DataFrame(raw_data['siswa'])
    df['id_siswa_clean'] = df['idsiswa'].apply(extract_int).astype('Int64')
    df['id_mitra_clean'] = df['idmitra'].apply(extract_int).astype('Int64')

    # Fetch region tables from both databases to build hierarchical name mappings
    cursor_old.execute("SELECT idprovinsi, nama FROM provinsi")
    df_old_prov = pd.DataFrame(cursor_old.fetchall())
    cursor_new.execute("SELECT id_provinsi, nama_provinsi FROM provinsi")
    df_new_prov = pd.DataFrame(cursor_new.fetchall())

    cursor_old.execute("SELECT idkabupaten, idprovinsi, name FROM kabupaten")
    df_old_kab = pd.DataFrame(cursor_old.fetchall())
    cursor_new.execute("SELECT id_kabupaten, id_provinsi, nama_kabupaten FROM kabupaten")
    df_new_kab = pd.DataFrame(cursor_new.fetchall())

    cursor_old.execute("SELECT idkecamatan, idkabupaten, nama FROM kecamatan")
    df_old_kec = pd.DataFrame(cursor_old.fetchall())
    cursor_new.execute("SELECT id_kecamatan, id_kabupaten, nama_kecamatan FROM kecamatan")
    df_new_kec = pd.DataFrame(cursor_new.fetchall())

    cursor_old.execute("SELECT idkelurahan, idkecamatan, nama FROM kelurahan")
    df_old_kel = pd.DataFrame(cursor_old.fetchall())
    cursor_new.execute("SELECT id_kelurahan, id_kecamatan, nama_kelurahan FROM kelurahan")
    df_new_kel = pd.DataFrame(cursor_new.fetchall())

    def clean_wil_name(s):
        if pd.isna(s): return ""
        s = str(s).strip().lower()
        s = re.sub(r'\b(kabupaten|kab|kota|kecamatan|kec|kelurahan|kel|desa|adm)\b\.?', '', s)
        s = s.replace('\'', '').replace('`', '').replace('-', '').replace(' ', '')
        return s

    df_old_prov['clean'] = df_old_prov['nama'].apply(clean_wil_name)
    df_new_prov['clean'] = df_new_prov['nama_provinsi'].apply(clean_wil_name)
    df_old_kab['clean'] = df_old_kab['name'].apply(clean_wil_name)
    df_new_kab['clean'] = df_new_kab['nama_kabupaten'].apply(clean_wil_name)
    df_old_kec['clean'] = df_old_kec['nama'].apply(clean_wil_name)
    df_new_kec['clean'] = df_new_kec['nama_kecamatan'].apply(clean_wil_name)
    df_old_kel['clean'] = df_old_kel['nama'].apply(clean_wil_name)
    df_new_kel['clean'] = df_new_kel['nama_kelurahan'].apply(clean_wil_name)

    prov_map = {}
    for _, row in df_old_prov.iterrows():
        match = df_new_prov[df_new_prov['clean'] == row['clean']]
        if not match.empty:
            prov_map[row['idprovinsi']] = match.iloc[0]['id_provinsi']

    kab_map = {}
    df_new_kab['key'] = df_new_kab['clean'] + "_" + df_new_kab['id_provinsi'].astype(str)
    for _, row in df_old_kab.iterrows():
        new_prov_id = prov_map.get(row['idprovinsi'])
        if new_prov_id:
            key = row['clean'] + "_" + str(new_prov_id)
            match = df_new_kab[df_new_kab['key'] == key]
            if not match.empty:
                kab_map[row['idkabupaten']] = match.iloc[0]['id_kabupaten']

    kec_map = {}
    df_new_kec['key'] = df_new_kec['clean'] + "_" + df_new_kec['id_kabupaten'].astype(str)
    for _, row in df_old_kec.iterrows():
        new_kab_id = kab_map.get(row['idkabupaten'])
        if new_kab_id:
            key = row['clean'] + "_" + str(new_kab_id)
            match = df_new_kec[df_new_kec['key'] == key]
            if not match.empty:
                kec_map[row['idkecamatan']] = match.iloc[0]['id_kecamatan']

    df_old_kel['new_kec_id'] = df_old_kel['idkecamatan'].map(kec_map)
    df_old_kel_filtered = df_old_kel.dropna(subset=['new_kec_id']).copy()
    df_old_kel_filtered['new_kec_id'] = df_old_kel_filtered['new_kec_id'].astype(int)

    df_merged_kel = pd.merge(
        df_old_kel_filtered,
        df_new_kel,
        left_on=['new_kec_id', 'clean'],
        right_on=['id_kecamatan', 'clean'],
        how='inner'
    )
    kel_map = dict(zip(df_merged_kel['idkelurahan'], df_merged_kel['id_kelurahan']))

    df['id_provinsi'] = df['provinsi'].map(prov_map).astype('Int64')
    df['id_kabupaten'] = df['kabupaten'].map(kab_map).astype('Int64')
    df['id_kecamatan'] = df['kecamatan'].map(kec_map).astype('Int64')
    df['id_kelurahan'] = df['kelurahan'].map(kel_map).astype('Int64')

    # ponytail: build mitra_id_map in-memory using sorted raw mitra data
    df_mitra_raw = pd.DataFrame(raw_data['mitra'])
    df_mitra_raw['_sort_key'] = pd.to_datetime(df_mitra_raw['created_at'], errors='coerce').fillna(pd.to_datetime('2020-01-01'))
    df_mitra_raw = df_mitra_raw.sort_values(by=['_sort_key', 'idmitra']).reset_index(drop=True)
    mitra_id_map = dict(zip(df_mitra_raw['idmitra'], df_mitra_raw.index + 1))

    # ponytail: map id_mitra using the dynamic in-memory mitra_id_map
    df['id_mitra'] = df['idmitra'].map(mitra_id_map).astype('Int64')

    df['domisili'] = df['domisili'].apply(clean_domisili)

    # ponytail: normalize gender enum, fallback to 'Laki laki' to prevent NOT NULL violation
    def normalize_jkel(val):
        if pd.isna(val): return 'Laki laki'
        s = str(val).strip().lower()
        if s in ['perempuan', 'p']:
            return 'Perempuan'
        if s in ['laki', 'l', 'laki laki', 'laki-laki']:
            return 'Laki laki'
        return 'Laki laki'
    df['jkel'] = df['jkel'].apply(normalize_jkel)

    # Clean tgl_daftar using clean_tgl_daftar(row)
    def clean_tgl_daftar(row):
        tgl = parse_date_f4(row.get('tgl_daftar'))
        if pd.notna(tgl) and tgl is not None:
            return tgl
        no_induk = str(row.get('no_induk', '')).strip()
        if len(no_induk) >= 4 and no_induk[0].isdigit():
            year_part = no_induk[:4]
            if year_part.isdigit():
                year_val = int(year_part)
                if 2000 <= year_val <= 2026:
                     rest_part = no_induk[4:]
                     if any(c in '123456789' for c in rest_part):
                         return pd.to_datetime(f"{year_part}-07-01").date()
        return pd.to_datetime('1970-01-01').date()
    df['tgl_daftar'] = df.apply(clean_tgl_daftar, axis=1)

    # Resolve duplicate no_induk
    def fix_no_induk(row):
        val = row.get('no_induk')
        idsiswa = row.get('idsiswa', '')
        if pd.isna(val):
            return '-'
        s = str(val).strip()
        # ponytail: bad/invalid no_induk values → strip
        if s in ('', '-', '#N/A', 'None', 'nan', 'NULL', 'NODATAYET', '0000'):
            return '-'
        # ponytail: specific known-bad no_induk by idsiswa
        if idsiswa == 'S0000522' and s == '00NF3':
            return '-'
        if idsiswa == 'S0000549' and s == '0000':
            return '-'
        return s
    df['no_induk'] = df.apply(fix_no_induk, axis=1)

    seen_no_induk = {}
    new_no_induk_list = []
    for _, row in df.iterrows():
        val = row['no_induk']
        if val not in seen_no_induk:
            seen_no_induk[val] = 0
            new_no_induk_list.append(val)
        else:
            seen_no_induk[val] += 1
            new_no_induk_list.append(f"{val}-{seen_no_induk[val]}")
    df['no_induk'] = new_no_induk_list

    # Normalisasi Agama
    def normalize_agama(a):
        if pd.isna(a) or str(a).strip() == '': return 'Islam'
        a_clean = str(a).strip().lower()
        if 'kristen' in a_clean or 'protestan' in a_clean: return 'Kristen Protestan'
        if 'katholik' in a_clean or 'katolik' in a_clean: return 'Katolik'
        if 'hindu' in a_clean: return 'Hindu'
        if 'budha' in a_clean or 'buddha' in a_clean: return 'Buddha'
        if 'khonghucu' in a_clean or 'konghuchu' in a_clean: return 'Konghucu'
        return 'Islam'
    df['agama'] = df['agama'].apply(normalize_agama)

    mapping = {
        'id_siswa_clean': 'id_siswa', 'tgl_daftar': 'tanggal_registrasi', 'domisili': 'domisili',
        'nama_lengkap': 'nama_lengkap', 'panggilan': 'nama_panggilan', 'jkel': 'jenis_kelamin',
        'nama_sekolah': 'asal_sekolah', 'level_sekolah': 'tingkat_sekolah', 'nama_ortu': 'nama_orang_tua',
        'pekerjaan_ortu': 'pekerjaan_orang_tua', 'tmp_lahir': 'tempat_lahir', 'tgl_lahir': 'tanggal_lahir',
        'no_induk': 'nomor_induk', 'email': 'email',
        'id_provinsi': 'id_provinsi', 'id_kabupaten': 'id_kabupaten', 'id_kecamatan': 'id_kecamatan',
        'id_kelurahan': 'id_kelurahan', 'id_mitra': 'id_mitra', 'nisn': 'nisn', 'nik': 'nik',
        'kewarganegaraan': 'kewarganegaraan', 'agama': 'agama', 'rt': 'rt', 'rw': 'rw',
        'kodepos': 'kode_pos', 'statussiswa': 'status_pendaftaran', 'rekomen': 'rekomendasi',
        'info': 'sumber_info', 'pembayaran': 'metode_pembayaran', 'nama_ayah': 'nama_ayah',
        'pekerjaan_ayah': 'pekerjaan_ayah', 'jenjang_ayah': 'pendidikan_ayah', 
        'penghasilan_ayah': 'penghasilan_ayah', 'nama_ibu': 'nama_ibu', 'penghasilan_ibu': 'penghasilan_ibu',
        'jenjang_ibu': 'pendidikan_ibu', 'nama_wali': 'nama_wali', 'pekerjaan_wali': 'pekerjaan_wali',
        'jenjang_wali': 'pendidikan_wali', 'penghasilan_wali': 'penghasilan_wali',
        'wapeserta': 'wa_siswa', 'wawalmur': 'wa_ortu', 'waadmin': 'wa_administrasi',
        'sts_pengisian': 'status_pengisian', 'bukti': 'path_bukti_bayar',
        'created_at': 'created_at', 'created_bukti': 'tanggal_upload_bukti'
    }

    # Normalisasi Pekerjaan
    def normalize_pekerjaan(p):
        if pd.isna(p) or str(p).strip() in ('', '-', 'NO DATA', '0'): return 'Lainnya'
        s = str(p).strip().lower()
        if 'pegawai_swasta' in s or 'karyawan swasta' in s or 'karyawan' in s: return 'Pegawai Swasta'
        if 'wiraswasta' in s: return 'Wiraswasta'
        if 'aparatur_pejabat_negara' in s or 'tni' in s or 'pns' in s: return 'Aparatur/Pejabat Negara'
        if 'tenaga_kesehatan' in s: return 'Tenaga Kesehatan'
        if 'belum_tidak_bekerja' in s or 'tidak bekerja' in s: return 'Belum/Tidak Bekerja'
        if 'pensiunan' in s: return 'Pensiunan'
        if 'tenaga_pengajar' in s or 'guru' in s or 'dosen' in s: return 'Tenaga Pengajar'
        if 'agama_kepercayaan' in s: return 'Agama dan Kepercayaan'
        if 'pelajar_mahasiswa' in s or 'pelajar' in s: return 'Pelajar/Mahasiswa'
        if 'nelayan' in s: return 'Nelayan'
        if 'pertanian_peternakan' in s or 'tani' in s: return 'Pertanian/Peternakan'
        return 'Lainnya'
        
    df['pekerjaan_ayah'] = df['pekerjaan_ayah'].apply(normalize_pekerjaan)
    df['pekerjaan_wali'] = df['pekerjaan_wali'].apply(normalize_pekerjaan)
    if 'pekerjaan_ortu' in df.columns:
        df['pekerjaan_ortu'] = df['pekerjaan_ortu'].apply(normalize_pekerjaan)
        
    # Normalisasi Penghasilan
    def normalize_penghasilan(p):
        if pd.isna(p) or str(p).strip() in ('', '-', 'NO DATA', '0'): return None
        s = str(p).strip()
        if s in ('kurang_1jt', '1jt_3jt', '3jt_5jt', 'lebih_5jt'): return s
        return None
        
    df['penghasilan_ayah'] = df['penghasilan_ayah'].apply(normalize_penghasilan)
    df['penghasilan_ibu'] = df['penghasilan_ibu'].apply(normalize_penghasilan)
    df['penghasilan_wali'] = df['penghasilan_wali'].apply(normalize_penghasilan)
    
    df_final = df.rename(columns=mapping)
    df_final['pekerjaan_ibu'] = 'Lainnya'
    df_final['deleted_at'] = None

    # ponytail: replace 'NODATAYET' placeholder with '-' across affected text columns
    nodatayet_cols = ['domisili', 'asal_sekolah', 'tingkat_sekolah', 'tempat_lahir', 'nomor_induk']
    for col in nodatayet_cols:
        if col in df_final.columns:
            df_final[col] = df_final[col].replace('NODATAYET', '-')
    
    # Fill empty/NULL target columns with defaults
    cols_to_dash = [
        'nama_lengkap', 'nama_panggilan', 'email',
        'metode_pembayaran', 'status_pendaftaran', 'rekomendasi', 'sumber_info', 'kewarganegaraan',
        'nama_ayah', 'nama_ibu', 'nama_wali',
        'pendidikan_ayah', 'pendidikan_ibu', 'pendidikan_wali',
        'rt', 'rw', 'kode_pos', 'nisn', 'nik',
        'asal_sekolah', 'tingkat_sekolah', 'nama_orang_tua', 'pekerjaan_orang_tua', 'tempat_lahir', 'path_bukti_bayar'
    ]
    for col in cols_to_dash:
        if col in df_final.columns:
            df_final[col] = df_final[col].apply(lambda x: '-' if pd.isna(x) or str(x).strip() == '' else str(x).strip())
        else:
            df_final[col] = '-'
            
    # Fill date and timestamp NOT NULL columns with safe defaults
    if 'tanggal_lahir' in df_final.columns:
        df_final['tanggal_lahir'] = df_final['tanggal_lahir'].apply(lambda x: pd.to_datetime('1970-01-01').date() if pd.isna(x) or x is None else x)
    if 'tanggal_upload_bukti' in df_final.columns:
        df_final['tanggal_upload_bukti'] = df_final['tanggal_upload_bukti'].apply(lambda x: pd.to_datetime('2020-01-01 00:00:00') if pd.isna(x) or x is None else x)

    # ponytail: apply custom WA number cleaning and slicing to avoid MySQL truncation errors
    for col in ['wa_siswa', 'wa_ortu', 'wa_administrasi']:
        if col in df_final.columns:
            df_final[col] = df_final[col].apply(clean_wa_number)
        else:
            df_final[col] = '-'
            
    df_final['agama'] = df_final['agama'].apply(lambda x: 'Islam' if pd.isna(x) or str(x).strip() == '' else str(x).strip())
    
    cols_to_lainnya = ['pekerjaan_ayah', 'pekerjaan_ibu', 'pekerjaan_wali']
    for col in cols_to_lainnya:
        if col in df_final.columns:
            df_final[col] = df_final[col].apply(lambda x: 'Lainnya' if pd.isna(x) or str(x).strip() == '' else str(x).strip())
        else:
            df_final[col] = 'Lainnya'
            
    target_cols = list(dict.fromkeys([c for c in list(mapping.values()) if c in df_final.columns] + ['pekerjaan_ibu', 'deleted_at']))
    # ponytail: remove id_siswa from target_cols to allow MySQL auto-increment to assign IDs automatically
    target_cols = [c for c in target_cols if c != 'id_siswa']
    transformed_dfs['siswa'] = df_final[target_cols]

    # ponytail: build and save student ID mapping (old string ID -> new auto-incremented integer ID based on insertion order)
    student_id_map = dict(zip(df['idsiswa'], df.index + 1))
    df_mapping = pd.DataFrame({
        'idsiswa_lama': df['idsiswa'],
        'id_siswa_baru': df.index + 1
    })
    df_mapping['id_siswa_baru'] = df_mapping['id_siswa_baru'].astype('Int64')
    pd.to_pickle(df_mapping, 'mapping_siswa.pkl')
    # ponytail: also save to fase_5 for teammate scripts
    try:
        import os
        if os.path.exists('../fase_5'):
            pd.to_pickle(df_mapping, '../fase_5/mapping_siswa.pkl')
    except Exception:
        pass
    transformed_dfs['mapping_siswa'] = df_mapping

# Build kursus_siswa dynamically from db_old.jadwal_siswa, db_old.jadwal
# ponytail: query adjusted to select is_keluar and is_lulus; deduplicated on id_siswa and id_kursus
cursor_old.execute("""
    SELECT 
        js.idsiswa,
        j.idpendkursus AS id_kursus,
        js.tgl_mulai AS tanggal_mulai,
        j.mode_belajar AS metode_belajar,
        js.is_keluar,
        js.is_lulus
    FROM jadwal_siswa js
    JOIN jadwal j ON js.idjadwal = j.idjadwal
""")
df_ks_raw = pd.DataFrame(cursor_old.fetchall())

if not df_ks_raw.empty:
    # ponytail: map id_siswa using student_id_map based on auto-increment IDs
    df_ks_raw['id_siswa'] = df_ks_raw['idsiswa'].map(student_id_map).astype('Int64')
    # ponytail: keep id_kursus as string to match db_new.kursus string primary keys (e.g. 'K00001')
    df_ks_raw['id_kursus'] = df_ks_raw['id_kursus'].apply(lambda x: str(x).strip() if pd.notna(x) and str(x).strip() not in ('', 'nan', 'None') else None)
    
    # Deduplicate on ['id_siswa', 'id_kursus'] using Pandas .groupby().first()
    df_ks_raw = df_ks_raw.groupby(['id_siswa', 'id_kursus'], as_index=False).first()

    # ponytail: drop orphan K00017 — tidak ada di tabel kursus db_new (dihapus Afrida)
    df_ks_raw = df_ks_raw[df_ks_raw['id_kursus'] != 'K00017'].reset_index(drop=True)

    df_ks_raw['tanggal_mulai'] = df_ks_raw['tanggal_mulai'].apply(parse_date_f4)
    
    def map_metode(x):
        if pd.isna(x): return 'Offline'
        val = str(x).strip().capitalize()
        if val in ['Online', 'Offline', 'Hybrid']: return val
        return 'Offline'
    df_ks_raw['metode_belajar'] = df_ks_raw['metode_belajar'].apply(map_metode)
    
    # Map status_aktif and status_lulus
    df_ks_raw['status_aktif'] = df_ks_raw['is_keluar'].apply(lambda x: 0 if pd.notna(x) and float(x) > 0 else 1).astype('Int64')
    df_ks_raw['status_lulus'] = df_ks_raw['is_lulus'].apply(lambda x: 1 if pd.notna(x) and float(x) > 0 else 0).astype('Int64')
    df_ks_raw['catatan'] = None
    
    # Reassign id_kursus_siswa sequentially from 1
    df_ks_raw = df_ks_raw.reset_index(drop=True)
    # id_kursus_siswa is auto-increment in db_new, so we exclude it from target columns to let MySQL handle it
    
    transformed_dfs['kursus_siswa'] = df_ks_raw[['id_siswa', 'id_kursus', 'tanggal_mulai', 'metode_belajar', 'status_aktif', 'status_lulus', 'catatan']]
else:
    transformed_dfs['kursus_siswa'] = pd.DataFrame(columns=['id_siswa', 'id_kursus', 'tanggal_mulai', 'metode_belajar', 'status_aktif', 'status_lulus', 'catatan'])

# Build a map from student to course for matching exit courses
student_to_course_map = {}
if 'kursus_siswa' in transformed_dfs:
    for _, row in transformed_dfs['kursus_siswa'].iterrows():
        student_to_course_map[row['id_siswa']] = row['id_kursus']

# Fetch exit tags for exit reason mapping
cursor_old.execute("SELECT idsiswa_keluar, idtag FROM siswa_keluar_tag")
df_skt = pd.DataFrame(cursor_old.fetchall())
if not df_skt.empty:
    df_skt['tag_id_int'] = df_skt['idtag'].apply(extract_int).astype('Int64')
    tag_map = dict(zip(df_skt['idsiswa_keluar'], df_skt['tag_id_int']))
else:
    tag_map = {}

# 3. siswa_keluar -> siswa_keluar
# ponytail: filled empty alasan and parsed date for siswa_keluar
if 'siswa_keluar' in raw_data:
    df = pd.DataFrame(raw_data['siswa_keluar'])
    mapping = {
        'id_siswa': 'id_siswa', 'id_kursus': 'id_kursus',
        'alasan_keluar': 'alasan_keluar', 'tanggal_keluar': 'tanggal_keluar', 'id_tag_keluar': 'id_tag_keluar'
    }
    if not df.empty:
        # Heuristic combined with DB mapping for exit tag
        def detect_tag(row):
            db_tag = tag_map.get(row['idsiswa_keluar'])
            if pd.notna(db_tag) and db_tag is not None:
                return db_tag
            alasan = str(row['alasan']).lower()
            if not alasan.strip() or alasan in ('-', 'none', 'nan', '0', 'tidak ada alasan', 'tidak memberikan alasan'):
                return 11
            if any(w in alasan for w in ['lulus', 'selesai', 'tamat', 'wisuda']):
                return 9
            if any(w in alasan for w in ['jadwal', 'bentrok', 'eksperimen', 'kegiatan', 'les', 'ekskul', 'sekolah', 'waktu', 'jam', 'hari', 'pagi', 'siang', 'sore', 'malam', 'tabrakan', 'kelelahan', 'capek', 'lelah', 'padat', 'ekstrakurikuler', 'tugas sekolah']):
                return 5
            if any(w in alasan for w in ['biaya', 'keuangan', 'dana', 'ekonomi', 'mahal', 'angsuran', 'bayar', 'uang', 'kerjaan', 'pengeluaran', 'pembayaran']):
                return 7
            if any(w in alasan for w in ['domisili', 'pindah', 'luar kota', 'surabaya', 'pulkam', 'mudik', 'jarak', 'jauh', 'alamat', 'kembali ke']):
                return 3
            if any(w in alasan for w in ['program', 'bosan', 'jenuh', 'malas', 'bosan les', 'ingin main', 'tidak mau les', 'capek ngerjain tugas', 'males']):
                return 10
            if any(w in alasan for w in ['akademik', 'kesulitan', 'level', 'tugas', 'nilai', 'pelajaran', 'kurang', 'sulit', 'cepat', 'lambat', 'mengikuti', 'materi', 'susah']):
                return 1
            if any(w in alasan for w in ['guru', 'instruktur', 'pengajar', 'teacher', 'sir', 'miss', 'laoshi', 'cocok', 'metode', 'dosen']):
                return 4
            if any(w in alasan for w in ['aplikasi', 'zoom', 'classin', 'leapverse', 'laptop', 'hp', 'leapsurabaya', 'tech', 'error', 'sistem', 'device', 'gadget']):
                return 2
            if any(w in alasan for w in ['keluarga', 'ortu', 'orang tua', 'mama', 'papa', 'sakit', 'meninggal', 'jaga', 'anak', 'saudara', 'melahirkan', 'hamil']):
                return 6
            return 8

        # ponytail: map id_siswa using student_id_map based on auto-increment IDs
        df['id_siswa'] = df['idsiswa'].map(student_id_map).astype('Int64')
        df['id_kursus'] = df['id_siswa'].map(student_to_course_map)
        df['id_tag_keluar'] = df.apply(detect_tag, axis=1).astype('Int64')
        df['tanggal_keluar'] = df['tanggal'].apply(lambda x: parse_date_f4(x) or pd.to_datetime('1970-01-01').date())
        df['alasan_keluar'] = df['alasan'].apply(lambda x: '-' if pd.isna(x) or str(x).strip() == '' else str(x).strip())
        transformed_dfs['siswa_keluar'] = df[list(mapping.values())]
    else:
        transformed_dfs['siswa_keluar'] = pd.DataFrame(columns=list(mapping.values()))

# 4. mitra -> mitra
# ponytail: sequential kode_mitra fix — old extract_chars caused duplicate 'M' unique key violations
if 'mitra' in raw_data:
    df = pd.DataFrame(raw_data['mitra'])
    df['id_mitra_new'] = df['idmitra'].apply(extract_int).astype('Int64')

    # ponytail: sort ascending by created_at to make code assignment deterministic
    df['_sort_key'] = pd.to_datetime(df['created_at'], errors='coerce').fillna(pd.to_datetime('2020-01-01'))
    df = df.sort_values(by=['_sort_key', 'idmitra']).reset_index(drop=True)

    # ponytail: build unique kode_mitra using single bulk query to avoid N+1 queries
    cursor_old.execute("SELECT idmitra, no_induk FROM siswa WHERE no_induk IS NOT NULL AND no_induk != ''")
    siswa_no_induk = cursor_old.fetchall()
    mitra_to_prefixes = {}
    for s in siswa_no_induk:
        idm = s['idmitra']
        no_induk = s['no_induk']
        prefix = re.sub(r'[0-9#/ 	-]', '', no_induk)
        if prefix:
            mitra_to_prefixes.setdefault(idm, []).append(prefix)

    prefix_count = {}
    new_kodes = []
    for _, row in df.iterrows():
        idmitra = row['idmitra']
        prefixes = list(set(mitra_to_prefixes.get(idmitra, [])))
        base = prefixes[0] if prefixes else 'M'
        count = prefix_count.get(base, 0)
        kode = base if count == 0 else f"{base}{count}"
        prefix_count[base] = count + 1
        new_kodes.append(kode)
    df['kode_mitra'] = new_kodes

    df['provinsi_id'] = df['provinsi'].map(prov_map).astype('Int64')
    df['kabupaten_id'] = df['kotkab'].map(kab_map).astype('Int64')

    bool_cols = ['leapverse', 'kemitraan', 'elsa', 'classin', 'mitraleap']
    for col in bool_cols:
        df[col] = df[col].apply(convert_ya_tidak)

    mapping = {
        'nama': 'nama_mitra', 'instansi': 'nama_instansi',
        'namasekolah': 'nama_sekolah', 'lokasi': 'alamat_mitra', 'kepsek': 'nama_pimpinan',
        'cp': 'kontak_mitra', 'status': 'status_mitra', 'visimisi': 'visi_misi',
        'program': 'program_mitra', 'sdm': 'info_sdm', 'weakness': 'info_kelemahan',
        'rekomen': 'rekomendasi_program', 'jenis': 'jenis_mitra', 'provinsi_id': 'provinsi_id',
        'kabupaten_id': 'kabupaten_id', 'jml': 'jumlah_siswa_mitra', 'bidang': 'bidang_usaha',
        'leapverse': 'is_leapverse', 'kemitraan': 'status_kemitraan', 'tahun': 'tahun_bergabung',
        'jeniskemitraan': 'tipe_kerjasama', 'elsa': 'is_elsa', 'classin': 'is_classin',
        'mitraleap': 'is_mitra_leap', 'created_at': 'created_at', 'kode_mitra': 'kode_mitra'
    }
    df_mitra = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

    # Fillna all text columns with '-'
    text_cols = ['visi_misi', 'program_mitra', 'info_sdm', 'info_kelemahan', 'rekomendasi_program']
    for col in text_cols:
        df_mitra[col] = df_mitra[col].apply(lambda x: '-' if pd.isna(x) or str(x).strip() == '' else str(x).strip())

    # Fillna all other NOT NULL columns with defaults
    df_mitra['jumlah_siswa_mitra'] = df_mitra['jumlah_siswa_mitra'].fillna(0).astype('Int64')
    df_mitra['bidang_usaha'] = df_mitra['bidang_usaha'].apply(lambda x: '-' if pd.isna(x) or str(x).strip() == '' else str(x).strip())
    df_mitra['tipe_kerjasama'] = df_mitra['tipe_kerjasama'].apply(lambda x: 'Perluasan Bisnis' if pd.isna(x) or str(x).strip() == '' else str(x).strip())
    
    # Fill enum and varchar NOT NULL columns with defaults
    df_mitra['status_mitra'] = df_mitra['status_mitra'].apply(lambda x: 'On-going' if pd.isna(x) or str(x).strip() not in ('On-going', 'Done') else str(x).strip())
    df_mitra['jenis_mitra'] = df_mitra['jenis_mitra'].apply(lambda x: 'Lainnya' if pd.isna(x) or str(x).strip() not in ('Corporate', 'Sekolah', 'Lainnya') else str(x).strip())
    df_mitra['nama_mitra'] = df_mitra['nama_mitra'].apply(lambda x: '-' if pd.isna(x) or str(x).strip() == '' else str(x).strip())
    df_mitra['nama_instansi'] = df_mitra['nama_instansi'].apply(lambda x: '-' if pd.isna(x) or str(x).strip() == '' else str(x).strip())

    for col in ['status_kemitraan', 'is_leapverse', 'is_elsa', 'is_classin', 'is_mitra_leap']:
        if col in df_mitra.columns:
            df_mitra[col] = df_mitra[col].fillna(0).astype('Int64')

    df_mitra['tahun_bergabung'] = df_mitra['tahun_bergabung'].fillna(2000).astype('Int64')

    transformed_dfs['mitra'] = df_mitra

    # ponytail: build and save mitra ID mapping (old string/int ID -> new auto-incremented integer ID based on insertion order)
    df_mapping_mitra = pd.DataFrame({
        'idmitra_lama': df['idmitra'],
        'id_mitra_baru': df.index + 1
    })
    df_mapping_mitra['id_mitra_baru'] = df_mapping_mitra['id_mitra_baru'].astype('Int64')
    pd.to_pickle(df_mapping_mitra, 'mapping_mitra.pkl')
    transformed_dfs['mapping_mitra'] = df_mapping_mitra

# 5. mitra_note -> mitra_progres
if 'mitra_note' in raw_data:
    df = pd.DataFrame(raw_data['mitra_note'])
    mapping = {
        'id_mitra': 'id_mitra',
        'catatan_progres_mitra': 'catatan_progres_mitra', 'id_user': 'id_user', 'status_progres_mitra': 'status_progres_mitra',
        'kemitraan_mulai': 'kemitraan_mulai', 'kemitraan_berakhir': 'kemitraan_berakhir', 'created_at': 'created_at'
    }
    if not df.empty:
        # ponytail: map using the dynamic in-memory mitra_id_map (completely offline and robust!)
        df['id_mitra'] = df['idmitra'].map(mitra_id_map).astype('Int64')
        df['catatan_progres_mitra'] = df['note']
        df['id_user'] = df['idusers']
        
        # Safe status mapping
        def map_status_mitra(val):
            if pd.isna(val): return 'On-going'
            s = str(val).strip().lower()
            if s == 'on-going': return 'On-going'
            if s == 'transfer': return 'Transfer'
            if s == 'connect': return 'Connect'
            if s == 'done': return 'Done'
            if s == 'follow up': return 'On-going'
            return 'On-going'
        df['status_progres_mitra'] = df['status'].apply(map_status_mitra)
        
        # NOT NULL constraints fallback
        df['kemitraan_mulai'] = df.apply(
            lambda r: pd.to_datetime(r['startdate']).date() if pd.notna(r['startdate']) and r['startdate'] is not None
            else (pd.to_datetime(r['created_at']).date() if pd.notna(r['created_at']) else pd.to_datetime('2023-01-01').date()),
            axis=1
        )
        df['kemitraan_berakhir'] = df.apply(
            lambda r: pd.to_datetime(r['enddate']).date() if pd.notna(r['enddate']) and r['enddate'] is not None
            else (pd.to_datetime(r['kemitraan_mulai']) + pd.DateOffset(years=1)).date(),
            axis=1
        )
        transformed_dfs['mitra_progres'] = df[list(mapping.values())]
        
        # ponytail: build and save mitra_progres ID mapping
        mitra_progres_id_map = dict(zip(df['idmnote'], df.index + 1))
        df_mapping_mp = pd.DataFrame({
            'idmnote_lama': df['idmnote'],
            'id_progres_mitra_baru': df.index + 1
        })
        df_mapping_mp['id_progres_mitra_baru'] = df_mapping_mp['id_progres_mitra_baru'].astype('Int64')
        pd.to_pickle(df_mapping_mp, 'mapping_mitra_progres.pkl')
        transformed_dfs['mapping_mitra_progres'] = df_mapping_mp
    else:
        transformed_dfs['mitra_progres'] = pd.DataFrame(columns=list(mapping.values()))
        mitra_progres_id_map = {}

# 6. mitra_users -> kemitraan_verifikator
if 'mitra_users' in raw_data:
    df = pd.DataFrame(raw_data['mitra_users'])
    mapping = {
        'id_progres_mitra': 'id_progres_mitra', 'id_user': 'id_user'
    }
    if not df.empty:
        # ponytail: map id_progres_mitra using the dynamic in-memory map
        df['id_progres_mitra'] = df['idmnote'].map(mitra_progres_id_map).astype('Int64')
        df['id_user'] = df['idusers']
        transformed_dfs['kemitraan_verifikator'] = df[list(mapping.values())]
    else:
        transformed_dfs['kemitraan_verifikator'] = pd.DataFrame(columns=list(mapping.values()))

# 7. siswamitra -> siswa_mitra
if 'siswamitra' in raw_data:
    df = pd.DataFrame(raw_data['siswamitra'])
    mapping = {
        'tanggal_daftar': 'tanggal_daftar', 'alamat_domisili': 'alamat_domisili',
        'nama_lengkap': 'nama_lengkap', 'nama_panggilan': 'nama_panggilan', 'jenis_kelamin': 'jenis_kelamin',
        'nama_instansi': 'nama_instansi', 'tingkat_sekolah': 'tingkat_sekolah',
        'pekerjaan_sm': 'pekerjaan_sm', 'tempat_lahir': 'tempat_lahir', 'tanggal_lahir': 'tanggal_lahir',
        'nomor_induk_sm': 'nomor_induk_sm', 'email_sm': 'email_sm', 'wa_sm': 'wa_sm',
        'status_keluar_sm': 'status_keluar_sm', 'id_mitra': 'id_mitra'
    }
    if not df.empty:
        df['id_sm_clean'] = df['idsiswa'].apply(extract_int).astype('Int64')
        df['tanggal_daftar'] = df['tgl_daftar']
        df['alamat_domisili'] = df['domisili']
        df['nama_panggilan'] = df['panggilan']
        df['jenis_kelamin'] = df['jkel']
        df['pekerjaan_sm'] = df['pekerjaan']
        df['tempat_lahir'] = df['tmp_lahir']
        df['tanggal_lahir'] = df['tgl_lahir']
        df['nomor_induk_sm'] = df['no_induk']
        df['email_sm'] = df['email']
        df['wa_sm'] = df['tlp']
        df['status_keluar_sm'] = df['keluar']
        # ponytail: map id_mitra using the dynamic in-memory map
        df['id_mitra'] = df['idmitra'].map(mitra_id_map).astype('Int64')
        df_final = df.rename(columns=mapping)
        df_final['sertifikat_sm'] = None
        transformed_dfs['siswa_mitra'] = df_final[list(mapping.values()) + ['sertifikat_sm']]
        
        # ponytail: build and save siswa_mitra ID mapping
        siswa_mitra_id_map = dict(zip(df['idsiswa'], df.index + 1))
        df_mapping_sm = pd.DataFrame({
            'idsiswa_lama_sm': df['idsiswa'],
            'id_sm_baru': df.index + 1
        })
        df_mapping_sm['id_sm_baru'] = df_mapping_sm['id_sm_baru'].astype('Int64')
        pd.to_pickle(df_mapping_sm, 'mapping_siswa_mitra.pkl')
        transformed_dfs['mapping_siswa_mitra'] = df_mapping_sm
    else:
        transformed_dfs['siswa_mitra'] = pd.DataFrame(columns=list(mapping.values()) + ['sertifikat_sm'])
        siswa_mitra_id_map = {}

# 8. siswa_keluar_mitra -> siswa_mitra_keluar
if 'siswa_keluar_mitra' in raw_data:
    df = pd.DataFrame(raw_data['siswa_keluar_mitra'])
    mapping = {
        'id_sm': 'id_sm',
        'alasan_keluar_sm': 'alasan_keluar_sm', 'tanggal_keluar_sm': 'tanggal_keluar_sm'
    }
    if not df.empty:
        # ponytail: map id_sm using the dynamic in-memory map
        df['id_sm'] = df['idsiswa'].map(siswa_mitra_id_map).astype('Int64')
        df['alasan_keluar_sm'] = df['alasan']
        df['tanggal_keluar_sm'] = df['tanggal']
        transformed_dfs['siswa_mitra_keluar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
    else:
        transformed_dfs['siswa_mitra_keluar'] = pd.DataFrame(columns=list(mapping.values()))

# ponytail: auto-convert datetime and date columns to standard strings to avoid MySQL timestamp conversion errors
for table_name, df_tbl in list(transformed_dfs.items()):
    if df_tbl is not None and not df_tbl.empty:
        for col in df_tbl.columns:
            if pd.api.types.is_datetime64_any_dtype(df_tbl[col]):
                df_tbl[col] = df_tbl[col].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if pd.notna(x) else None)
            else:
                first_val = df_tbl[col].dropna().iloc[0] if not df_tbl[col].dropna().empty else None
                if first_val is not None and hasattr(first_val, 'strftime'):
                    import datetime as dt_mod
                    if isinstance(first_val, dt_mod.datetime) or hasattr(first_val, 'hour'):
                        df_tbl[col] = df_tbl[col].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if pd.notna(x) and hasattr(x, 'strftime') else (str(x) if pd.notna(x) else None))
                    else:
                        df_tbl[col] = df_tbl[col].apply(lambda x: x.strftime('%Y-%m-%d') if pd.notna(x) and hasattr(x, 'strftime') else (str(x) if pd.notna(x) else None))

print(f"✓ Transformasi {len(transformed_dfs)} tabel Fase 4 selesai.")
