import os
import sys
import mysql.connector
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config
from scratch.investigate_questions import parse_questions_md

def main():
    students = parse_questions_md()
    cfg = get_db_config()
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    # Pre-fetch students by name
    cursor_new.execute("SELECT id_siswa, nama_lengkap, id_mitra, nomor_induk FROM siswa")
    db_students = {r['nama_lengkap'].lower().strip(): r for r in cursor_new.fetchall()}
    
    print("--- Database Verification of the 47 Students ---")
    correct_count = 0
    
    for idx, s in enumerate(students):
        name_clean = s['nama_lengkap'].lower().strip()
        db_s = db_students.get(name_clean)
        
        if not db_s:
            # try contains
            for n, r in db_students.items():
                if name_clean in n or n in name_clean:
                    db_s = r
                    break
                    
        if db_s:
            id_siswa = db_s['id_siswa']
            id_mitra = db_s['id_mitra']
            
            # Fetch kursus_siswa
            cursor_new.execute("SELECT * FROM kursus_siswa WHERE id_siswa = %s", (id_siswa,))
            ks_rows = cursor_new.fetchall()
            ks_courses = [r['id_kursus'] for r in ks_rows]
            
            # Fetch siswa_keluar
            cursor_new.execute("SELECT * FROM siswa_keluar WHERE id_siswa = %s", (id_siswa,))
            sk_rows = cursor_new.fetchall()
            sk_courses = [r['id_kursus'] for r in sk_rows]
            
            # Verify B2B partner
            partner_ok = True
            if "SHAQUEENA" in s['nama_lengkap']:
                partner_ok = (id_mitra == 21)
            elif "YUDISTIRA" in s['nama_lengkap']:
                partner_ok = (id_mitra == 16)
                
            has_records = len(ks_courses) > 0 and len(sk_courses) > 0
            
            if has_records and partner_ok:
                correct_count += 1
                if idx < 10 or "SHAQUEENA" in s['nama_lengkap'] or "YUDISTIRA" in s['nama_lengkap']:
                    print(f"[OK] {s['nama_lengkap']:<35} | ID: {id_siswa:<4} | Mitra: {id_mitra} | KS: {ks_courses} | SK: {sk_courses}")
            else:
                print(f"[FAIL] {s['nama_lengkap']:<35} | ID: {id_siswa:<4} | Mitra: {id_mitra} | KS: {ks_courses} | SK: {sk_courses} | Partner OK: {partner_ok}")
        else:
            print(f"[NOT FOUND] {s['nama_lengkap']}")
            
    print(f"\nVerification finished: {correct_count} out of {len(students)} students are fully corrected and verified in the database!")
    conn_new.close()

if __name__ == '__main__':
    main()
