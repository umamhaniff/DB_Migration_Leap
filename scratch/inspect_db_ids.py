import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config
import pandas as pd

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
conn_new = mysql.connector.connect(**cfg['db_new'])

cursor_old = conn_old.cursor(dictionary=True)
cursor_new = conn_new.cursor(dictionary=True)

# 1. Check a few rows of db_old.pelamar
cursor_old.execute("SELECT idpelamar, idpengajuan, nama FROM pelamar WHERE idpengajuan IS NOT NULL LIMIT 10")
old_pelamar = cursor_old.fetchall()
print("--- db_old.pelamar sample ---")
for r in old_pelamar:
    print(r)

# 2. Check a few rows of db_old.pengajuan
cursor_old.execute("SELECT idpengajuan, keterangan FROM pengajuan LIMIT 10")
old_pengajuan = cursor_old.fetchall()
print("\n--- db_old.pengajuan sample ---")
for r in old_pengajuan:
    print(r)

# 3. Check a few rows of db_new.pengajuan_karyawan
cursor_new.execute("SELECT id_pengajuan, posisi FROM pengajuan_karyawan LIMIT 10")
new_pengajuan = cursor_new.fetchall()
print("\n--- db_new.pengajuan_karyawan sample ---")
for r in new_pengajuan:
    print(r)

cursor_old.close()
cursor_new.close()
conn_old.close()
conn_new.close()
