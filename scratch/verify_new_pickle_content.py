import pickle
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scratch.generate_audit_report import parse_questions_md

def main():
    with open('fase_4/fase_4_hanif.pkl', 'rb') as f:
        data = pickle.load(f)
        
    df_siswa = data['siswa']
    df_ks = data['kursus_siswa']
    df_sk = data['siswa_keluar']
    df_map = data['mapping_siswa']
    
    siswa_map = dict(zip(df_map['idsiswa_lama'], df_map['id_siswa_baru']))
    
    # Check SHAQUEENA NAUREEN (S0000351) in siswa
    shaq_row = df_siswa[df_siswa['nomor_induk'] == '20210000253']
    if not shaq_row.empty:
        print("SHAQUEENA NAUREEN id_mitra in pickle:", shaq_row.iloc[0]['id_mitra'])
    else:
        # try by name
        shaq_row_name = df_siswa[df_siswa['nama_lengkap'].str.contains('SHAQUEENA')]
        if not shaq_row_name.empty:
            print("SHAQUEENA NAUREEN id_mitra in pickle:", shaq_row_name.iloc[0]['id_mitra'])
        else:
            print("SHAQUEENA NAUREEN NOT FOUND in pickle siswa!")
            
    # Check course and exit logs for some of the 47 students in the pickle
    students = parse_questions_md()
    
    # Get ID mapping for these students
    print("\nPickle Audit of the 47 students:")
    found_count = 0
    has_ks = 0
    has_sk = 0
    
    # We will search old ID for each name
    # Get df of old siswa to match
    # Since we can't connect to old db easily here, let's load it from the mapping
    # which has idsiswa_lama.
    # Let's map old ID to name by reading df_siswa (which has nama_lengkap)
    # df_siswa index matches the 0-based index of old siswa in extract.
    # Wait, df_siswa index + 1 is the new ID.
    df_siswa_indexed = df_siswa.copy()
    df_siswa_indexed['id_siswa_baru'] = df_siswa_indexed.index + 1
    
    for idx, s in enumerate(students[:10]):
        name_clean = s['nama_lengkap'].lower().strip()
        match_s = df_siswa_indexed[df_siswa_indexed['nama_lengkap'].str.lower().str.strip() == name_clean]
        if match_s.empty:
            # try contains
            match_s = df_siswa_indexed[df_siswa_indexed['nama_lengkap'].str.lower().str.strip().str.contains(name_clean)]
            
        if not match_s.empty:
            found_count += 1
            new_id = match_s.iloc[0]['id_siswa_baru']
            
            # check in df_ks
            ks_rows = df_ks[df_ks['id_siswa'] == new_id]
            ks_courses = ks_rows['id_kursus'].tolist()
            if ks_courses: has_ks += 1
            
            # check in df_sk
            sk_rows = df_sk[df_sk['id_siswa'] == new_id]
            sk_courses = sk_rows['id_kursus'].tolist()
            if sk_courses: has_sk += 1
            
            print(f"Name: {s['nama_lengkap']} | Pickle ID: {new_id} | ks_courses: {ks_courses} | sk_courses: {sk_courses}")
            
    print(f"\nAudit completed. Verified {found_count} students in pickle.")

if __name__ == '__main__':
    main()
