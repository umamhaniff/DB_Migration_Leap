import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    print(f"Connecting to database {cfg['db_new']['database']} to drop unique constraint...")
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE pelamar DROP INDEX pelamar_email_pelamar_unique;")
        conn.commit()
        print("✅ SUCCESS: Unique index 'pelamar_email_pelamar_unique' has been dropped!")
    except mysql.connector.Error as err:
        if err.errno == 1091: # Key doesn't exist
            print("ℹ️ NOTE: Unique index 'pelamar_email_pelamar_unique' already dropped or does not exist.")
        else:
            print(f"❌ ERROR: Failed to drop index: {err}")
            
    conn.close()

if __name__ == '__main__':
    main()
