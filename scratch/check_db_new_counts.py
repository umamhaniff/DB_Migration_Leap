import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    cursor.execute("SHOW TABLES")
    tables = [r[0] for r in cursor.fetchall()]
    
    print("=== Row counts in db_new ===")
    for table in tables:
        try:
            cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
            count = cursor.fetchone()[0]
            if count > 0 or table in ['pelamar', 'pengajuan_karyawan', 'histori_pengajuan']:
                print(f"Table {table}: {count} rows")
        except Exception as e:
            print(f"Table {table}: Error: {e}")
            
    conn.close()

if __name__ == '__main__':
    main()
