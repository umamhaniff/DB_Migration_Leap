import json
import os

def ensure_csv_export_cell(nb):
    csv_source = [
        "# --- EXPORT KE CSV UNTUK VERIFIKASI ---\n",
        "EXPORT_TO_CSV = True  # Ubah ke False jika tidak ingin menghasilkan file CSV\n",
        "\n",
        "if EXPORT_TO_CSV:\n",
        "    import os\n",
        "    import pandas as pd\n",
        "    target_dir = \"../extract/cek_csv\"\n",
        "    os.makedirs(target_dir, exist_ok=True)\n",
        "    for tbl_name, df_tbl in transformed_dfs.items():\n",
        "        csv_path = os.path.join(target_dir, f\"{tbl_name}.csv\")\n",
        "        df_to_save = df_tbl.copy()\n",
        "        \n",
        "        # Clean any float ID/FK columns that contain .0 to pure integers\n",
        "        for col in df_to_save.columns:\n",
        "            col_lower = col.lower()\n",
        "            is_id_col = col_lower.startswith('id_') or col_lower.endswith('_id') or col_lower == 'id' or 'id_' in col_lower or '_id_' in col_lower\n",
        "            if is_id_col:\n",
        "                try:\n",
        "                    df_to_save[col] = pd.to_numeric(df_to_save[col], errors='coerce').round().astype('Int64')\n",
        "                except Exception:\n",
        "                    pass\n",
        "        \n",
        "        # Fix: Convert any StringDtype to object for clean serialization\n",
        "        for col in df_to_save.columns:\n",
        "            if str(df_to_save[col].dtype) in ['string', 'string[python]']:\n",
        "                df_to_save[col] = df_to_save[col].astype(object)\n",
        "        df_to_save.to_csv(csv_path, index=False)\n",
        "        print(f\"💾 Tabel {tbl_name} diekspor ke {csv_path} ({len(df_tbl)} baris)\")\n",
        "else:\n",
        "    print(\"ℹ️ Ekspor ke CSV dinonaktifkan.\")"
    ]
    
    found_idx = -1
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code" and "EXPORT_TO_CSV" in "".join(cell["source"]):
            found_idx = i
            break
            
    if found_idx >= 0:
        nb["cells"][found_idx]["source"] = csv_source
    else:
        csv_cell = {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": csv_source
        }
        nb["cells"].append(csv_cell)

def patch_fase_3():
    path = "fase_3/script_hanif.ipynb"
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    new_transformations = """# 3. pelamar -> pelamar
if 'pelamar' in raw_data:
    df = pd.DataFrame(raw_data['pelamar'])
    df['tempat_lahir'] = df['ttl'].apply(extract_place)
    df['tanggal_lahir'] = df['ttl'].apply(extract_date).apply(parse_date)
    
    # enum & data cleaning
    def map_nikah(x):
        val = str(x).strip().lower()
        if val in ['menikah', 'nikah', 'kawin']: return 'Menikah'
        if val in ['lajang', 'belum', 'single', 'x', 'none', 'nan', '', '0']: return 'Belum Menikah'
        return 'Belum Menikah'
    
    df['status_pernikahan'] = df['statusnikah'].apply(map_nikah)
    df['penggunaan_laptop'] = df['gunalaptop'].apply(lambda x: 'Pernah' if str(x).strip().lower() in ['pernah', 'ya, pernah', 'ya'] else 'Tidak Pernah')
    df['gaji'] = df['gaji'].apply(clean_currency)
    
    # Generate integer ID auto-increment mapping
    df = df.reset_index()
    df['id_pelamar_new'] = df['index'] + 1
    pelamar_id_map = dict(zip(df['idpelamar'], df['id_pelamar_new']))
    df['id_pelamar'] = df['id_pelamar_new']
    
    # Cast id_pengajuan to Int64 to prevent decimal formats in CSV
    df['id_pengajuan'] = df['idpengajuan'].astype('Int64')
    
    mapping = {
        'id_pelamar': 'id_pelamar', 'id_pengajuan': 'id_pengajuan', 'email': 'email_pelamar',
        'nama': 'nama_lengkap', 'panggilan': 'nama_panggilan', 'jk': 'jenis_kelamin',
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
    transformed_dfs['pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# Build mapping from idusers -> id_pelamar using advanced matching (Nama & Email)
cursor_old.execute("SELECT idusers, email, nama FROM users")
df_users = pd.DataFrame(cursor_old.fetchall())
cursor_old.execute("SELECT idpelamar, idusers FROM pelamar_users")
df_pu = pd.DataFrame(cursor_old.fetchall())

def clean_str(s):
    if pd.isna(s): return ""
    return str(s).strip().lower()

def clean_name(s):
    if pd.isna(s): return ""
    s = str(s).strip().lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

df_users['email_clean'] = df_users['email'].apply(clean_str)
df_users['name_clean'] = df_users['nama'].apply(clean_name)

df_pel_temp = pd.DataFrame(raw_data['pelamar'])
df_pel_temp['email_clean'] = df_pel_temp['email'].apply(clean_str)
df_pel_temp['name_clean'] = df_pel_temp['nama'].apply(clean_name)
df_pel_temp['id_pelamar_new'] = df_pel_temp.index + 1
temp_pelamar_id_map = dict(zip(df_pel_temp['idpelamar'], df_pel_temp['id_pelamar_new']))

user_to_pelamar_id = {}
# 1. Map via pelamar_users
for _, row in df_pu.iterrows():
    u_id = row['idusers']
    p_id = row['idpelamar']
    if p_id in temp_pelamar_id_map:
        user_to_pelamar_id[u_id] = temp_pelamar_id_map[p_id]

# 2. Map via Email
email_to_new_id = dict(zip(df_pel_temp[df_pel_temp['email_clean'] != '']['email_clean'], df_pel_temp[df_pel_temp['email_clean'] != '']['id_pelamar_new']))
for _, row in df_users.iterrows():
    u_id = row['idusers']
    email = row['email_clean']
    if u_id not in user_to_pelamar_id and email in email_to_new_id:
        user_to_pelamar_id[u_id] = email_to_new_id[email]

# 3. Map via Name
name_to_new_id = dict(zip(df_pel_temp[df_pel_temp['name_clean'] != '']['name_clean'], df_pel_temp[df_pel_temp['name_clean'] != '']['id_pelamar_new']))
for _, row in df_users.iterrows():
    u_id = row['idusers']
    name = row['name_clean']
    if u_id not in user_to_pelamar_id and name in name_to_new_id:
        user_to_pelamar_id[u_id] = name_to_new_id[name]

# 4. pekerjaan -> pelamar_kerja
if 'pekerjaan' in raw_data:
    df = pd.DataFrame(raw_data['pekerjaan'])
    df['id_pelamar'] = df['idusers'].map(user_to_pelamar_id).astype('Int64')
    mapping = {
        'idpekerjaan': 'id_pelamar_kerja', 'id_pelamar': 'id_pelamar',
        'namaperusahaan': 'nama_perusahaan', 'periode': 'periode', 'jabatan': 'jabatan',
        'jobdesk': 'deskripsi_kerja'
    }
    transformed_dfs['pelamar_kerja'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 5. pendidikan -> pelamar_sekolah
if 'pendidikan' in raw_data:
    df = pd.DataFrame(raw_data['pendidikan'])
    df['tahun'] = df['tahun'].apply(extract_latest_year)
    df['ipk'] = df['ipk'].apply(clean_ipk)
    df['id_pelamar'] = df['idusers'].map(user_to_pelamar_id).astype('Int64')
    mapping = {
        'idpendidikan': 'id_pelamar_sekolah', 'id_pelamar': 'id_pelamar',
        'sekolah': 'nama_sekolah', 'jenjang': 'jenjang', 'prodi': 'prodi',
        'tahun': 'tahun_lulus', 'ipk': 'ipk', 'organisasi': 'organisasi'
    }
    transformed_dfs['pelamar_sekolah'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 6. kursus -> pelamar_kursus
if 'kursus' in raw_data:
    df = pd.DataFrame(raw_data['kursus'])
    df['tanggal'] = df['tanggal'].apply(parse_date)
    df['id_pelamar'] = df['idusers'].map(user_to_pelamar_id).astype('Int64')
    mapping = {
        'idkursus': 'id_pelamar_kursus', 'id_pelamar': 'id_pelamar',
        'nama': 'nama_kursus', 'tanggal': 'tanggal', 'deskripsi': 'deskripsi',
        'lokasi': 'lokasi', 'nosertifikat': 'nomor_sertifikat'
    }
    transformed_dfs['pelamar_kursus'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 7. pelamar_note -> progres_pelamar
if 'pelamar_note' in raw_data:
    df = pd.DataFrame(raw_data['pelamar_note'])
    df['status'] = df['status'].replace('baru', 'Baru')
    df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
    mapping = {
        'idnote': 'id_progres_pelamar', 'id_pelamar': 'id_pelamar',
        'idusers': 'id_user', 'status': 'status_progres_pelamar',
        'note': 'catatan', 'link': 'tautan_file', 'pertanyaan': 'pertanyaan',
        'created_at': 'created_at'
    }
    transformed_dfs['progres_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 8. pelamar_users -> rekrutmen_pelamar
if 'pelamar_users' in raw_data:
    df = pd.DataFrame(raw_data['pelamar_users'])
    df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
    mapping = {
        'idassign': 'id_rekrutmen', 'id_pelamar': 'id_pelamar', 'idusers': 'id_user'
    }
    transformed_dfs['rekrutmen_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

print(f"OK: Transformasi {len(transformed_dfs)} tabel Fase 3 selesai.")"""

    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "# 3. pelamar -> pelamar" in "".join(cell["source"]):
            source_lines = cell["source"]
            target_idx = -1
            for idx, line in enumerate(source_lines):
                if "# 3. pelamar -> pelamar" in line:
                    target_idx = idx
                    break
            
            if target_idx != -1:
                new_lines = source_lines[:target_idx]
                for line in new_transformations.split("\n"):
                    new_lines.append(line + "\n")
                if new_lines[-1] == "\n": new_lines.pop()
                cell["source"] = new_lines
                patched = True
                break

    if patched:
        ensure_csv_export_cell(nb)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 3 notebook patched successfully!")
    else:
        print("Error: Target cell in Fase 3 notebook not found.")

def patch_fase_4():
    path = "fase_4/script_hanif.ipynb"
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    new_transformations = """# 1. siswa -> siswa
if 'siswa' in raw_data:
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
        s = re.sub(r'\\b(kabupaten|kab|kota|kecamatan|kec|kelurahan|kel|desa|adm)\\b\\.?', '', s)
        s = s.replace('\\'', '').replace('`', '').replace('-', ' ')
        s = re.sub(r'\\s+', ' ', s).strip()
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
    df['id_mitra'] = df['id_mitra_clean'].astype('Int64')
    
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
        'no_induk': 'nomor_induk', 'email': 'email', 'idcalon': 'id_calon',
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
        'created_bukti': 'tanggal_upload_bukti'
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
    target_cols = [c for c in list(mapping.values()) if c in df_final.columns] + ['pekerjaan_ibu', 'deleted_at']
    transformed_dfs['siswa'] = df_final[target_cols]

# 2. kursus_siswa
# Build kursus_siswa dynamically from db_old.jadwal_siswa & db_old.jadwal
cursor_old.execute(\"\"\"
    SELECT 
        js.idsiswa,
        j.idpendkursus AS id_kursus,
        js.tgl_mulai AS tanggal_mulai,
        j.mode_belajar AS metode_belajar,
        js.is_keluar,
        js.is_lulus
    FROM jadwal_siswa js
    JOIN jadwal j ON js.idjadwal = j.idjadwal
\"\"\")
df_ks_raw = pd.DataFrame(cursor_old.fetchall())

if not df_ks_raw.empty:
    df_ks_raw['id_siswa'] = df_ks_raw['idsiswa'].apply(extract_int).astype('Int64')
    
    # Redefine parse_date for Fase 4
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
        
    df_ks_raw['tanggal_mulai'] = df_ks_raw['tanggal_mulai'].apply(parse_date_f4)
    
    def map_metode(x):
        if pd.isna(x): return 'Offline'
        val = str(x).strip().capitalize()
        if val in ['Online', 'Offline', 'Hybrid']: return val
        return 'Offline'
    df_ks_raw['metode_belajar'] = df_ks_raw['metode_belajar'].apply(map_metode)
    df_ks_raw['status_aktif'] = df_ks_raw['is_keluar'].apply(lambda x: 0 if float(x) > 0 else 1).astype('Int64')
    df_ks_raw['status_lulus'] = df_ks_raw['is_lulus'].apply(lambda x: 1 if float(x) > 0 else 0).astype('Int64')
    df_ks_raw['catatan'] = None
    
    df_ks_raw = df_ks_raw.reset_index()
    df_ks_raw['id_kursus_siswa'] = df_ks_raw['index'] + 1
    
    transformed_dfs['kursus_siswa'] = df_ks_raw[['id_kursus_siswa', 'id_siswa', 'id_kursus', 'tanggal_mulai', 'metode_belajar', 'status_aktif', 'status_lulus', 'catatan']]
else:
    transformed_dfs['kursus_siswa'] = pd.DataFrame(columns=['id_kursus_siswa', 'id_siswa', 'id_kursus', 'tanggal_mulai', 'metode_belajar', 'status_aktif', 'status_lulus', 'catatan'])

# Build a map from student to course for matching exit courses
student_to_course_map = {}
if 'kursus_siswa' in transformed_dfs:
    for _, row in transformed_dfs['kursus_siswa'].iterrows():
        student_to_course_map[row['id_siswa']] = row['id_kursus']

# Fetch exit tags for exit reason mapping
cursor_old.execute("SELECT idsiswa_keluar, idsiswa, idtag FROM siswa_keluar_tag")
df_skt = pd.DataFrame(cursor_old.fetchall())
if not df_skt.empty:
    df_skt['tag_id_int'] = df_skt['idtag'].apply(extract_int).astype('Int64')
    tag_map = dict(zip(df_skt['idsiswa_keluar'], df_skt['tag_id_int']))
else:
    tag_map = {}

# 3. siswa_keluar -> siswa_keluar
if 'siswa_keluar' in raw_data:
    df = pd.DataFrame(raw_data['siswa_keluar'])
    mapping = {
        'id_keluar': 'id_keluar', 'id_siswa': 'id_siswa', 'id_kursus': 'id_kursus',
        'alasan_keluar': 'alasan_keluar', 'tanggal_keluar': 'tanggal_keluar', 'id_tag_keluar': 'id_tag_keluar'
    }
    if not df.empty:
        df['id_siswa'] = df['idsiswa'].apply(extract_int).astype('Int64')
        df['id_keluar'] = df['idsiswa_keluar'].apply(extract_int).astype('Int64')
        df['id_kursus'] = df['id_siswa'].map(student_to_course_map)
        df['id_tag_keluar'] = df['idsiswa_keluar'].map(tag_map).fillna(8).astype('Int64')
        df['tanggal_keluar'] = df['tanggal']
        df['alasan_keluar'] = df['alasan']
        transformed_dfs['siswa_keluar'] = df[list(mapping.values())]
    else:
        transformed_dfs['siswa_keluar'] = pd.DataFrame(columns=list(mapping.values()))

# 4. mitra -> mitra
if 'mitra' in raw_data:
    df = pd.DataFrame(raw_data['mitra'])
    df['id_mitra_new'] = df['idmitra'].apply(extract_int).astype('Int64')
    df['kode_mitra'] = df['idmitra'].apply(extract_chars)
    
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

# 5. mitra_note -> mitra_progres
if 'mitra_note' in raw_data:
    df = pd.DataFrame(raw_data['mitra_note'])
    mapping = {
        'id_progres_mitra': 'id_progres_mitra', 'id_mitra': 'id_mitra',
        'catatan_progres_mitra': 'catatan_progres_mitra', 'id_user': 'id_user', 'status_progres_mitra': 'status_progres_mitra',
        'kemitraan_mulai': 'kemitraan_mulai', 'kemitraan_berakhir': 'kemitraan_berakhir', 'created_at': 'created_at'
    }
    if not df.empty:
        df['id_mitra_clean'] = df['idmitra'].apply(extract_int).astype('Int64')
        df['id_progres_mitra'] = df['idmnote'].apply(extract_int).astype('Int64')
        df['id_mitra'] = df['id_mitra_clean']
        df['catatan_progres_mitra'] = df['note']
        df['id_user'] = df['idusers']
        df['status_progres_mitra'] = df['status']
        df['kemitraan_mulai'] = df['startdate']
        df['kemitraan_berakhir'] = df['enddate']
        transformed_dfs['mitra_progres'] = df[list(mapping.values())]
    else:
        transformed_dfs['mitra_progres'] = pd.DataFrame(columns=list(mapping.values()))

# 6. mitra_users -> kemitraan_verifikator
if 'mitra_users' in raw_data:
    df = pd.DataFrame(raw_data['mitra_users'])
    mapping = {
        'id_kemitraan': 'id_kemitraan', 'id_progres_mitra': 'id_progres_mitra', 'id_user': 'id_user'
    }
    if not df.empty:
        df['id_kemitraan_clean'] = df['idmusers'].apply(extract_int).astype('Int64')
        df['id_progres_mitra_clean'] = df['idmnote'].apply(extract_int).astype('Int64')
        df['id_kemitraan'] = df['id_kemitraan_clean']
        df['id_progres_mitra'] = df['id_progres_mitra_clean']
        df['id_user'] = df['idusers']
        transformed_dfs['kemitraan_verifikator'] = df[list(mapping.values())]
    else:
        transformed_dfs['kemitraan_verifikator'] = pd.DataFrame(columns=list(mapping.values()))

# 7. siswamitra -> siswa_mitra
if 'siswamitra' in raw_data:
    df = pd.DataFrame(raw_data['siswamitra'])
    mapping = {
        'id_sm': 'id_sm', 'tanggal_daftar': 'tanggal_daftar', 'alamat_domisili': 'alamat_domisili',
        'nama_lengkap': 'nama_lengkap', 'nama_panggilan': 'nama_panggilan', 'jenis_kelamin': 'jenis_kelamin',
        'nama_instansi': 'nama_instansi', 'tingkat_sekolah': 'tingkat_sekolah',
        'pekerjaan_sm': 'pekerjaan_sm', 'tempat_lahir': 'tempat_lahir', 'tanggal_lahir': 'tanggal_lahir',
        'nomor_induk_sm': 'nomor_induk_sm', 'email_sm': 'email_sm', 'wa_sm': 'wa_sm',
        'status_keluar_sm': 'status_keluar_sm', 'id_mitra': 'id_mitra'
    }
    if not df.empty:
        df['id_sm_clean'] = df['idsiswa'].apply(extract_int).astype('Int64')
        df['id_mitra_clean'] = df['idmitra'].apply(extract_int).astype('Int64')
        df['id_sm'] = df['id_sm_clean']
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
        df['id_mitra'] = df['id_mitra_clean']
        df_final = df.rename(columns=mapping)
        df_final['sertifikat_sm'] = None
        transformed_dfs['siswa_mitra'] = df_final[list(mapping.values()) + ['sertifikat_sm']]
    else:
        transformed_dfs['siswa_mitra'] = pd.DataFrame(columns=list(mapping.values()) + ['sertifikat_sm'])

# 8. siswa_keluar_mitra -> siswa_mitra_keluar
if 'siswa_keluar_mitra' in raw_data:
    df = pd.DataFrame(raw_data['siswa_keluar_mitra'])
    mapping = {
        'id_sm_keluar': 'id_sm_keluar', 'id_sm': 'id_sm',
        'alasan_keluar_sm': 'alasan_keluar_sm', 'tanggal_keluar_sm': 'tanggal_keluar_sm'
    }
    if not df.empty:
        df['id_sm_keluar_clean'] = df['idsiswa_keluar'].apply(extract_int).astype('Int64')
        df['id_sm_clean'] = df['idsiswa'].apply(extract_int).astype('Int64')
        df['id_sm_keluar'] = df['id_sm_keluar_clean']
        df['id_sm'] = df['id_sm_clean']
        df['alasan_keluar_sm'] = df['alasan']
        df['tanggal_keluar_sm'] = df['tanggal']
        transformed_dfs['siswa_mitra_keluar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
    else:
        transformed_dfs['siswa_mitra_keluar'] = pd.DataFrame(columns=list(mapping.values()))

print(f"✓ Transformasi {len(transformed_dfs)} tabel Fase 4 selesai.")"""

    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "# 1. siswa -> siswa" in "".join(cell["source"]):
            source_lines = cell["source"]
            target_idx = -1
            for idx, line in enumerate(source_lines):
                if "# 1. siswa -> siswa" in line:
                    target_idx = idx
                    break
            
            if target_idx != -1:
                new_lines = source_lines[:target_idx]
                for line in new_transformations.split("\n"):
                    new_lines.append(line + "\n")
                if new_lines[-1] == "\n": new_lines.pop()
                cell["source"] = new_lines
                patched = True
                break

    if patched:
        ensure_csv_export_cell(nb)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 4 notebook patched successfully!")
    else:
        print("Error: Target cell in Fase 4 notebook not found.")

def patch_fase_5():
    path = "fase_5/script_hanif.ipynb"
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    new_transformations = """# Helper extract_int in Fase 5
def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\\d+', str(s))
    return int(nums[0]) if nums else None

# 7. rapor -> rapor_siswa
if 'rapor' in raw_data:
    df = pd.DataFrame(raw_data['rapor'])
    
    # Generate integer ID auto-increment mapping
    df = df.reset_index()
    df['id_rapor_siswa_new'] = df['index'] + 1
    rapor_id_map = dict(zip(df['idrapor'], df['id_rapor_siswa_new']))
    df['id_rapor_siswa'] = df['id_rapor_siswa_new']
    
    df['id_siswa_clean'] = df['idsiswa'].apply(extract_int).astype('Int64')
    df['id_jadwal_clean'] = df['idjadwal'].apply(extract_int).astype('Int64')
    
    # Map idp_nilai string (e.g. 'P00745') to new parameter_nilai auto-increment ID
    cursor_old.execute("SELECT idp_nilai FROM parameter_nilai ORDER BY idp_nilai")
    param_rows = cursor_old.fetchall()
    param_map = {}
    for idx, row in enumerate(param_rows):
        if isinstance(row, dict):
            param_map[row['idp_nilai']] = idx + 1
        elif isinstance(row, (list, tuple)):
            param_map[row[0]] = idx + 1
    df['id_parameter_nilai'] = df['idp_nilai'].map(param_map).astype('Int64')
    
    mapping = {
        'id_rapor_siswa': 'id_rapor_siswa', 'id_jadwal_clean': 'id_jadwal', 'id_siswa_clean': 'id_siswa',
        'tanggal': 'tanggal_input', 'id_parameter_nilai': 'id_parameter_nilai', 'nilai': 'final_result'
    }
    transformed_dfs['rapor_siswa'] = df.rename(columns=mapping)[list(mapping.values())]

# 8. file_rapor_siswa -> rapor_siswa_file
if 'file_rapor_siswa' in raw_data and 'rapor_siswa' in transformed_dfs:
    df = pd.DataFrame(raw_data['file_rapor_siswa'])
    
    # Generate integer ID auto-increment mapping for file table
    df = df.reset_index()
    df['id_rapor_siswa_file_new'] = df['index'] + 1
    file_id_map = dict(zip(df['idfile'], df['id_rapor_siswa_file_new']))
    df['id_rapor_siswa_file'] = df['id_rapor_siswa_file_new']
    
    # Fetch old idrapor string and map it to new id_rapor_siswa integer
    df_rapor_old = pd.DataFrame(raw_data['rapor'])[['idsiswa', 'idjadwal', 'idrapor']].drop_duplicates(subset=['idsiswa', 'idjadwal'])
    df = df.merge(df_rapor_old, on=['idsiswa', 'idjadwal'], how='left')
    df['id_rapor_siswa'] = df['idrapor'].map(rapor_id_map).astype('Int64')
    
    mapping = {
        'id_rapor_siswa_file': 'id_rapor_siswa_file', 'id_rapor_siswa': 'id_rapor_siswa', 'path': 'file_rapor_path'
    }
    transformed_dfs['rapor_siswa_file'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 9. history_rapor -> rapor_lacak
if 'history_rapor' in raw_data and 'rapor_siswa_file' in transformed_dfs:
    df = pd.DataFrame(raw_data['history_rapor'])
    df['status'] = df['status'].replace({'Terkirim': 'Terkirim', 'Gagal': 'Gagal'})
    
    df_file_old = pd.DataFrame(raw_data['file_rapor_siswa'])[['idfile', 'idsiswa', 'idjadwal']]
    df_file_old['id_rapor_siswa_file'] = df_file_old['idfile'].map(file_id_map).astype('Int64')
    
    df['id_siswa_clean'] = df['idsiswa'].apply(extract_int).astype('Int64')
    df['id_jadwal_clean'] = df['idjadwal'].apply(extract_int).astype('Int64')
    
    df_merged = df.merge(df_file_old[['idsiswa', 'idjadwal', 'id_rapor_siswa_file']], on=['idsiswa', 'idjadwal'], how='left')
    df_merged['id_rapor_siswa_file'] = df_merged['id_rapor_siswa_file'].astype('Int64')
    df_merged['id_rapor_lacak'] = df_merged['idhistori'].apply(extract_int).astype('Int64')
    
    mapping = {
        'id_rapor_lacak': 'id_rapor_lacak', 'id_siswa_clean': 'id_siswa',
        'id_jadwal_clean': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'
    }
    transformed_dfs['rapor_lacak'] = df_merged.rename(columns=mapping)[list(mapping.values()) + ['id_rapor_siswa_file']]

print(f"OK: Transformasi {len(transformed_dfs)} tabel Fase 5 selesai.")"""

    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "# 7. rapor -> rapor_siswa" in "".join(cell["source"]):
            source_lines = cell["source"]
            target_idx = -1
            for idx, line in enumerate(source_lines):
                if "# 7. rapor -> rapor_siswa" in line:
                    target_idx = idx
                    break
            
            if target_idx != -1:
                new_lines = source_lines[:target_idx]
                for line in new_transformations.split("\n"):
                    new_lines.append(line + "\n")
                if new_lines[-1] == "\n": new_lines.pop()
                cell["source"] = new_lines
                patched = True
                break

    if patched:
        ensure_csv_export_cell(nb)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 5 notebook patched successfully!")
    else:
        print("Error: Target cell in Fase 5 notebook not found.")

if __name__ == "__main__":
    patch_fase_3()
    patch_fase_4()
    patch_fase_5()
