import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("fase_3/insert_handler.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

for idx, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if "pelamar" in source.lower():
            print(f"Cell {idx}:")
            print(source[:500])
            print("-" * 50)
