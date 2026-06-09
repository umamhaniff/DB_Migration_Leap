import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor = conn_new.cursor(dictionary=True)

# Check schema description
cursor.execute("DESCRIBE pengajuan_karyawan")
schema = cursor.fetchall()
print("--- Schema of db_new.pengajuan_karyawan ---")
for col in schema:
    print(col)

cursor.close()
conn_new.close()
