import sys
import os
import pandas as pd
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor_old = conn_old.cursor(dictionary=True)
cursor_new = conn_new.cursor(dictionary=True)

# 1. Fetch tables from db_new
try:
    cursor_new.execute("SHOW TABLES")
    print("--- db_new tables ---")
    for r in cursor_new.fetchall():
        print(list(r.values())[0])
    
    cursor_new.execute("SELECT * FROM tag_siswa_keluar")
    df_new_tags = pd.DataFrame(cursor_new.fetchall())
    print("\n--- db_new.tag_siswa_keluar ---")
    print(df_new_tags)
except Exception as e:
    print(f"Error reading db_new tables: {e}")

# 2. Fetch tag_keluar/siswa_keluar_tag from db_old if it exists
print("\n--- db_old tables search ---")
try:
    cursor_old.execute("SELECT * FROM tag_keluar")
    print("db_old.tag_keluar found:")
    print(pd.DataFrame(cursor_old.fetchall()))
except Exception as e:
    print(f"db_old.tag_keluar NOT found or error: {e}")

try:
    cursor_old.execute("SELECT * FROM siswa_keluar_tag LIMIT 10")
    print("\ndb_old.siswa_keluar_tag sample:")
    print(pd.DataFrame(cursor_old.fetchall()))
except Exception as e:
    print(f"db_old.siswa_keluar_tag NOT found or error: {e}")

# Check how many rows in old siswa_keluar
cursor_old.execute("SELECT idsiswa_keluar, idsiswa, alasan FROM siswa_keluar LIMIT 10")
print("\n--- db_old.siswa_keluar sample ---")
for r in cursor_old.fetchall():
    print(r)

cursor_old.execute("SELECT idsiswa_keluar, idtag FROM siswa_keluar_tag LIMIT 10")
print("\n--- db_old.siswa_keluar_tag sample ---")
for r in cursor_old.fetchall():
    print(r)

import re

# If we have siswa_keluar_tag in db_old, let's see how many matches we can get
try:
    cursor_old.execute("SELECT idsiswa_keluar, idsiswa, alasan FROM siswa_keluar")
    df_sk = pd.DataFrame(cursor_old.fetchall())
    cursor_old.execute("SELECT idsiswa_keluar, idtag FROM siswa_keluar_tag")
    df_skt = pd.DataFrame(cursor_old.fetchall())
    
    # Clean tag mapping from old DB
    def clean_tag_id(tag_str):
        if pd.isna(tag_str): return None
        nums = re.findall(r'\d+', str(tag_str))
        return int(nums[0]) if nums else None
        
    df_skt['tag_id_int'] = df_skt['idtag'].apply(clean_tag_id)
    tag_map = dict(zip(df_skt['idsiswa_keluar'], df_skt['tag_id_int']))
    
    # Combined detection function
    def detect_tag(row):
        # First priority: check database mapping
        db_tag = tag_map.get(row['idsiswa_keluar'])
        if pd.notna(db_tag) and db_tag is not None:
            return db_tag
            
        # Fallback: keyword heuristic on alasan
        alasan = str(row['alasan']).lower()
        if not alasan.strip() or alasan in ('-', 'none', 'nan', '0', 'tidak ada alasan', 'tidak memberikan alasan'):
            return 11 # TIDAK ADA ALASAN
            
        if any(w in alasan for w in ['lulus', 'selesai', 'tamat', 'wisuda']):
            return 9 # LULUS
            
        if any(w in alasan for w in ['jadwal', 'bentrok', 'eksperimen', 'kegiatan', 'les', 'ekskul', 'sekolah', 'waktu', 'jam', 'hari', 'pagi', 'siang', 'sore', 'malam', 'tabrakan', 'kelelahan', 'capek', 'lelah', 'padat', 'ekstrakurikuler', 'tugas sekolah']):
            return 5 # JADWAL
            
        if any(w in alasan for w in ['biaya', 'keuangan', 'dana', 'ekonomi', 'mahal', 'angsuran', 'bayar', 'uang', 'kerjaan', 'pengeluaran', 'pembayaran']):
            return 7 # KEUANGAN
            
        if any(w in alasan for w in ['domisili', 'pindah', 'luar kota', 'surabaya', 'pulkam', 'mudik', 'jarak', 'jauh', 'alamat', 'kembali ke']):
            return 3 # DOMISILI
            
        if any(w in alasan for w in ['program', 'bosan', 'jenuh', 'malas', 'bosan les', 'ingin main', 'tidak mau les', 'capek ngerjain tugas', 'males']):
            return 10 # PROGRAM
            
        if any(w in alasan for w in ['akademik', 'kesulitan', 'level', 'tugas', 'nilai', 'pelajaran', 'kurang', 'sulit', 'cepat', 'lambat', 'mengikuti', 'materi', 'susah']):
            return 1 # AKADEMIK
            
        if any(w in alasan for w in ['guru', 'instruktur', 'pengajar', 'teacher', 'sir', 'miss', 'laoshi', 'cocok', 'metode', 'dosen']):
            return 4 # INSTRUKTUR
            
        if any(w in alasan for w in ['aplikasi', 'zoom', 'classin', 'leapverse', 'laptop', 'hp', 'leapsurabaya', 'tech', 'error', 'sistem', 'device', 'gadget']):
            return 2 # APLIKASI
            
        if any(w in alasan for w in ['keluarga', 'ortu', 'orang tua', 'mama', 'papa', 'sakit', 'meninggal', 'jaga', 'anak', 'saudara', 'melahirkan', 'hamil']):
            return 6 # KELUARGA
            
        return 8 # LAINNYA
        
    df_sk['detected_tag'] = df_sk.apply(detect_tag, axis=1)
    
    print("\nCombined Detection Distribution:")
    print(df_sk['detected_tag'].value_counts())
    
    print("\nSample of detected tags:")
    for i, row in df_sk.head(20).iterrows():
        print(f"Alasan: {row['alasan'][:80]}...")
        print(f"  -> Tag: {row['detected_tag']}")
except Exception as e:
    print(f"Error merging: {e}")

cursor_old.close()
cursor_new.close()
conn_old.close()
conn_new.close()
