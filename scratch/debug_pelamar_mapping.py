import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Database config
db_config_old = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3307)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_OLD', 'dataleap_v5_example_new'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

conn = mysql.connector.connect(**db_config_old)
cursor = conn.cursor(dictionary=True)

# Get all idpelamar from old pelamar table
cursor.execute("SELECT idpelamar FROM pelamar")
old_pelamars = set(r['idpelamar'] for r in cursor.fetchall())

# Get all idpelamar from old pelamar_users table
cursor.execute("SELECT idusers, idpelamar FROM pelamar_users")
pelamar_users = cursor.fetchall()

missing_in_pelamar = []
for pu in pelamar_users:
    if pu['idpelamar'] not in old_pelamars:
        missing_in_pelamar.append(pu)

print(f"Total rows in pelamar_users: {len(pelamar_users)}")
print(f"Total unique idpelamar in old pelamar table: {len(old_pelamars)}")
print(f"Total rows in pelamar_users whose idpelamar is NOT in the old pelamar table: {len(missing_in_pelamar)}")
print("First 20 missing mapping rows:")
for row in missing_in_pelamar[:20]:
    print(row)

cursor.close()
conn.close()
