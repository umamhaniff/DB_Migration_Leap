# ==========================================
# CELL 1
# ==========================================
def display(*args, **kwargs):
    for arg in args:
        print(arg)

import sys
import os
import mysql.connector
import pandas as pd
import re
from datetime import datetime
import pickle
import json
sys.path.append(os.path.abspath('..'))
from config import get_db_config
import warnings
warnings.filterwarnings('ignore')

# ==========================================
# CELL 2
# ==========================================
config = get_db_config()
db_old = mysql.connector.connect(**config['db_old'])
cursor_old = db_old.cursor(dictionary=True)
db_new = mysql.connector.connect(**config['db_future'])
cursor_new = db_new.cursor(dictionary=True)
print(f"Connected to {config['db_old']['database']} and {config['db_future']['database']}")

# ==========================================
# CELL 3
# ==========================================
hanif_tables_map = [
    ('format_rapor', 'rapor_format'),
    ('format_rapor_detil', 'rapor_format_sub'),
    ('format_rapor_rumus', 'rapor_format_formula'),
    ('format_rapor_detil_rumus', 'rapor_format_formula_sub'),
    ('format_raport_level', 'rapor_level_config'),
    ('rapor', 'rapor_siswa'),
    ('file_rapor_siswa', 'rapor_siswa_file'),
    ('history_rapor', 'rapor_lacak')
]

raw_data = {}
for old_t, new_t in hanif_tables_map:
    try:
        cursor_old.execute(f"SELECT * FROM `{old_t}`")
        raw_data[old_t] = cursor_old.fetchall()
        print(f"✅ {old_t} loaded: {len(raw_data[old_t])} records")
    except Exception as e:
        print(f"❌ ERROR loading {old_t}: {e}")

# ==========================================
# CELL 4
# ==========================================
transformed_dfs = {}

# --- HELPER FUNCTIONS ---
# Helper extract_int in Fase 5
def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\d+', str(s))
    return int(nums[0]) if nums else None

# ponytail: load student ID auto-increment mapping from Fase 4
import os
student_id_map = {}
mapping_path = '../fase_4/mapping_siswa.pkl'
if not os.path.exists(mapping_path):
    mapping_path = 'fase_4/mapping_siswa.pkl'
if os.path.exists(mapping_path):
    df_map = pd.read_pickle(mapping_path)
    student_id_map = dict(zip(df_map['idsiswa_lama'], df_map['id_siswa_baru']))

def map_student_id(idsiswa_val):
    if pd.isna(idsiswa_val): return None
    val_str = str(idsiswa_val).strip()
    return student_id_map.get(val_str, None)

# ponytail: load schedule ID auto-increment mapping from Fase 4
schedule_id_map = {}
sched_mapping_path = '../fase_4/mapping_id_jadwal.pkl'
if not os.path.exists(sched_mapping_path):
    sched_mapping_path = 'fase_4/mapping_id_jadwal.pkl'
if os.path.exists(sched_mapping_path):
    schedule_id_map = pd.read_pickle(sched_mapping_path)

def map_schedule_id(idjadwal_val):
    if pd.isna(idjadwal_val): return None
    val_str = str(idjadwal_val).strip()
    return schedule_id_map.get(val_str, None)

# ponytail: clean placeholder comments (Category A) and preserve genuine ones (Category B)
def clean_nilai_comment(val):
    if pd.isna(val): return ""
    val_str = str(val).strip()
    garbage_keywords = ['comment', 'coba ini', 'long comment', 'test', 'dummy', 'qwerty', 'asdf']
    if any(kw in val_str.lower() for kw in garbage_keywords):
        return ""
    return val_str

# ponytail: define valid student and schedule IDs directly from loaded Fase 4 mappings (since target DB is empty locally)
valid_siswa = set(student_id_map.values())
valid_jadwal = set(schedule_id_map.values())

# --- TRANSFORMATION ---

# 1. format_rapor -> rapor_format (+ urutan dari import CSV)
if 'format_rapor' in raw_data:
    df = pd.DataFrame(raw_data['format_rapor'])
    mapping = {
        'idformat_rapor': 'id_rapor_format',
        'idpendkursus': 'id_kursus', 'title': 'judul_rapor'
    }
    df_rf = df.rename(columns=mapping)[list(mapping.values())]
    # ponytail: filter out rows belonging to deleted course 'K00017' directly using Pandas
    df_rf = df_rf[df_rf['id_kursus'] != 'K00017']
    # Merge kolom urutan dari rapor_format_import.csv (sudah diurutkan manual)
    # ponytail: merge directly on id_rapor_format to avoid duplicates and Cartesian product!
    df_urutan_rf = pd.read_csv('rapor_format_import.csv')[['id_rapor_format', 'urutan']]
    df_rf = df_rf.merge(df_urutan_rf, on='id_rapor_format', how='left')
    df_rf['urutan'] = df_rf['urutan'].fillna(0).astype('Int64')  # default to 0 if NaN
    transformed_dfs['rapor_format'] = df_rf

# 2. format_rapor_detil -> rapor_format_sub (+ urutan dari import CSV)
if 'format_rapor_detil' in raw_data:
    df = pd.DataFrame(raw_data['format_rapor_detil'])
    mapping = {
        'idformat_rd': 'id_rapor_format_sub',
        'idformat_rapor': 'id_rapor_format', 'subtitle': 'sub_judul_rapor'
    }
    df_rfs = df.rename(columns=mapping)[list(mapping.values())]
    # Filter out sub-formats where parent format was filtered out due to deleted courses
    df_rfs = df_rfs[df_rfs['id_rapor_format'].isin(transformed_dfs['rapor_format']['id_rapor_format'])]
    # Merge kolom urutan dari rapor_format_sub_import.csv (sudah diurutkan manual)
    # ponytail: merge directly on id_rapor_format_sub to avoid any key alignment bugs!
    df_urutan_rfs = pd.read_csv('rapor_format_sub_import.csv')[['id_rapor_format_sub', 'urutan']]
    df_rfs = df_rfs.merge(df_urutan_rfs, on='id_rapor_format_sub', how='left')
    df_rfs['urutan'] = df_rfs['urutan'].fillna(0).astype('Int64')  # default to 0 if NaN
    transformed_dfs['rapor_format_sub'] = df_rfs

# 3. format_rapor_rumus -> rapor_format_formula
if 'format_rapor_rumus' in raw_data:
    df = pd.DataFrame(raw_data['format_rapor_rumus'])
    mapping = {
        'idformat_rapor': 'id_rapor_format', 'param_operator': 'logika_operator'
    }
    df_rff = df.rename(columns=mapping)[list(mapping.values())]
    # Filter out records where parent format was filtered out due to deleted courses
    df_rff = df_rff[df_rff['id_rapor_format'].isin(transformed_dfs['rapor_format']['id_rapor_format'])]
    transformed_dfs['rapor_format_formula'] = df_rff

# 4. format_rapor_detil_rumus -> rapor_format_formula_sub
if 'format_rapor_detil_rumus' in raw_data:
    df = pd.DataFrame(raw_data['format_rapor_detil_rumus'])
    mapping = {
        'idformat_rd': 'id_rapor_format_sub', 'param_operator': 'logika_operator',
        'idlevel': 'id_level'
    }
    df_rffs = df.rename(columns=mapping)[list(mapping.values())]
    # Filter out records where parent sub-format was filtered out
    df_rffs = df_rffs[df_rffs['id_rapor_format_sub'].isin(transformed_dfs['rapor_format_sub']['id_rapor_format_sub'])]
    transformed_dfs['rapor_format_formula_sub'] = df_rffs

# 5. format_raport_level -> rapor_level_config
if 'format_raport_level' in raw_data:
    df = pd.DataFrame(raw_data['format_raport_level'])
    mapping = {
        'idlevel': 'id_level',
        'idpendkursus': 'id_kursus', 'idformat_rapor': 'id_rapor_format'
    }
    df_rlc = df.rename(columns=mapping)[list(mapping.values())]
    # Filter out skipped formats and deleted courses
    df_rlc = df_rlc[
        (df_rlc['id_kursus'] != 'K00017') &
        df_rlc['id_rapor_format'].isin(transformed_dfs['rapor_format']['id_rapor_format'])
    ]
    transformed_dfs['rapor_level_config'] = df_rlc

# 6. rapor_sub_level (Tabel Baru)
transformed_dfs['rapor_sub_level'] = pd.DataFrame(columns=['id_rapor_format_sub', 'id_level'])

# 7. rapor -> rapor_siswa
if 'rapor' in raw_data:
    df = pd.DataFrame(raw_data['rapor'])
    
    # ponytail: map id_siswa and id_jadwal using the loaded mappings
    df['id_siswa_clean'] = df['idsiswa'].apply(map_student_id).astype('Int64')
    df['id_jadwal_clean'] = df['idjadwal'].apply(map_schedule_id).astype('Int64')
    
    # ponytail: clean placeholder comments (Category A) and keep Category B intact (to be VARCHAR(255))
    df['nilai_clean'] = df['nilai'].apply(clean_nilai_comment)
    
    # Map idp_nilai string (e.g. 'P00745') to new parameter_nilai auto-increment ID
    cursor_old.execute("SELECT idp_nilai FROM parameter_nilai ORDER BY idp_nilai")
    param_rows = cursor_old.fetchall()
    param_map = {}
    for idx, row in enumerate(param_rows):
        if isinstance(row, dict):
            param_map[row['idp_nilai']] = idx + 1
        elif isinstance(row, (list, tuple)):
            param_map[row[0]] = idx + 1
    df['id_parameter_nilai'] = df['idp_nilai'].map(param_map).astype('Int64')
    valid_param = set(param_map.values())
    
    # ponytail: filter to only include rows with valid FKs to avoid any database insertion skip
    df_filtered = df[
        df['id_siswa_clean'].isin(valid_siswa) &
        df['id_jadwal_clean'].isin(valid_jadwal) &
        (df['id_parameter_nilai'].isna() | df['id_parameter_nilai'].isin(valid_param))
    ].copy()
    
    # ponytail: AFTER filtering, generate sequential auto-increment IDs to avoid any drift!
    df_filtered = df_filtered.reset_index(drop=True)
    df_filtered['id_rapor_siswa_new'] = df_filtered.index + 1
    rapor_id_map = dict(zip(df_filtered['idrapor'], df_filtered['id_rapor_siswa_new']))
    
    # ponytail: build and save rapor_siswa ID mapping
    df_mapping_rs = pd.DataFrame({
        'idrapor_lama': df_filtered['idrapor'],
        'id_rapor_siswa_baru': df_filtered['id_rapor_siswa_new']
    })
    df_mapping_rs['id_rapor_siswa_baru'] = df_mapping_rs['id_rapor_siswa_baru'].astype('Int64')
    pd.to_pickle(df_mapping_rs, 'mapping_rapor_siswa.pkl')
    transformed_dfs['mapping_rapor_siswa'] = df_mapping_rs
    
    valid_rapor_siswa_ids = set(df_filtered['id_rapor_siswa_new'])
    
    mapping = {
        'id_jadwal_clean': 'id_jadwal', 'id_siswa_clean': 'id_siswa',
        'tanggal': 'tanggal_input', 'id_parameter_nilai': 'id_parameter_nilai', 'nilai_clean': 'final_result'
    }
    transformed_dfs['rapor_siswa'] = df_filtered.rename(columns=mapping)[list(mapping.values())]

# 8. file_rapor_siswa -> rapor_siswa_file
if 'file_rapor_siswa' in raw_data and 'rapor_siswa' in transformed_dfs:
    df = pd.DataFrame(raw_data['file_rapor_siswa'])
    
    # Fetch old idrapor string and map it to new id_rapor_siswa integer
    df_rapor_old = pd.DataFrame(raw_data['rapor'])[['idsiswa', 'idjadwal', 'idrapor']].drop_duplicates(subset=['idsiswa', 'idjadwal'])
    df = df.merge(df_rapor_old, on=['idsiswa', 'idjadwal'], how='left')
    df['id_rapor_siswa'] = df['idrapor'].map(rapor_id_map).astype('Int64')
    
    # ponytail: filter out rows if parent rapor_siswa was filtered out (to avoid FK failure)
    df_filtered = df[df['id_rapor_siswa'].isin(valid_rapor_siswa_ids)].copy()
    
    # ponytail: AFTER filtering, generate sequential auto-increment IDs to avoid any drift!
    df_filtered = df_filtered.reset_index(drop=True)
    df_filtered['id_rapor_siswa_file_new'] = df_filtered.index + 1
    file_id_map = dict(zip(df_filtered['idfile'], df_filtered['id_rapor_siswa_file_new']))
    
    # ponytail: build and save rapor_siswa_file ID mapping
    df_mapping_rsf = pd.DataFrame({
        'idfile_lama': df_filtered['idfile'],
        'id_rapor_siswa_file_baru': df_filtered['id_rapor_siswa_file_new']
    })
    df_mapping_rsf['id_rapor_siswa_file_baru'] = df_mapping_rsf['id_rapor_siswa_file_baru'].astype('Int64')
    pd.to_pickle(df_mapping_rsf, 'mapping_rapor_siswa_file.pkl')
    transformed_dfs['mapping_rapor_siswa_file'] = df_mapping_rsf
    
    valid_file_ids = set(df_filtered['id_rapor_siswa_file_new'])
    
    mapping = {
        'id_rapor_siswa': 'id_rapor_siswa', 'path': 'file_rapor_path'
    }
    transformed_dfs['rapor_siswa_file'] = df_filtered.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 9. history_rapor -> rapor_lacak
if 'history_rapor' in raw_data and 'rapor_siswa_file' in transformed_dfs:
    df = pd.DataFrame(raw_data['history_rapor'])
    df['status'] = df['status'].replace({'Terkirim': 'Terkirim', 'Gagal': 'Gagal'})
    
    df_file_old = pd.DataFrame(raw_data['file_rapor_siswa'])[['idfile', 'idsiswa', 'idjadwal']]
    df_file_old['id_rapor_siswa_file'] = df_file_old['idfile'].map(file_id_map).astype('Int64')
    
    # ponytail: map id_siswa and id_jadwal using the loaded mappings
    df['id_siswa_clean'] = df['idsiswa'].apply(map_student_id).astype('Int64')
    df['id_jadwal_clean'] = df['idjadwal'].apply(map_schedule_id).astype('Int64')
    
    df_merged = df.merge(df_file_old[['idsiswa', 'idjadwal', 'id_rapor_siswa_file']], on=['idsiswa', 'idjadwal'], how='left')
    df_merged['id_rapor_siswa_file'] = df_merged['id_rapor_siswa_file'].astype('Int64')
    
    # ponytail: filter out rows if parent student/schedule/file was filtered out (to avoid FK failure)
    df_merged = df_merged[
        df_merged['id_siswa_clean'].isin(valid_siswa) &
        df_merged['id_jadwal_clean'].isin(valid_jadwal) &
        (df_merged['id_rapor_siswa_file'].isna() | df_merged['id_rapor_siswa_file'].isin(valid_file_ids))
    ]
    
    mapping = {
        'id_siswa_clean': 'id_siswa',
        'id_jadwal_clean': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'
    }
    transformed_dfs['rapor_lacak'] = df_merged.rename(columns=mapping)[list(mapping.values()) + ['id_rapor_siswa_file']]

# ponytail: auto-convert datetime and date columns to standard strings to avoid MySQL timestamp conversion errors
for table_name, df_tbl in list(transformed_dfs.items()):
    if df_tbl is not None and not df_tbl.empty:
        for col in df_tbl.columns:
            if pd.api.types.is_datetime64_any_dtype(df_tbl[col]):
                df_tbl[col] = df_tbl[col].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if pd.notna(x) else None)
            else:
                first_val = df_tbl[col].dropna().iloc[0] if not df_tbl[col].dropna().empty else None
                if first_val is not None and hasattr(first_val, 'strftime'):
                    import datetime as dt_mod
                    if isinstance(first_val, dt_mod.datetime) or hasattr(first_val, 'hour'):
                        df_tbl[col] = df_tbl[col].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if pd.notna(x) and hasattr(x, 'strftime') else (str(x) if pd.notna(x) else None))
                    else:
                        df_tbl[col] = df_tbl[col].apply(lambda x: x.strftime('%Y-%m-%d') if pd.notna(x) and hasattr(x, 'strftime') else (str(x) if pd.notna(x) else None))

print("OK: Transformasi 11 tabel Fase 5 selesai.")

# 3.1.3 Detail Perbandingan Kolom & Tipe Data (Side-by-Side)
print("\n🔍 PERBANDINGAN TIPE DATA SIDE-BY-SIDE")
for old_t, new_t in hanif_tables_map:
    print(f"\n{'='*15} {old_t.upper()} ➔ {new_t.upper()} {'='*15}")
    
    df_old = pd.DataFrame(raw_data.get(old_t, []))
    df_new = transformed_dfs.get(new_t, pd.DataFrame())
    
    if not df_new.empty or not df_old.empty:
        comparison = []
        table_mapping = {}
        if old_t == 'format_rapor': table_mapping = {'idformat_rapor': 'id_rapor_format', 'idpendkursus': 'id_kursus', 'title': 'judul_rapor'}
        elif old_t == 'format_rapor_detil': table_mapping = {'idformat_rd': 'id_rapor_format_sub', 'idformat_rapor': 'id_rapor_format', 'subtitle': 'sub_judul_rapor'}
        elif old_t == 'format_rapor_rumus': table_mapping = {'idfrr': 'id_rapor_format_formula', 'idformat_rapor': 'id_rapor_format', 'param_operator': 'logika_operator'}
        elif old_t == 'format_rapor_detil_rumus': table_mapping = {'idfrdr': 'id_rapor_format_formula_sub', 'idformat_rd': 'id_rapor_format_sub', 'param_operator': 'logika_operator', 'idlevel': 'id_level'}
        elif old_t == 'format_raport_level': table_mapping = {'idformat_rl': 'id_rapor_level_config', 'idlevel': 'id_level', 'idpendkursus': 'id_kursus', 'idformat_rapor': 'id_rapor_format'}
        elif old_t == 'rapor': table_mapping = {'idrapor': 'id_rapor_siswa', 'idjadwal': 'id_jadwal', 'idsiswa': 'id_siswa', 'tanggal': 'tanggal_input', 'idp_nilai': 'id_parameter_nilai', 'nilai': 'final_result'}
        elif old_t == 'file_rapor_siswa': table_mapping = {'idfile': 'id_rapor_siswa_file', 'idsiswa': 'id_rapor_siswa', 'path': 'file_rapor_path'}
        elif old_t == 'history_rapor': table_mapping = {'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa', 'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'}

        for old_col, new_col in table_mapping.items():
            comparison.append({
                'Old Column': old_col,
                'Old Type': str(df_old[old_col].dtype) if not df_old.empty and old_col in df_old.columns else "N/A",
                '➔': '➔',
                'New Column': new_col,
                'New Type': str(df_new[new_col].dtype) if not df_new.empty and new_col in df_new.columns else "N/A"
            })
        
        # Cek kolom baru
        if not df_new.empty:
            for col in df_new.columns:
                if col not in table_mapping.values():
                    comparison.append({
                        'Old Column': '(KOLOM BARU / CUSTOM)',
                        'Old Type': '-',
                        '➔': '➔',
                        'New Column': col,
                        'New Type': str(df_new[col].dtype)
                    })
        
        display(pd.DataFrame(comparison))
        if not df_new.empty:
            print(f"\n--- SAMPLE DATA NEW (2 Baris) ---")
            display(df_new.head(2))
    else:
        print(f"⚠️ Tabel {new_t} kosong.")


# ==========================================
# CELL 5
# ==========================================
# 3.1.1 Ringkasan Jumlah Baris
print("📊 RINGKASAN MIGRASI (RECORDS COUNT)")
print("="*70)
summary_list = []
for old_t, new_t in hanif_tables_map:
    old_c = len(raw_data.get(old_t, []))
    new_c = len(transformed_dfs.get(new_t, []))
    summary_list.append({
        'Tabel Lama': old_t,
        'Tabel Baru': new_t,
        'Old Recs': old_c,
        'New Recs': new_c,
        'Diff': new_c - old_c,
        'Status': "✅ OK" if old_c == new_c else "⚠️ Cek"
    })
display(pd.DataFrame(summary_list))

total_old_all = sum(len(records) for records in raw_data.values())
total_new_all = sum(len(df) for df in transformed_dfs.values())
print(f"\n📢 TOTAL REKAPITULASI: {total_old_all} (Old) ➔ {total_new_all} (New)")
if total_old_all == total_new_all: print("✅ SEMUA DATA TERANGKUT")
else: print(f"⚠️ ADA SELISIH: {total_new_all - total_old_all} baris")

# ==========================================
# CELL 6
# ==========================================
# 3.1.2 Output Pengecekan Kolom Spesifik (KETERANGAN mapping.md)
print("\n🔍 PENGECEKAN TRANSFORMASI SPESIFIK (KETERANGAN mapping.md)")
print("="*70)

# 1. Pengecekan Tanggal Input (Rapor Siswa)
if 'rapor_siswa' in transformed_dfs:
    print("\n[RAPOR_SISWA] Pengecekan tanggal_input (Direct Mapping):")
    display(transformed_dfs['rapor_siswa'][['id_siswa', 'tanggal_input']].head(5))

# 2. Pengecekan Rapor Lacak (Enum Status)
if 'rapor_lacak' in transformed_dfs:
    print("\n[RAPOR_LACAK] Pengecekan Normalisasi Status Pengiriman:")
    display(transformed_dfs['rapor_lacak']['status_pengiriman'].value_counts())

# 3. Pengecekan Rapor Siswa File
if 'rapor_siswa_file' in transformed_dfs:
    print("\n[RAPOR_SISWA_FILE] Pengecekan path file:")
    display(transformed_dfs['rapor_siswa_file'][['id_rapor_siswa', 'file_rapor_path']].head(5))


# ==========================================
# CELL 7
# ==========================================


# ==========================================
# CELL 8
# ==========================================
# 3.1.3 Detail Perbandingan Kolom & Tipe Data (Side-by-Side)
print("\n🔍 PERBANDINGAN TIPE DATA SIDE-BY-SIDE")
for old_t, new_t in hanif_tables_map:
    print(f"\n{'='*15} {old_t.upper()} ➔ {new_t.upper()} {'='*15}")
    
    df_old = pd.DataFrame(raw_data.get(old_t, []))
    df_new = transformed_dfs.get(new_t, pd.DataFrame())
    
    if not df_new.empty or not df_old.empty:
        comparison = []
        table_mapping = {}
        if old_t == 'format_rapor': table_mapping = {'idformat_rapor': 'id_rapor_format', 'idpendkursus': 'id_kursus', 'title': 'judul_rapor'}
        elif old_t == 'format_rapor_detil': table_mapping = {'idformat_rd': 'id_rapor_format_sub', 'idformat_rapor': 'id_rapor_format', 'subtitle': 'sub_judul_rapor'}
        elif old_t == 'format_rapor_rumus': table_mapping = {'idfrr': 'id_rapor_format_formula', 'idformat_rapor': 'id_rapor_format', 'param_operator': 'logika_operator'}
        elif old_t == 'format_rapor_detil_rumus': table_mapping = {'idfrdr': 'id_rapor_format_formula_sub', 'idformat_rd': 'id_rapor_format_sub', 'param_operator': 'logika_operator', 'idlevel': 'id_level'}
        elif old_t == 'format_raport_level': table_mapping = {'idformat_rl': 'id_rapor_level_config', 'idlevel': 'id_level', 'idpendkursus': 'id_kursus', 'idformat_rapor': 'id_rapor_format'}
        elif old_t == 'rapor': table_mapping = {'idrapor': 'id_rapor_siswa', 'idjadwal': 'id_jadwal', 'idsiswa': 'id_siswa', 'tanggal': 'tanggal_input', 'idp_nilai': 'id_parameter_nilai', 'nilai': 'final_result'}
        elif old_t == 'file_rapor_siswa': table_mapping = {'idfile': 'id_rapor_siswa_file', 'idsiswa': 'id_rapor_siswa', 'path': 'file_rapor_path'}
        elif old_t == 'history_rapor': table_mapping = {'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa', 'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'}

        for old_col, new_col in table_mapping.items():
            comparison.append({
                'Old Column': old_col,
                'Old Type': str(df_old[old_col].dtype) if not df_old.empty and old_col in df_old.columns else "N/A",
                '➔': '➔',
                'New Column': new_col,
                'New Type': str(df_new[new_col].dtype) if not df_new.empty and new_col in df_new.columns else "N/A"
            })
        
        # Cek kolom baru
        if not df_new.empty:
            for col in df_new.columns:
                if col not in table_mapping.values():
                    comparison.append({
                        'Old Column': '(KOLOM BARU / CUSTOM)',
                        'Old Type': '-',
                        '➔': '➔',
                        'New Column': col,
                        'New Type': str(df_new[col].dtype)
                    })
        
        display(pd.DataFrame(comparison))
        if not df_new.empty:
            print(f"\n--- SAMPLE DATA NEW (2 Baris) ---")
            display(df_new.head(2))
    else:
        print(f"⚠️ Tabel {new_t} kosong.")

# ==========================================
# CELL 9
# ==========================================
file_name = 'fase_5_hanif.pkl'
with open(file_name, 'wb') as f:
    pickle.dump(transformed_dfs, f)

total_records_new = sum(len(df) for df in transformed_dfs.values())
total_records_old = sum(len(records) for records in raw_data.values())

migration_result = {
    'fase': 'fase_5',
    'script': 'script_hanif',
    'fase_num': 5,
    'status': 'ready_for_insert',
    'old_records_total': total_records_old,
    'new_records_total': total_records_new,
    'diff': total_records_new - total_records_old,
    'pickle_file': file_name,
    'timestamp': datetime.now().isoformat()
}
print(json.dumps(migration_result, indent=2))

cursor_old.close()
cursor_new.close()
db_old.close()
db_new.close()

# ==========================================
# CELL 10
# ==========================================
# --- EXPORT KE CSV UNTUK VERIFIKASI ---
EXPORT_TO_CSV = True  # Ubah ke False jika tidak ingin menghasilkan file CSV

if EXPORT_TO_CSV:
    import os
    import pandas as pd
    target_dir = "../extract/cek_csv"
    os.makedirs(target_dir, exist_ok=True)
    for tbl_name, df_tbl in transformed_dfs.items():
        csv_path = os.path.join(target_dir, f"{tbl_name}.csv")
        df_to_save = df_tbl.copy()
        
        # Clean any float ID/FK columns that contain .0 to pure integers
        for col in df_to_save.columns:
            col_lower = col.lower()
            is_id_col = col_lower.startswith('id_') or col_lower.endswith('_id') or col_lower == 'id' or 'id_' in col_lower or '_id_' in col_lower
            if is_id_col:
                non_nulls = df_to_save[col].dropna()
                if not non_nulls.empty:
                    try:
                        pd.to_numeric(non_nulls, errors='raise')
                        df_to_save[col] = pd.to_numeric(df_to_save[col], errors='coerce').round().astype('Int64')
                    except (ValueError, TypeError):
                        pass
        
        # Fix: Convert any StringDtype to object for clean serialization
        for col in df_to_save.columns:
            if str(df_to_save[col].dtype) in ['string', 'string[python]']:
                df_to_save[col] = df_to_save[col].astype(object)
        df_to_save.to_csv(csv_path, index=False)
        print(f"💾 Tabel {tbl_name} diekspor ke {csv_path} ({len(df_tbl)} baris)")
else:
    print("ℹ️ Ekspor ke CSV dinonaktifkan.")

