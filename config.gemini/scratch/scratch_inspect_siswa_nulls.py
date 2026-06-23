import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor()

cursor.execute("SELECT COUNT(*) FROM siswa WHERE tgl_daftar IS NULL OR tgl_daftar = ''")
print("Null/empty tgl_daftar in old DB:", cursor.fetchone()[0])

cursor.close()
conn_old.close()
