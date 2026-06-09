import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
import re
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor_old = conn_old.cursor(dictionary=True)
cursor_new = conn_new.cursor(dictionary=True)

# Fetch data as done in apply_migration_updates
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
    s = re.sub(r'\b(kabupaten|kab|kota|kecamatan|kec|kelurahan|kel|desa|adm)\b\.?', '', s)
    s = s.replace('\'', '').replace('`', '').replace('-', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
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

print("--- prov_map sample ---")
print(list(prov_map.items())[:5])

# Print types of keys in prov_map
print("Key type in prov_map:", type(list(prov_map.keys())[0]) if prov_map else "empty")

# Fetch student data
cursor_old.execute("SELECT idsiswa, provinsi, kabupaten, kecamatan, kelurahan FROM siswa LIMIT 5")
df_siswa = pd.DataFrame(cursor_old.fetchall())
print("\n--- df_siswa types ---")
print(df_siswa.dtypes)

# Try mapping
df_siswa['id_provinsi'] = df_siswa['provinsi'].map(prov_map)
print("\n--- df_siswa mapped id_provinsi ---")
print(df_siswa[['idsiswa', 'provinsi', 'id_provinsi']])

cursor_old.close()
cursor_new.close()
conn_old.close()
conn_new.close()
