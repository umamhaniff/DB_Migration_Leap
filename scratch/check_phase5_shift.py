import os
import sys
import mysql.connector
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    # Check count in db_new.rapor_siswa
    cursor_new.execute("SELECT COUNT(*) as count FROM rapor_siswa")
    print("New DB 'rapor_siswa' count:", cursor_new.fetchone()['count'])
    
    # Fetch some sample rows
    cursor_new.execute("SELECT * FROM rapor_siswa LIMIT 5")
    print("\nSample rapor_siswa rows:")
    for r in cursor_new.fetchall():
        print(r)
        
    conn_new.close()

if __name__ == '__main__':
    main()
