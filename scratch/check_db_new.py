import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Database config for db_new
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3307)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NEW', 'dataleap_v5_migration'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

print("--- INSPECTING TARGET DATABASE (DB_NEW) ---")

# Check mitra
try:
    cursor.execute("SELECT COUNT(*) as count FROM mitra")
    m_count = cursor.fetchone()['count']
    print(f"Total rows in db_new.mitra: {m_count}")
    
    if m_count > 0:
        cursor.execute("SELECT id_mitra, nama_mitra, kode_mitra FROM mitra LIMIT 10")
        print("First 10 rows in db_new.mitra:")
        print(pd.DataFrame(cursor.fetchall()))
except Exception as e:
    print(f"Error reading db_new.mitra: {e}")

# Check siswa
try:
    cursor.execute("SELECT COUNT(*) as count FROM siswa")
    s_count = cursor.fetchone()['count']
    print(f"\nTotal rows in db_new.siswa: {s_count}")
    
    if s_count > 0:
        cursor.execute("SELECT id_siswa, nama_lengkap, nomor_induk FROM siswa LIMIT 10")
        print("First 10 rows in db_new.siswa:")
        print(pd.DataFrame(cursor.fetchall()))
except Exception as e:
    print(f"Error reading db_new.siswa: {e}")

cursor.close()
conn.close()
