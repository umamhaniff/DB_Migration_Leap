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
    
    cursor_new.execute("SELECT id_mitra, nama_mitra, nama_instansi, kode_mitra FROM mitra")
    rows = cursor_new.fetchall()
    print("Mitra in db_new.mitra:")
    for r in rows:
        print(f"ID: {r['id_mitra']} | Name: {r['nama_mitra']} | Instansi: {r['nama_instansi']} | Code: {r['kode_mitra']}")
        
    conn_new.close()

if __name__ == '__main__':
    main()
