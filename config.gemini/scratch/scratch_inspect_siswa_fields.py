import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor = conn_new.cursor()

cursor.execute("DESCRIBE siswa")
for row in cursor.fetchall():
    if row[0] in ['jenis_kelamin', 'tanggal_registrasi']:
        print(row)

cursor.close()
conn_new.close()
