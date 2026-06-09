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

cursor = db_old.cursor(dictionary=True)
cursor.execute("SELECT idp_nilai FROM parameter_nilai ORDER BY idp_nilai")
rows = cursor.fetchall()

print(f"Total rows: {len(rows)}")
print(f"First row: {rows[0]['idp_nilai']}")
print(f"Last row: {rows[-1]['idp_nilai']}")

# Check if there are any gaps
ids_ints = []
for r in rows:
    val = r['idp_nilai']
    num = int(val[1:])
    ids_ints.append(num)

gaps = []
for i in range(len(ids_ints) - 1):
    diff = ids_ints[i+1] - ids_ints[i]
    if diff > 1:
        gaps.append((rows[i]['idp_nilai'], rows[i+1]['idp_nilai'], diff))

print(f"Number of gaps found: {len(gaps)}")
if gaps:
    print("Gaps sample:")
    for g in gaps[:10]:
        print(f"  Between {g[0]} and {g[1]} (diff: {g[2]})")

db_old.close()
