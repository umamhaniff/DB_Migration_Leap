import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pickle
import pandas as pd
import mysql.connector
from config import get_db_config

def main():
    # 1. Load pickle data
    pkl_path = "fase_3/fase_3_hanif.pkl"
    with open(pkl_path, 'rb') as f:
        data = pickle.load(f)
        
    df_pel = data['pelamar']
    print(f"Total rows in pelamar pickle: {len(df_pel)}")
    print(f"Null count in id_pengajuan column in pickle: {df_pel['id_pengajuan'].isna().sum()}")
    print("Value counts of id_pengajuan in pickle:")
    print(df_pel['id_pengajuan'].value_counts(dropna=False))
    
    # 2. Check the real pengajuan_karyawan IDs in DB
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_pengajuan FROM pengajuan_karyawan")
    existing_ids = [r[0] for r in cursor.fetchall()]
    print(f"\nExisting id_pengajuan in db_new.pengajuan_karyawan: {len(existing_ids)} rows")
    print("Existing IDs:", existing_ids)
    
    # 3. Find which rows in pickle refer to IDs NOT in db_new
    df_invalid = df_pel[~df_pel['id_pengajuan'].isin(existing_ids) & df_pel['id_pengajuan'].notna()]
    print(f"\nRows in pickle with invalid id_pengajuan: {len(df_invalid)}")
    if not df_invalid.empty:
        print(df_invalid[['email_pelamar', 'nama_lengkap', 'id_pengajuan']].head(10))
        
    conn.close()

if __name__ == '__main__':
    main()
