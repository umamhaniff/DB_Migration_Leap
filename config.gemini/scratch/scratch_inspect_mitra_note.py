import mysql.connector
from config import get_db_config

try:
    config = get_db_config()
    db_old = mysql.connector.connect(**config['db_old'])
    cursor = db_old.cursor()
    
    cursor.execute("DESCRIBE mitra_note")
    print("=== Schema of db_old.mitra_note ===")
    for row in cursor.fetchall():
        print(row)
        
    cursor.execute("SELECT * FROM mitra_note LIMIT 5")
    print("\n=== Sample of db_old.mitra_note ===")
    for row in cursor.fetchall():
        print(row)
        
    cursor.close()
    db_old.close()
except Exception as e:
    print("Error:", e)
