import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("fase_3/script_hanif.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

for idx, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if "pelamar" in source or "pekerjaan" in source:
            print(f"Cell {idx} (len={len(source)}):")
            print(source[:200])
            print("-" * 50)
