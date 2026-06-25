import os

# Define the file paths
target_file = 'config.gemini/apply_migration_updates.py'

if not os.path.exists(target_file):
    print(f"Error: {target_file} not found!")
    exit(1)

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new patch_fase_5 function
new_patch_fase_5 = """def patch_fase_5():
    path = "fase_5/script_hanif.ipynb"
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    new_combined_code = \"\"\"transformed_dfs = {}

# --- HELPER FUNCTIONS ---
# Helper extract_int in Fase 5
def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\\\\d+', str(s))
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
print("\\\\n🔍 PERBANDINGAN TIPE DATA SIDE-BY-SIDE")
for old_t, new_t in hanif_tables_map:
    print(f"\\\\n{'='*15} {old_t.upper()} ➔ {new_t.upper()} {'='*15}")
    
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
            print(f"\\\\n--- SAMPLE DATA NEW (2 Baris) ---")
            display(df_new.head(2))
    else:
        print(f"⚠️ Tabel {new_t} kosong.")\"\"\"

    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "transformed_dfs = {}" in "".join(cell["source"]):
            cell["source"] = [line + "\\n" for line in new_combined_code.split("\\n")]
            if cell["source"] and cell["source"][-1] == "\\n":
                cell["source"].pop()
            patched = True
            break

    if patched:
        # Patch verification cell to avoid KeyError on removed PK id_rapor_siswa
        for cell in nb["cells"]:
            if cell["cell_type"] == "code" and "# 3.1.2 Output Pengecekan Kolom Spesifik" in "".join(cell["source"]):
                source = "".join(cell["source"])
                source = source.replace("transformed_dfs['rapor_siswa'][['id_rapor_siswa',", "transformed_dfs['rapor_siswa'][['id_siswa',")
                cell["source"] = [line + "\\n" for line in source.split("\\n")]
                if cell["source"] and cell["source"][-1] == "\\n":
                    cell["source"].pop()
        ensure_csv_export_cell(nb)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 5 notebook patched successfully with combined code!")
    else:
        print("Error: Target cell in Fase 5 notebook not found.")"""

# Define the new patch_fase_5_rapor_urutan function
new_patch_fase_5_rapor_urutan = """def patch_fase_5_rapor_urutan():
    \"\"\"
    Dummy function for backward compatibility. All urutan and format patches
    are now handled robustly by the unified patch_fase_5() block.
    \"\"\"
    print("OK: patch_fase_5_rapor_urutan is a no-op (unified with patch_fase_5).")
    return True"""

# Find patch_fase_5 in the file content and replace it
start_p5 = content.find('def patch_fase_5():')
end_p5 = content.find('print("Error: Target cell in Fase 5 notebook not found.")') + len('print("Error: Target cell in Fase 5 notebook not found.")')

if start_p5 != -1 and end_p5 != -1:
    content = content[:start_p5] + new_patch_fase_5 + content[end_p5:]
else:
    print("Error: Could not find patch_fase_5 function in file!")

# Find patch_fase_5_rapor_urutan in the file content and replace it
start_urutan = content.find('def patch_fase_5_rapor_urutan():')
end_urutan = content.find('if __name__ == "__main__":')

if start_urutan != -1 and end_urutan != -1:
    content = content[:start_urutan] + new_patch_fase_5_rapor_urutan + '\n\n\n' + content[end_urutan:]
else:
    print("Error: Could not find patch_fase_5_rapor_urutan function in file!")

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated apply_migration_updates.py!")
