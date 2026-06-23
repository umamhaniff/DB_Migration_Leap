import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor = conn_new.cursor()

tables = ['pelamar', 'pelamar_sekolah', 'pelamar_kursus', 'progres_pelamar', 'rekrutmen_pelamar']

for t in tables:
    print(f"\n=== Columns for table: {t} ===")
    cursor.execute(f"DESCRIBE {t}")
    for row in cursor.fetchall():
        print(f"  {row[0]:<25} | {row[1]:<20} | Null: {row[2]:<4} | Default: {str(row[4]):<10} | Key: {row[3]}")

cursor.close()
conn_new.close()
