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
                if name and no_induk:
                    students.append({
                        'nama_lengkap': name,
                        'nomor_induk': no_induk
                    })
    return students

def main():
    students = parse_questions_md()
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    # Get all distinct idmitra for these students
    old_mitra_ids = set()
    for s in students:
        cursor_old.execute(
            "SELECT idmitra FROM siswa WHERE no_induk = %s OR LOWER(nama_lengkap) = LOWER(%s)", 
            (s['nomor_induk'], s['nama_lengkap'])
        )
        rows = cursor_old.fetchall()
        for r in rows:
            if r['idmitra']:
                old_mitra_ids.add(r['idmitra'])
                
    print("Old Mitra IDs referenced by these students:", old_mitra_ids)
    
    if old_mitra_ids:
        # Fetch their details from old DB
        format_strings = ','.join(['%s'] * len(old_mitra_ids))
        cursor_old.execute(f"SELECT idmitra, nama, instansi FROM mitra WHERE idmitra IN ({format_strings})", tuple(old_mitra_ids))
        mitra_old_rows = cursor_old.fetchall()
        print("\nDetails of these Mitra in Old DB:")
        for r in mitra_old_rows:
            print(f"ID: {r['idmitra']} | Name: {r['nama']} | Instansi: {r['instansi']}")
            
    conn_old.close()

if __name__ == '__main__':
    main()
