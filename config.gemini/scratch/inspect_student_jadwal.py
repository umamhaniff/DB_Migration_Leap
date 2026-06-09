import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

cursor.execute("SELECT idsiswa, idjadwal FROM jadwal_siswa WHERE idsiswa = 'S0000283'")
rows = cursor.fetchall()
print("--- db_old.jadwal_siswa for S0000283 ---")
for r in rows:
    print(r)

cursor.close()
conn_old.close()
