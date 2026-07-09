import os
import subprocess
import sys
import mysql.connector

# Add parent dir to sys.path to load config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    
    print("Connecting to DB to disable global foreign key checks...")
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    cursor.execute("SET GLOBAL foreign_key_checks = 0;")
    conn.commit()
    conn.close()
    print("Global foreign key checks disabled successfully.")
    
    path = "fase_3/insert_handler.ipynb"
    out_path = "../scratch/temp_insert_handler_fase3.ipynb"
    print(f"Executing {path} safely using virtual env's python. Output will be saved to scratch/temp_insert_handler_fase3.ipynb")
    
    # Use the virtual environment's python to ensure same package versions
    venv_python = os.path.join("..", "venv", "Scripts", "python.exe")
    if not os.path.exists(venv_python):
        venv_python = os.path.join("venv", "Scripts", "python.exe")
        
    cmd = [
        venv_python, "-m", "nbconvert",
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
    finally:
        print("Connecting to DB to restore global foreign key checks...")
        conn = mysql.connector.connect(**cfg['db_new'])
        cursor = conn.cursor()
        cursor.execute("SET GLOBAL foreign_key_checks = 1;")
        conn.commit()
        conn.close()
        print("Global foreign key checks restored successfully.")

if __name__ == '__main__':
    main()
