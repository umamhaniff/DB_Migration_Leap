import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor = conn_new.cursor(dictionary=True)

cursor.execute("DESCRIBE pelamar")
schema = cursor.fetchall()
print("--- Schema of db_new.pelamar ---")
for col in schema:
    if col['Field'] in ['id_pelamar', 'id_pengajuan']:
        print(col)

cursor.close()
conn_new.close()
