import json

def main():
    path = "fase_5/insert_handler_uprid.ipynb"
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    # Let's search for line containing ordered_list
    for idx, cell in enumerate(nb['cells']):
        source = "".join(cell['source'])
        if "ordered_list" in source or "insert_data" in source:
            print(f"--- Cell {idx} ---")
            # print only lines containing inserts or list setup, safely
            lines = source.split("\n")
            for line in lines:
                if any(x in line for x in ['insert', 'table', 'list', 'ordered', 'data']):
                    ascii_line = line.encode('ascii', errors='replace').decode('ascii')
                    print(ascii_line)

if __name__ == '__main__':
    main()
