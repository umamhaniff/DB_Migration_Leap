import pickle
import mysql.connector
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    with open('fase_4/fase_4_hanif.pkl', 'rb') as f:
        data = pickle.load(f)
        
    df_sk = data['siswa_keluar']
    print("Siswa keluar DataFrame shape in Pickle:", df_sk.shape)
    if not df_sk.empty:
        print("\nFirst 5 rows in Pickle:")
        print(df_sk.head())
        print("\nChecking nulls in columns:")
        print(df_sk.isnull().sum())
        
        # Check if the id_siswa exist in db_new.siswa
        cfg = get_db_config()
        conn_new = mysql.connector.connect(**cfg['db_new'])
        cursor_new = conn_new.cursor()
        
        # Get all id_siswa in db_new
        cursor_new.execute("SELECT id_siswa FROM siswa")
        db_siswa_ids = {r[0] for r in cursor_new.fetchall()}
        
        # Get all id_kursus in db_new
        cursor_new.execute("SELECT id_kursus FROM kursus")
        db_kursus_ids = {r[0] for r in cursor_new.fetchall()}
        
        # Get all id_tag_keluar in db_new.tag_siswa_keluar
        cursor_new.execute("SELECT id_tag_keluar FROM tag_siswa_keluar")
        db_tag_ids = {r[0] for r in cursor_new.fetchall()}
        
        print(f"\nTotal siswa in DB: {len(db_siswa_ids)}")
        print(f"Total kursus in DB: {len(db_kursus_ids)}")
        print(f"Total tag_siswa_keluar in DB: {len(db_tag_ids)}")
        
        # Validate pickle rows against DB foreign keys
        invalid_siswa = 0
        invalid_kursus = 0
        invalid_tag = 0
        
        for idx, row in df_sk.iterrows():
            if int(row['id_siswa']) not in db_siswa_ids:
                invalid_siswa += 1
            if str(row['id_kursus']) not in db_kursus_ids:
                invalid_kursus += 1
            if row['id_tag_keluar'] is not None and int(row['id_tag_keluar']) not in db_tag_ids:
                invalid_tag += 1
                
        print(f"\nPickle Validation against DB Constraints:")
        print(f"Invalid id_siswa (not in db_new.siswa): {invalid_siswa}")
        print(f"Invalid id_kursus (not in db_new.kursus): {invalid_kursus}")
        print(f"Invalid id_tag_keluar (not in db_new.tag_siswa_keluar): {invalid_tag}")
        
        conn_new.close()

if __name__ == '__main__':
    main()
