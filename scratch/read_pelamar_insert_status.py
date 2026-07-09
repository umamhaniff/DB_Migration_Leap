import json
import os

def main():
    path = "scratch/temp_insert_handler_fase3.ipynb"
    if not os.path.exists(path):
        print(f"File {path} does not exist.")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            outputs = cell.get("outputs", [])
            for out in outputs:
                if out.get("output_type") == "stream" and out.get("name") == "stdout":
                    text_val = out.get("text", "")
                    if isinstance(text_val, list):
                        text_val = "".join(text_val)
                    # Filter lines mentioning pelamar or showing execution summary
                    lines = text_val.split("\n")
                    printed = False
                    for line in lines:
                        if any(x in line.lower() for x in ["pelamar", "warning", "error", "skip", "sukses", "preview", "diagnostik"]):
                            if not printed:
                                print(f"--- Cell {i} ---")
                                printed = True
                            print(line)

if __name__ == '__main__':
    main()
