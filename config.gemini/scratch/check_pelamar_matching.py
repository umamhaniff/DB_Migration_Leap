import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = "fase_4/script_hanif.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for idx, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if "mitra_progres" in source:
            print(f"Cell {idx}:")
            print(source)
            print("================================")
