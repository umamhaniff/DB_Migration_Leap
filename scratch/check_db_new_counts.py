import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_new = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", 3307)),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database="dataleap_v5_migration",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

cursor = db_new.cursor()
cursor.execute("SHOW TABLES")
tables = [t[0] for t in cursor.fetchall()]

print("Row counts in dataleap_v5_migration:")
for t in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {t}")
    cnt = cursor.fetchone()[0]
    if cnt > 0:
        print(f"  - {t}: {cnt} rows")

db_new.close()
