import json
import sys

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass
        
    with open('fase_4/insert_handler.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    # Search for tables_to_insert_ordered lists and any code around them
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            if 'tables_to_insert_ordered' in source or 'mapping_siswa' in source or 'student_id_map' in source:
                print(f"\n--- Cell {idx} ---")
                print(source)

if __name__ == '__main__':
    main()
