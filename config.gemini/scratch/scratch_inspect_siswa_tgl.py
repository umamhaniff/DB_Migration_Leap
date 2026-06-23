import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor()

cursor.execute("SELECT tgl_daftar, COUNT(*) FROM siswa WHERE tgl_daftar IS NULL OR tgl_daftar = '0000-00-00' OR tgl_daftar < '2000-01-01' GROUP BY tgl_daftar")
for r in cursor.fetchall():
    print(r)

cursor.close()
conn_old.close()
