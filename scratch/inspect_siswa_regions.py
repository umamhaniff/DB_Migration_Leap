import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

cursor.execute("SELECT idsiswa, provinsi, kabupaten, kecamatan, kelurahan, idmitra FROM siswa LIMIT 10")
rows = cursor.fetchall()
print("--- Raw db_old.siswa region columns ---")
for r in rows:
    print(r)

cursor.close()
conn_old.close()
