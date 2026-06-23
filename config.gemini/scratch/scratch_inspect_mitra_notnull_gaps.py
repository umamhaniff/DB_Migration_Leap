import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor_old = conn_old.cursor(dictionary=True)

# Fetch raw data
cursor_old.execute("SELECT * FROM mitra")
df = pd.DataFrame(cursor_old.fetchall())

# Helper function
def extract_int(s):
    import re
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\d+', str(s))
    return int(nums[0]) if nums else None

def convert_ya_tidak(x):
    if pd.isna(x): return 0
    val = str(x).strip().lower()
    if val in ('ya', 'yes', '1', 'true'): return 1
    return 0

df['id_mitra_new'] = df['idmitra'].apply(extract_int).astype('Int64')
df['kode_mitra'] = df['idmitra'] # using direct idmitra instead of extract_chars to check

bool_cols = ['leapverse', 'kemitraan', 'elsa', 'classin', 'mitraleap']
for col in bool_cols:
    df[col] = df[col].apply(convert_ya_tidak)

mapping = {
    'id_mitra_new': 'id_mitra', 'nama': 'nama_mitra', 'instansi': 'nama_instansi',
    'namasekolah': 'nama_sekolah', 'lokasi': 'alamat_mitra', 'kepsek': 'nama_pimpinan',
    'cp': 'kontak_mitra', 'status': 'status_mitra', 'visimisi': 'visi_misi',
    'program': 'program_mitra', 'sdm': 'info_sdm', 'weakness': 'info_kelemahan',
    'rekomen': 'rekomendasi_program', 'jenis': 'jenis_mitra', 
    'jml': 'jumlah_siswa_mitra', 'bidang': 'bidang_usaha',
    'leapverse': 'is_leapverse', 'kemitraan': 'status_kemitraan', 'tahun': 'tahun_bergabung',
    'jeniskemitraan': 'tipe_kerjasama', 'elsa': 'is_elsa', 'classin': 'is_classin',
    'mitraleap': 'is_mitra_leap', 'created_at': 'created_at', 'kode_mitra': 'kode_mitra'
}

df_transformed = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# Get the not null columns in db_new
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor_new = conn_new.cursor()
cursor_new.execute("DESCRIBE mitra")
not_null_cols = []
for row in cursor_new.fetchall():
    if row[2] == 'NO' and row[4] is None and row[5] != 'auto_increment':
        not_null_cols.append(row[0])
print("NOT NULL columns with no default:", not_null_cols)

print("\n--- Rows with NULL values in NOT NULL columns of mitra ---")
for col in not_null_cols:
    if col in df_transformed.columns:
        null_count = df_transformed[col].isna().sum()
        empty_count = (df_transformed[col] == '').sum() if df_transformed[col].dtype == object else 0
        total_missing = null_count + empty_count
        print(f"Column '{col}': {null_count} nulls, {empty_count} empty strings. Total missing: {total_missing}")

cursor_new.close()
conn_new.close()
cursor_old.close()
conn_old.close()
