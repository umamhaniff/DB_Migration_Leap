import json
import os

paths = ['fase_3/script_hanif.ipynb', 'fase_4/script_hanif.ipynb', 'fase_5/script_hanif.ipynb']

for p in paths:
    if os.path.exists(p):
        try:
            with open(p, 'r', encoding='utf-8') as f:
                nb = json.load(f)
            
            # Write back with ensure_ascii=False to write raw UTF-8 characters instead of \uXXXX escapes
            with open(p, 'w', encoding='utf-8') as f:
                json.dump(nb, f, ensure_ascii=False, indent=1)
                
            print(f"✅ Re-saved {p} with ensure_ascii=False")
        except Exception as e:
            print(f"❌ Error fixing {p}: {e}")
