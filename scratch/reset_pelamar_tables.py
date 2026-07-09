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
        'pelamar_kerja',
        'pelamar_sekolah',
        'pelamar_kursus',
        'progres_pelamar',
        'rekrutmen_pelamar',
        'pelamar'
    ]
    
    print("Disabling foreign key checks...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    
    for table in tables:
        print(f"Truncating table {table}...")
        cursor.execute(f"TRUNCATE TABLE `{table}`")
        
    print("Enabling foreign key checks...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    
    conn.commit()
    conn.close()
    print("Truncation and reset completed successfully!")

if __name__ == '__main__':
    main()
