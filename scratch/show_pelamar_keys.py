import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    cursor.execute("SHOW INDEX FROM pelamar")
    indexes = cursor.fetchall()
    
    print("=== Indexes on pelamar table ===")
    for idx in indexes:
        print(f"Table: {idx[0]}, Non_unique: {idx[1]}, Key_name: {idx[2]}, Column_name: {idx[4]}")
        
    conn.close()

if __name__ == '__main__':
    main()
