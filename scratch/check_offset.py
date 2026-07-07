import os
import sys
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    df_map = pd.read_pickle('fase_4/mapping_siswa.pkl')
    siswa_map = dict(zip(df_map['idsiswa_lama'], df_map['id_siswa_baru']))
    
    cfg = get_db_config()
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    cursor_new.execute("SELECT id_siswa, nama_lengkap, nomor_induk FROM siswa")
    db_siswa = cursor_new.fetchall()
    
    print(f"Total students in db_new.siswa: {len(db_siswa)}")
    print(f"Total mappings in mapping_siswa.pkl: {len(df_map)}")
    
    # We will try to match by name or nomor_induk (if not -)
    offsets = []
    mismatch_count = 0
    
    # Build dictionary of old students
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    cursor_old.execute("SELECT idsiswa, nama_lengkap, no_induk FROM siswa")
    old_students = {r['idsiswa']: r for r in cursor_old.fetchall()}
    conn_old.close()
    
    for old_id, new_id_pkl in siswa_map.items():
        old_stud = old_students.get(old_id)
        if not old_stud:
            continue
        old_name = old_stud['nama_lengkap'].lower().strip()
        old_no_induk = old_stud['no_induk']
        
        # Find in db_new
        match = None
        for s in db_siswa:
            if s['nama_lengkap'].lower().strip() == old_name:
                match = s
                break
        
        if match:
            db_id = match['id_siswa']
            diff = db_id - new_id_pkl
            offsets.append(diff)
        else:
            mismatch_count += 1
            
    if offsets:
        from collections import Counter
        c = Counter(offsets)
        print("Offset distribution (db_id - pkl_id):", c)
    else:
        print("No matches found to compute offsets.")
        
    print(f"Number of mapped students not found in db_new: {mismatch_count}")
    
    conn_new.close()

if __name__ == '__main__':
    main()
