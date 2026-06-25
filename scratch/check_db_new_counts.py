import sys
import os
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    cursor_new.execute("SHOW TABLES")
    tables = [list(row.values())[0] for row in cursor_new.fetchall()]
    print(f"Total tables in new DB: {len(tables)}")
    
    for tbl in sorted(tables):
        cursor_new.execute(f"SELECT COUNT(*) as cnt FROM `{tbl}`")
        cnt = cursor_new.fetchone()['cnt']
        if cnt > 0:
            print(f"Table `{tbl}`: {cnt} rows")
        else:
            print(f"Table `{tbl}`: EMPTY")
            
    conn_new.close()

if __name__ == '__main__':
    main()
