import json
import os

path = 'fase_4/script_hanif.ipynb'
if not os.path.exists(path):
    print("Not found")
    exit(1)

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'def extract_int(s):' in ''.join(cell['source']):
        source = ''.join(cell['source'])
        
        # Fix extract_int
        source = source.replace("nums = re.findall(r'\\\\d+', str(s))", "nums = re.findall(r'\\\\d+', str(s))")
        # Wait, inside python script it's tricky. Let's just use regular strings without r.
        # Original: nums = re.findall(r'\\\\d+', str(s))
        
        # Let's replace the whole functions.
        old_funcs = """def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\\\\d+', str(s))
    return int(nums[0]) if nums else None

def extract_chars(s):
    if pd.isna(s) or not str(s).strip(): return None
    return re.sub(r'\\\\d+', '', str(s)).strip()"""

        new_funcs = """def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\\d+', str(s))
    return int(nums[0]) if nums else None

def extract_chars(s):
    if pd.isna(s) or not str(s).strip(): return None
    return re.sub(r'\\d+', '', str(s)).strip()"""

        if old_funcs in source:
            source = source.replace(old_funcs, new_funcs)
            cell['source'] = [line + '\n' for line in source.split('\n')]
            if cell['source'][-1] == '\n': cell['source'].pop()

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Regex patched")
