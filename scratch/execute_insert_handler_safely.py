import os
import subprocess
import sys

def main():
    path = "fase_4/insert_handler.ipynb"
    # We output to scratch/temp_insert_handler.ipynb to avoid modifying the original file in Git
    out_path = "../scratch/temp_insert_handler.ipynb"
    print(f"Executing {path} safely. Output will be saved to scratch/temp_insert_handler.ipynb")
    
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
        print("[SUCCESS] insert_handler.ipynb executed safely! Data inserted cleanly.")
    except subprocess.CalledProcessError as e:
        print("[ERROR] Failed to execute insert_handler.ipynb:")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
