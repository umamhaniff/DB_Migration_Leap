import nbformat
import os

paths = ['fase_3/script_hanif.ipynb', 'fase_4/script_hanif.ipynb', 'fase_5/script_hanif.ipynb']

for p in paths:
    if os.path.exists(p):
        try:
            with open(p, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            print(f"✅ {p} is VALID NOTEBOOK FORMAT")
        except Exception as e:
            print(f"❌ {p} is INVALID NOTEBOOK FORMAT: {e}")
