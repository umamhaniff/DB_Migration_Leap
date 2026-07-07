import json

def main():
    path = "fase_5/insert_handler_uprid.ipynb"
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    for idx, cell in enumerate(nb['cells']):
        source = "".join(cell['source'])
        if "master_urutan_insert" in source and "=" in source:
            print(f"--- Cell {idx} ---")
            lines = source.split("\n")
            for line in lines:
                ascii_line = line.encode('ascii', errors='replace').decode('ascii')
                print(ascii_line)

if __name__ == '__main__':
    main()
