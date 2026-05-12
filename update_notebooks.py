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
