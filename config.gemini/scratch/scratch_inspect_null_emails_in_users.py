import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

# Fetch the 20 records
cursor.execute("SELECT idpelamar, email FROM pelamar WHERE jk IS NULL OR jk = ''")
null_pels = cursor.fetchall()

print("=== Checking if applicant emails exist in users ===")
for p in null_pels:
    email = p['email']
    cursor.execute("SELECT idusers, nama, email FROM users WHERE LOWER(TRIM(email)) = %s", (email.strip().lower(),))
    u = cursor.fetchone()
    if u:
        print(f"idpelamar: {p['idpelamar']} -> idusers: {u['idusers']}, Name: {u['nama']}, Email: {u['email']}")
    else:
        print(f"idpelamar: {p['idpelamar']} -> Email {email} NOT found in users")

cursor.close()
conn_old.close()
