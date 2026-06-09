import json
import glob
import sys

# Ensure UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob("fase_1/*.ipynb")
for path in files:
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    for i, cell in enumerate(nb["cells"]):
        cell_str = json.dumps(cell)
        if "parameter_nilai" in cell_str:
            print(f"=== {path} Cell {i} ({cell['cell_type']}) ===")
            source = "".join(cell.get("source", []))
            print("SOURCE:")
            print(source[:500])
            print("OUTPUTS:")
            for out in cell.get("outputs", []):
                text = "".join(out.get("text", []))
                if "parameter_nilai" in text:
                    print(text[:500])
            print("-" * 60)
