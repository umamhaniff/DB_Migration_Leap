import json
import os

def update_fase_4():
    path = 'fase_4/script_hanif.ipynb'
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'normalize_agama' in ''.join(cell['source']):
            source = ''.join(cell['source'])
            
            # Update normalize_agama
            old_normalize = """    def normalize_agama(a):
        if pd.isna(a): return 'Islam'
        a_clean = str(a).strip()
        for k, v in agama_map.items():
            if k in a_clean.lower(): return v
        return a_clean"""
            
            new_normalize = """    def normalize_agama(a):
        if pd.isna(a) or str(a).strip() == '': return 'Islam'
        a_clean = str(a).strip().lower()
        if 'kristen' in a_clean or 'protestan' in a_clean: return 'Kristen Protestan'
        if 'katholik' in a_clean or 'katolik' in a_clean: return 'Katolik'
        if 'hindu' in a_clean: return 'Hindu'
        if 'budha' in a_clean or 'buddha' in a_clean: return 'Buddha'
        if 'khonghucu' in a_clean or 'konghuchu' in a_clean: return 'Konghucu'
        return 'Islam'"""
            
            source = source.replace(old_normalize, new_normalize)
            
            # Update id_tag_keluar logic in siswa_keluar
            old_siswa_keluar = """# 3. siswa_keluar -> siswa_keluar
if 'siswa_keluar' in raw_data:
    df = pd.DataFrame(raw_data['siswa_keluar'])
    mapping = {
        'idsiswa_keluar': 'id_keluar', 'idsiswa': 'id_siswa',
        'alasan': 'alasan_keluar', 'tanggal': 'tanggal_keluar'
    }
    df = df.rename(columns=mapping)
    df['id_kursus'] = None
    df['id_tag_keluar'] = None
    transformed_dfs['siswa_keluar'] = df[list(mapping.values()) + ['id_kursus', 'id_tag_keluar']]"""

            new_siswa_keluar = """# 3. siswa_keluar -> siswa_keluar
if 'siswa_keluar' in raw_data:
    df = pd.DataFrame(raw_data['siswa_keluar'])
    mapping = {
        'idsiswa_keluar': 'id_keluar', 'idsiswa': 'id_siswa',
        'alasan': 'alasan_keluar', 'tanggal': 'tanggal_keluar'
    }
    df = df.rename(columns=mapping)
    df['id_kursus'] = None
    
    # Heuristic for id_tag_keluar based on mapping.md "cek kolom alasan_keluar & keterangan_keluar"
    # Tag IDs from Fase 1 (1: Pindah, 2: Ekonomi, 3: Lulus, 4: Lainnya) - assuming heuristic
    def detect_tag(alasan):
        s = str(alasan).lower()
        if 'pindah' in s: return 1
        if 'ekonomi' in s or 'biaya' in s: return 2
        if 'lulus' in s or 'selesai' in s: return 3
        return 4 # Lainnya
        
    df['id_tag_keluar'] = df['alasan_keluar'].apply(detect_tag)
    transformed_dfs['siswa_keluar'] = df[list(mapping.values()) + ['id_kursus', 'id_tag_keluar']]"""

            source = source.replace(old_siswa_keluar, new_siswa_keluar)
            
            # --- UPDATE SISWA & MITRA GEO MAPPING ---
            old_siswa_transform = """# 1. siswa -> siswa
if 'siswa' in raw_data:
    df = pd.DataFrame(raw_data['siswa'])
    df['idmitra_int'] = df['idmitra'].apply(extract_int)
    
    # Normalisasi Agama"""

            new_siswa_transform = """# 1. siswa -> siswa
if 'siswa' in raw_data:
    df = pd.DataFrame(raw_data['siswa'])
    df['idmitra_int'] = df['idmitra'].apply(extract_int)

    # Fetch region tables from both databases to build hierarchical name mappings (Read-only lookup)
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
        
        # Remove administrative words/abbreviations as whole words, including optional dot
        s = re.sub(r'\\b(kabupaten|kab|kota|kecamatan|kec|kelurahan|kel|desa|adm)\\b\\.?', '', s)
        
        # Replace special punctuation/characters
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

    # Vectorized merge for Kelurahan mapping (Instant 1-second mapping for 83k rows!)
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

    df['id_provinsi'] = df['provinsi'].map(prov_map)
    df['id_kabupaten'] = df['kabupaten'].map(kab_map)
    df['id_kecamatan'] = df['kecamatan'].map(kec_map)
    df['id_kelurahan'] = df['kelurahan'].map(kel_map)
    
    # Normalisasi Agama"""

            source = source.replace(old_siswa_transform, new_siswa_transform)

            old_siswa_mapping = """        'provinsi': 'id_provinsi', 'kabupaten': 'id_kabupaten', 'kecamatan': 'id_kecamatan',
        'kelurahan': 'id_kelurahan', 'idmitra_int': 'id_mitra',"""

            new_siswa_mapping = """        'id_provinsi': 'id_provinsi', 'id_kabupaten': 'id_kabupaten', 'id_kecamatan': 'id_kecamatan',
        'id_kelurahan': 'id_kelurahan', 'idmitra_int': 'id_mitra',"""

            source = source.replace(old_siswa_mapping, new_siswa_mapping)

            old_mitra_transform = """# 4. mitra -> mitra
if 'mitra' in raw_data:
    df = pd.DataFrame(raw_data['mitra'])
    df['id_mitra_new'] = df['idmitra'].apply(extract_int)
    df['kode_mitra'] = df['idmitra'].apply(extract_chars)
    
    bool_cols = ['leapverse', 'kemitraan', 'elsa', 'classin', 'mitraleap']"""

            new_mitra_transform = """# 4. mitra -> mitra
if 'mitra' in raw_data:
    df = pd.DataFrame(raw_data['mitra'])
    df['id_mitra_new'] = df['idmitra'].apply(extract_int)
    df['kode_mitra'] = df['idmitra'].apply(extract_chars)
    
    df['provinsi_id'] = df['provinsi'].map(prov_map)
    df['kabupaten_id'] = df['kotkab'].map(kab_map)
    
    bool_cols = ['leapverse', 'kemitraan', 'elsa', 'classin', 'mitraleap']"""

            source = source.replace(old_mitra_transform, new_mitra_transform)

            old_mitra_mapping = """        'rekomen': 'rekomendasi_program', 'jenis': 'jenis_mitra', 'provinsi': 'provinsi_id',
        'kotkab': 'kabupaten_id',"""

            new_mitra_mapping = """        'rekomen': 'rekomendasi_program', 'jenis': 'jenis_mitra', 'provinsi_id': 'provinsi_id',
        'kabupaten_id': 'kabupaten_id',"""

            source = source.replace(old_mitra_mapping, new_mitra_mapping)
            
            # Update source list
            cell['source'] = [line + '\n' for line in source.split('\n')]
            if cell['source'][-1] == '\n': cell['source'].pop()
            # Ensure last line doesn't have \n if it didn't before, but usually they do
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

def update_fase_5():
    path = 'fase_5/script_hanif.ipynb'
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'rapor_map = dict' in ''.join(cell['source']):
            source = ''.join(cell['source'])
            
            # Fix rapor_siswa_file lookup
            old_rapor_file = """    rapor_map = dict(zip(pd.DataFrame(raw_data['rapor'])['idsiswa'], pd.DataFrame(raw_data['rapor'])['idrapor']))
    
    df['id_rapor_siswa'] = df['idsiswa'].map(rapor_map)
    
    mapping = {
        'idfile': 'id_rapor_siswa_file', 'id_rapor_siswa': 'id_rapor_siswa', 'path': 'file_rapor_path'
    }
    transformed_dfs['rapor_siswa_file'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))"""

            new_rapor_file = """    # Using merge instead of dict to avoid data loss if idsiswa has multiple reports
    df_rapor_old = pd.DataFrame(raw_data['rapor'])[['idsiswa', 'idrapor']]
    df = df.merge(df_rapor_old, on='idsiswa', how='left')
    df = df.rename(columns={'idrapor': 'id_rapor_siswa'})
    
    mapping = {
        'idfile': 'id_rapor_siswa_file', 'id_rapor_siswa': 'id_rapor_siswa', 'path': 'file_rapor_path'
    }
    transformed_dfs['rapor_siswa_file'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))"""

            source = source.replace(old_rapor_file, new_rapor_file)
            
            # Fix rapor_lacak lookup
            old_rapor_lacak = """    # id_rapor_siswa_file: cari di rapor_siswa_file
    # Kita butuh mapping dari idsiswa (old) ke id_rapor_siswa_file (new)
    file_map = dict(zip(pd.DataFrame(raw_data['file_rapor_siswa'])['idsiswa'], transformed_dfs['rapor_siswa_file']['id_rapor_siswa_file']))
    
    mapping = {
        'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa',
        'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'
    }
    df_final = df.rename(columns=mapping)
    df_final['id_rapor_siswa_file'] = df_final['id_siswa'].map(file_map)
    
    transformed_dfs['rapor_lacak'] = df_final[list(mapping.values()) + ['id_rapor_siswa_file']]"""

            new_rapor_lacak = """    # Using merge instead of dict to avoid data loss
    df_file_new = transformed_dfs['rapor_siswa_file'][['id_rapor_siswa_file']]
    # We need idsiswa from old file data to merge with history
    df_file_old = pd.DataFrame(raw_data['file_rapor_siswa'])[['idfile', 'idsiswa']]
    df_file_mapping = pd.concat([df_file_old, df_file_new], axis=1)
    
    mapping = {
        'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa',
        'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'
    }
    df_final = df.rename(columns=mapping)
    # Join on id_siswa (and id_jadwal if available in both for better precision)
    df_final = df_final.merge(df_file_mapping[['idsiswa', 'id_rapor_siswa_file']], left_on='id_siswa', right_on='idsiswa', how='left')
    
    transformed_dfs['rapor_lacak'] = df_final[list(mapping.values()) + ['id_rapor_siswa_file']]"""

            source = source.replace(old_rapor_lacak, new_rapor_lacak)
            
            cell['source'] = [line + '\n' for line in source.split('\n')]
            if cell['source'][-1] == '\n': cell['source'].pop()

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

def update_fase_3():
    path = 'fase_3/script_hanif.ipynb'
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'def extract_place' in ''.join(cell['source']):
            source = ''.join(cell['source'])
            
            # Improved helper functions
            old_helpers = """def extract_date(ttl):
    if pd.isna(ttl) or not str(ttl).strip(): return None
    s = str(ttl).strip()
    if ',' in s:
        parts = s.split(',')
        if len(parts) > 1: return parts[1].strip()
    # If no comma, try to take everything from the first digit onwards
    match = re.search(r'\\d.*', s)
    return match.group(0).strip() if match else None

def parse_date(date_str):
    if pd.isna(date_str) or not str(date_str).strip(): return None
    months = {
        'Januari': 'January', 'Februari': 'February', 'Maret': 'March', 'April': 'April',
        'Mei': 'May', 'Juni': 'June', 'Juli': 'July', 'Agustus': 'August',
        'September': 'September', 'Oktober': 'October', 'November': 'November', 'Desember': 'December',
        'Jan': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Apr', 'Mei': 'May', 'Jun': 'Jun',
        'Jul': 'Jul', 'Agu': 'Aug', 'Sep': 'Sep', 'Okt': 'Oct', 'Nov': 'Nov', 'Des': 'Dec'
    }
    s = str(date_str).strip()
    for indo, eng in months.items():
        s = re.sub(rf'\\b{indo}\\b', eng, s, flags=re.IGNORECASE)
    
    try:
        # Try several formats
        return pd.to_datetime(s, errors='coerce').date()
    except:
        return None"""

            new_helpers = """def extract_date(ttl):
    if pd.isna(ttl) or not str(ttl).strip(): return None
    s = str(ttl).strip()
    if ',' in s:
        parts = s.split(',')
        if len(parts) > 1: return parts[1].strip()
    # If no comma, try to find the first digit and take everything from there
    match = re.search(r'(\\d.*)', s)
    return match.group(1).strip() if match else None

def parse_date(date_str):
    if pd.isna(date_str) or not str(date_str).strip(): return None
    months = {
        'Januari': 'January', 'Februari': 'February', 'Maret': 'March', 'April': 'April',
        'Mei': 'May', 'Juni': 'June', 'Juli': 'July', 'Agustus': 'August',
        'September': 'September', 'Oktober': 'October', 'November': 'November', 'Desember': 'December',
        'Jan': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Apr', 'Mei': 'May', 'Jun': 'Jun',
        'Jul': 'Jul', 'Agu': 'Aug', 'Sep': 'Sep', 'Okt': 'Oct', 'Nov': 'Nov', 'Des': 'Dec'
    }
    s = str(date_str).strip()
    # Replace Indonesian months with English
    for indo, eng in months.items():
        s = re.sub(rf'\\\\b{indo}\\\\b', eng, s, flags=re.IGNORECASE)
    
    # Common formats
    formats = ['%d %B %Y', '%d %b %Y', '%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y']
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt).date()
        except:
            continue
            
    # Fallback to pandas
    try:
        return pd.to_datetime(s, errors='coerce').date()
    except:
        return None"""

            source = source.replace(old_helpers, new_helpers)

            # Update status_pernikahan enum logic
            old_pelamar = """    # enum & data cleaning
    df['status_pernikahan'] = df['statusnikah'].apply(lambda x: 'Belum Menikah' if str(x).strip().lower() in ['lajang', 'belum', 'single', 'x', 'none', 'nan', ''] else 'Menikah' if str(x).strip().lower() == 'menikah' else 'Belum Menikah')
    df['gunalaptop'] = df['gunalaptop'].replace('Ya, Pernah', 'Pernah')"""

            new_pelamar = """    # enum & data cleaning
    # mapping.md: "Lajang","Belum","Single","x" -> "Belum Menikah"
    def map_nikah(x):
        val = str(x).strip().lower()
        if val in ['menikah', 'nikah', 'kawin']: return 'Menikah'
        if val in ['lajang', 'belum', 'single', 'x', 'none', 'nan', '', '0']: return 'Belum Menikah'
        return 'Belum Menikah'
    
    df['status_pernikahan'] = df['statusnikah'].apply(map_nikah)
    
    # mapping.md: enum('Pernah','Tidak Pernah'); "Ya, Pernah" jd "Pernah"
    df['penggunaan_laptop'] = df['gunalaptop'].apply(lambda x: 'Pernah' if str(x).strip().lower() in ['pernah', 'ya, pernah', 'ya'] else 'Tidak Pernah')"""

            source = source.replace(old_pelamar, new_pelamar)
            
            # Map usage of penggunaan_laptop in mapping dict
            source = source.replace("'gunalaptop': 'penggunaan_laptop'", "'penggunaan_laptop': 'penggunaan_laptop'")

            cell['source'] = [line + '\n' for line in source.split('\n')]
            if cell['source'][-1] == '\n': cell['source'].pop()

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

if __name__ == '__main__':
    update_fase_3()
    update_fase_4()
    update_fase_5()
    print("Update notebooks finished.")
