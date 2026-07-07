import os
import sys
import mysql.connector
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def parse_questions_md():
    path = "questions.md"
    students = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if "|" in line and "nama_lengkap" not in line and "---" not in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                name = parts[1]
                no_induk = parts[2]
                kursus = parts[3]
                tipe_kursus = parts[4]
                if name and no_induk:
                    students.append({
                        'nama_lengkap': name,
                        'nomor_induk': no_induk,
                        'kursus': kursus,
                        'tipe_kursus': tipe_kursus
                    })
    return students

def main():
    students = parse_questions_md()
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    print("--- Detailed Records in db_old (First 15) ---")
    for s in students[:15]:
        cursor_old.execute(
            "SELECT idsiswa, nama_lengkap, no_induk, idmitra, keluar, lulus FROM siswa WHERE no_induk = %s OR LOWER(nama_lengkap) = LOWER(%s)", 
            (s['nomor_induk'], s['nama_lengkap'])
        )
        rows = cursor_old.fetchall()
        if not rows:
            cursor_old.execute(
                "SELECT idsiswa, nama_lengkap, no_induk, idmitra, keluar, lulus FROM siswa WHERE LOWER(nama_lengkap) LIKE %s", 
                (f"%{s['nama_lengkap'].lower()}%",)
            )
            rows = cursor_old.fetchall()
            
        for r in rows:
            # check old siswa_keluar
            cursor_old.execute("SELECT * FROM siswa_keluar WHERE idsiswa = %s", (r['idsiswa'],))
            sk = cursor_old.fetchall()
            # check old KBM
            cursor_old.execute(
                "SELECT js.*, j.idpendkursus FROM jadwal_siswa js JOIN jadwal j ON js.idjadwal = j.idjadwal WHERE js.idsiswa = %s",
                (r['idsiswa'],)
            )
            js = cursor_old.fetchall()
            print(f"Name: {r['nama_lengkap']} | Old ID: {r['idsiswa']} | No Induk: {r['no_induk']} | Mitra: {r['idmitra']}")
            print(f"  siswa_keluar: {sk}")
            print(f"  jadwal_siswa: {[{'idjadwal': x['idjadwal'], 'id_kursus': x['idpendkursus']} for x in js]}")
            
    conn_old.close()

if __name__ == '__main__':
    main()
