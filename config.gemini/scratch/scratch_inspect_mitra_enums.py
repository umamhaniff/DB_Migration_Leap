import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor()

print("--- Unique jenis in old DB mitra ---")
cursor.execute("SELECT DISTINCT jenis FROM mitra")
for r in cursor.fetchall():
    print(r)

print("\n--- Unique jeniskemitraan in old DB mitra ---")
cursor.execute("SELECT DISTINCT jeniskemitraan FROM mitra")
for r in cursor.fetchall():
    print(r)

cursor.close()
conn_old.close()
