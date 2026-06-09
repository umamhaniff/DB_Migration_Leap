import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("fase_3/script_hanif.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

cell = nb["cells"][7]
print("Cell 7 length:", len("".join(cell["source"])))
print("First 500 chars:")
print("".join(cell["source"])[:500])
print("\nLast 500 chars:")
print("".join(cell["source"])[-500:])
