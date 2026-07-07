import os
import sys
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    df_map = pd.read_pickle('fase_4/mapping_siswa.pkl')
    print("mapping_siswa.pkl head:")
    print(df_map.head(25))
    
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    # Get the names for these first 25 ids
    first_ids = df_map.head(25)['idsiswa_lama'].tolist()
    
    # Fetch from old DB
    format_strings = ','.join(['%s'] * len(first_ids))
    cursor_old.execute(f"SELECT idsiswa, nama_lengkap, no_induk, keluar, lulus FROM siswa WHERE idsiswa IN ({format_strings})", tuple(first_ids))
    rows = cursor_old.fetchall()
    
    print("\nOld DB details for these IDs:")
    rows_dict = {r['idsiswa']: r for r in rows}
    for old_id in first_ids:
        r = rows_dict.get(old_id)
        if r:
            print(f"Old ID: {old_id} | Name: {r['nama_lengkap']} | No Induk: {r['no_induk']} | Keluar: {r['keluar']} | Lulus: {r['lulus']}")
        else:
            print(f"Old ID: {old_id} | NOT FOUND IN OLD DB")

    conn_old.close()

if __name__ == '__main__':
    main()
