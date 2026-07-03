import os
import mysql.connector
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

# List all tables and counts in old DB
cursor.execute("SHOW TABLES")
tables = [list(row.values())[0] for row in cursor.fetchall()]
print(f"Total tables in old DB: {len(tables)}")

# Look for mitra/siswa related tables and check their row counts
for tbl in sorted(tables):
    if any(x in tbl.lower() for x in ['mitra', 'siswa', 'pelamar', 'rapor']):
        cursor.execute(f"SELECT COUNT(*) as cnt FROM `{tbl}`")
        cnt = cursor.fetchone()['cnt']
        print(f"Old Table `{tbl}`: {cnt} rows")

cursor.close()
conn.close()
