import pickle
import mysql.connector
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    path = "fase_1/fase_1_hanif.pkl"
    with open(path, "rb") as f:
        data = pickle.load(f)
        
    df_tag = data['tag_siswa_keluar']
    print("tag_siswa_keluar in pickle:")
    print(df_tag)
    
    cfg = get_db_config()
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor()
    
    # Disable FK checks temporarily just in case
    cursor_new.execute("SET FOREIGN_KEY_CHECKS = 0")
    conn_new.commit()
    
    # Clean the target table
    cursor_new.execute("TRUNCATE TABLE tag_siswa_keluar")
    conn_new.commit()
    print("Table tag_siswa_keluar truncated.")
    
    # Insert rows
    for idx, row in df_tag.iterrows():
        sql = """
            INSERT INTO tag_siswa_keluar (id_tag_keluar, nama_tag, keterangan_keluar)
            VALUES (%s, %s, %s)
        """
        val = (int(row['id_tag_keluar']), row['nama_tag'], row['keterangan_keluar'])
        cursor_new.execute(sql, val)
        
    conn_new.commit()
    print(f"Successfully inserted {len(df_tag)} rows into db_new.tag_siswa_keluar.")
    
    # Re-enable FK checks
    cursor_new.execute("SET FOREIGN_KEY_CHECKS = 1")
    conn_new.commit()
    
    conn_new.close()

if __name__ == '__main__':
    main()
