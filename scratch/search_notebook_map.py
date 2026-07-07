import json
import sys

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass
        
    with open('fase_4/insert_handler.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            if 'map' in source.lower():
                lines = source.split('\n')
                non_comment_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
                if any('map' in l.lower() for l in non_comment_lines):
                    print(f"\n--- Cell {idx} ---")
                    print("\n".join(non_comment_lines[:15]))
                    if len(non_comment_lines) > 15:
                        print("...")

if __name__ == '__main__':
    main()
