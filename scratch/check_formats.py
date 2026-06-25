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
    
    # Get unique idformat_rapor from format_rapor_detil
    cursor_old.execute("SELECT DISTINCT idformat_rapor FROM format_rapor_detil")
    old_detil_ids = [row['idformat_rapor'] for row in cursor_old.fetchall()]
    print("Unique idformat_rapor in old format_rapor_detil:", old_detil_ids[:10])
    print("Total unique:", len(old_detil_ids))
    
    # Get unique idformat_rapor from format_rapor
    cursor_old.execute("SELECT DISTINCT idformat_rapor FROM format_rapor")
    old_format_ids = [row['idformat_rapor'] for row in cursor_old.fetchall()]
    print("Unique idformat_rapor in old format_rapor:", old_format_ids[:10])
    print("Total unique:", len(old_format_ids))

    # Read CSV
    df_csv = pd.read_csv('fase_5/rapor_format_sub_import.csv')
    print("Unique id_rapor_format in CSV:", df_csv['id_rapor_format'].unique()[:10])
    print("Total unique in CSV:", len(df_csv['id_rapor_format'].unique()))

    # Check if they overlap perfectly
    overlap = set(old_detil_ids).intersection(set(df_csv['id_rapor_format']))
    print("Overlap size:", len(overlap))
    print("Diff (old - csv):", set(old_detil_ids) - set(df_csv['id_rapor_format']))
    print("Diff (csv - old):", set(df_csv['id_rapor_format']) - set(old_detil_ids))

    conn_old.close()

if __name__ == '__main__':
    main()
