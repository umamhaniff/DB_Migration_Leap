import sys
import os
import pandas as pd
import mysql.connector

# Add parent directory to path to import config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    db_old_cfg = cfg['db_old']
    db_new_cfg = cfg['db_new']

    print("Connecting to DBs...")
    conn_old = mysql.connector.connect(**db_old_cfg)
    conn_new = mysql.connector.connect(**db_new_cfg)
    
    cursor_old = conn_old.cursor(dictionary=True)
    cursor_new = conn_new.cursor(dictionary=True)

    print("\n=== 1. CHECKING NEW DB SCHEMAS FOR RAPOR TABLES ===")
    rapor_tables = [
        'rapor_format', 'rapor_format_sub', 'rapor_format_formula', 
        'rapor_format_formula_sub', 'rapor_level_config', 'rapor_sub_level',
        'rapor_siswa', 'rapor_siswa_file', 'rapor_lacak'
    ]
    for tbl in rapor_tables:
        try:
            cursor_new.execute(f"DESCRIBE {tbl}")
            cols = cursor_new.fetchall()
            print(f"\nTable: {tbl}")
            for col in cols:
                print(f"  {col['Field']}: {col['Type']} | Null: {col['Null']} | Key: {col['Key']} | Default: {col['Default']} | Extra: {col['Extra']}")
        except Exception as e:
            print(f"Error describing {tbl}: {e}")

    print("\n=== 2. CHECKING OLD DB ROW COUNTS ===")
    old_tables = [
        'format_rapor', 'format_rapor_detil', 'format_rapor_rumus',
        'format_rapor_detil_rumus', 'format_raport_level', 'rapor',
        'file_rapor_siswa', 'history_rapor'
    ]
    for tbl in old_tables:
        try:
            cursor_old.execute(f"SELECT COUNT(*) as cnt FROM {tbl}")
            row = cursor_old.fetchone()
            print(f"Old Table {tbl}: {row['cnt']} rows")
        except Exception as e:
            print(f"Error counting old {tbl}: {e}")

    print("\n=== 3. ANALYZING DUPLICATES IN format_rapor ===")
    try:
        cursor_old.execute("SELECT idformat_rapor, COUNT(*) as cnt FROM format_rapor GROUP BY idformat_rapor HAVING cnt > 1")
        dups = cursor_old.fetchall()
        print(f"Duplicates in old format_rapor by idformat_rapor: {len(dups)}")
        for d in dups[:5]:
            print(d)
            
        cursor_old.execute("SELECT title, COUNT(*) as cnt FROM format_rapor GROUP BY title HAVING cnt > 1")
        title_dups = cursor_old.fetchall()
        print(f"Duplicates in old format_rapor by title: {len(title_dups)}")
        for d in title_dups[:5]:
            print(d)
    except Exception as e:
        print(f"Error analyzing format_rapor dups: {e}")

    print("\n=== 4. EXAMINING CSV FILES ===")
    for csv_file in ['fase_5/rapor_format_import.csv', 'fase_5/rapor_format_sub_import.csv']:
        if os.path.exists(csv_file):
            df_csv = pd.read_csv(csv_file)
            print(f"\nCSV {csv_file}: shape {df_csv.shape}")
            print(df_csv.head(3))
            print("Duplicate count of merge keys:")
            if 'judul_rapor' in df_csv.columns:
                print(f"  judul_rapor: {df_csv['judul_rapor'].duplicated().sum()} duplicates")
            if 'sub_judul_rapor' in df_csv.columns:
                # Group by id_rapor_format and sub_judul_rapor to see duplicates
                group_cols = ['id_rapor_format', 'sub_judul_rapor']
                dups_cnt = df_csv.duplicated(subset=group_cols).sum()
                print(f"  id_rapor_format + sub_judul_rapor: {dups_cnt} duplicates")
        else:
            print(f"CSV {csv_file} not found!")

    print("\n=== 5. CHECKING MAPPING_SISWA.PKL ===")
    mapping_siswa_f4 = 'fase_4/mapping_siswa.pkl'
    mapping_siswa_f5 = 'fase_5/mapping_siswa.pkl'
    for pkl in [mapping_siswa_f4, mapping_siswa_f5]:
        if os.path.exists(pkl):
            try:
                df_pkl = pd.read_pickle(pkl)
                print(f"\nPickle {pkl}: shape {df_pkl.shape}")
                print(df_pkl.head(3))
                print(f"Columns: {list(df_pkl.columns)}")
            except Exception as e:
                print(f"Error reading pickle {pkl}: {e}")
        else:
            print(f"Pickle {pkl} not found!")

    conn_old.close()
    conn_new.close()

if __name__ == '__main__':
    main()
