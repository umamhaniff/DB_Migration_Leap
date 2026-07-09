import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    for db_name in ['db_old', 'db_new']:
        print(f"\n=== Schema for {db_name} ({cfg[db_name]['database']}) ===")
        conn = mysql.connector.connect(**cfg[db_name])
        cursor = conn.cursor()
        
        try:
            cursor.execute("SHOW CREATE TABLE pelamar")
            create_table = cursor.fetchone()[1]
            print(create_table)
        except Exception as e:
            print(f"Error reading pelamar: {e}")
            
        conn.close()

if __name__ == '__main__':
    main()
