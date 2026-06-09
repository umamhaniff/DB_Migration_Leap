import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

names = [
    'Ni Putu Jayanti Nirmala Pradnya Santosa',
    'Reza Ananda Pratama',
    'Intan Adelia Safitri',
    'Achmad Ferdiansyah'
]

print("--- Raw db_old.pelamar records for specific names ---")
for name in names:
    cursor.execute("SELECT idpelamar, idpengajuan, nama FROM pelamar WHERE nama LIKE %s", (f"%{name.strip()}%",))
    rows = cursor.fetchall()
    for r in rows:
        print(r)

cursor.close()
conn_old.close()
