import json
import sys

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass
        
    with open('fase_4/script_hanif.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            if 'kursus_siswa' in source and 'df_ks_raw' in source:
                print(f"\n--- Cell {idx} ---")
                print(source)
            elif 'siswa_keluar' in source and 'detect_tag' in source:
                print(f"\n--- Cell {idx} ---")
                print(source)

if __name__ == '__main__':
    main()
