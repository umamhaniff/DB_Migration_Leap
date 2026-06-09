import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

# 1. Check a few records from db_old.siswa_keluar
cursor.execute("SELECT idsiswa, alasan, tanggal FROM siswa_keluar LIMIT 5")
old_sk = cursor.fetchall()
print("--- db_old.siswa_keluar sample ---")
for r in old_sk:
    print(r)

# 2. Check if student 'S0000283' or '283' exists in db_old.jadwal_siswa
cursor.execute("SELECT idsiswa, idjadwal FROM jadwal_siswa WHERE idsiswa LIKE '%283%' OR idsiswa = '283'")
rows_js = cursor.fetchall()
print("\n--- db_old.jadwal_siswa matching student '283' ---")
for r in rows_js:
    print(r)

# 3. Check what ID format is in db_old.jadwal_siswa
cursor.execute("SELECT idsiswa, idjadwal FROM jadwal_siswa LIMIT 5")
rows_js_sample = cursor.fetchall()
print("\n--- db_old.jadwal_siswa sample ---")
for r in rows_js_sample:
    print(r)

cursor.close()
conn_old.close()
