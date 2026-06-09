import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import mysql.connector
from config import get_db_config

# 1. Read from pickle
data = pd.read_pickle("fase_3/fase_3_hanif.pkl")
df_p = data.get("pelamar")
print("--- Pickle pelamar.id_pengajuan (first 10 non-null) ---")
print(df_p[df_p["id_pengajuan"].notna()][["id_pelamar", "id_pengajuan", "nama_lengkap"]].head(10))

# 2. Read from CSV
df_csv = pd.read_csv("extract/cek_csv/pelamar.csv")
print("\n--- CSV pelamar.id_pengajuan (first 10 non-null) ---")
print(df_csv[df_csv["id_pengajuan"].notna()][["id_pelamar", "id_pengajuan", "nama_lengkap"]].head(10))

# 3. Read raw from db_old
cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)
cursor.execute("SELECT idpelamar, idpengajuan, nama FROM pelamar WHERE idpengajuan IS NOT NULL LIMIT 10")
rows = cursor.fetchall()
print("\n--- db_old raw pelamar table (first 10 non-null) ---")
for r in rows:
    print(r)

# 4. Check if we have missing/different values
cursor.execute("SELECT COUNT(*) FROM pelamar WHERE idpengajuan IS NOT NULL")
total_non_null_old = cursor.fetchone()[0]
print(f"\nTotal non-null idpengajuan in db_old: {total_non_null_old}")
print(f"Total non-null id_pengajuan in df_p: {df_p['id_pengajuan'].notna().sum()}")

cursor.close()
conn_old.close()
