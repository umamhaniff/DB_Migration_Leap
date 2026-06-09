import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

cursor.execute("SELECT idsiswa, nama_lengkap, email FROM siswa WHERE idsiswa IN ('S0000283', 'S0002283')")
rows = cursor.fetchall()
print("--- db_old.siswa matching IDs ---")
for r in rows:
    print(r)

# Let's count how many students have '283' in their id
cursor.execute("SELECT idsiswa, nama_lengkap FROM siswa WHERE idsiswa LIKE '%283%'")
rows_2 = cursor.fetchall()
print("\n--- db_old.siswa containing '283' ---")
for r in rows_2:
    print(r)

cursor.close()
conn_old.close()
