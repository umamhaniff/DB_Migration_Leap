import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

cursor.execute("SELECT idmitra, nama, instansi, status FROM mitra LIMIT 10")
for r in cursor.fetchall():
    print(r)

cursor.close()
conn_old.close()
