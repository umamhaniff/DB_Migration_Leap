import json
import os

def main():
    path = "scratch/temp_insert_handler_fase3.ipynb"
    if not os.path.exists(path):
        print(f"File {path} does not exist.")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    print(f"Checking cells in {path} for errors...")
    error_found = False
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            outputs = cell.get("outputs", [])
            for out in outputs:
                if out.get("output_type") == "error":
                    print(f"\n[CELL {i}] raised an error:")
                    print("Ename:", out.get("ename"))
                    print("Evalue:", out.get("evalue"))
                    print("Traceback:")
                    print("\n".join(out.get("traceback", [])))
                    error_found = True
                elif out.get("output_type") == "stream" and out.get("name") == "stderr":
                    print(f"\n[CELL {i}] stderr output:")
                    print(out.get("text"))
                    error_found = True
                    
    if not error_found:
        print("No cell errors found in the notebook!")

if __name__ == '__main__':
    main()
