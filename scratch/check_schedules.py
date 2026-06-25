import sys
import os
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    conn_new = mysql.connector.connect(**cfg['db_new'])
    
    cursor_old = conn_old.cursor(dictionary=True)
    cursor_new = conn_new.cursor(dictionary=True)
    
    # Get unique id_jadwal from new db 'jadwal' table
    cursor_new.execute("SELECT id_jadwal FROM jadwal")
    new_schedules = {row['id_jadwal'] for row in cursor_new.fetchall() if row['id_jadwal']}
    print(f"Unique schedules in new DB 'jadwal' table: {len(new_schedules)}")

    # Get unique idjadwal from old db 'rapor'
    cursor_old.execute("SELECT DISTINCT idjadwal FROM rapor")
    old_rapor_schedules = {row['idjadwal'] for row in cursor_old.fetchall() if row['idjadwal']}
    print(f"Unique schedules in old 'rapor': {len(old_rapor_schedules)}")

    # Get unique idjadwal from old db 'history_rapor'
    cursor_old.execute("SELECT DISTINCT idjadwal FROM history_rapor")
    old_history_schedules = {row['idjadwal'] for row in cursor_old.fetchall() if row['idjadwal']}
    print(f"Unique schedules in old 'history_rapor': {len(old_history_schedules)}")

    # Check for missing schedules
    missing_rapor = old_rapor_schedules - new_schedules
    print(f"\nSchedules in old rapor but missing from new DB: {len(missing_rapor)}")
    print("Missing rapor schedules (first 10):", sorted(list(missing_rapor))[:10])

    missing_history = old_history_schedules - new_schedules
    print(f"Schedules in old history_rapor but missing from new DB: {len(missing_history)}")
    print("Missing history schedules (first 10):", sorted(list(missing_history))[:10])

    conn_old.close()
    conn_new.close()

if __name__ == '__main__':
    main()
