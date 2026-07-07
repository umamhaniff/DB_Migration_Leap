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
    
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    # Check S0000027 (FATIMAH NADA SAKINAH QOLBI) in old database
    cursor_old.execute(
        "SELECT js.*, j.idpendkursus FROM jadwal_siswa js JOIN jadwal j ON js.idjadwal = j.idjadwal WHERE js.idsiswa = 'S0000027'"
    )
    old_c = cursor_old.fetchall()
    print("Old DB courses for S0000027 (pkl_id: 21):", [x['idpendkursus'] for x in old_c])
    
    # Check id_siswa = 21 (EZRA RAFA DANAR) in new database
    cursor_new.execute("SELECT * FROM kursus_siswa WHERE id_siswa = 21")
    new_c = cursor_new.fetchall()
    print("New DB courses for id_siswa = 21 (EZRA RAFA DANAR):", [x['id_kursus'] for x in new_c])
    
    conn_old.close()
    conn_new.close()

if __name__ == '__main__':
    main()
