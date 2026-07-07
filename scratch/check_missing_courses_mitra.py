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
    print(f"Parsed {len(students)} students from questions.md.")
    
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    # 1. Fetch all student mappings by matching name and old ID
    # Since we know there is some mismatch in IDs, let's map them by name
    cursor_new.execute("SELECT id_siswa, nama_lengkap, id_mitra, nomor_induk FROM siswa")
    db_new_siswa = {r['nama_lengkap'].lower().strip(): r for r in cursor_new.fetchall()}
    
    # Check each student
    results = []
    for s in students:
        name_lower = s['nama_lengkap'].lower().strip()
        new_s = db_new_siswa.get(name_lower)
        
        # If not found by name, try fallback search
        if not new_s:
            cursor_new.execute("SELECT id_siswa, nama_lengkap, id_mitra, nomor_induk FROM siswa WHERE LOWER(nama_lengkap) LIKE %s", (f"%{name_lower}%",))
            matches = cursor_new.fetchall()
            if matches:
                new_s = matches[0]
                
        if new_s:
            new_id = new_s['id_siswa']
            new_id_mitra = new_s['id_mitra']
            
            # Fetch old student info
            cursor_old.execute("SELECT idsiswa, idmitra, keluar, lulus FROM siswa WHERE LOWER(nama_lengkap) = %s", (new_s['nama_lengkap'].lower(),))
            old_s_rows = cursor_old.fetchall()
            old_id = old_s_rows[0]['idsiswa'] if old_s_rows else None
            old_id_mitra = old_s_rows[0]['idmitra'] if old_s_rows else None
            
            # Fetch db_new.kursus_siswa
            cursor_new.execute("SELECT * FROM kursus_siswa WHERE id_siswa = %s", (new_id,))
            ks_new = cursor_new.fetchall()
            
            # Fetch db_new.siswa_keluar
            cursor_new.execute("SELECT * FROM siswa_keluar WHERE id_siswa = %s", (new_id,))
            sk_new = cursor_new.fetchall()
            
            # Fetch db_old course info (from jadwal_siswa -> jadwal)
            old_courses = []
            if old_id:
                cursor_old.execute(
                    "SELECT js.*, j.idpendkursus FROM jadwal_siswa js JOIN jadwal j ON js.idjadwal = j.idjadwal WHERE js.idsiswa = %s",
                    (old_id,)
                )
                old_courses = cursor_old.fetchall()
                
            results.append({
                'name': s['nama_lengkap'],
                'no_induk_q': s['nomor_induk'],
                'kursus_q': s['kursus'],
                'tipe_q': s['tipe_kursus'],
                'new_id': new_id,
                'new_id_mitra': new_id_mitra,
                'old_id': old_id,
                'old_id_mitra': old_id_mitra,
                'ks_new': ks_new,
                'sk_new': sk_new,
                'old_courses': old_courses
            })
        else:
            results.append({
                'name': s['nama_lengkap'],
                'no_induk_q': s['nomor_induk'],
                'new_id': None
            })
            
    print("\n--- Summary of Findings ---")
    missing_ks = 0
    missing_sk = 0
    mitra_mismatches = 0
    for r in results:
        if not r['new_id']:
            print(f"Siswa {r['name']} ({r['no_induk_q']}) NOT FOUND in new DB.")
            continue
            
        ks_str = ", ".join([f"{k['id_kursus']} (status_aktif: {k['status_aktif']})" for k in r['ks_new']]) if r['ks_new'] else "None"
        sk_str = ", ".join([f"{k['id_kursus']} (alasan: {k['alasan_keluar']})" for k in r['sk_new']]) if r['sk_new'] else "None"
        old_c_str = ", ".join([k['idpendkursus'] for k in r['old_courses']]) if r['old_courses'] else "None"
        
        # Check if missing kursus_siswa or siswa_keluar
        if not r['ks_new']:
            missing_ks += 1
        if not r['sk_new']:
            missing_sk += 1
            
        # Check if id_mitra is consistent
        mitra_status = f"Old Mitra: {r['old_id_mitra']} | New id_mitra: {r['new_id_mitra']}"
        
        print(f"Name: {r['name']} (ID: {r['new_id']})\n"
              f"  - Old courses: {old_c_str}\n"
              f"  - New kursus_siswa: {ks_str}\n"
              f"  - New siswa_keluar: {sk_str}\n"
              f"  - {mitra_status}")
              
    print(f"\nTotal students missing from kursus_siswa: {missing_ks}/{len(results)}")
    print(f"Total students missing from siswa_keluar: {missing_sk}/{len(results)}")

    conn_old.close()
    conn_new.close()

if __name__ == '__main__':
    main()
