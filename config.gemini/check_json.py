import json
import os

paths = ['fase_3/script_hanif.ipynb', 'fase_4/script_hanif.ipynb', 'fase_5/script_hanif.ipynb']

for p in paths:
    if os.path.exists(p):
        try:
            with open(p, 'r', encoding='utf-8') as f:
                json.load(f)
            print(f"✅ {p} is VALID JSON")
        except Exception as e:
            print(f"❌ {p} is INVALID JSON: {e}")
