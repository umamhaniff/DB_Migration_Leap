import sys
import os
import mysql.connector
import pandas as pd
import re
import time

sys.path.append(os.path.abspath('.'))
from config import get_db_config

config = get_db_config()
db_old = mysql.connector.connect(**config['db_old'])
cursor_old = db_old.cursor(dictionary=True)

db_new = mysql.connector.connect(**config['db_new'])
cursor_new = db_new.cursor(dictionary=True)

# 1. Load old tables
print("Loading old tables...")
cursor_old.execute("SELECT idprovinsi, nama FROM provinsi")
df_old_prov = pd.DataFrame(cursor_old.fetchall())

cursor_old.execute("SELECT idkabupaten, idprovinsi, name FROM kabupaten")
df_old_kab = pd.DataFrame(cursor_old.fetchall())

cursor_old.execute("SELECT idkecamatan, idkabupaten, nama FROM kecamatan")
df_old_kec = pd.DataFrame(cursor_old.fetchall())

cursor_old.execute("SELECT idkelurahan, idkecamatan, nama FROM kelurahan")
df_old_kel = pd.DataFrame(cursor_old.fetchall())

# 2. Load new tables
print("Loading new tables...")
cursor_new.execute("SELECT id_provinsi, nama_provinsi FROM provinsi")
df_new_prov = pd.DataFrame(cursor_new.fetchall())

cursor_new.execute("SELECT id_kabupaten, id_provinsi, nama_kabupaten FROM kabupaten")
df_new_kab = pd.DataFrame(cursor_new.fetchall())

cursor_new.execute("SELECT id_kecamatan, id_kabupaten, nama_kecamatan FROM kecamatan")
df_new_kec = pd.DataFrame(cursor_new.fetchall())

cursor_new.execute("SELECT id_kelurahan, id_kecamatan, nama_kelurahan FROM kelurahan")
df_new_kel = pd.DataFrame(cursor_new.fetchall())

# Robust clean function
def clean_wil_name(s):
    if pd.isna(s): return ""
    s = str(s).strip().lower()
    s = re.sub(r'\b(kabupaten|kab|kota|kecamatan|kec|kelurahan|kel|desa|adm)\b\.?', '', s)
    s = s.replace('\'', '').replace('`', '').replace('-', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    return s

start_time = time.time()

df_old_prov['clean'] = df_old_prov['nama'].apply(clean_wil_name)
df_new_prov['clean'] = df_new_prov['nama_provinsi'].apply(clean_wil_name)
df_old_kab['clean'] = df_old_kab['name'].apply(clean_wil_name)
df_new_kab['clean'] = df_new_kab['nama_kabupaten'].apply(clean_wil_name)
df_old_kec['clean'] = df_old_kec['nama'].apply(clean_wil_name)
df_new_kec['clean'] = df_new_kec['nama_kecamatan'].apply(clean_wil_name)
df_old_kel['clean'] = df_old_kel['nama'].apply(clean_wil_name)
df_new_kel['clean'] = df_new_kel['nama_kelurahan'].apply(clean_wil_name)

# 4. Create Provinsi Mapping
prov_map = {}
for _, row in df_old_prov.iterrows():
    match = df_new_prov[df_new_prov['clean'] == row['clean']]
    if not match.empty:
        prov_map[row['idprovinsi']] = match.iloc[0]['id_provinsi']

# 5. Create Kabupaten Mapping
kab_map = {}
df_new_kab['key'] = df_new_kab['clean'] + "_" + df_new_kab['id_provinsi'].astype(str)
for _, row in df_old_kab.iterrows():
    new_prov_id = prov_map.get(row['idprovinsi'])
    if new_prov_id:
        key = row['clean'] + "_" + str(new_prov_id)
        match = df_new_kab[df_new_kab['key'] == key]
        if not match.empty:
            kab_map[row['idkabupaten']] = match.iloc[0]['id_kabupaten']

# 6. Create Kecamatan Mapping
kec_map = {}
df_new_kec['key'] = df_new_kec['clean'] + "_" + df_new_kec['id_kabupaten'].astype(str)
for _, row in df_old_kec.iterrows():
    new_kab_id = kab_map.get(row['idkabupaten'])
    if new_kab_id:
        key = row['clean'] + "_" + str(new_kab_id)
        match = df_new_kec[df_new_kec['key'] == key]
        if not match.empty:
            kec_map[row['idkecamatan']] = match.iloc[0]['id_kecamatan']

# 7. Create Kelurahan Mapping (VECTORIZED MERGE!)
# Map idkecamatan to new_kec_id
df_old_kel['new_kec_id'] = df_old_kel['idkecamatan'].map(kec_map)

# Filter out rows with no new_kec_id
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

print(f"Time taken to clean & map: {time.time() - start_time:.4f} seconds")

# 8. Load old siswa
cursor_old.execute("SELECT idsiswa, nama_lengkap, provinsi, kabupaten, kecamatan, kelurahan FROM siswa")
df_siswa = pd.DataFrame(cursor_old.fetchall())

df_siswa_with_geo = df_siswa[df_siswa['provinsi'].notna() & (df_siswa['provinsi'] != '') & (df_siswa['provinsi'] != '-')]
df_siswa_with_geo = df_siswa_with_geo.copy()

df_siswa_with_geo['new_provinsi'] = df_siswa_with_geo['provinsi'].map(prov_map)
df_siswa_with_geo['new_kabupaten'] = df_siswa_with_geo['kabupaten'].map(kab_map)
df_siswa_with_geo['new_kecamatan'] = df_siswa_with_geo['kecamatan'].map(kec_map)
df_siswa_with_geo['new_kelurahan'] = df_siswa_with_geo['kelurahan'].map(kel_map)

mapped_kel = df_siswa_with_geo['new_kelurahan'].notna().sum()
print(f"Kelurahan mapped: {mapped_kel} / {len(df_siswa_with_geo)} ({mapped_kel/len(df_siswa_with_geo)*100:.2f}%)")

cursor_old.close()
cursor_new.close()
db_old.close()
db_new.close()
