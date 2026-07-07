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

def clean_wil_name(s):
    import re
    if pd.isna(s): return ""
    s = str(s).strip().lower()
    s = re.sub(r'\b(kabupaten|kab|kota|kecamatan|kec|kelurahan|kel|desa|adm)\b\.?', '', s)
    s = s.replace('\'', '').replace('`', '').replace('-', '').replace(' ', '')
    return s

def extract_int(s):
    import re
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\d+', str(s))
    return int(nums[0]) if nums else None

def main():
    students = parse_questions_md()
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    # Pre-fetch new database students by name
    cursor_new.execute("SELECT id_siswa, nama_lengkap, id_mitra, nomor_induk FROM siswa")
    new_db_students = {r['nama_lengkap'].lower().strip(): r for r in cursor_new.fetchall()}
    
    # Load mapping_siswa.pkl to check what it has
    df_map = pd.read_pickle('fase_4/mapping_siswa.pkl')
    siswa_map = dict(zip(df_map['idsiswa_lama'], df_map['id_siswa_baru']))
    
    # Fetch course list to map course names
    cursor_new.execute("SELECT id_kursus, nama_kursus FROM kursus")
    courses = cursor_new.fetchall()
    course_name_map = {}
    for c in courses:
        # Normalize course names for easier matching
        norm_name = clean_wil_name(c['nama_kursus'])
        course_name_map[norm_name] = c['id_kursus']
    
    # Add special overrides for B2B courses in questions.md
    # "Kemitraan - B2B TK Mitra" -> K00021
    # "Kemitraan - B2B CC Mitra" -> K00022
    # "LEAP - Leap Literacy Club" -> K00003
    # "LEAP - Conversation Class" -> K00004
    # "LEAP - General English 2024" -> K00010
    special_course_map = {
        clean_wil_name("Kemitraan - B2B TK Mitra"): "K00021",
        clean_wil_name("Kemitraan - B2B CC Mitra"): "K00022",
        clean_wil_name("LEAP - Leap Literacy Club"): "K00003",
        clean_wil_name("LEAP - Conversation Class"): "K00004",
        clean_wil_name("LEAP - General English 2024"): "K00010",
        clean_wil_name("LEAP - General English"): "K00001",
    }
    
    print("--- Audit of 47 Students ---")
    
    report_data = []
    
    for idx, s in enumerate(students):
        name_lower = s['nama_lengkap'].lower().strip()
        new_s = new_db_students.get(name_lower)
        
        # Determine target course ID
        norm_c_q = clean_wil_name(s['kursus'])
        target_course_id = special_course_map.get(norm_c_q)
        if not target_course_id:
            target_course_id = course_name_map.get(norm_c_q)
            
        # Determine target Mitra ID
        # AHMAD YUDISTIRA RACHMAN (ID 1313) -> 16
        # MAXINE KIRANA SUBARKAH (ID 711) -> 5
        # SHAQUEENA NAUREEN (ID 357) -> 21
        target_mitra_id = None
        if "YUDISTIRA" in s['nama_lengkap']:
            target_mitra_id = 16
        elif "MAXINE" in s['nama_lengkap']:
            target_mitra_id = 5
        elif "SHAQUEENA" in s['nama_lengkap']:
            target_mitra_id = 21
            
        if new_s:
            new_id = new_s['id_siswa']
            current_id_mitra = new_s['id_mitra']
            
            # Fetch current kursus_siswa
            cursor_new.execute("SELECT * FROM kursus_siswa WHERE id_siswa = %s", (new_id,))
            current_ks = cursor_new.fetchall()
            
            # Fetch current siswa_keluar
            cursor_new.execute("SELECT * FROM siswa_keluar WHERE id_siswa = %s", (new_id,))
            current_sk = cursor_new.fetchall()
            
            # Fetch old DB records
            cursor_old.execute("SELECT idsiswa, idmitra FROM siswa WHERE LOWER(nama_lengkap) = %s", (new_s['nama_lengkap'].lower(),))
            old_s_rows = cursor_old.fetchall()
            old_id = old_s_rows[0]['idsiswa'] if old_s_rows else None
            
            old_sk = None
            old_kbm = []
            if old_id:
                cursor_old.execute("SELECT * FROM siswa_keluar WHERE idsiswa = %s", (old_id,))
                old_sk = cursor_old.fetchone()
                
                cursor_old.execute(
                    "SELECT js.*, j.idpendkursus FROM jadwal_siswa js JOIN jadwal j ON js.idjadwal = j.idjadwal WHERE js.idsiswa = %s",
                    (old_id,)
                )
                old_kbm = cursor_old.fetchall()
                
            report_data.append({
                'name': s['nama_lengkap'],
                'no_induk': s['nomor_induk'],
                'new_id': new_id,
                'current_id_mitra': current_id_mitra,
                'target_id_mitra': target_mitra_id,
                'current_ks': current_ks,
                'current_sk': current_sk,
                'target_course_id': target_course_id,
                'old_sk': old_sk,
                'old_kbm': old_kbm
            })
        else:
            report_data.append({
                'name': s['nama_lengkap'],
                'no_induk': s['nomor_induk'],
                'new_id': None,
                'target_course_id': target_course_id,
                'target_id_mitra': target_mitra_id
            })

    # Print report
    print(f"{'No':<3} | {'Nama Lengkap':<35} | {'ID Baru':<7} | {'Mitra (C/T)':<11} | {'Kursus (C/T)':<13} | {'SK (C/T)':<8}")
    print("-" * 90)
    for i, r in enumerate(report_data):
        no = i + 1
        name = r['name']
        if not r['new_id']:
            print(f"{no:<3} | {name:<35} | NOT FOUND IN DB_NEW")
            continue
            
        new_id = r['new_id']
        mitra_str = f"{r['current_id_mitra']}/{r['target_id_mitra']}"
        
        curr_ks_courses = [x['id_kursus'] for x in r['current_ks']]
        curr_ks_str = ",".join(curr_ks_courses) if curr_ks_courses else "None"
        ks_str = f"{curr_ks_str}/{r['target_course_id']}"
        
        curr_sk_courses = [str(x['id_kursus']) for x in r['current_sk']]
        curr_sk_str = ",".join(curr_sk_courses) if curr_sk_courses else "None"
        sk_str = f"{curr_sk_str}/{r['target_course_id']}"
        
        print(f"{no:<3} | {name:<35} | {new_id:<7} | {mitra_str:<11} | {ks_str:<13} | {sk_str:<8}")
        
    conn_old.close()
    conn_new.close()

if __name__ == '__main__':
    main()
