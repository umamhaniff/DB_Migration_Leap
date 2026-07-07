import os
import sys
import mysql.connector
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_new = mysql.connector.connect(**cfg['db_new'])
    cursor_new = conn_new.cursor(dictionary=True)
    
    hanif_tables = {
        'fase_1': ['busdev_bidang', 'syarat_resign', 'ttd', 'tag_siswa_keluar'],
        'fase_2': ['division_user'],
        'fase_3': ['pelamar', 'pelamar_kerja', 'pelamar_sekolah', 'pelamar_kursus', 'progres_pelamar', 'rekrutmen_pelamar', 'pengajuan_karyawan', 'histori_pengajuan'],
        'fase_4': ['siswa', 'kursus_siswa', 'siswa_keluar', 'mitra', 'mitra_progres', 'kemitraan_verifikator', 'siswa_mitra', 'siswa_mitra_keluar'],
        'fase_5': ['rapor_format', 'rapor_format_formula', 'rapor_format_formula_sub', 'rapor_format_sub', 'rapor_level_config', 'rapor_sub_level']
    }
    
    print("=== TECHNICAL VALUE & MAPPING INTEGRITY AUDIT ===")
    
    for phase, tables in hanif_tables.items():
        print(f"\n[{phase.upper()}]")
        for tbl in tables:
            cursor_new.execute(f"SHOW TABLES LIKE '{tbl}'")
            if not cursor_new.fetchone():
                print(f"  - {tbl:<25}: NOT CREATED IN DB_NEW")
                continue
                
            cursor_new.execute(f"SELECT COUNT(*) as cnt FROM `{tbl}`")
            row_count = cursor_new.fetchone()['cnt']
            
            # Basic validation
            null_checks = []
            if tbl == 'siswa':
                # Check that no email has value '0' or dummy issues, and check B2B mitra mapping
                cursor_new.execute("SELECT COUNT(*) as cnt FROM siswa WHERE email = '0'")
                zeros = cursor_new.fetchone()['cnt']
                if zeros > 0:
                    null_checks.append(f"Found {zeros} rows with email='0'")
                
                # Check B2B mitra
                cursor_new.execute("SELECT id_siswa, nama_lengkap, id_mitra FROM siswa WHERE id_siswa IN (1293, 337)")
                b2b_check = cursor_new.fetchall()
                for r in b2b_check:
                    null_checks.append(f"B2B check: {r['nama_lengkap']} -> id_mitra: {r['id_mitra']}")
                    
            elif tbl == 'kursus_siswa':
                # Check that there are no student IDs mapping to non-existing students
                cursor_new.execute("SELECT COUNT(*) as cnt FROM kursus_siswa WHERE id_siswa NOT IN (SELECT id_siswa FROM siswa)")
                orphans = cursor_new.fetchone()['cnt']
                if orphans > 0:
                    null_checks.append(f"Orphan id_siswa found: {orphans}")
                
            elif tbl == 'siswa_keluar':
                # Check that id_siswa and id_kursus are fully resolved
                cursor_new.execute("SELECT COUNT(*) as cnt FROM siswa_keluar WHERE id_siswa IS NULL OR id_kursus IS NULL")
                nulls = cursor_new.fetchone()['cnt']
                if nulls > 0:
                    null_checks.append(f"Null FKs: {nulls}")
                    
            elif tbl == 'rekrutmen_pelamar':
                # Check for null id_pelamar
                cursor_new.execute("SELECT COUNT(*) as cnt FROM rekrutmen_pelamar WHERE id_pelamar IS NULL")
                null_p = cursor_new.fetchone()['cnt']
                if null_p > 0:
                    null_checks.append(f"Null id_pelamar: {null_p} (Note: check if nullable in schema)")
            
            status_str = "OK" if not null_checks else "ATTENTION"
            print(f"  - {tbl:<25}: {row_count:<5} rows | Status: {status_str}")
            for check in null_checks:
                print(f"    * {check}")
                
    conn_new.close()

if __name__ == '__main__':
    main()
