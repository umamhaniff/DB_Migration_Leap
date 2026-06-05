import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def import_sql(sql_file_path):
    if not os.path.exists(sql_file_path):
        print(f"Error: File {sql_file_path} not found.")
        return False
        
    cfg = get_db_config()['db_new']
    print(f"Connecting to database {cfg['database']}...")
    conn = mysql.connector.connect(**cfg)
    cursor = conn.cursor()
    
    print("Disabling foreign key checks...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    
    print(f"Reading SQL file {sql_file_path}...")
    with open(sql_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        statement = []
        in_multi_line_comment = False
        
        for line_num, line in enumerate(f, 1):
            stripped = line.strip()
            
            # Skip empty lines
            if not stripped:
                continue
                
            # Handle comments
            if stripped.startswith('--') or stripped.startswith('#'):
                continue
            if stripped.startswith('/*'):
                if '*/' in stripped:
                    continue
                in_multi_line_comment = True
                continue
            if in_multi_line_comment:
                if '*/' in stripped:
                    in_multi_line_comment = False
                continue
                
            statement.append(line)
            
            # End of statement
            if stripped.endswith(';'):
                stmt_str = "".join(statement).strip()
                statement = []
                if stmt_str:
                    try:
                        cursor.execute(stmt_str)
                    except mysql.connector.Error as err:
                        print(f"Error at line {line_num}: {err}")
                        print("Statement was:", stmt_str[:200])
                        # Proceed anyway
                        
    conn.commit()
    print("Enabling foreign key checks...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    conn.close()
    print("Database restored successfully!")
    return True

if __name__ == "__main__":
    import_sql("extract/dataleap_v5_migration-202604211322.sql")
