import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config
import pandas as pd

def main():
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_old'])
    cursor = conn.cursor()
    
    # 1. Check duplicate emails in old pelamar
    query_dup = """
        SELECT email, COUNT(*), GROUP_CONCAT(idpelamar) 
        FROM pelamar 
        GROUP BY email 
        HAVING COUNT(*) > 1
    """
    cursor.execute(query_dup)
    dups = cursor.fetchall()
    print("=== Duplicate Emails in db_old.pelamar ===")
    for dup in dups:
        print(f"Email: {dup[0]}, Count: {dup[1]}, IDs: {dup[2]}")
        
    # 2. Check wfo values exceeding 50 chars
    query_wfo = """
        SELECT idpelamar, email, nama, wfo, LENGTH(wfo) 
        FROM pelamar 
        WHERE LENGTH(wfo) > 50
    """
    cursor.execute(query_wfo)
    wfos = cursor.fetchall()
    print("\n=== wfo Values Exceeding 50 Chars ===")
    for row in wfos:
        print(f"ID: {row[0]}, Email: {row[1]}, Name: {row[2]}, Length: {row[4]}, Value: {row[3]}")
        
    # 3. Let's see some other values of wfo
    query_all_wfo = "SELECT wfo, COUNT(*) FROM pelamar GROUP BY wfo"
    cursor.execute(query_all_wfo)
    all_wfos = cursor.fetchall()
    print("\n=== Distinct wfo Values ===")
    for row in all_wfos:
        print(f"wfo: {row[0]}, Count: {row[1]}")

    conn.close()

if __name__ == '__main__':
    main()
