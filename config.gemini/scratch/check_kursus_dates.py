import sys
import os
import pandas as pd
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor_old = conn_old.cursor(dictionary=True)

cursor_old.execute("SELECT idkursus, nama, tanggal FROM kursus")
df_kursus = pd.DataFrame(cursor_old.fetchall())

print("--- Raw dates in kursus table ---")
print(df_kursus['tanggal'].value_counts(dropna=False))
print("\nSample records:")
for _, row in df_kursus.iterrows():
    if pd.notna(row['tanggal']):
        print(f"ID: {row['idkursus']} | Nama: {row['nama']} | Tanggal: {row['tanggal']}")

cursor_old.close()
conn_old.close()
