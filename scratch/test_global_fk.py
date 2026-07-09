import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    # Get current global and session value
    cursor.execute("SELECT @@global.foreign_key_checks, @@session.foreign_key_checks;")
    res = cursor.fetchone()
    print("Before:")
    print("Global FK checks:", res[0])
    print("Session FK checks:", res[1])
    
    # Try setting global to 0
    print("\nSetting global foreign_key_checks to 0...")
    cursor.execute("SET GLOBAL foreign_key_checks = 0;")
    conn.commit()
    
    # Open a new connection and check its session value
    conn2 = mysql.connector.connect(**cfg['db_new'])
    cursor2 = conn2.cursor()
    cursor2.execute("SELECT @@global.foreign_key_checks, @@session.foreign_key_checks;")
    res2 = cursor2.fetchone()
    print("\nAfter (New Connection):")
    print("Global FK checks:", res2[0])
    print("Session FK checks:", res2[1])
    
    # Restore global to 1
    print("\nRestoring global foreign_key_checks to 1...")
    cursor2.execute("SET GLOBAL foreign_key_checks = 1;")
    conn2.commit()
    
    conn.close()
    conn2.close()

if __name__ == '__main__':
    main()
