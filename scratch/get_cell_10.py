import json

with open('fase_4/script_hanif.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)
    
found_idx = -1
for idx, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = "".join(cell.get('source', []))
        if '# Build kursus_siswa dynamically' in source:
            found_idx = idx
            break

if found_idx != -1:
    source = "".join(nb['cells'][found_idx].get('source', []))
    with open('scratch/cell_10_source.py', 'w', encoding='utf-8') as f:
        f.write(source)
    print(f"Saved Cell {found_idx} source to scratch/cell_10_source.py")
else:
    print("Not found!")
