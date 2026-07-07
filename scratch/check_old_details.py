import os
import sys
import pandas as pd
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
    
    print("--- Detailed Records in db_old ---")
    for s in students:
        # Search old DB
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
            
        if rows:
            for r in rows:
                idsiswa = r['idsiswa']
                # Get old siswa_keluar info
                cursor_old.execute("SELECT * FROM siswa_keluar WHERE idsiswa = %s", (idsiswa,))
                sk_rows = cursor_old.fetchall()
                sk_info = []
                for sk in sk_rows:
                    sk_info.append(f"alasan: {sk['alasan']}, tanggal: {sk['tanggal']}, idsiswa_keluar: {sk['idsiswa_keluar']}")
                
                # Get old jadwal_siswa info
                cursor_old.execute(
                    "SELECT js.*, j.idpendkursus, j.mode_belajar FROM jadwal_siswa js JOIN jadwal j ON js.idjadwal = j.idjadwal WHERE js.idsiswa = %s",
                    (idsiswa,)
                )
                js_rows = cursor_old.fetchall()
                js_info = []
                for js in js_rows:
                    js_info.append(f"idjadwal: {js['idjadwal']}, kursus: {js['idpendkursus']}, is_keluar: {js['is_keluar']}, is_lulus: {js['is_lulus']}")
                
                print(f"Name: {r['nama_lengkap']} ({idsiswa}) | no_induk: {r['no_induk']} | idmitra: {r['idmitra']}")
                print(f"  Old siswa_keluar records: {sk_info}")
                print(f"  Old KBM (jadwal_siswa) records: {js_info}")
        else:
            print(f"Name: {s['nama_lengkap']} ({s['nomor_induk']}) | NOT FOUND AT ALL IN DB_OLD")
            
    conn_old.close()

if __name__ == '__main__':
    main()
