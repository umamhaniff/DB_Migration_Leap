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
    
    # Get unique id_kursus from new db 'kursus' table
    cursor_new.execute("SELECT id_kursus FROM kursus")
    new_courses = {row['id_kursus'] for row in cursor_new.fetchall() if row['id_kursus']}
    print(f"Unique courses in new DB 'kursus' table: {len(new_courses)}")
    print("New courses:", sorted(list(new_courses)))

    # Get unique idpendkursus from old db 'format_rapor'
    cursor_old.execute("SELECT DISTINCT idpendkursus FROM format_rapor")
    old_format_courses = {row['idpendkursus'] for row in cursor_old.fetchall() if row['idpendkursus']}
    print(f"\nUnique courses in old 'format_rapor': {len(old_format_courses)}")
    print("Old format courses:", sorted(list(old_format_courses)))

    # Get unique idpendkursus from old db 'format_raport_level'
    cursor_old.execute("SELECT DISTINCT idpendkursus FROM format_raport_level")
    old_level_courses = {row['idpendkursus'] for row in cursor_old.fetchall() if row['idpendkursus']}
    print(f"Unique courses in old 'format_raport_level': {len(old_level_courses)}")
    print("Old level courses:", sorted(list(old_level_courses)))

    # Check for missing courses
    missing_format = old_format_courses - new_courses
    print(f"\nCourses in old format_rapor but missing from new DB: {len(missing_format)}")
    print("Missing format courses:", sorted(list(missing_format)))

    missing_level = old_level_courses - new_courses
    print(f"Courses in old format_raport_level but missing from new DB: {len(missing_level)}")
    print("Missing level courses:", sorted(list(missing_level)))

    conn_old.close()
    conn_new.close()

if __name__ == '__main__':
    main()
