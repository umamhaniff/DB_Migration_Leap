import json
import os

def extract_code_from_notebook(notebook_path, output_py_path):
    if not os.path.exists(notebook_path):
        print(f"File not found: {notebook_path}")
        return
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        try:
            notebook = json.load(f)
        except Exception as e:
            print(f"Error reading {notebook_path}: {e}")
            return
            
    code_lines = []
    cell_count = 1
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, list):
                source_str = "".join(source)
            else:
                source_str = source
            
            code_lines.append(f"# ==========================================\n# CELL {cell_count}\n# ==========================================\n")
            # If this is the first cell, inject a fallback for the Jupyter 'display' function
            if cell_count == 1:
                code_lines.append("def display(*args, **kwargs):\n    for arg in args:\n        print(arg)\n\n")
            code_lines.append(source_str)
            code_lines.append("\n\n")
            cell_count += 1
            
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_py_path), exist_ok=True)
    with open(output_py_path, 'w', encoding='utf-8') as f:
        f.write("".join(code_lines))
    print(f"Extracted {notebook_path} to {output_py_path}")

if __name__ == '__main__':
    base_dir = r"D:\_CampusLife\ProjectCampus\6Magang\db_migration_leap"
    extract_code_from_notebook(os.path.join(base_dir, "fase_3", "script_hanif.ipynb"), os.path.join(base_dir, "scratch", "fase_3_hanif.py"))
    extract_code_from_notebook(os.path.join(base_dir, "fase_4", "script_hanif.ipynb"), os.path.join(base_dir, "scratch", "fase_4_hanif.py"))
    extract_code_from_notebook(os.path.join(base_dir, "fase_5", "script_hanif.ipynb"), os.path.join(base_dir, "scratch", "fase_5_hanif.py"))
