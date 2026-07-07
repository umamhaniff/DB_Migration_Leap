import json

def main():
    path = "fase_5/insert_handler.ipynb"
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    for idx, cell in enumerate(nb['cells']):
        source = "".join(cell['source'])
        if "tables_to_insert_ordered" in source or "insert_data" in source:
            print(f"\n==================== CELL {idx} ====================")
            print(source[:2000])

if __name__ == '__main__':
    main()
