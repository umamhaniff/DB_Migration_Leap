import os
import sys
import mysql.connector
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor()
    
    tables_to_truncate = [
        'siswa_mitra_keluar',
        'siswa_mitra',
        'siswa_keluar',
        'kursus_siswa',
        'siswa'
    ]
    
    print("--- Resetting db_new student tables (Opsi 1) ---")
    try:
        # Disable foreign key checks
        cursor_new.execute("SET FOREIGN_KEY_CHECKS = 0")
        conn_new.commit()
        print("Foreign Key Checks temporarily disabled.")
        
        for tbl in tables_to_truncate:
            # Check if table exists
            cursor_new.execute(f"SHOW TABLES LIKE '{tbl}'")
            if cursor_new.fetchone():
                cursor_new.execute(f"TRUNCATE TABLE `{tbl}`")
                conn_new.commit()
                print(f"Table `{tbl}` truncated and AUTO_INCREMENT reset to 1.")
            else:
                print(f"Table `{tbl}` does not exist, skipped.")
                
        # Enable foreign key checks
        cursor_new.execute("SET FOREIGN_KEY_CHECKS = 1")
        conn_new.commit()
        print("Foreign Key Checks re-enabled successfully.")
        print("\n[SUCCESS] Database tables reset successfully! Ready for clean re-insertion.")
        
    except Exception as e:
        conn_new.rollback()
        # Ensure FK checks are re-enabled in case of error
        try:
            cursor_new.execute("SET FOREIGN_KEY_CHECKS = 1")
            conn_new.commit()
        except:
            pass
        print(f"\n[ERROR] Reset failed: {e}")
        sys.exit(1)
        
    finally:
        conn_new.close()

if __name__ == '__main__':
    main()
