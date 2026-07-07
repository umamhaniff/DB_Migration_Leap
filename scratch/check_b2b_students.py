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
    
    # Check AHMAD YUDISTIRA RACHMAN (ID: 1313)
    cursor_new.execute("SELECT id_siswa, nama_lengkap, id_mitra FROM siswa WHERE id_siswa = 1313")
    print("AHMAD YUDISTIRA RACHMAN in siswa:", cursor_new.fetchone())
    cursor_new.execute("SELECT * FROM kursus_siswa WHERE id_siswa = 1313")
    print("AHMAD YUDISTIRA RACHMAN in kursus_siswa:", cursor_new.fetchall())
    cursor_new.execute("SELECT * FROM siswa_keluar WHERE id_siswa = 1313")
    print("AHMAD YUDISTIRA RACHMAN in siswa_keluar:", cursor_new.fetchall())
    
    # Check SHAQUEENA NAUREEN (ID: 357)
    cursor_new.execute("SELECT id_siswa, nama_lengkap, id_mitra FROM siswa WHERE id_siswa = 357")
    print("\nSHAQUEENA NAUREEN in siswa:", cursor_new.fetchone())
    cursor_new.execute("SELECT * FROM kursus_siswa WHERE id_siswa = 357")
    print("SHAQUEENA NAUREEN in kursus_siswa:", cursor_new.fetchall())
    cursor_new.execute("SELECT * FROM siswa_keluar WHERE id_siswa = 357")
    print("SHAQUEENA NAUREEN in siswa_keluar:", cursor_new.fetchall())
    
    conn_new.close()

if __name__ == '__main__':
    main()
