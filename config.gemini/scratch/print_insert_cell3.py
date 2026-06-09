import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("fase_3/insert_handler.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

cell = nb["cells"][3]
print("".join(cell["source"]))
