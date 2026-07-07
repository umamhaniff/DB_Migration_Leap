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
    
    # Select first 20 students from db_new
    cursor_new.execute("SELECT id_siswa, nama_lengkap, nomor_induk FROM siswa ORDER BY id_siswa LIMIT 30")
    rows = cursor_new.fetchall()
    print("First 30 rows in db_new.siswa:")
    for r in rows:
        print(f"ID: {r['id_siswa']} | Name: {r['nama_lengkap']} | No Induk: {r['nomor_induk']}")
        
    conn_new.close()

if __name__ == '__main__':
    main()
