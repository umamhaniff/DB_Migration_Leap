import sys
import os
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    # Get all schedule IDs in the old DB
    cursor_old.execute("SELECT idjadwal FROM jadwal")
    old_jadwal_ids = {row['idjadwal'] for row in cursor_old.fetchall() if row['idjadwal']}
    print(f"Total schedules in old DB 'jadwal' table: {len(old_jadwal_ids)}")

    # Get unique schedules in old history_rapor
    cursor_old.execute("SELECT DISTINCT idjadwal FROM history_rapor")
    history_jadwal_ids = {row['idjadwal'] for row in cursor_old.fetchall() if row['idjadwal']}
    print(f"Unique schedules in old 'history_rapor': {len(history_jadwal_ids)}")

    # Check if any schedule in history_rapor is NOT in old 'jadwal'
    missing_from_old_jadwal = history_jadwal_ids - old_jadwal_ids
    print(f"Schedules in history_rapor but NOT in old 'jadwal' table: {len(missing_from_old_jadwal)}")
    if missing_from_old_jadwal:
        print("Missing schedule IDs:", missing_from_old_jadwal)

    # Let's also check old 'rapor' table
    cursor_old.execute("SELECT DISTINCT idjadwal FROM rapor")
    rapor_jadwal_ids = {row['idjadwal'] for row in cursor_old.fetchall() if row['idjadwal']}
    print(f"Unique schedules in old 'rapor': {len(rapor_jadwal_ids)}")
    
    missing_rapor_from_old_jadwal = rapor_jadwal_ids - old_jadwal_ids
    print(f"Schedules in rapor but NOT in old 'jadwal' table: {len(missing_rapor_from_old_jadwal)}")
    if missing_rapor_from_old_jadwal:
        print("Missing schedule IDs:", missing_rapor_from_old_jadwal)

    conn_old.close()

if __name__ == '__main__':
    main()
