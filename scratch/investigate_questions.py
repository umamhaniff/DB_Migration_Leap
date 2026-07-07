import os
import re
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
    
    # Load mapping_siswa.pkl if it exists
    siswa_map = {}
    if os.path.exists('fase_4/mapping_siswa.pkl'):
        df_map = pd.read_pickle('fase_4/mapping_siswa.pkl')
        siswa_map = dict(zip(df_map['idsiswa_lama'], df_map['id_siswa_baru']))
        print(f"Loaded {len(siswa_map)} mappings from mapping_siswa.pkl")

    print("\n--- Investigating Students ---")
    
    results = []
    for idx, s in enumerate(students):
        # 1. Search in db_old by nomor_induk or nama_lengkap
        cursor_old.execute(
            "SELECT * FROM siswa WHERE no_induk = %s OR LOWER(nama_lengkap) = LOWER(%s)", 
            (s['nomor_induk'], s['nama_lengkap'])
        )
        old_siswa = cursor_old.fetchall()
        
        if not old_siswa:
            # Try fuzzy check by name
            cursor_old.execute(
                "SELECT * FROM siswa WHERE LOWER(nama_lengkap) LIKE %s", 
                (f"%{s['nama_lengkap'].lower()}%",)
            )
            old_siswa = cursor_old.fetchall()
            
        if old_siswa:
            for os_row in old_siswa:
                idsiswa = os_row['idsiswa']
                nama_lengkap = os_row['nama_lengkap']
                no_induk = os_row['no_induk']
                idmitra = os_row['idmitra']
                keluar = os_row.get('keluar', None)
                lulus = os_row.get('lulus', None)
                
                # Check in db_old.siswa_keluar
                cursor_old.execute("SELECT * FROM siswa_keluar WHERE idsiswa = %s", (idsiswa,))
                sk_old = cursor_old.fetchall()
                
                # Check in db_old.jadwal_siswa
                cursor_old.execute(
                    "SELECT js.*, j.idpendkursus FROM jadwal_siswa js JOIN jadwal j ON js.idjadwal = j.idjadwal WHERE js.idsiswa = %s", 
                    (idsiswa,)
                )
                js_old = cursor_old.fetchall()
                
                # Check mapping
                mapped_new_id = siswa_map.get(idsiswa)
                
                # Check in db_new.siswa
                new_siswa_row = None
                if pd.notna(mapped_new_id):
                    cursor_new.execute("SELECT * FROM siswa WHERE id_siswa = %s", (int(mapped_new_id),))
                    new_siswa_row = cursor_new.fetchone()
                else:
                    # search by name or no_induk in db_new
                    cursor_new.execute(
                        "SELECT * FROM siswa WHERE nomor_induk = %s OR LOWER(nama_lengkap) = LOWER(%s)", 
                        (no_induk if no_induk else "", nama_lengkap)
                    )
                    new_siswa_row = cursor_new.fetchone()
                
                results.append({
                    'original': s,
                    'found_old': True,
                    'idsiswa_old': idsiswa,
                    'nama_lengkap_old': nama_lengkap,
                    'no_induk_old': no_induk,
                    'idmitra_old': idmitra,
                    'keluar_old': keluar,
                    'lulus_old': lulus,
                    'sk_old': sk_old,
                    'js_old': js_old,
                    'mapped_new_id': mapped_new_id,
                    'new_siswa_row': new_siswa_row
                })
        else:
            results.append({
                'original': s,
                'found_old': False
            })
            
    # Print summary
    found_count = sum(1 for r in results if r.get('found_old'))
    print(f"\nSummary: Found {found_count}/{len(students)} in old DB.")
    
    # Detail
    for r in results:
        orig = r['original']
        if not r.get('found_old'):
            print(f"MISSING IN OLD DB: {orig['nama_lengkap']} ({orig['nomor_induk']})")
        else:
            new_status = "Mapped to " + str(r['mapped_new_id']) if pd.notna(r['mapped_new_id']) else "Not Mapped"
            in_new_db = "Found in db_new (ID: " + str(r['new_siswa_row']['id_siswa']) + ")" if r['new_siswa_row'] else "NOT in db_new"
            sk_info = f"Old Exit Records: {len(r['sk_old'])}"
            js_info = f"Jadwal count: {len(r['js_old'])}"
            courses = [j['idpendkursus'] for j in r['js_old']]
            print(f"Old: {r['nama_lengkap_old']} ({r['idsiswa_old']}), no_induk: {r['no_induk_old']}, idmitra: {r['idmitra_old']}, keluar: {r['keluar_old']}, lulus: {r['lulus_old']} -> {new_status} ({in_new_db}) | {sk_info} | {js_info} (Courses: {courses})")

    conn_old.close()
    conn_new.close()

if __name__ == '__main__':
    main()
