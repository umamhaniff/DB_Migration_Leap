import os
import sys
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    cursor_new.execute("SELECT id_siswa, id_kursus, alasan_keluar, tanggal_keluar FROM siswa_keluar WHERE id_kursus IS NULL")
    rows = cursor_new.fetchall()
    print("Rows in db_new.siswa_keluar with id_kursus IS NULL:")
    for r in rows:
        # Get student name
        cursor_new.execute("SELECT nama_lengkap FROM siswa WHERE id_siswa = %s", (r['id_siswa'],))
        s_row = cursor_new.fetchone()
        name = s_row['nama_lengkap'] if s_row else "Unknown"
        print(f"ID Siswa: {r['id_siswa']} | Name: {name:<25} | Alasan: {r['alasan_keluar']} | Tanggal: {r['tanggal_keluar']}")
        
    conn_new.close()

if __name__ == '__main__':
    main()
