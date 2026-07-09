import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_old'])
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pelamar")
    print(f"Old pelamar table count: {cursor.fetchone()[0]}")
    conn.close()

if __name__ == '__main__':
    main()
