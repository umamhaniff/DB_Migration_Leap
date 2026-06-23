import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor()

print("--- Unique jk in old DB pelamar ---")
cursor.execute("SELECT DISTINCT jk FROM pelamar")
for r in cursor.fetchall():
    print(r)

print("\n--- Unique jkel in old DB siswa ---")
cursor.execute("SELECT DISTINCT jkel FROM siswa")
for r in cursor.fetchall():
    print(r)

cursor.close()
conn_old.close()
