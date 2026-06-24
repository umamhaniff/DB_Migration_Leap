import os
import re
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Database config
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3307)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_OLD', 'dataleap_v5_example'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

# 1. Analyze siswa no_induk
print("--- ANALYZING SISWA NO_INDUK ---")
cursor.execute("SELECT idsiswa, no_induk FROM siswa")
siswa_rows = cursor.fetchall()
df_siswa = pd.DataFrame(siswa_rows)

print(f"Total rows in old siswa: {len(df_siswa)}")

# Check duplicate no_induk in old database (excluding nulls/blanks)
def clean_val(val):
    if pd.isna(val): return None
    s = str(val).strip()
    if s in ('', '-', '#N/A', 'None', 'nan', 'NULL'): return None
    return s

df_siswa['clean_no_induk'] = df_siswa['no_induk'].apply(clean_val)
non_null_ni = df_siswa.dropna(subset=['clean_no_induk'])
print(f"Non-null/non-blank no_induk count: {len(non_null_ni)}")

duplicates = non_null_ni[non_null_ni.duplicated(subset=['clean_no_induk'], keep=False)]
print(f"Duplicate clean no_induk rows in old database: {len(duplicates)}")
if len(duplicates) > 0:
    print(duplicates.sort_values(by='clean_no_induk').head(20))

# Check for specific duplicate in warning: '20220000080' and '20220000293'
print("\nSpecific checks:")
for specific in ['20220000080', '20220000293', 'TEMP-S0000009', 'S0000009']:
    matches = df_siswa[df_siswa['idsiswa'].str.contains(specific, na=False) | df_siswa['no_induk'].astype(str).str.contains(specific, na=False)]
    print(f"Matches for '{specific}':")
    print(matches)

# 2. Analyze mitra kode_mitra generation
print("\n--- ANALYZING MITRA KODE_MITRA GENERATION ---")
cursor.execute("SELECT idmitra, nama, instansi, created_at FROM mitra")
mitra_rows = cursor.fetchall()
df_mitra = pd.DataFrame(mitra_rows)
df_mitra['_sort_key'] = pd.to_datetime(df_mitra['created_at'], errors='coerce').fillna(pd.to_datetime('2020-01-01'))
df_mitra = df_mitra.sort_values(by=['_sort_key', 'idmitra']).reset_index(drop=True)

prefix_count = {}
new_kodes = []
for _, row in df_mitra.iterrows():
    idmitra = row['idmitra']
    cursor.execute("SELECT no_induk FROM siswa WHERE idmitra = %s AND no_induk IS NOT NULL AND no_induk != ''", (idmitra,))
    students = cursor.fetchall()
    prefixes = []
    for s in students:
        # Extract letters only from no_induk
        prefix = re.sub(r'[0-9#/ \t-]', '', s['no_induk'])
        if prefix:
            prefixes.append(prefix)
    unique_prefixes = list(set(prefixes))
    base = unique_prefixes[0] if unique_prefixes else 'M'
    
    # Let's clean the base to uppercase to prevent casing duplicates in case-insensitive DBs
    base = base.upper().strip()
    
    count = prefix_count.get(base, 0)
    kode = base if count == 0 else f"{base}{count}"
    prefix_count[base] = count + 1
    new_kodes.append(kode)
    
df_mitra['generated_kode'] = new_kodes

print(f"Total generated kodes: {len(df_mitra)}")
print("Generated kodes and count:")
print(df_mitra[['idmitra', 'nama', 'generated_kode']])

# Check duplicates in generated kodes
dup_kodes = df_mitra[df_mitra.duplicated(subset=['generated_kode'], keep=False)]
print(f"\nDuplicate generated kodes: {len(dup_kodes)}")
if len(dup_kodes) > 0:
    print(dup_kodes[['idmitra', 'nama', 'generated_kode']])

cursor.close()
conn.close()
