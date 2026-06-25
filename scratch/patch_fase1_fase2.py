import json
import os

def patch_fase_1():
    nb_path = 'fase_1/script_hanif.ipynb'
    if not os.path.exists(nb_path):
        print(f"File {nb_path} not found.")
        return
        
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    updated = False
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
            
        source = cell['source']
        source_str = "".join(source)
        
        # 1. Patch hanif_tables_map
        if "hanif_tables_map = [" in source_str and "('role', 'roles')" in source_str:
            new_source = []
            for line in source:
                if "('role', 'roles')" in line:
                    continue
                new_source.append(line)
            cell['source'] = new_source
            updated = True
            print("Patched hanif_tables_map in Fase 1")
            
        # 2. Patch roles transformation
        if "# 1. roles" in source_str and "transformed_dfs['roles'] =" in source_str:
            # We want to replace the roles transformation block
            new_source = []
            skip = False
            for line in source:
                if "# 1. roles" in line:
                    skip = True
                    new_source.append("    # ponytail: roles table is not managed by Hanif anymore\n")
                    continue
                if skip:
                    if "transformed_dfs['roles'] =" in line:
                        skip = False
                    continue
                new_source.append(line)
            cell['source'] = new_source
            updated = True
            print("Patched roles transformation in Fase 1")
            
        # 3. Patch expected_counts
        if "expected_counts = {" in source_str and "'roles': 9" in source_str:
            new_source = []
            for line in source:
                if "'roles': 9" in line:
                    continue
                new_source.append(line)
            cell['source'] = new_source
            updated = True
            print("Patched expected_counts in Fase 1")
            
    if updated:
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print("Fase 1 notebook written.")
    else:
        print("No updates needed for Fase 1.")

def patch_fase_2():
    nb_path = 'fase_2/script_hanif.ipynb'
    if not os.path.exists(nb_path):
        print(f"File {nb_path} not found.")
        return
        
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    updated = False
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
            
        source = cell['source']
        source_str = "".join(source)
        
        # 1. Patch hanif_tables_map
        if "hanif_tables_map = [" in source_str and "('kelurahan', 'kelurahan')" in source_str:
            new_source = []
            for line in source:
                if "('kelurahan', 'kelurahan')" in line:
                    # check if the previous line has a trailing comma we need to handle, but since python list allows trailing comma, it's fine.
                    # Just skip the line.
                    continue
                new_source.append(line)
            cell['source'] = new_source
            updated = True
            print("Patched hanif_tables_map in Fase 2")
            
        # 2. Patch kelurahan transformation
        if "# 2. kelurahan (Source: kelurahan lama)" in source_str and "transformed_dfs['kelurahan'] =" in source_str:
            new_source = []
            skip = False
            for line in source:
                if "# 2. kelurahan (Source: kelurahan lama)" in line:
                    skip = True
                    new_source.append("    # ponytail: kelurahan table is not managed by Hanif anymore\n")
                    continue
                if skip:
                    if "transformed_dfs['kelurahan'] =" in line:
                        skip = False
                    continue
                new_source.append(line)
            cell['source'] = new_source
            updated = True
            print("Patched kelurahan transformation in Fase 2")
            
    if updated:
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print("Fase 2 notebook written.")
    else:
        print("No updates needed for Fase 2.")

if __name__ == '__main__':
    patch_fase_1()
    patch_fase_2()
