import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = "fase_2/insert_handler.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for i, cell in enumerate(nb["cells"]):
    source = "".join(cell.get("source", []))
    if "parameter_nilai" in source:
        print(f"=== Cell {i} ===")
        print(source[:2000])
        print("-" * 60)
