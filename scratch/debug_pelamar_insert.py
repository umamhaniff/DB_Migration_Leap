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
    df_pel = pkl_data['pelamar']
    
    # 2. Reset the table first
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    print("Resetting pelamar table...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("TRUNCATE TABLE pelamar")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    conn.commit()
    
    # 3. Clean columns (dropna/placeholder) like the insert handler
    df_to_push = df_pel.dropna(axis=1, how='all')
    columns_str = ', '.join([f'`{col}`' for col in df_to_push.columns])
    placeholders_str = ', '.join(['%s'] * len(df_to_push.columns))
    insert_query = f"INSERT INTO `pelamar` ({columns_str}) VALUES ({placeholders_str})"
    
    raw_numpy_list = df_to_push.to_numpy().tolist()
    clean_data_tuples = [
        tuple(None if pd.isna(x) or str(x).strip() in ["NaT", "NaN"] else x for x in row) 
        for row in raw_numpy_list
    ]
    
    print(f"Total rows to insert: {len(clean_data_tuples)}")
    
    success_count = 0
    fail_count = 0
    
    # Insert row by row to capture individual errors
    for idx, row in enumerate(clean_data_tuples):
        try:
            cursor.execute(insert_query, row)
            conn.commit()
            success_count += 1
        except Exception as e:
            fail_count += 1
            # Print row index, email, and error message
            email_idx = list(df_to_push.columns).index('email_pelamar')
            name_idx = list(df_to_push.columns).index('nama_lengkap')
            email = row[email_idx]
            name = row[name_idx]
            print(f"❌ Row {idx+1} Failed: Email={email}, Name={name}, Error={e}")
            
    print(f"\nSummary: Success={success_count}, Failed={fail_count}")
    conn.close()

if __name__ == '__main__':
    main()
