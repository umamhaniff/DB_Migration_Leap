import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor()

# Get all idsiswa in siswa
cursor.execute("SELECT idsiswa FROM siswa")
siswa_ids = set(r[0] for r in cursor.fetchall())

# Get all idsiswa in siswa_keluar
cursor.execute("SELECT DISTINCT idsiswa FROM siswa_keluar")
siswa_keluar_ids = set(r[0] for r in cursor.fetchall())

mismatches = siswa_keluar_ids - siswa_ids
print(f"Total distinct idsiswa in siswa_keluar: {len(siswa_keluar_ids)}")
print(f"Mismatched idsiswa (in siswa_keluar but not in siswa): {len(mismatches)}")
if mismatches:
    print("Mismatched examples:", list(mismatches)[:10])

cursor.close()
conn_old.close()
