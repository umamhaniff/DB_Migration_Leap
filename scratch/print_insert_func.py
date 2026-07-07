import json
import sys

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass
        
    with open('fase_4/insert_handler.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    cell = nb['cells'][9]
    source = "".join(cell.get('source', []))
    print(source)

if __name__ == '__main__':
    main()
