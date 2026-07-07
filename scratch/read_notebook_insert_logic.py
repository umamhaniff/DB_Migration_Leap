import json
import sys

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass
        
    with open('fase_4/insert_handler.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    print("Notebook has", len(nb['cells']), "cells.")
    
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            if 'cursor' in source and 'insert' in source.lower():
                lines = source.split('\n')
                non_comment_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
                if non_comment_lines:
                    print(f"\n--- Cell {idx} (execution_count: {cell.get('execution_count')}) ---")
                    print("\n".join(non_comment_lines[:20]))
                    if len(non_comment_lines) > 20:
                        print("...")

if __name__ == '__main__':
    main()
