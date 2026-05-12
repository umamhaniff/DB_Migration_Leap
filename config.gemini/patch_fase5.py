import json
import os

path = 'fase_5/script_hanif.ipynb'
if not os.path.exists(path):
    print("Not found")
    exit(1)

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'file_rapor_siswa -> rapor_siswa_file' in ''.join(cell['source']):
        source = ''.join(cell['source'])
        
        # Original logic causing explosion:
        # df_rapor_old = pd.DataFrame(raw_data['rapor'])[['idsiswa', 'idrapor']]
        # df = df.merge(df_rapor_old, on='idsiswa', how='left')
        
        # The correct logic: Both 'file_rapor_siswa' and 'rapor' contain 'idsiswa' and 'idjadwal'.
        # We need to merge on both 'idsiswa' and 'idjadwal' to avoid Cartesian explosion because a student
        # can have multiple reports (different schedules/idjadwal) and multiple parameters per schedule.
        # But wait, 'rapor' has multiple rows for the same idsiswa and idjadwal (different parameters).
        # We just need ONE 'idrapor' per (idsiswa, idjadwal) for 'rapor_siswa_file', or maybe mapping.md
        # indicates something else. mapping.md: cari id_rapor_siswa di rapor_siswa (db_new).
        # Since 'rapor' table has multiple 'idrapor' for a single (idsiswa, idjadwal), picking the first one
        # is the standard approach when a file represents the whole report card.
        
        new_rapor_file = """    # file_rapor_siswa and rapor both have idsiswa and idjadwal
    # 'rapor' has multiple rows per (idsiswa, idjadwal) for different parameter scores.
    # We drop duplicates on ['idsiswa', 'idjadwal'] to get one representative idrapor per report card.
    df_rapor_old = pd.DataFrame(raw_data['rapor'])[['idsiswa', 'idjadwal', 'idrapor']].drop_duplicates(subset=['idsiswa', 'idjadwal'])
    df = df.merge(df_rapor_old, on=['idsiswa', 'idjadwal'], how='left')
    df = df.rename(columns={'idrapor': 'id_rapor_siswa'})
    
    mapping = {
        'idfile': 'id_rapor_siswa_file', 'id_rapor_siswa': 'id_rapor_siswa', 'path': 'file_rapor_path'
    }
    transformed_dfs['rapor_siswa_file'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))"""

        # Replace the logic for 8
        old_8_logic = """    # Using merge instead of dict to avoid data loss if idsiswa has multiple reports
    df_rapor_old = pd.DataFrame(raw_data['rapor'])[['idsiswa', 'idrapor']]
    df = df.merge(df_rapor_old, on='idsiswa', how='left')
    df = df.rename(columns={'idrapor': 'id_rapor_siswa'})
    
    mapping = {
        'idfile': 'id_rapor_siswa_file', 'id_rapor_siswa': 'id_rapor_siswa', 'path': 'file_rapor_path'
    }
    transformed_dfs['rapor_siswa_file'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))"""
        
        if old_8_logic in source:
            source = source.replace(old_8_logic, new_rapor_file)

        # Fix history_rapor -> rapor_lacak logic
        old_9_logic = """    # Using merge instead of dict to avoid data loss
    df_file_new = transformed_dfs['rapor_siswa_file'][['id_rapor_siswa_file']]
    # We need idsiswa from old file data to merge with history
    df_file_old = pd.DataFrame(raw_data['file_rapor_siswa'])[['idfile', 'idsiswa']]
    df_file_mapping = pd.concat([df_file_old, df_file_new], axis=1)
    
    mapping = {
        'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa',
        'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'
    }
    df_final = df.rename(columns=mapping)
    # Join on id_siswa (and id_jadwal if available in both for better precision)
    df_final = df_final.merge(df_file_mapping[['idsiswa', 'id_rapor_siswa_file']], left_on='id_siswa', right_on='idsiswa', how='left')
    
    transformed_dfs['rapor_lacak'] = df_final[list(mapping.values()) + ['id_rapor_siswa_file']]"""

        new_9_logic = """    # history_rapor has idsiswa and idjadwal. file_rapor_siswa also has idsiswa and idjadwal.
    # We merge them on ['idsiswa', 'idjadwal'] to find the correct file id for the history log.
    df_file_old = pd.DataFrame(raw_data['file_rapor_siswa'])[['idfile', 'idsiswa', 'idjadwal']]
    # Rename idfile to id_rapor_siswa_file as mapped in step 8
    df_file_old = df_file_old.rename(columns={'idfile': 'id_rapor_siswa_file'})
    
    mapping = {
        'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa',
        'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'
    }
    # Do the merge BEFORE renaming columns to keep 'idsiswa' and 'idjadwal'
    df_merged = df.merge(df_file_old[['idsiswa', 'idjadwal', 'id_rapor_siswa_file']], on=['idsiswa', 'idjadwal'], how='left')
    
    df_final = df_merged.rename(columns=mapping)
    transformed_dfs['rapor_lacak'] = df_final[list(mapping.values()) + ['id_rapor_siswa_file']]"""
        
        if old_9_logic in source:
            source = source.replace(old_9_logic, new_9_logic)
            
        cell['source'] = [line + '\n' for line in source.split('\n')]
        if cell['source'][-1] == '\n': cell['source'].pop()

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Patch Fase 5 applied")