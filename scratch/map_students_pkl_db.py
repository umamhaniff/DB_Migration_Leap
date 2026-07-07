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
    
    # Load mapping
    df_map = pd.read_pickle('fase_4/mapping_siswa.pkl')
    siswa_map = dict(zip(df_map['idsiswa_lama'], df_map['id_siswa_baru']))
    
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    # Pre-fetch new database students by name
    cursor_new.execute("SELECT id_siswa, nama_lengkap FROM siswa")
    new_db_students = {r['nama_lengkap'].lower().strip(): r['id_siswa'] for r in cursor_new.fetchall()}
    
    print("--- Pickle Mapping check for the 47 students ---")
    for s in students:
        # Search by name in old DB to get idsiswa
        cursor_old.execute("SELECT idsiswa, nama_lengkap FROM siswa WHERE LOWER(nama_lengkap) = %s", (s['nama_lengkap'].lower(),))
        old_rows = cursor_old.fetchall()
        if not old_rows:
            cursor_old.execute("SELECT idsiswa, nama_lengkap FROM siswa WHERE LOWER(nama_lengkap) LIKE %s", (f"%{s['nama_lengkap'].lower()}%",))
            old_rows = cursor_old.fetchall()
            
        for r in old_rows:
            old_id = r['idsiswa']
            pkl_mapped_id = siswa_map.get(old_id)
            new_db_id = new_db_students.get(r['nama_lengkap'].lower().strip())
            
            print(f"Name: {r['nama_lengkap']} | Old ID: {old_id} | pkl_mapped_id: {pkl_mapped_id} | new_db_id: {new_db_id} | Diff: {new_db_id - pkl_mapped_id if new_db_id and pkl_mapped_id else 'N/A'}")
            
    conn_old.close()
    conn_new.close()

if __name__ == '__main__':
    main()
