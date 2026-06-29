# ==========================================
# CELL 1
# ==========================================
def display(*args, **kwargs):
    for arg in args:
        print(arg)

import sys
import os
import mysql.connector 
import pandas as pd
import re
from datetime import datetime
import pickle
import json
sys.path.append(os.path.abspath('..'))
from config import get_db_config
import warnings
warnings.filterwarnings('ignore')

# ==========================================
# CELL 2
# ==========================================
config = get_db_config()
db_old = mysql.connector.connect(**config['db_old'])
cursor_old = db_old.cursor(dictionary=True)
db_new = mysql.connector.connect(**config['db_future'])
cursor_new = db_new.cursor(dictionary=True)
print(f"Connected to {config['db_old']['database']} and {config['db_future']['database']}")

# ==========================================
# CELL 3
# ==========================================
hanif_tables_map = [
    ('pengajuan', 'pengajuan_karyawan'),
    ('histori_pengajuan', 'histori_pengajuan'),
    ('pelamar', 'pelamar'),
    ('pekerjaan', 'pelamar_kerja'),
    ('pendidikan', 'pelamar_sekolah'),
    ('kursus', 'pelamar_kursus'),
    ('pelamar_note', 'progres_pelamar'),
    ('pelamar_users', 'rekrutmen_pelamar')
]

raw_data = {}
for old_t, new_t in hanif_tables_map:
    cursor_old.execute(f"SELECT * FROM `{old_t}`")
    raw_data[old_t] = cursor_old.fetchall()
    print(f"✅ {old_t} loaded: {len(raw_data[old_t])} records")

# ==========================================
# CELL 4
# ==========================================
transformed_dfs = {}

# --- HELPER FUNCTIONS ---
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
    nums = re.findall(r'\\d+', str(s))
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
    match = re.search(r'(\\d.*)', s)
    return match.group(1).strip() if match else None

def parse_date(date_str):
    if pd.isna(date_str): return None
    s = str(date_str).strip()
    if s in ('', '-', '0', 'nan', 'NaN'): return None
    
    # First normalize day-of-month ranges: "27 - 29 Mei 2023" -> "27 Mei 2023"
    s = re.sub(r'\\b(\\d{1,2})\\s*-\\s*\\d{1,2}\\b', r'\\1', s)
    
    # Try to see if it's a month-level range: e.g. "29 September - 6 Oktober 2021"
    parts = re.split(r'\\s+-\\s+|\\s+(?:sd|s/d|dan|s\\.d\\.)\\s+', s, flags=re.IGNORECASE)
    if len(parts) > 1:
        part1 = parts[0].strip()
        part2 = parts[1].strip()
        if not re.search(r'\\b\\d{4}\\b', part1):
            year_match = re.search(r'\\b\\d{4}\\b', part2)
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
    s = re.sub(r'\\s+', ' ', s)
    
    for id_m, en_m in months_id_to_en.items():
        s = re.sub(rf'\\b{id_m}\\b', en_m, s, flags=re.IGNORECASE)
        
    year_match = re.search(r'\\b\\d{4}\\b', s)
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
    years = re.findall(r'\\d{4}', str(tahun_str))
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
    match = re.search(r'\\d+\\.?\\d*', s)
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
        r'\\bs\\.?\\s*pd\\b', r'\\bm\\.?\\s*pd\\b', r'\\bs\\.?\\s*s\\b', r'\\bs\\.?\\s*t\\b', 
        r'\\bs\\.?\\s*hum\\b', r'\\bs\\.?\\s*kom\\b', r'\\ba\\.?\\s*md\\b', r'\\bs\\.?\\s*e\\b', 
        r'\\bm\\.?\\s*m\\b', r'\\bdr\\b', r'\\bdra\\b', r'\\bdrs\\b', r'\\bprof\\b',
        r'\\bpsi\\b', r'\\bs\\.?\\s*psi\\b'
    ]
    for title in titles:
        s = re.sub(title, '', s, flags=re.IGNORECASE)
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

# --- TRANSFORMATION ---

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

print(f"OK: Transformasi {len(transformed_dfs)} tabel Fase 3 selesai.")


# ==========================================
# CELL 5
# ==========================================
# 3.1.1 Ringkasan Jumlah Baris
print("📊 RINGKASAN MIGRASI (RECORDS COUNT)")
print("="*70)
summary_list = []
for old_t, new_t in hanif_tables_map:
    old_c = len(raw_data.get(old_t, []))
    new_c = len(transformed_dfs.get(new_t, []))
    summary_list.append({
        'Tabel Lama': old_t,
        'Tabel Baru': new_t,
        'Old Recs': old_c,
        'New Recs': new_c,
        'Diff': new_c - old_c,
        'Status': "✅ OK" if old_c == new_c else "⚠️ Cek"
    })
display(pd.DataFrame(summary_list))

total_old_all = sum(len(records) for records in raw_data.values())
total_new_all = sum(len(df) for df in transformed_dfs.values())
print(f"\n📢 TOTAL REKAPITULASI: {total_old_all} (Old) ➔ {total_new_all} (New)")
if total_old_all == total_new_all: print("✅ SEMUA DATA TERANGKUT")
else: print(f"⚠️ ADA SELISIH: {total_new_all - total_old_all} baris")

# ==========================================
# CELL 6
# ==========================================
# 3.1.2 Output Pengecekan Kolom Spesifik (Keterangan Mapping)
print("\n🔍 PENGECEKAN TRANSFORMASI SPESIFIK (KETERANGAN mapping.md)")
print("="*70)

# 1. Pengecekan Tanggal & TTL (Tabel Pelamar)
if 'pelamar' in transformed_dfs:
    print("\n[PELAMAR] Pengecekan Parsing TTL & Tanggal:")
    display(transformed_dfs['pelamar'][['nama_lengkap', 'tempat_lahir', 'tanggal_lahir']].dropna(subset=['tanggal_lahir']).head(5))

# 2. Pengecekan Konversi Gaji (Tabel Pelamar)
if 'pelamar' in transformed_dfs:
    print("\n[PELAMAR] Pengecekan Konversi Gaji (String IDR -> BigInt):")
    display(transformed_dfs['pelamar'][['nama_lengkap', 'ekspektasi_gaji']].head(5))

# 3. Pengecekan Enum Status & Laptop (Tabel Pelamar)
if 'pelamar' in transformed_dfs:
    print("\n[PELAMAR] Pengecekan Mapping Enum (Status Nikah & Laptop):")
    display(transformed_dfs['pelamar'][['nama_lengkap', 'status_pernikahan', 'penggunaan_laptop']].head(5))

# 4. Pengecekan Tahun & IPK (Tabel Pelamar Sekolah)
if 'pelamar_sekolah' in transformed_dfs:
    print("\n[PELAMAR_SEKOLAH] Pengecekan Tahun Lulus (Latest) & IPK (Decimal):")
    display(transformed_dfs['pelamar_sekolah'][['nama_sekolah', 'tahun_lulus', 'ipk']].head(5))

# 5. Pengecekan Tanggal Kursus (Tabel Pelamar Kursus)
if 'pelamar_kursus' in transformed_dfs:
    print("\n[PELAMAR_KURSUS] Pengecekan Konversi Tanggal Kursus:")
    display(transformed_dfs['pelamar_kursus'][['nama_kursus', 'tanggal']].head(5))

# 6. Pengecekan Status Progress (Tabel Progres Pelamar)
if 'progres_pelamar' in transformed_dfs:
    print("\n[PROGRES_PELAMAR] Pengecekan Normalisasi Status (baru -> Baru):")
    display(transformed_dfs['progres_pelamar'][['status_progres_pelamar']].drop_duplicates())

# ==========================================
# CELL 7
# ==========================================
# 3.1.3 Detail Perbandingan Kolom & Tipe Data (Side-by-Side)
print("\n🔍 PERBANDINGAN TIPE DATA SIDE-BY-SIDE")
for old_t, new_t in hanif_tables_map:
    print(f"\n{'='*15} {old_t.upper()} ➔ {new_t.upper()} {'='*15}")
    
    df_old = pd.DataFrame(raw_data.get(old_t, []))
    df_new = transformed_dfs.get(new_t, pd.DataFrame())
    
    if not df_new.empty:
        comparison = []
        # table_mapping defined for each table
        table_mapping = {}
        if old_t == 'pengajuan': table_mapping = {'idpengajuan': 'id_pengajuan', 'idusers': 'id_user', 'keterangan': 'posisi', 'jumlah': 'jumlah', 'syarat': 'syarat', 'pertanyaan': 'pertanyaan', 'alur': 'alur_seleksi', 'test': 'daftar_tes', 'status': 'status', 'created_at': 'created_at'}
        elif old_t == 'histori_pengajuan': table_mapping = {'idhistori': 'id_verifikasi', 'idpengajuan': 'id_pengajuan', 'status': 'status_verifikasi_pengajuan', 'catatan': 'catatan', 'created_at': 'created_at'}
        elif old_t == 'pelamar': table_mapping = {'idpelamar': 'id_pelamar', 'idpengajuan': 'id_pengajuan', 'email': 'email_pelamar', 'nama': 'nama_lengkap', 'panggilan': 'nama_panggilan', 'jk': 'jenis_kelamin', 'ttl': 'tanggal_lahir', 'alamat': 'alamat_ktp', 'domisili': 'alamat_domisili', 'wa': 'nomor_wa', 'linkedin': 'akun_linkedin', 'ig': 'akun_instagram', 'fb': 'akun_facebook', 'sosmed': 'sosmed_lain', 'laptop': 'spesifikasi_laptop', 'internet': 'internet', 'kegiatan': 'kegiatan_sekarang', 'rencana': 'rencana_karir', 'mobilitas': 'mobilitas', 'info': 'sumber_info', 'wfo': 'siap_wfo', 'bergabung': 'tanggal_bergabung', 'jenis': 'kategori_pelamar', 'work': 'riwayat_kerja', 'ppdk': 'riwayat_pendidikan', 'pengalaman': 'pengalaman_bidang', 'wawasan': 'wawasan', 'sehat': 'riwayat_kesehatan', 'statusnikah': 'status_pernikahan', 'ajar': 'kemampuan_ajar', 'app': 'penguasaan_aplikasi', 'apps': 'aplikasi_lainnya', 'gunalaptop': 'penggunaan_laptop', 'toefl': 'skor_toefl', 'gaji': 'ekspektasi_gaji', 'link': 'tautan_berkas', 'resign': 'alasan_resign', 'hasiliq': 'skor_iq', 'piciq': 'foto_iq', 'picminat': 'foto_minat', 'picpribadi': 'foto_kepribadian', 'created_at': 'created_at'}
        elif old_t == 'pekerjaan': table_mapping = {'idpekerjaan': 'id_pelamar_kerja', 'idusers': 'id_pelamar', 'namaperusahaan': 'nama_perusahaan', 'periode': 'periode', 'jabatan': 'jabatan', 'jobdesk': 'deskripsi_kerja'}
        elif old_t == 'pendidikan': table_mapping = {'idpendidikan': 'id_pelamar_sekolah', 'idusers': 'id_pelamar', 'sekolah': 'nama_sekolah', 'jenjang': 'jenjang', 'prodi': 'prodi', 'tahun': 'tahun_lulus', 'ipk': 'ipk', 'organisasi': 'organisasi'}
        elif old_t == 'kursus': table_mapping = {'idkursus': 'id_pelamar_kursus', 'idusers': 'id_pelamar', 'nama': 'nama_kursus', 'tanggal': 'tanggal', 'deskripsi': 'deskripsi', 'lokasi': 'lokasi', 'nosertifikat': 'nomor_sertifikat'}
        elif old_t == 'pelamar_note': table_mapping = {'idnote': 'id_progres_pelamar', 'idpelamar': 'id_pelamar', 'idusers': 'id_user', 'status': 'status_progres_pelamar', 'note': 'catatan', 'link': 'tautan_file', 'pertanyaan': 'pertanyaan', 'created_at': 'created_at'}
        elif old_t == 'pelamar_users': table_mapping = {'idassign': 'id_rekrutmen', 'idpelamar': 'id_pelamar', 'idusers': 'id_user'}

        for old_col, new_col in table_mapping.items():
            comparison.append({
                'Old Column': old_col,
                'Old Type': str(df_old[old_col].dtype) if old_col in df_old.columns else "N/A",
                '➔': '➔',
                'New Column': new_col,
                'New Type': str(df_new[new_col].dtype) if new_col in df_new.columns else "N/A"
            })
        
        # Cek kolom baru yang tidak ada di mapping
        for col in df_new.columns:
            if col not in table_mapping.values():
                comparison.append({
                    'Old Column': '(KOLOM BARU / CUSTOM)',
                    'Old Type': '-',
                    '➔': '➔',
                    'New Column': col,
                    'New Type': str(df_new[col].dtype)
                })
        
        display(pd.DataFrame(comparison))
        print(f"\n--- SAMPLE DATA NEW (2 Baris) ---")
        display(df_new.head(2))
    else:
        print(f"⚠️ Tabel {new_t} kosong.")

# ==========================================
# CELL 8
# ==========================================
file_name = 'fase_3_hanif.pkl'
with open(file_name, 'wb') as f:
    pickle.dump(transformed_dfs, f)

total_records_new = sum(len(df) for df in transformed_dfs.values())
total_records_old = sum(len(records) for records in raw_data.values())

migration_result = {
    'fase': 'fase_3',
    'script': 'script_hanif',
    'fase_num': 3,
    'status': 'ready_for_insert',
    'old_records_total': total_records_old,
    'new_records_total': total_records_new,
    'diff': total_records_new - total_records_old,
    'pickle_file': file_name,
    'timestamp': datetime.now().isoformat()
}
print(json.dumps(migration_result, indent=2))

cursor_old.close()
cursor_new.close()
db_old.close()
db_new.close()

# ==========================================
# CELL 9
# ==========================================
# --- EXPORT KE CSV UNTUK VERIFIKASI ---
EXPORT_TO_CSV = True  # Ubah ke False jika tidak ingin menghasilkan file CSV

if EXPORT_TO_CSV:
    import os
    import pandas as pd
    target_dir = "../extract/cek_csv"
    os.makedirs(target_dir, exist_ok=True)
    for tbl_name, df_tbl in transformed_dfs.items():
        csv_path = os.path.join(target_dir, f"{tbl_name}.csv")
        df_to_save = df_tbl.copy()
        
        # Clean any float ID/FK columns that contain .0 to pure integers
        for col in df_to_save.columns:
            col_lower = col.lower()
            is_id_col = col_lower.startswith('id_') or col_lower.endswith('_id') or col_lower == 'id' or 'id_' in col_lower or '_id_' in col_lower
            if is_id_col:
                non_nulls = df_to_save[col].dropna()
                if not non_nulls.empty:
                    try:
                        pd.to_numeric(non_nulls, errors='raise')
                        df_to_save[col] = pd.to_numeric(df_to_save[col], errors='coerce').round().astype('Int64')
                    except (ValueError, TypeError):
                        pass
        
        # Fix: Convert any StringDtype to object for clean serialization
        for col in df_to_save.columns:
            if str(df_to_save[col].dtype) in ['string', 'string[python]']:
                df_to_save[col] = df_to_save[col].astype(object)
        df_to_save.to_csv(csv_path, index=False)
        print(f"💾 Tabel {tbl_name} diekspor ke {csv_path} ({len(df_tbl)} baris)")
else:
    print("ℹ️ Ekspor ke CSV dinonaktifkan.")

