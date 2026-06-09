import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor = conn_new.cursor(dictionary=True)

cursor.execute("DESCRIBE mitra_progres")
schema = cursor.fetchall()
print("--- Schema of db_new.mitra_progres ---")
for col in schema:
    if col['Field'] == 'id_mitra':
        print(col)

cursor.close()
conn_new.close()
