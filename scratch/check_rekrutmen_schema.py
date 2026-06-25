import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    port=int(os.getenv('DB_PORT', 3307)),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASS', ''),
    database=os.getenv('DB_NEW', 'dataleap_v5_migration'),
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
)

cursor = conn.cursor()
print("=== Target DB schema for rekrutmen_pelamar ===")
try:
    cursor.execute("DESCRIBE rekrutmen_pelamar")
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print(f"Error: {e}")
    
print("\n=== Target DB schema for progres_pelamar ===")
try:
    cursor.execute("DESCRIBE progres_pelamar")
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print(f"Error: {e}")

cursor.close()
conn.close()
