import os
import pickle
import pandas as pd
import numpy as np

def audit_fase_1(data):
    print("\n--- Auditing Fase 1 ---")
    required_keys = ['busdev_bidang', 'syarat_resign', 'ttd', 'tag_siswa_keluar']
    for key in required_keys:
        if key not in data:
            print(f"[ERROR] Fase 1 is missing table: {key}")
            continue
        df = data[key]
        print(f"Table '{key}': {len(df)} rows")
        # Check for nulls
        null_counts = df.isna().sum()
        if null_counts.any():
            print(f"  [WARN] Nulls found: {null_counts[null_counts > 0].to_dict()}")
        # Check decimal .0
        for col in df.columns:
            if 'id' in col or 'id_' in col:
                has_decimal = df[col].astype(str).str.contains(r'\.0$').any()
                if has_decimal:
                    print(f"  [WARN] Column '{col}' contains decimal '.0'")

def audit_fase_2(data):
    print("\n--- Auditing Fase 2 ---")
    required_keys = ['division_user', 'model_has_roles', 'model_has_permissions']
    for key in required_keys:
        if key not in data:
            print(f"[ERROR] Fase 2 is missing table: {key}")
            continue
        df = data[key]
        print(f"Table '{key}': {len(df)} rows")
        # Check for nulls
        null_counts = df.isna().sum()
        if null_counts.any():
            print(f"  [WARN] Nulls found: {null_counts[null_counts > 0].to_dict()}")
            
def audit_fase_3(data):
    print("\n--- Auditing Fase 3 ---")
    required_keys = ['pengajuan_karyawan', 'histori_pengajuan', 'pelamar', 'pelamar_kerja', 'pelamar_sekolah', 'pelamar_kursus', 'progres_pelamar', 'rekrutmen_pelamar']
    for key in required_keys:
        if key not in data:
            print(f"[ERROR] Fase 3 is missing table: {key}")
            continue
        df = data[key]
        print(f"Table '{key}': {len(df)} rows")
        # Check for PK presence (we removed PKs for auto-increment)
        pk_cols = ['id_pelamar', 'id_pelamar_kerja', 'id_pelamar_sekolah', 'id_pelamar_kursus', 'id_progres_pelamar', 'id_rekrutmen', 'id_pengajuan', 'id_verifikasi']
        for pk in pk_cols:
            if pk in df.columns and key in ['pelamar', 'pelamar_kerja', 'pelamar_sekolah', 'pelamar_kursus', 'progres_pelamar', 'rekrutmen_pelamar', 'pengajuan_karyawan', 'histori_pengajuan']:
                # Wait, child tables have id_pelamar as FK, that is fine. But they should NOT have their own PK.
                is_pk_of_this_table = (pk == 'id_pelamar' and key == 'pelamar') or \
                                      (pk == 'id_pelamar_kerja' and key == 'pelamar_kerja') or \
                                      (pk == 'id_pelamar_sekolah' and key == 'pelamar_sekolah') or \
                                      (pk == 'id_pelamar_kursus' and key == 'pelamar_kursus') or \
                                      (pk == 'id_progres_pelamar' and key == 'progres_pelamar') or \
                                      (pk == 'id_rekrutmen' and key == 'rekrutmen_pelamar') or \
                                      (pk == 'id_pengajuan' and key == 'pengajuan_karyawan') or \
                                      (pk == 'id_verifikasi' and key == 'histori_pengajuan')
                if is_pk_of_this_table:
                    print(f"  [WARN] PK Column '{pk}' should be removed from '{key}' to let MySQL auto-increment")
        
        # Check FK reference to pelamar
        if 'id_pelamar' in df.columns and key != 'pelamar':
            # Check if there are any nulls or floats
            nulls = df['id_pelamar'].isna().sum()
            if nulls > 0:
                print(f"  [WARN] 'id_pelamar' in '{key}' has {nulls} nulls")
            # Check decimal .0
            has_decimal = df['id_pelamar'].astype(str).str.contains(r'\.0$').any()
            if has_decimal:
                print(f"  [WARN] 'id_pelamar' in '{key}' has decimal '.0'")

def audit_fase_4(data):
    print("\n--- Auditing Fase 4 ---")
    required_keys = ['siswa', 'kursus_siswa', 'siswa_keluar', 'mitra', 'mitra_progres', 'kemitraan_verifikator', 'siswa_mitra', 'siswa_mitra_keluar']
    for key in required_keys:
        if key not in data:
            print(f"[ERROR] Fase 4 is missing table: {key}")
            continue
        df = data[key]
        print(f"Table '{key}': {len(df)} rows")
        
        if key == 'siswa':
            # Check WA length (max 20)
            wa_cols = ['wa_siswa', 'wa_ortu', 'wa_administrasi']
            for col in wa_cols:
                if col in df.columns:
                    lens = df[col].dropna().astype(str).apply(len)
                    too_long = lens[lens > 20]
                    if len(too_long) > 0:
                        print(f"  [ERROR] {len(too_long)} rows in '{col}' exceed 20 chars! Max len={too_long.max()}")
            # Check domisili length (max 100)
            if 'domisili' in df.columns:
                lens = df['domisili'].dropna().astype(str).apply(len)
                too_long = lens[lens > 100]
                if len(too_long) > 0:
                    print(f"  [ERROR] {len(too_long)} rows in 'domisili' exceed 100 chars! Max len={too_long.max()}")
            # Check for NODATAYET
            for col in df.columns:
                has_nodata = (df[col].astype(str) == 'NODATAYET').any()
                if has_nodata:
                    print(f"  [WARN] Column '{col}' contains 'NODATAYET'")
                    
        if key == 'kursus_siswa':
            # Check for deleted course K00017
            has_k00017 = (df['id_kursus'] == 'K00017').any()
            if has_k00017:
                print(f"  [ERROR] 'kursus_siswa' contains deleted course K00017!")
                
        # Check PK removal
        pk_cols = {
            'siswa': 'id_siswa',
            'kursus_siswa': 'id_kursus_siswa',
            'siswa_keluar': 'id_keluar',
            'mitra': 'id_mitra',
            'mitra_progres': 'id_progres_mitra',
            'kemitraan_verifikator': 'id_kemitraan',
            'siswa_mitra': 'id_sm',
            'siswa_mitra_keluar': 'id_sm_keluar'
        }
        pk = pk_cols.get(key)
        if pk and pk in df.columns:
            print(f"  [WARN] PK Column '{pk}' should be removed from '{key}' to let MySQL auto-increment")

def audit_fase_5(data):
    print("\n--- Auditing Fase 5 ---")
    required_keys = ['rapor_format', 'rapor_format_sub', 'rapor_format_formula', 'rapor_format_formula_sub', 'rapor_level_config', 'rapor_sub_level', 'rapor_siswa', 'rapor_siswa_file', 'rapor_lacak']
    for key in required_keys:
        if key not in data:
            print(f"[ERROR] Fase 5 is missing table: {key}")
            continue
        df = data[key]
        print(f"Table '{key}': {len(df)} rows")
        
        # Check PK duplicates
        pk_map = {
            'rapor_format': 'id_rapor_format',
            'rapor_format_sub': 'id_rapor_format_sub',
            'rapor_format_formula': 'id_rapor_format_formula',
            'rapor_format_formula_sub': 'id_rapor_format_formula_sub',
            'rapor_level_config': 'id_rapor_level_config',
            'rapor_sub_level': 'id_rapor_sub_level',
            'rapor_siswa': 'id_rapor_siswa',
            'rapor_siswa_file': 'id_rapor_siswa_file',
            'rapor_lacak': 'id_rapor_lacak'
        }
        pk = pk_map.get(key)
        # Note: In Fase 5, for format tables (rapor_format, rapor_format_sub) they might keep their PKs if they are fixed references,
        # but for student tables (rapor_siswa, rapor_siswa_file, rapor_lacak) they should be removed.
        # Let's check duplicates for whatever PK column exists.
        if pk in df.columns:
            dups = df[pk].duplicated().sum()
            if dups > 0:
                print(f"  [ERROR] Table '{key}' has {dups} duplicate PKs on '{pk}'!")
            # Also warning if PK is in student tables
            if key in ['rapor_siswa', 'rapor_siswa_file', 'rapor_lacak']:
                print(f"  [WARN] PK Column '{pk}' should be removed from '{key}' to let MySQL auto-increment")
        
        # Check for K00017
        for col in df.columns:
            if df[col].astype(str).str.contains('K00017').any():
                print(f"  [ERROR] Table '{key}' column '{col}' contains reference to deleted course K00017!")
                
        # Check for null urutan in format sub
        if key == 'rapor_format_sub' and 'urutan' in df.columns:
            null_urutan = df['urutan'].isna().sum()
            if null_urutan > 0:
                print(f"  [ERROR] 'rapor_format_sub' has {null_urutan} nulls in 'urutan'!")
                
        # Check final_result lengths in rapor_siswa
        if key == 'rapor_siswa' and 'final_result' in df.columns:
            max_len = df['final_result'].dropna().astype(str).apply(len).max()
            if max_len > 255:
                print(f"  [ERROR] 'rapor_siswa.final_result' has comments exceeding 255 chars! Max len={max_len}")
            # Check for placeholder garbage
            garbage_keywords = ['comment', 'coba', 'test', 'dummy']
            garbage_rows = df[df['final_result'].str.lower().str.contains('|'.join(garbage_keywords), na=False)]
            if len(garbage_rows) > 0:
                print(f"  [WARN] 'rapor_siswa' contains {len(garbage_rows)} placeholder/garbage comments in final_result")
                
        # Check for drift/old string IDs in child tables
        if key == 'rapor_lacak':
            if 'id_siswa' in df.columns:
                has_old_s = df['id_siswa'].astype(str).str.contains('S').any()
                if has_old_s:
                    print(f"  [ERROR] 'rapor_lacak.id_siswa' contains old string IDs (e.g. S0000007)")
            if 'id_jadwal' in df.columns:
                has_old_j = df['id_jadwal'].astype(str).str.contains('J').any()
                if has_old_j:
                    print(f"  [ERROR] 'rapor_lacak.id_jadwal' contains old string IDs (e.g. J000000023)")

def main():
    pickle_paths = {
        1: 'fase_1/fase_1_hanif.pkl',
        2: 'fase_2/fase_2_hanif.pkl',
        3: 'fase_3/fase_3_hanif.pkl',
        4: 'fase_4/fase_4_hanif.pkl',
        5: 'fase_5/fase_5_hanif.pkl'
    }
    
    for phase, path in pickle_paths.items():
        if not os.path.exists(path):
            print(f"[ERROR] Pickle file for Fase {phase} not found at {path}")
            continue
        with open(path, 'rb') as f:
            data = pickle.load(f)
            
        if phase == 1:
            audit_fase_1(data)
        elif phase == 2:
            audit_fase_2(data)
        elif phase == 3:
            audit_fase_3(data)
        elif phase == 4:
            audit_fase_4(data)
        elif phase == 5:
            audit_fase_5(data)

if __name__ == '__main__':
    main()
