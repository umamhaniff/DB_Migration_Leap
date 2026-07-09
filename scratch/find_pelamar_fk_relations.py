import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    # Query information_schema to find all foreign keys referencing pelamar
    query = """
        SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE REFERENCED_TABLE_NAME = 'pelamar' 
          AND REFERENCED_COLUMN_NAME = 'id_pelamar'
          AND TABLE_SCHEMA = %s
    """
    cursor.execute(query, (cfg['db_new']['database'],))
    relations = cursor.fetchall()
    
    print("=== Tables referencing pelamar(id_pelamar) ===")
    if relations:
        for r in relations:
            print(f"Table: {r[0]}, Column: {r[1]}, Constraint: {r[2]}")
    else:
        print("No foreign keys reference pelamar(id_pelamar)!")
        
    conn.close()

if __name__ == '__main__':
    main()
