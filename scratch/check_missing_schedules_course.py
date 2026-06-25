import sys
import os
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    # Get columns of old 'jadwal' table
    cursor_old.execute("DESCRIBE jadwal")
    cols = [r['Field'] for r in cursor_old.fetchall()]
    print("Columns in old 'jadwal':", cols)
    
    course_col = 'idkursus' if 'idkursus' in cols else ('idpendkursus' if 'idpendkursus' in cols else 'id_kursus')
    print(f"Using course column: {course_col}")

    # Get all schedules in old DB and their courses
    cursor_old.execute(f"SELECT idjadwal, {course_col} FROM jadwal")
    old_schedules = {row['idjadwal']: row[course_col] for row in cursor_old.fetchall()}
    
    # We saw in the previous check that there are missing schedules.
    # Let's check which courses those missing schedules belong to!
    
    # 1. Get unique idjadwal from old 'rapor'
    cursor_old.execute("SELECT DISTINCT idjadwal FROM rapor")
    rapor_j_ids = [row['idjadwal'] for row in cursor_old.fetchall() if row['idjadwal']]
    
    # 2. Get unique idjadwal from old 'history_rapor'
    cursor_old.execute("SELECT DISTINCT idjadwal FROM history_rapor")
    history_j_ids = [row['idjadwal'] for row in cursor_old.fetchall() if row['idjadwal']]

    # Find the courses for all schedules in rapor
    rapor_courses = {}
    for j in rapor_j_ids:
        course = old_schedules.get(j, 'UNKNOWN')
        rapor_courses[course] = rapor_courses.get(course, 0) + 1
        
    print("Schedules in old 'rapor' grouped by their course:")
    for course, count in sorted(rapor_courses.items()):
        print(f"  Course {course}: {count} schedules")
        
    # Find the courses for all schedules in history_rapor
    history_courses = {}
    for j in history_j_ids:
        course = old_schedules.get(j, 'UNKNOWN')
        history_courses[course] = history_courses.get(course, 0) + 1
        
    print("\nSchedules in old 'history_rapor' grouped by their course:")
    for course, count in sorted(history_courses.items()):
        print(f"  Course {course}: {count} schedules")

    conn_old.close()

if __name__ == '__main__':
    main()
