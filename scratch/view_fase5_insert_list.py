import json

def main():
    path = "fase_5/insert_handler.ipynb"
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    # search for the list
    for idx, cell in enumerate(nb['cells']):
        source = "".join(cell['source'])
        if "rapor_siswa" in source:
            print(f"--- Cell {idx} containing 'rapor_siswa' ---")
            print(source)

if __name__ == '__main__':
    main()
