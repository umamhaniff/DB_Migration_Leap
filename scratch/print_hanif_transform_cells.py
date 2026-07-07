import json
import sys

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass
        
    with open('fase_4/script_hanif.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    # Find cell that has transform logic
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            if '# Build kursus_siswa dynamically' in source or 'siswa_keluar' in source:
                print(f"\n--- Cell {idx} ---")
                print(source)

if __name__ == '__main__':
    main()
