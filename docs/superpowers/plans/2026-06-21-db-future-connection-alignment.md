# Database Future Connection Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align the target database connection configuration in Hanif's scripts (Fase 1-5) to connect to `db_future` instead of `db_new` while keeping variable names intact.

**Architecture:** Programmatically load and update the connection code cell in each of the 5 notebooks (`script_hanif.ipynb` under `fase_1` through `fase_5`), replacing `config['db_new']` with `config['db_future']` in the database connection initialization. Run and verify each notebook to confirm it executes successfully and outputs the expected `.pkl` file.

**Tech Stack:** Python, Jupyter Notebooks (.ipynb), Pandas, mysql-connector-python

---

### Task 1: Create and Run Patching Script

**Files:**
- Create: `config.gemini/scratch/patch_db_future.py`

- [ ] **Step 1: Write the patching script**

Create the patch script to replace the connection configuration dynamically across all 5 notebooks:

```python
import json
import os

def patch_notebook(path):
    print(f"Reading {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    modified = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            src_str = ''.join(cell['source'])
            if "config['db_new']" in src_str or 'config["db_new"]' in src_str:
                print(f"Found connection cell in {path}. Patching...")
                new_source = []
                for line in cell['source']:
                    line_replaced = line.replace("config['db_new']", "config['db_future']").replace('config["db_new"]', 'config["db_future"]')
                    if 'Connected to new database' in line_replaced:
                        line_replaced = line_replaced.replace('Connected to new database', 'Connected to target database (db_future config)')
                    new_source.append(line_replaced)
                cell['source'] = new_source
                modified = True
                break
                
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"Successfully patched {path}.")
    else:
        print(f"No changes made to {path}.")

if __name__ == '__main__':
    notebooks = [
        'fase_1/script_hanif.ipynb',
        'fase_2/script_hanif.ipynb',
        'fase_3/script_hanif.ipynb',
        'fase_4/script_hanif.ipynb',
        'fase_5/script_hanif.ipynb'
    ]
    for nb_path in notebooks:
        if os.path.exists(nb_path):
            patch_notebook(nb_path)
        else:
            print(f"Warning: {nb_path} does not exist.")
```

- [ ] **Step 2: Run the patching script**

Run: `python config.gemini/scratch/patch_db_future.py`
Expected: Output showing successful patching for all 5 notebooks.

- [ ] **Step 3: Delete the scratch patching script**

Run: `Remove-Item config.gemini/scratch/patch_db_future.py`
Expected: File is deleted successfully.

- [ ] **Step 4: Commit the connection updates**

```bash
git add fase_1/script_hanif.ipynb fase_2/script_hanif.ipynb fase_3/script_hanif.ipynb fase_4/script_hanif.ipynb fase_5/script_hanif.ipynb
git commit -m "refactor: align target database connections to db_future in script_hanif notebooks"
```

---

### Task 2: Headless Execution and Verification (Fase 1-5)

**Files:**
- Modify: None (Execution verification only)

- [ ] **Step 1: Execute Fase 1 script**

Run: `venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_1/script_hanif.ipynb`
Expected: Notebook executes successfully without database connection errors.

- [ ] **Step 2: Execute Fase 2 script**

Run: `venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_2/script_hanif.ipynb`
Expected: Notebook executes successfully without database connection errors.

- [ ] **Step 3: Execute Fase 3 script**

Run: `venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_3/script_hanif.ipynb`
Expected: Notebook executes successfully without database connection errors.

- [ ] **Step 4: Execute Fase 4 script**

Run: `venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_4/script_hanif.ipynb`
Expected: Notebook executes successfully without database connection errors.

- [ ] **Step 5: Execute Fase 5 script**

Run: `venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_5/script_hanif.ipynb`
Expected: Notebook executes successfully without database connection errors.

- [ ] **Step 6: Verify all pickle files exist and have valid data**

Verify that:
- `fase_1/fase_1_hanif.pkl` exists.
- `fase_2/fase_2_hanif.pkl` exists.
- `fase_3/fase_3_hanif.pkl` exists.
- `fase_4/fase_4_hanif.pkl` exists.
- `fase_5/fase_5_hanif.pkl` exists.

- [ ] **Step 7: Commit any updated outputs (if any cell values/outputs changed during execution)**

```bash
git add fase_1/fase_1_hanif.pkl fase_2/fase_2_hanif.pkl fase_3/fase_3_hanif.pkl fase_4/fase_4_hanif.pkl fase_5/fase_5_hanif.pkl
git commit -m "chore: update executed notebooks and pickelled outputs"
```
