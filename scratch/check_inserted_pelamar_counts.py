import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    tables = [
        'pelamar',
        'pelamar_kerja',
        'pelamar_sekolah',
        'pelamar_kursus',
        'progres_pelamar',
        'rekrutmen_pelamar'
    ]
    
    print("=== Row counts in db_new ===")
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
        count = cursor.fetchone()[0]
        print(f"Table {table}: {count} rows")
        
    conn.close()

if __name__ == '__main__':
    main()
