import os
import subprocess
import sys

def run_notebook(path):
    print(f"\n==================== RUNNING {path} ====================")
    cmd = [
        sys.executable, "-m", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",
        path
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"[OK] Successfully executed {path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error executing {path}:")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        return False

def main():
    notebooks = [
        "fase_1/script_hanif.ipynb",
        "fase_2/script_hanif.ipynb",
        "fase_3/script_hanif.ipynb",
        "fase_4/script_hanif.ipynb",
        "fase_5/script_hanif.ipynb"
    ]
    
    success = True
    for nb in notebooks:
        if os.path.exists(nb):
            if not run_notebook(nb):
                success = False
                break
        else:
            print(f"[WARN] Notebook not found: {nb}")
            
    if success:
        print("\n[SUCCESS] All notebooks executed successfully!")
    else:
        print("\n[FAILED] Execution failed on one of the notebooks.")

if __name__ == '__main__':
    main()
