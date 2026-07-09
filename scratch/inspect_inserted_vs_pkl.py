import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config
import pandas as pd

def main():
    # 1. Load pickle data
    pkl_path = "fase_3/fase_3_hanif.pkl"
    with open(pkl_path, 'rb') as f:
        import pickle
        pkl_data = pickle.load(f)
    df_pkl = pkl_data['pelamar']
    print(f"Pickle pelamar row count: {len(df_pkl)}")
    
    # 2. Load DB data
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_pelamar, email_pelamar, nama_lengkap FROM pelamar")
    db_rows = cursor.fetchall()
    df_db = pd.DataFrame(db_rows, columns=['id_pelamar', 'email_pelamar', 'nama_lengkap'])
    print(f"DB pelamar row count: {len(df_db)}")
    
    # Check if there are any mismatch
    print("\nFirst 5 rows in DB:")
    print(df_db.head())
    
    print("\nFirst 5 rows in Pickle:")
    print(df_pkl[['email_pelamar', 'nama_lengkap']].head())
    
    # Find which pickle emails are not in the DB
    pkl_emails = set(df_pkl['email_pelamar'].dropna().apply(lambda x: str(x).strip().lower()))
    db_emails = set(df_db['email_pelamar'].dropna().apply(lambda x: str(x).strip().lower()))
    
    missing_in_db = pkl_emails - db_emails
    print(f"\nEmails in Pickle but missing in DB: {len(missing_in_db)}")
    if missing_in_db:
        print("Sample missing emails:", list(missing_in_db)[:10])
        
    conn.close()

if __name__ == '__main__':
    main()
