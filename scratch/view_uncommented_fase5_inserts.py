import json
import sys

def main():
    path = "fase_5/insert_handler_uprid.ipynb"
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    for idx, cell in enumerate(nb['cells']):
        source = "".join(cell['source'])
        # check if it defines tables list
        if "tables_to_insert_ordered" in source:
            print(f"\n==================== CELL {idx} ====================")
            # print lines that are not commented
            lines = source.split("\n")
            for line in lines:
                if "'" in line or '"' in line:
                    cleaned = line.strip()
                    is_comment = cleaned.startswith("#")
                    status = "[COMMENTED]" if is_comment else "[ACTIVE]"
                    # safely print ASCII representation
                    ascii_line = line.encode('ascii', errors='replace').decode('ascii')
                    print(f"  {status:<12}: {ascii_line}")

if __name__ == '__main__':
    main()
