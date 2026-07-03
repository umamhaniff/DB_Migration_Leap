import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Database config for db_old
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3307)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_OLD', 'dataleap_v5_example_new'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

# Select all from pelamar_users for idusers: U00020, U00014, U00015, U00016, U00018
cursor.execute("SELECT idusers, idpelamar FROM pelamar_users WHERE idusers IN ('U00020', 'U00014', 'U00015', 'U00016', 'U00018')")
rows = cursor.fetchall()
print("Raw pelamar_users table for target users:")
print(pd.DataFrame(rows))

# Check in old database's pelamar table to see if those idpelamar exist
idpelamars = [r['idpelamar'] for r in rows if r['idpelamar'] is not None]
if idpelamars:
    placeholders = ', '.join(['%s'] * len(idpelamars))
    cursor.execute(f"SELECT idpelamar, nama FROM pelamar WHERE idpelamar IN ({placeholders})", idpelamars)
    print("\nCorresponding rows in old pelamar table:")
    print(pd.DataFrame(cursor.fetchall()))
else:
    print("\nNo idpelamar values found in raw pelamar_users for these users.")

cursor.close()
conn.close()
