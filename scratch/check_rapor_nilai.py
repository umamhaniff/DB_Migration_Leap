import sys
import os
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    # Check lengths of 'nilai' column in old 'rapor'
    cursor_old.execute("SELECT idrapor, idsiswa, idjadwal, nilai, LENGTH(nilai) as len FROM rapor ORDER BY len DESC LIMIT 10")
    rows = cursor_old.fetchall()
    print("Top 10 longest 'nilai' values:")
    for r in rows:
        print(f"ID: {r['idrapor']} | Len: {r['len']} | Value: {repr(r['nilai'])}")
        
    # Count how many are > 150 characters
    cursor_old.execute("SELECT COUNT(*) as cnt FROM rapor WHERE LENGTH(nilai) > 150")
    cnt_over = cursor_old.fetchone()['cnt']
    print(f"\nTotal rows with 'nilai' length > 150: {cnt_over}")
    
    if cnt_over > 0:
        cursor_old.execute("SELECT idrapor, LENGTH(nilai) as len, nilai FROM rapor WHERE LENGTH(nilai) > 150 LIMIT 5")
        for r in cursor_old.fetchall():
            print(f"  ID: {r['idrapor']} (len={r['len']}): {repr(r['nilai'][:160])}...")

    conn_old.close()

if __name__ == '__main__':
    main()
