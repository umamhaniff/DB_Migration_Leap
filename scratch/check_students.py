import sys
import os
import pandas as pd
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    # Load mapping_siswa.pkl
    df_map = pd.read_pickle('fase_4/mapping_siswa.pkl')
    student_id_map = dict(zip(df_map['idsiswa_lama'], df_map['id_siswa_baru']))
    print(f"Loaded student map with {len(student_id_map)} entries.")

    # Get unique students in old rapor
    cursor_old.execute("SELECT DISTINCT idsiswa FROM rapor")
    rapor_students = [row['idsiswa'] for row in cursor_old.fetchall() if row['idsiswa']]
    print(f"Unique students in old rapor: {len(rapor_students)}")
    
    # Get unique students in old history_rapor
    cursor_old.execute("SELECT DISTINCT idsiswa FROM history_rapor")
    history_students = [row['idsiswa'] for row in cursor_old.fetchall() if row['idsiswa']]
    print(f"Unique students in old history_rapor: {len(history_students)}")

    # Check how many are missing from the map
    missing_rapor = [s for s in rapor_students if s not in student_id_map]
    print(f"Students in rapor but missing from map: {len(missing_rapor)}")
    if missing_rapor:
        print("First 10 missing in rapor:", missing_rapor[:10])

    missing_history = [s for s in history_students if s not in student_id_map]
    print(f"Students in history_rapor but missing from map: {len(missing_history)}")
    if missing_history:
        print("First 10 missing in history_rapor:", missing_history[:10])

    conn_old.close()

if __name__ == '__main__':
    main()
