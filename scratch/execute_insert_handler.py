import os
import subprocess
import sys

def main():
    path = "fase_4/insert_handler.ipynb"
    print(f"Executing {path} to run the migration insertions...")
    cmd = [
        sys.executable, "-m", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",
        path
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("[SUCCESS] insert_handler.ipynb executed successfully! Data inserted cleanly.")
    except subprocess.CalledProcessError as e:
        print("[ERROR] Failed to execute insert_handler.ipynb:")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
