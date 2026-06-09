import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_old = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", 3307)),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database="dataleap_v5_example",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)
db_new = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", 3307)),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database="dataleap_v5_migration",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

cursor_old = db_old.cursor(dictionary=True)
cursor_new = db_new.cursor(dictionary=True)

# Inspect parameter_nilai in old database
try:
    cursor_old.execute("DESCRIBE parameter_nilai")
    print("Old DB 'parameter_nilai' schema:")
    for r in cursor_old.fetchall():
        print(f"  {r['Field']}: {r['Type']}")
    
    cursor_old.execute("SELECT * FROM parameter_nilai LIMIT 5")
    print("\nOld DB 'parameter_nilai' samples:")
    for r in cursor_old.fetchall():
        print(r)
except Exception as e:
    print("Error querying old DB parameter_nilai:", e)

# Inspect parameter_nilai in new database
try:
    cursor_new.execute("SELECT * FROM parameter_nilai LIMIT 5")
    print("\nNew DB 'parameter_nilai' samples:")
    for r in cursor_new.fetchall():
        print(r)
except Exception as e:
    print("Error querying new DB parameter_nilai:", e)

db_old.close()
db_new.close()
