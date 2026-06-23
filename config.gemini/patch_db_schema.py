import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def apply_alterations():
    cfg = get_db_config()['db_new']
    print(f"Connecting to database {cfg['database']} to apply schema alterations...")
    conn = mysql.connector.connect(**cfg)
    cursor = conn.cursor()
    
    # Disable foreign key checks while altering schema to avoid strict constraint validation errors
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    
    alterations = [
        # 1. siswa table changes
        ("siswa", "ADD COLUMN status_pendaftaran VARCHAR(50) NULL AFTER kode_pos", "status_pendaftaran"),
        ("siswa", "DROP COLUMN status_lulus_siswa", "status_lulus_siswa", True), # invert=True, check if column exists to drop it
        
        # 2. jadwal_siswa table changes
        ("jadwal_siswa", "ADD COLUMN is_acc_rapor TINYINT(1) NOT NULL DEFAULT 0", "is_acc_rapor"),
        ("jadwal_siswa", "ADD COLUMN status_ketuntasan VARCHAR(50) NULL", "status_ketuntasan"),
        ("jadwal_siswa", "ADD COLUMN catatan_ketuntasan_guru TEXT NULL", "catatan_ketuntasan_guru"),
        ("jadwal_siswa", "ADD COLUMN catatan_ketuntasan_admin TEXT NULL", "catatan_ketuntasan_admin"),
        ("jadwal_siswa", "ADD COLUMN ketuntasan_diperbarui_oleh VARCHAR(100) NULL", "ketuntasan_diperbarui_oleh"),
        ("jadwal_siswa", "ADD COLUMN ketuntasan_diperbarui_pada TIMESTAMP NULL", "ketuntasan_diperbarui_pada"),
        
        # 3. kursus_siswa table changes
        ("kursus_siswa", "ADD COLUMN status_lulus TINYINT(1) NOT NULL DEFAULT 0", "status_lulus"),
        
        # 4. catatan_kelas_tag table changes
        ("catatan_kelas_tag", "RENAME COLUMN id_ck TO id_catatan_kelas", "id_catatan_kelas"),
        
        # 5. jadwal_detail table changes
        ("jadwal_detail", "ADD COLUMN presensi_disimpan_at TIMESTAMP NULL", "presensi_disimpan_at"),
        
        # 6. catatan_kelas table changes
        ("catatan_kelas", "ADD COLUMN id_karyawan BIGINT(20) UNSIGNED NULL AFTER id_jadwal_detail", "id_karyawan"),
        
        # 7. rapor_format table changes
        ("rapor_format", "ADD COLUMN urutan INT(11) NOT NULL DEFAULT 0", "urutan"),
        
        # 8. rapor_format_sub table changes
        ("rapor_format_sub", "ADD COLUMN urutan INT(11) NOT NULL DEFAULT 0", "urutan"),
        
        # 9. rapor_format_formula_sub table changes
        ("rapor_format_formula_sub", "ADD COLUMN urutan INT(11) NOT NULL DEFAULT 0", "urutan"),
        
        # 10. catatan_siswa table changes
        ("catatan_siswa", "ADD COLUMN id_karyawan BIGINT(20) UNSIGNED NULL AFTER id_siswa", "id_karyawan"),
        ("catatan_siswa", "ADD COLUMN tanggal DATE NULL AFTER id_karyawan", "tanggal")
    ]
    
    for table, query, column, *extra in alterations:
        invert = extra[0] if extra else False
        
        # Check if column exists
        cursor.execute(f"DESCRIBE {table}")
        cols = [col[0] for col in cursor.fetchall()]
        
        should_run = False
        if not invert:
            # We want to add/rename a column, so run if it does NOT exist yet
            if column not in cols:
                # If renaming, make sure target column doesn't exist and source does
                if "RENAME COLUMN" in query:
                    source_col = query.split()[2]
                    if source_col in cols:
                        should_run = True
                else:
                    should_run = True
        else:
            # We want to drop a column, so run if it DOES exist
            if column in cols:
                should_run = True
                
        if should_run:
            alter_stmt = f"ALTER TABLE {table} {query};"
            print(f"Executing: {alter_stmt}")
            try:
                cursor.execute(alter_stmt)
            except Exception as e:
                print(f"Error executing alteration on {table}: {e}")
        else:
            print(f"Alteration for {table}.{column} already applied or not applicable.")
            
    conn.commit()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    conn.close()
    print("Database schema alterations applied successfully!")

if __name__ == '__main__':
    apply_alterations()
