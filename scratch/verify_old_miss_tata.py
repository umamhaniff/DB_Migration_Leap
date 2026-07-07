import os
import sys
import mysql.connector
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    # Check for Miss Tata or CC Convo in db_old.mitra
    cursor_old.execute("SELECT idmitra, nama, instansi FROM mitra WHERE nama LIKE '%Tata%' OR instansi LIKE '%Convo%' OR idmitra = 'M00021'")
    rows = cursor_old.fetchall()
    print("Miss Tata in db_old.mitra:")
    for r in rows:
        print(r)
        
    conn_old.close()

if __name__ == '__main__':
    main()
