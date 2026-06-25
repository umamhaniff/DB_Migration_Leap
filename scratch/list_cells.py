import json

def main():
    path = 'fase_5/script_hanif.ipynb'
    nb = json.load(open(path, 'r', encoding='utf-8'))
    
    print("=== LISTING ALL CODE CELLS ===")
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell['source']).strip()
            first_line = source.split('\n')[0] if source else "EMPTY"
            print(f"Cell {idx:2d} | Length: {len(source):5d} chars | First line: {first_line}")

if __name__ == '__main__':
    main()
