import os
import subprocess
import sys

def main():
    path = "fase_5/insert_handler_uprid.ipynb"
    out_path = "../scratch/temp_insert_handler_fase5_uprid.ipynb"
    print(f"Executing {path} safely. Output will be saved to scratch/temp_insert_handler_fase5_uprid.ipynb")
    
    cmd = [
        sys.executable, "-m", "nbconvert",
        "--to", "notebook",
        "--execute",
        path,
        "--output",
        out_path
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("[SUCCESS] fase_5/insert_handler_uprid.ipynb executed safely! Data inserted cleanly.")
    except subprocess.CalledProcessError as e:
        print("[ERROR] Failed to execute fase_5/insert_handler_uprid.ipynb:")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
