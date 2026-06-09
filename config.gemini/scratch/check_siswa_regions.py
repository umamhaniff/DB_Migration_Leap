import sys
import os
import re
import pandas as pd
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor_old = conn_old.cursor(dictionary=True)
cursor_new = conn_new.cursor(dictionary=True)

# Fetch region data
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

# Clean function with space removal
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

# Fetch students
cursor_old.execute("SELECT idsiswa, provinsi, kabupaten, kecamatan, kelurahan, idmitra FROM siswa")
df_siswa = pd.DataFrame(cursor_old.fetchall())

df_siswa['id_provinsi'] = df_siswa['provinsi'].map(prov_map).astype('Int64')
df_siswa['id_kabupaten'] = df_siswa['kabupaten'].map(kab_map).astype('Int64')
df_siswa['id_kecamatan'] = df_siswa['kecamatan'].map(kec_map).astype('Int64')
df_siswa['id_kelurahan'] = df_siswa['kelurahan'].map(kel_map).astype('Int64')

def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\d+', str(s))
    return int(nums[0]) if nums else None
df_siswa['id_mitra'] = df_siswa['idmitra'].apply(extract_int).astype('Int64')

print(f"Total students: {len(df_siswa)}")
print(f"Mapped provinsi: {df_siswa['id_provinsi'].notna().sum()} | Null: {df_siswa['id_provinsi'].isna().sum()}")
print(f"Mapped kabupaten: {df_siswa['id_kabupaten'].notna().sum()} | Null: {df_siswa['id_kabupaten'].isna().sum()}")
print(f"Mapped kecamatan: {df_siswa['id_kecamatan'].notna().sum()} | Null: {df_siswa['id_kecamatan'].isna().sum()}")
print(f"Mapped kelurahan: {df_siswa['id_kelurahan'].notna().sum()} | Null: {df_siswa['id_kelurahan'].isna().sum()}")
print(f"Mapped mitra: {df_siswa['id_mitra'].notna().sum()} | Null: {df_siswa['id_mitra'].isna().sum()}")

# Print first few rows of mapped values
print("\nSample mapped rows:")
print(df_siswa[['idsiswa', 'provinsi', 'id_provinsi', 'kabupaten', 'id_kabupaten', 'kecamatan', 'id_kecamatan', 'kelurahan', 'id_kelurahan', 'id_mitra']].head(10))

cursor_old.close()
cursor_new.close()
conn_old.close()
conn_new.close()
