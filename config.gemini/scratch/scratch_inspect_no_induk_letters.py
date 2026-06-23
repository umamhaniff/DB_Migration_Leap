import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

# Fetch rows where no_induk contains alphabetical characters
cursor.execute("SELECT no_induk, idmitra, nama_lengkap FROM siswa WHERE no_induk REGEXP '[a-zA-Z]' LIMIT 30")
rows = cursor.fetchall()
print("Siswa with letters in no_induk count:", len(rows))
for r in rows:
    print(r)

# Check all unique no_induk prefix letters
cursor.execute("SELECT DISTINCT REGEXP_REPLACE(no_induk, '[0-9-]', '') as prefix, idmitra FROM siswa WHERE no_induk REGEXP '[a-zA-Z]'")
prefixes = cursor.fetchall()
print("\nUnique letter prefixes in no_induk:")
for p in prefixes:
    print(p)

cursor.close()
conn_old.close()
