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
        "                non_nulls = df_to_save[col].dropna()\n",
        "                if not non_nulls.empty:\n",
        "                    try:\n",
        "                        pd.to_numeric(non_nulls, errors='raise')\n",
        "                        df_to_save[col] = pd.to_numeric(df_to_save[col], errors='coerce').round().astype('Int64')\n",
        "                    except (ValueError, TypeError):\n",
        "                        pass\n",
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

    new_helpers = """# --- HELPER FUNCTIONS ---
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

def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\\\\d+', str(s))
    return int(nums[0]) if nums else None

def extract_place(ttl):
    if pd.isna(ttl) or not str(ttl).strip(): return None
    s = str(ttl).strip()
    if ',' in s:
        return s.split(',')[0].strip()
    match = re.search(r'^[^0-9]+', s)
    return match.group(0).strip() if match else s

def extract_date(ttl):
    if pd.isna(ttl) or not str(ttl).strip(): return None
    s = str(ttl).strip()
    if ',' in s:
        parts = s.split(',')
        if len(parts) > 1: return parts[1].strip()
    match = re.search(r'(\\\\d.*)', s)
    return match.group(1).strip() if match else None

def parse_date(date_str):
    if pd.isna(date_str): return None
    s = str(date_str).strip()
    if s in ('', '-', '0', 'nan', 'NaN'): return None
    
    # First normalize day-of-month ranges: "27 - 29 Mei 2023" -> "27 Mei 2023"
    s = re.sub(r'\\\\b(\\\\d{1,2})\\\\s*-\\\\s*\\\\d{1,2}\\\\b', r'\\\\1', s)
    
    # Try to see if it's a month-level range: e.g. "29 September - 6 Oktober 2021"
    parts = re.split(r'\\\\s+-\\\\s+|\\\\s+(?:sd|s/d|dan|s\\\\.d\\\\.)\\\\s+', s, flags=re.IGNORECASE)
    if len(parts) > 1:
        part1 = parts[0].strip()
        part2 = parts[1].strip()
        if not re.search(r'\\\\b\\\\d{4}\\\\b', part1):
            year_match = re.search(r'\\\\b\\\\d{4}\\\\b', part2)
            if year_match:
                part1 = part1 + " " + year_match.group(0)
        s = part1
        
    months_id_to_en = {
        'januari': 'January', 'februari': 'February', 'maret': 'March', 'april': 'April',
        'mei': 'May', 'juni': 'June', 'juli': 'July', 'agustus': 'August',
        'september': 'September', 'oktober': 'October', 'november': 'November', 'desember': 'December',
        'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April', 'jun': 'June',
        'jul': 'July', 'agu': 'August', 'agst': 'August', 'sep': 'September', 'okt': 'October', 'nov': 'November', 'des': 'December'
    }
    
    s = s.replace('-', ' ').replace('/', ' ').replace('.', '').strip()
    s = re.sub(r'\\\\s+', ' ', s)
    
    for id_m, en_m in months_id_to_en.items():
        s = re.sub(rf'\\\\b{id_m}\\\\b', en_m, s, flags=re.IGNORECASE)
        
    year_match = re.search(r'\\\\b\\\\d{4}\\\\b', s)
    if not year_match:
        s = s + " 2023"
        
    formats = [
        '%d %B %Y', '%d %b %Y', '%B %Y', '%b %Y',
        '%d %m %Y', '%m %d %Y', '%Y %m %d',
        '%d %m %y', '%m %d %y', '%y %m %d'
    ]
    for fmt in formats:
        try:
            return pd.to_datetime(s, format=fmt).date()
        except:
            continue
            
    try:
        res = pd.to_datetime(s, errors='coerce')
        if pd.notna(res):
            return res.date()
    except:
        pass
        
    return None

def extract_latest_year(tahun_str):
    if pd.isna(tahun_str) or not str(tahun_str).strip(): return None
    years = re.findall(r'\\\\d{4}', str(tahun_str))
    if years:
        return max(map(int, years))
    return None

def clean_currency(val):
    if pd.isna(val): return 0
    s = str(val).strip()
    nums = re.sub(r'[^0-9]', '', s)
    return int(nums) if nums else 0

def clean_ipk(val):
    if pd.isna(val): return 0.0
    s = str(val).strip().replace(',', '.')
    match = re.search(r'\\\\d+\\\\.?\\\\d*', s)
    if match:
        try: return float(match.group(0))
        except: return 0.0
    return 0.0

def clean_name_without_titles(s):
    if pd.isna(s): return ""
    s = str(s).strip().lower()
    if ',' in s: 
        s = s.split(',')[0]
    titles = [
        r'\\\\bs\\\\.?\\\\s*pd\\\\b', r'\\\\bm\\\\.?\\\\s*pd\\\\b', r'\\\\bs\\\\.?\\\\s*s\\\\b', r'\\\\bs\\\\.?\\\\s*t\\\\b', 
        r'\\\\bs\\\\.?\\\\s*hum\\\\b', r'\\\\bs\\\\.?\\\\s*kom\\\\b', r'\\\\ba\\\\.?\\\\s*md\\\\b', r'\\\\bs\\\\.?\\\\s*e\\\\b', 
        r'\\\\bm\\\\.?\\\\s*m\\\\b', r'\\\\bdr\\\\b', r'\\\\bdra\\\\b', r'\\\\bdrs\\\\b', r'\\\\bprof\\\\b',
        r'\\\\bpsi\\\\b', r'\\\\bs\\\\.?\\\\s*psi\\\\b'
    ]
    for title in titles:
        s = re.sub(title, '', s, flags=re.IGNORECASE)
    s = re.sub(r'[^a-z0-9]', '', s)
    return s"""

    new_transformations = """# --- TRANSFORMATION ---

# 1. pengajuan -> pengajuan_karyawan
if 'pengajuan' in raw_data:
    df = pd.DataFrame(raw_data['pengajuan'])
    df['status'] = df['status'].replace('Sudah Direvisi', 'Sudah Revisi')
    df['id_pengajuan_new'] = df.index + 1
    pengajuan_id_map = dict(zip(df['idpengajuan'], df['id_pengajuan_new']))
    
    # ponytail: build and save pengajuan_karyawan ID mapping (old ID -> new auto-incremented ID)
    df_mapping_peng = pd.DataFrame({
        'idpengajuan_lama': df['idpengajuan'],
        'id_pengajuan_baru': df['id_pengajuan_new']
    })
    df_mapping_peng['id_pengajuan_baru'] = df_mapping_peng['id_pengajuan_baru'].astype('Int64')
    pd.to_pickle(df_mapping_peng, 'mapping_pengajuan_karyawan.pkl')
    transformed_dfs['mapping_pengajuan_karyawan'] = df_mapping_peng
    
    df['id_user'] = df['idusers']
    mapping = {
        'id_user': 'id_user', 'keterangan': 'posisi',
        'jumlah': 'jumlah', 'syarat': 'syarat', 'pertanyaan': 'pertanyaan',
        'alur': 'alur_seleksi', 'test': 'daftar_tes', 'status': 'status',
        'created_at': 'created_at'
    }
    transformed_dfs['pengajuan_karyawan'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 2. histori_pengajuan -> histori_pengajuan
if 'histori_pengajuan' in raw_data:
    df = pd.DataFrame(raw_data['histori_pengajuan'])
    df['status'] = df['status'].replace('Sudah Direvisi', 'Sudah Revisi')
    df['id_pengajuan'] = df['idpengajuan'].map(pengajuan_id_map).astype('Int64')
    mapping = {
        'id_pengajuan': 'id_pengajuan',
        'status': 'status_verifikasi_pengajuan', 'catatan': 'catatan',
        'created_at': 'created_at'
    }
    transformed_dfs['histori_pengajuan'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

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
    
    # ponytail: build and save pelamar ID mapping (old ID -> new auto-incremented ID)
    df_mapping_pel = pd.DataFrame({
        'idpelamar_lama': df_pel_extended['idpelamar'],
        'id_pelamar_baru': df_pel_extended['id_pelamar_new']
    })
    df_mapping_pel['id_pelamar_baru'] = df_mapping_pel['id_pelamar_baru'].astype('Int64')
    pd.to_pickle(df_mapping_pel, 'mapping_pelamar.pkl')
    transformed_dfs['mapping_pelamar'] = df_mapping_pel
    
    final_user_to_pelamar_id = {}
    for u_id in child_users:
        old_p_id = user_to_pelamar_id.get(u_id)
        if old_p_id:
            final_user_to_pelamar_id[u_id] = pelamar_id_map.get(old_p_id)
        else:
            final_user_to_pelamar_id[u_id] = pelamar_id_map.get(u_id)
            
    df_pel_extended['id_pelamar'] = df_pel_extended['id_pelamar_new']
    df_pel_extended['id_pengajuan'] = df_pel_extended['idpengajuan'].map(pengajuan_id_map).astype('Int64')
    
    # ponytail: fill missing NOT NULL columns in pelamar
    df_pel_extended['email'] = df_pel_extended['email'].fillna('-')
    df_pel_extended['nama'] = df_pel_extended['nama'].fillna('-')
    df_pel_extended['panggilan'] = df_pel_extended['panggilan'].fillna('-')
    df_pel_extended['tempat_lahir'] = df_pel_extended['tempat_lahir'].fillna('-')
    df_pel_extended['tanggal_lahir'] = df_pel_extended['tanggal_lahir'].fillna(pd.to_datetime('1970-01-01').date())
    df_pel_extended['status_pernikahan'] = df_pel_extended['status_pernikahan'].fillna('Belum Menikah')
    df_pel_extended['penggunaan_laptop'] = df_pel_extended['penggunaan_laptop'].fillna('Tidak Pernah')
    df_pel_extended['gaji'] = df_pel_extended['gaji'].fillna(0)
    
    for text_col in ['alamat', 'domisili', 'wa', 'ig', 'fb', 'sosmed', 'laptop', 'internet', 'kegiatan', 'rencana', 'mobilitas', 'info', 'wfo', 'jenis', 'work', 'ppdk', 'pengalaman', 'wawasan', 'sehat', 'ajar', 'app', 'apps', 'link', 'resign', 'piciq', 'picminat', 'picpribadi']:
        df_pel_extended[text_col] = df_pel_extended[text_col].fillna('-')
    # ponytail: clean and convert integer columns to prevent string values like 'asd'
    df_pel_extended['toefl'] = pd.to_numeric(df_pel_extended['toefl'], errors='coerce').fillna(0).astype(int)
    df_pel_extended['hasiliq'] = pd.to_numeric(df_pel_extended['hasiliq'], errors='coerce').fillna(0).astype(int)
    df_pel_extended['bergabung'] = df_pel_extended['bergabung'].fillna(pd.to_datetime('1970-01-01').date())
    # ponytail: use safe modern date for created_at to avoid MySQL TIMESTAMP out of range errors due to timezone conversion
    df_pel_extended['created_at'] = df_pel_extended['created_at'].fillna(pd.to_datetime('2020-01-01 00:00:00'))
    
    mapping = {
        'id_pengajuan': 'id_pengajuan', 'email': 'email_pelamar',
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

# 4. pekerjaan -> pelamar_kerja
if 'pekerjaan' in raw_data:
    df = pd.DataFrame(raw_data['pekerjaan'])
    df['id_pelamar'] = df['idusers'].map(final_user_to_pelamar_id).astype('Int64')
    mapping = {
        'id_pelamar': 'id_pelamar',
        'namaperusahaan': 'nama_perusahaan', 'periode': 'periode', 'jabatan': 'jabatan',
        'jobdesk': 'deskripsi_kerja'
    }
    transformed_dfs['pelamar_kerja'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 5. pendidikan -> pelamar_sekolah
if 'pendidikan' in raw_data:
    df = pd.DataFrame(raw_data['pendidikan'])
    df['tahun'] = df['tahun'].apply(extract_latest_year).fillna(2000).astype(int)
    df['ipk'] = df['ipk'].apply(clean_ipk).fillna(0.0)
    df['id_pelamar'] = df['idusers'].map(final_user_to_pelamar_id).astype('Int64')
    
    for col in ['sekolah', 'jenjang', 'prodi', 'organisasi']:
        df[col] = df[col].fillna('-')
        
    mapping = {
        'id_pelamar': 'id_pelamar',
        'sekolah': 'nama_sekolah', 'jenjang': 'jenjang', 'prodi': 'prodi',
        'tahun': 'tahun_lulus', 'ipk': 'ipk', 'organisasi': 'organisasi'
    }
    transformed_dfs['pelamar_sekolah'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 6. kursus -> pelamar_kursus
if 'kursus' in raw_data:
    df = pd.DataFrame(raw_data['kursus'])
    df['tanggal'] = df['tanggal'].apply(parse_date).fillna(pd.to_datetime('1970-01-01').date())
    df['id_pelamar'] = df['idusers'].map(final_user_to_pelamar_id).astype('Int64')
    
    for col in ['nama', 'deskripsi', 'lokasi', 'nosertifikat']:
        df[col] = df[col].fillna('-')
        
    mapping = {
        'id_pelamar': 'id_pelamar',
        'nama': 'nama_kursus', 'tanggal': 'tanggal', 'deskripsi': 'deskripsi',
        'lokasi': 'lokasi', 'nosertifikat': 'nomor_sertifikat'
    }
    transformed_dfs['pelamar_kursus'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 7. pelamar_note -> progres_pelamar
if 'pelamar_note' in raw_data:
    df = pd.DataFrame(raw_data['pelamar_note'])
    df['status'] = df['status'].replace('baru', 'Baru')
    df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
    df['id_user'] = df['idusers']
    
    for col in ['note', 'link', 'pertanyaan']:
        df[col] = df[col].fillna('-')
        
    mapping = {
        'id_pelamar': 'id_pelamar',
        'id_user': 'id_user', 'status': 'status_progres_pelamar',
        'note': 'catatan', 'link': 'tautan_file', 'pertanyaan': 'pertanyaan',
        'created_at': 'created_at'
    }
    transformed_dfs['progres_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 8. pelamar_users -> rekrutmen_pelamar
if 'pelamar_users' in raw_data:
    df = pd.DataFrame(raw_data['pelamar_users'])
    df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
    df['id_user'] = df['idusers']
    mapping = {
        'id_pelamar': 'id_pelamar', 'id_user': 'id_user'
    }
    transformed_dfs['rekrutmen_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

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

print(f"OK: Transformasi {len(transformed_dfs)} tabel Fase 3 selesai.")"""

    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "# --- HELPER FUNCTIONS ---" in "".join(cell["source"]):
            new_lines = ["transformed_dfs = {}\n\n"]
            for line in new_helpers.split("\n"):
                new_lines.append(line + "\n")
            new_lines.append("\n")
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
        s = re.sub(r'\\b(kabupaten|kab|kota|kecamatan|kec|kelurahan|kel|desa|adm)\\b\\.?', '', s)
        s = s.replace('\\'', '').replace('`', '').replace('-', '').replace(' ', '')
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
        if pd.isna(val):
            return f"TEMP-{row['idsiswa']}"
        s = str(val).strip()
        if s in ('', '-', '#N/A', 'None', 'nan', 'NULL'):
            return f"TEMP-{row['idsiswa']}"
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
    
    # Fill empty/NULL target columns with defaults
    cols_to_dash = [
        'nama_lengkap', 'nama_panggilan', 'email',
        'metode_pembayaran', 'status_pendaftaran', 'rekomendasi', 'sumber_info', 'kewarganegaraan',
        'nama_ayah', 'nama_ibu', 'nama_wali',
        'pendidikan_ayah', 'pendidikan_ibu', 'pendidikan_wali',
        'rt', 'rw', 'kode_pos', 'nisn', 'nik'
    ]
    for col in cols_to_dash:
        if col in df_final.columns:
            df_final[col] = df_final[col].apply(lambda x: '-' if pd.isna(x) or str(x).strip() == '' else str(x).strip())
        else:
            df_final[col] = '-'
            
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
    transformed_dfs['mapping_siswa'] = df_mapping

# Build kursus_siswa dynamically from db_old.jadwal_siswa, db_old.jadwal
# ponytail: query adjusted to select is_keluar and is_lulus; deduplicated on id_siswa and id_kursus
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
    # ponytail: map id_siswa using student_id_map based on auto-increment IDs
    df_ks_raw['id_siswa'] = df_ks_raw['idsiswa'].map(student_id_map).astype('Int64')
    # ponytail: keep id_kursus as string to match db_new.kursus string primary keys (e.g. 'K00001')
    df_ks_raw['id_kursus'] = df_ks_raw['id_kursus'].apply(lambda x: str(x).strip() if pd.notna(x) and str(x).strip() not in ('', 'nan', 'None') else None)
    
    # Deduplicate on ['id_siswa', 'id_kursus'] using Pandas .groupby().first()
    df_ks_raw = df_ks_raw.groupby(['id_siswa', 'id_kursus'], as_index=False).first()
    
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
    df_ks_raw['id_kursus_siswa'] = df_ks_raw.index + 1
    
    transformed_dfs['kursus_siswa'] = df_ks_raw[['id_kursus_siswa', 'id_siswa', 'id_kursus', 'tanggal_mulai', 'metode_belajar', 'status_aktif', 'status_lulus', 'catatan']]
else:
    transformed_dfs['kursus_siswa'] = pd.DataFrame(columns=['id_kursus_siswa', 'id_siswa', 'id_kursus', 'tanggal_mulai', 'metode_belajar', 'status_aktif', 'status_lulus', 'catatan'])

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

    # ponytail: build unique kode_mitra from student no_induk alpha prefix, sequential if duplicate
    prefix_count = {}
    new_kodes = []
    for _, row in df.iterrows():
        idmitra = row['idmitra']
        cursor_old.execute("SELECT no_induk FROM siswa WHERE idmitra = %s AND no_induk IS NOT NULL AND no_induk != ''", (idmitra,))
        students = cursor_old.fetchall()
        prefixes = []
        for s in students:
            prefix = re.sub(r'[0-9#/ \t-]', '', s['no_induk'])
            if prefix:
                prefixes.append(prefix)
        unique_prefixes = list(set(prefixes))
        base = unique_prefixes[0] if unique_prefixes else 'M'
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
        # Patch verification cell to avoid KeyError on removed PK id_mitra
        for cell in nb["cells"]:
            if cell["cell_type"] == "code" and "# 3.1.2 Output Pengecekan Kolom Spesifik" in "".join(cell["source"]):
                source = "".join(cell["source"])
                source = source.replace("transformed_dfs['mitra'][['nama_mitra', 'id_mitra',", "transformed_dfs['mitra'][['nama_mitra', 'nama_instansi',")
                cell["source"] = [line + "\n" for line in source.split("\n")]
                if cell["source"] and cell["source"][-1] == "\n":
                    cell["source"].pop()
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

# ponytail: load student ID auto-increment mapping from Fase 4
import os
student_id_map = {}
mapping_path = '../fase_4/mapping_siswa.pkl'
if os.path.exists(mapping_path):
    df_map = pd.read_pickle(mapping_path)
    student_id_map = dict(zip(df_map['idsiswa_lama'], df_map['id_siswa_baru']))

def map_student_id(idsiswa_val):
    if pd.isna(idsiswa_val): return None
    val_str = str(idsiswa_val).strip()
    if val_str in student_id_map:
        return student_id_map[val_str]
    return extract_int(val_str)

# 7. rapor -> rapor_siswa
if 'rapor' in raw_data:
    df = pd.DataFrame(raw_data['rapor'])
    
    # Generate integer ID auto-increment mapping
    df = df.reset_index()
    df['id_rapor_siswa_new'] = df['index'] + 1
    rapor_id_map = dict(zip(df['idrapor'], df['id_rapor_siswa_new']))
    
    # ponytail: build and save rapor_siswa ID mapping
    df_mapping_rs = pd.DataFrame({
        'idrapor_lama': df['idrapor'],
        'id_rapor_siswa_baru': df['id_rapor_siswa_new']
    })
    df_mapping_rs['id_rapor_siswa_baru'] = df_mapping_rs['id_rapor_siswa_baru'].astype('Int64')
    pd.to_pickle(df_mapping_rs, 'mapping_rapor_siswa.pkl')
    transformed_dfs['mapping_rapor_siswa'] = df_mapping_rs
    
    # ponytail: map id_siswa using the loaded student ID mapping based on auto-increment IDs
    df['id_siswa_clean'] = df['idsiswa'].apply(map_student_id).astype('Int64')
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
        'id_jadwal_clean': 'id_jadwal', 'id_siswa_clean': 'id_siswa',
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
    
    # ponytail: build and save rapor_siswa_file ID mapping
    df_mapping_rsf = pd.DataFrame({
        'idfile_lama': df['idfile'],
        'id_rapor_siswa_file_baru': df['id_rapor_siswa_file_new']
    })
    df_mapping_rsf['id_rapor_siswa_file_baru'] = df_mapping_rsf['id_rapor_siswa_file_baru'].astype('Int64')
    pd.to_pickle(df_mapping_rsf, 'mapping_rapor_siswa_file.pkl')
    transformed_dfs['mapping_rapor_siswa_file'] = df_mapping_rsf
    
    # Fetch old idrapor string and map it to new id_rapor_siswa integer
    df_rapor_old = pd.DataFrame(raw_data['rapor'])[['idsiswa', 'idjadwal', 'idrapor']].drop_duplicates(subset=['idsiswa', 'idjadwal'])
    df = df.merge(df_rapor_old, on=['idsiswa', 'idjadwal'], how='left')
    df['id_rapor_siswa'] = df['idrapor'].map(rapor_id_map).astype('Int64')
    
    mapping = {
        'id_rapor_siswa': 'id_rapor_siswa', 'path': 'file_rapor_path'
    }
    transformed_dfs['rapor_siswa_file'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 9. history_rapor -> rapor_lacak
if 'history_rapor' in raw_data and 'rapor_siswa_file' in transformed_dfs:
    df = pd.DataFrame(raw_data['history_rapor'])
    df['status'] = df['status'].replace({'Terkirim': 'Terkirim', 'Gagal': 'Gagal'})
    
    df_file_old = pd.DataFrame(raw_data['file_rapor_siswa'])[['idfile', 'idsiswa', 'idjadwal']]
    df_file_old['id_rapor_siswa_file'] = df_file_old['idfile'].map(file_id_map).astype('Int64')
    
    # ponytail: map id_siswa using the loaded student ID mapping based on auto-increment IDs
    df['id_siswa_clean'] = df['idsiswa'].apply(map_student_id).astype('Int64')
    df['id_jadwal_clean'] = df['idjadwal'].apply(extract_int).astype('Int64')
    
    df_merged = df.merge(df_file_old[['idsiswa', 'idjadwal', 'id_rapor_siswa_file']], on=['idsiswa', 'idjadwal'], how='left')
    df_merged['id_rapor_siswa_file'] = df_merged['id_rapor_siswa_file'].astype('Int64')
    
    mapping = {
        'id_siswa_clean': 'id_siswa',
        'id_jadwal_clean': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'
    }
    transformed_dfs['rapor_lacak'] = df_merged.rename(columns=mapping)[list(mapping.values()) + ['id_rapor_siswa_file']]

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
        # Patch verification cell to avoid KeyError on removed PK id_rapor_siswa
        for cell in nb["cells"]:
            if cell["cell_type"] == "code" and "# 3.1.2 Output Pengecekan Kolom Spesifik" in "".join(cell["source"]):
                source = "".join(cell["source"])
                source = source.replace("transformed_dfs['rapor_siswa'][['id_rapor_siswa',", "transformed_dfs['rapor_siswa'][['id_siswa',")
                cell["source"] = [line + "\n" for line in source.split("\n")]
                if cell["source"] and cell["source"][-1] == "\n":
                    cell["source"].pop()
        ensure_csv_export_cell(nb)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 5 notebook patched successfully!")
    else:
        print("Error: Target cell in Fase 5 notebook not found.")

def patch_fase_3_insert_handler():
    path = "fase_3/insert_handler.ipynb"
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "tables_to_insert_ordered" in "".join(cell["source"]):
            source = "".join(cell["source"])
            old_order = """    # --- BLOK A: PENDAFTARAN & SDM (Karya Hanif) ---
    'pelamar',                  # Induk data pelamar kerja/kursus
    'pelamar_kerja',            # Detail pelamar posisi kerja
    'pelamar_sekolah',          # Riwayat sekolah pelamar
    'pelamar_kursus',           # Riwayat kursus pelamar
    'progres_pelamar',          # Log catatan tahapan seleksi
    'rekrutmen_pelamar',        # Keputusan akhir rekrutmen pelamar
    'pengajuan_karyawan',       # Form pengajuan penambahan staff baru
    'histori_pengajuan',        # Log alur persetujuan pengajuan staff"""
            
            new_order = """    # --- BLOK A: PENDAFTARAN & SDM (Karya Hanif) ---
    'pengajuan_karyawan',       # Form pengajuan penambahan staff baru
    'histori_pengajuan',        # Log alur persetujuan pengajuan staff
    'pelamar',                  # Induk data pelamar kerja/kursus
    'pelamar_kerja',            # Detail pelamar posisi kerja
    'pelamar_sekolah',          # Riwayat sekolah pelamar
    'pelamar_kursus',           # Riwayat kursus pelamar
    'progres_pelamar',          # Log catatan tahapan seleksi
    'rekrutmen_pelamar',        # Keputusan akhir rekrutmen pelamar"""
            
            if old_order in source:
                source = source.replace(old_order, new_order)
                cell["source"] = [line + "\n" for line in source.split("\n")]
                if cell["source"][-1] == "\n": cell["source"].pop()
                patched = True
                break
            
    if patched:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 3 insert_handler patched successfully!")
    else:
        print("Error: Target cell in Fase 3 insert_handler not found or already patched.")

def patch_fase_5_rapor_urutan():
    """
    Tambah kolom `urutan` ke transform rapor_format (block #1) dan
    rapor_format_sub (block #2) di fase_5/script_hanif.ipynb.

    Strategi:
    - rapor_format  : merge LEFT ke rapor_format_import.csv via kolom `judul_rapor`
    - rapor_format_sub : merge LEFT ke rapor_format_sub_import.csv via
      `sub_judul_rapor` + `id_rapor_format` (F00001 -> digit int, matched
      terhadap id_rapor_format numerik dari old DB)

    Jalankan notebook dari direktori fase_5/ agar path CSV relatif valid.
    """
    path = "fase_5/script_hanif.ipynb"
    nb = json.load(open(path, "r", encoding="utf-8"))

    MATCH_KEY = "# 1. format_rapor -> rapor_format"

    old_block_1 = (
        "# 1. format_rapor -> rapor_format\n"
        "if 'format_rapor' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_rapor'])\n"
        "    mapping = {\n"
        "        'idformat_rapor': 'id_rapor_format',\n"
        "        'idpendkursus': 'id_kursus', 'title': 'judul_rapor'\n"
        "    }\n"
        "    transformed_dfs['rapor_format'] = df.rename(columns=mapping)[list(mapping.values())]\n"
    )

    new_block_1 = (
        "# 1. format_rapor -> rapor_format (+ urutan dari import CSV)\n"
        "if 'format_rapor' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_rapor'])\n"
        "    mapping = {\n"
        "        'idformat_rapor': 'id_rapor_format',\n"
        "        'idpendkursus': 'id_kursus', 'title': 'judul_rapor'\n"
        "    }\n"
        "    df_rf = df.rename(columns=mapping)[list(mapping.values())]\n"
        "    # Merge kolom urutan dari rapor_format_import.csv (sudah diurutkan manual)\n"
        "    df_urutan_rf = pd.read_csv('rapor_format_import.csv')[['judul_rapor', 'urutan']]\n"
        "    df_rf = df_rf.merge(df_urutan_rf, on='judul_rapor', how='left')\n"
        "    df_rf['urutan'] = df_rf['urutan'].astype('Int64')  # cegah float karena NaN\n"
        "    transformed_dfs['rapor_format'] = df_rf\n"
    )

    old_block_2 = (
        "# 2. format_rapor_detil -> rapor_format_sub\n"
        "if 'format_rapor_detil' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_rapor_detil'])\n"
        "    mapping = {\n"
        "        'idformat_rd': 'id_rapor_format_sub',\n"
        "        'idformat_rapor': 'id_rapor_format', 'subtitle': 'sub_judul_rapor'\n"
        "    }\n"
        "    transformed_dfs['rapor_format_sub'] = df.rename(columns=mapping)[list(mapping.values())]\n"
    )

    new_block_2 = (
        "# 2. format_rapor_detil_rumus -> rapor_format_sub (+ urutan dari import CSV)\n"
        "if 'format_rapor_detil' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_rapor_detil'])\n"
        "    mapping = {\n"
        "        'idformat_rd': 'id_rapor_format_sub',\n"
        "        'idformat_rapor': 'id_rapor_format', 'subtitle': 'sub_judul_rapor'\n"
        "    }\n"
        "    df_rfs = df.rename(columns=mapping)[list(mapping.values())]\n"
        "    # Merge kolom urutan dari rapor_format_sub_import.csv (sudah diurutkan manual)\n"
        "    # id_rapor_format di import CSV: format 'F00001' -> ambil digit -> int untuk join\n"
        "    df_urutan_rfs = pd.read_csv('rapor_format_sub_import.csv')\n"
        "    df_urutan_rfs['_rf_key'] = df_urutan_rfs['id_rapor_format'].str.extract(r'(\\d+)', expand=False).astype(int)\n"
        "    df_urutan_rfs = df_urutan_rfs[['_rf_key', 'sub_judul_rapor', 'urutan']]\n"
        "    df_rfs = df_rfs.copy()\n"
        "    df_rfs['_rf_key'] = pd.to_numeric(df_rfs['id_rapor_format'], errors='coerce').astype('Int64')\n"
        "    df_urutan_rfs['_rf_key'] = df_urutan_rfs['_rf_key'].astype('Int64')\n"
        "    df_rfs = df_rfs.merge(df_urutan_rfs, on=['_rf_key', 'sub_judul_rapor'], how='left').drop(columns=['_rf_key'])\n"
        "    df_rfs['urutan'] = df_rfs['urutan'].astype('Int64')  # cegah float karena NaN\n"
        "    transformed_dfs['rapor_format_sub'] = df_rfs\n"
    )

    old_block_3 = (
        "# 3. format_rapor_rumus -> rapor_format_formula\n"
        "if 'format_rapor_rumus' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_rapor_rumus'])\n"
        "    mapping = {\n"
        "        'idfrr': 'id_rapor_format_formula',\n"
        "        'idformat_rapor': 'id_rapor_format', 'param_operator': 'logika_operator'\n"
        "    }\n"
        "    transformed_dfs['rapor_format_formula'] = df.rename(columns=mapping)[list(mapping.values())]\n"
    )

    new_block_3 = (
        "# 3. format_rapor_rumus -> rapor_format_formula\n"
        "if 'format_rapor_rumus' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_rapor_rumus'])\n"
        "    mapping = {\n"
        "        'idformat_rapor': 'id_rapor_format', 'param_operator': 'logika_operator'\n"
        "    }\n"
        "    transformed_dfs['rapor_format_formula'] = df.rename(columns=mapping)[list(mapping.values())]\n"
    )

    old_block_4 = (
        "# 4. format_rapor_detil_rumus -> rapor_format_formula_sub\n"
        "if 'format_rapor_detil_rumus' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_rapor_detil_rumus'])\n"
        "    mapping = {\n"
        "        'idfrdr': 'id_rapor_format_formula_sub',\n"
        "        'idformat_rd': 'id_rapor_format_sub', 'param_operator': 'logika_operator',\n"
        "        'idlevel': 'id_level'\n"
        "    }\n"
        "    transformed_dfs['rapor_format_formula_sub'] = df.rename(columns=mapping)[list(mapping.values())]\n"
    )

    new_block_4 = (
        "# 4. format_rapor_detil_rumus -> rapor_format_formula_sub\n"
        "if 'format_rapor_detil_rumus' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_rapor_detil_rumus'])\n"
        "    mapping = {\n"
        "        'idformat_rd': 'id_rapor_format_sub', 'param_operator': 'logika_operator',\n"
        "        'idlevel': 'id_level'\n"
        "    }\n"
        "    transformed_dfs['rapor_format_formula_sub'] = df.rename(columns=mapping)[list(mapping.values())]\n"
    )

    old_block_5 = (
        "# 5. format_raport_level -> rapor_level_config\n"
        "if 'format_raport_level' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_raport_level'])\n"
        "    mapping = {\n"
        "        'idformat_rl': 'id_rapor_level_config', 'idlevel': 'id_level',\n"
        "        'idpendkursus': 'id_kursus', 'idformat_rapor': 'id_rapor_format'\n"
        "    }\n"
        "    transformed_dfs['rapor_level_config'] = df.rename(columns=mapping)[list(mapping.values())]\n"
    )

    new_block_5 = (
        "# 5. format_raport_level -> rapor_level_config\n"
        "if 'format_raport_level' in raw_data:\n"
        "    df = pd.DataFrame(raw_data['format_raport_level'])\n"
        "    mapping = {\n"
        "        'idlevel': 'id_level',\n"
        "        'idpendkursus': 'id_kursus', 'idformat_rapor': 'id_rapor_format'\n"
        "    }\n"
        "    transformed_dfs['rapor_level_config'] = df.rename(columns=mapping)[list(mapping.values())]\n"
    )

    old_block_6 = (
        "# 6. rapor_sub_level (Tabel Baru)\n"
        "transformed_dfs['rapor_sub_level'] = pd.DataFrame(columns=['id_rapor_sub_level', 'id_rapor_format_sub', 'id_level'])\n"
    )

    new_block_6 = (
        "# 6. rapor_sub_level (Tabel Baru)\n"
        "transformed_dfs['rapor_sub_level'] = pd.DataFrame(columns=['id_rapor_format_sub', 'id_level'])\n"
    )

    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and MATCH_KEY in "".join(cell["source"]):
            source = "".join(cell["source"])
            if old_block_1 in source:
                source = source.replace(old_block_1, new_block_1)
            if old_block_2 in source:
                source = source.replace(old_block_2, new_block_2)
            if old_block_3 in source:
                source = source.replace(old_block_3, new_block_3)
            if old_block_4 in source:
                source = source.replace(old_block_4, new_block_4)
            if old_block_5 in source:
                source = source.replace(old_block_5, new_block_5)
            if old_block_6 in source:
                source = source.replace(old_block_6, new_block_6)
            cell["source"] = [line + "\n" for line in source.split("\n")]
            if cell["source"] and cell["source"][-1] == "\n":
                cell["source"].pop()
            patched = True
            break

    if patched:
        ensure_csv_export_cell(nb)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: patch_fase_5_rapor_urutan - rapor_format, rapor_format_sub, formulas, and levels updated.")
    else:
        print("Error: target cell not found in patch_fase_5_rapor_urutan. Sudah di-patch sebelumnya atau cell marker berubah.")
        print("  Hint: cari sel dengan marker:", repr(MATCH_KEY))


if __name__ == "__main__":
    patch_fase_3()
    patch_fase_4()
    patch_fase_5()
    patch_fase_5_rapor_urutan()
