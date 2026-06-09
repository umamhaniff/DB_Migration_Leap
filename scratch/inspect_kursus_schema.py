import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor = conn_new.cursor(dictionary=True)

for t in ['kursus', 'kursus_siswa']:
    cursor.execute(f"DESCRIBE {t}")
    schema = cursor.fetchall()
    print(f"--- Schema of db_new.{t} ---")
    for col in schema:
        if col['Field'] == 'id_kursus':
            print(col)

cursor.close()
conn_new.close()
