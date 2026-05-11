import json
import os

path = 'fase_4/script_hanif.ipynb'
if not os.path.exists(path):
    print("Not found")
    exit(1)

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'df[\'id_mitra\'] = df[\'idmitra\'].apply(extract_int)' in ''.join(cell['source']):
        source = ''.join(cell['source'])
        
        # We rename the new extracted column to 'idmitra_int' instead of 'id_mitra'
        # to avoid collision in the mapping dict
        source = source.replace("df['id_mitra'] = df['idmitra'].apply(extract_int)", "df['idmitra_int'] = df['idmitra'].apply(extract_int)")
        
        # And we fix the mapping reference
        source = source.replace("'kelurahan': 'id_kelurahan', 'id_mitra': 'id_mitra', 'nisn': 'nisn', 'nik': 'nik',", "'kelurahan': 'id_kelurahan', 'idmitra_int': 'id_mitra', 'nisn': 'nisn', 'nik': 'nik',")
        # Just in case the previous attempt failed but was partially formatted differently:
        source = source.replace("'id_mitra': 'id_mitra'", "'idmitra_int': 'id_mitra'")
            
        cell['source'] = [line + '\n' for line in source.split('\n')]
        if cell['source'][-1] == '\n': cell['source'].pop()

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Phase 4 id_mitra mapping patched")
