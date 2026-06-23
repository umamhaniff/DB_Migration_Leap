import sys
import os
import mysql.connector
import pandas as pd
import numpy as np
import re

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
    match = re.search(r'(\d.*)', s)
    return match.group(1).strip() if match else None

def parse_date(date_str):
    if pd.isna(date_str): return None
    s = str(date_str).strip()
    if s in ('', '-', '0', 'nan', 'NaN'): return None
    s = re.sub(r'\b(\d{1,2})\s*-\s*\d{1,2}\b', r'\1', s)
    parts = re.split(r'\s+-\s+|\s+(?:sd|s/d|dan|s\.d\.)\s+', s, flags=re.IGNORECASE)
    if len(parts) > 1:
        part1 = parts[0].strip()
        part2 = parts[1].strip()
        if not re.search(r'\b\d{4}\b', part1):
            year_match = re.search(r'\b\d{4}\b', part2)
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
    s = re.sub(r'\s+', ' ', s)
    for id_m, en_m in months_id_to_en.items():
        s = re.sub(rf'\b{id_m}\b', en_m, s, flags=re.IGNORECASE)
    year_match = re.search(r'\b\d{4}\b', s)
    if not year_match:
        s = s + " 2023"
    formats = [
        '%d %B %Y', '%d %b %Y', '%B %Y', '%b %Y',
        '%d %m %Y', '%m %d %Y', '%Y %m %d',
        '%d %m %y', '%m %d %y', '%y %m %d'
    ]
    for fmt in formats:
        try: return pd.to_datetime(s, format=fmt).date()
        except: continue
    try:
        res = pd.to_datetime(s, errors='coerce')
        if pd.notna(res): return res.date()
    except: pass
    return None

def clean_currency(val):
    if pd.isna(val): return 0
    s = str(val).strip()
    nums = re.sub(r'[^0-9]', '', s)
    return int(nums) if nums else 0

def clean_name_without_titles(s):
    if pd.isna(s): return ""
    s = str(s).strip().lower()
    if ',' in s: 
        s = s.split(',')[0]
    titles = [
        r'\bs\.?\s*pd\b', r'\bm\.?\s*pd\b', r'\bs\.?\s*s\b', r'\bs\.?\s*t\b', 
        r'\bs\.?\s*hum\b', r'\bs\.?\s*kom\b', r'\ba\.?\s*md\b', r'\bs\.?\s*e\b', 
        r'\bm\.?\s*m\b', r'\bdr\b', r'\bdra\b', r'\bdrs\b', r'\bprof\b',
        r'\bpsi\b', r'\bs\.?\s*psi\b'
    ]
    for title in titles:
        s = re.sub(title, '', s, flags=re.IGNORECASE)
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor_old = conn_old.cursor(dictionary=True)

# Fetch raw data
cursor_old.execute("SELECT * FROM pelamar")
df_pel = pd.DataFrame(cursor_old.fetchall())

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

# Transform pelamar table
df_pel['tempat_lahir'] = df_pel['ttl'].apply(extract_place)
df_pel['tanggal_lahir'] = df_pel['ttl'].apply(extract_date).apply(parse_date)

def map_nikah(x):
    val = str(x).strip().lower()
    if val in ['menikah', 'nikah', 'kawin']: return 'Menikah'
    return 'Belum Menikah'

df_pel['status_pernikahan'] = df_pel['statusnikah'].apply(map_nikah)
df_pel['penggunaan_laptop'] = df_pel['gunalaptop'].apply(lambda x: 'Pernah' if str(x).strip().lower() in ['pernah', 'ya, pernah', 'ya'] else 'Tidak Pernah')
df_pel['gaji'] = df_pel['gaji'].apply(clean_currency)

df_pel_extended = df_pel.copy()
for u_id, name, email in unmatched_users:
    new_row = {
        'idpelamar': u_id,
        'nama': name,
        'email': email,
        'idpengajuan': None,
    }
    df_pel_extended = pd.concat([df_pel_extended, pd.DataFrame([new_row])], ignore_index=True)
    
df_pel_extended['id_pelamar_new'] = df_pel_extended.index + 1
pelamar_id_map = dict(zip(df_pel_extended['idpelamar'], df_pel_extended['id_pelamar_new']))

df_pel_extended['id_pelamar'] = df_pel_extended['id_pelamar_new']
df_pel_extended['id_pengajuan'] = df_pel_extended['idpengajuan'].astype('Int64')

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

df_transformed = df_pel_extended.rename(columns=mapping)
df_transformed = df_transformed.reindex(columns=list(mapping.values()))

# Get the not null columns in db_new
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor_new = conn_new.cursor()
cursor_new.execute("DESCRIBE pelamar")
not_null_cols = []
for row in cursor_new.fetchall():
    if row[2] == 'NO' and row[4] is None and row[5] != 'auto_increment':
        not_null_cols.append(row[0])
print("NOT NULL columns with no default:", not_null_cols)

print("\n--- Rows with NULL values in NOT NULL columns ---")
for col in not_null_cols:
    if col in df_transformed.columns:
        null_count = df_transformed[col].isna().sum()
        empty_count = (df_transformed[col] == '').sum() if df_transformed[col].dtype == object else 0
        total_missing = null_count + empty_count
        print(f"Column '{col}': {null_count} nulls, {empty_count} empty strings. Total missing: {total_missing}")
        if total_missing > 0:
            print("  First 3 missing values examples:")
            missing_df = df_transformed[df_transformed[col].isna() | (df_transformed[col] == '')] if df_transformed[col].dtype == object else df_transformed[df_transformed[col].isna()]
            for idx, row in missing_df.head(3).iterrows():
                print(f"    Row index {idx} (id_pelamar: {row['id_pelamar']}, nama: {row['nama_lengkap']}): value={row[col]}")

cursor_new.close()
conn_new.close()
cursor_old.close()
conn_old.close()
