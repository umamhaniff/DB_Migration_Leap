import json
import os
import re

def main():
    path = "scratch/temp_insert_handler_fase3.ipynb"
    if not os.path.exists(path):
        print(f"File {path} does not exist.")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    print("=== Extracting Full Diagnostics of Fase 3 Tables ===")
    
    # Let's extract the stdout text from cell 7, 8, 9
    text_content = ""
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            outputs = cell.get("outputs", [])
            for out in outputs:
                if out.get("output_type") == "stream" and out.get("name") == "stdout":
                    text_val = out.get("text", "")
                    if isinstance(text_val, list):
                        text_val = "".join(text_val)
                    text_content += f"\n--- Cell {i} Output ---\n" + text_val
                    
    # Let's write the raw outputs to a log file for reference
    with open("scratch/fase3_run_outputs.log", "w", encoding="utf-8") as f_out:
        f_out.write(text_content)
    print("Raw output written to scratch/fase3_run_outputs.log")
    
    # Parse table status using regex
    # Successful lines look like: ✓ table_name: Sukses diproses! Sebanyak X baris sukses dimasukkan / di-skip aman.
    # Failed lines look like: ✗ table_name: Gagal total saat insert - Alasan: ...
    # Empty lines look like: ℹ️ table_name: DataFrame kosong (0 baris)
    
    success_matches = re.findall(r"✓\s+(\w+):\s+Sukses diproses!\s+Sebanyak\s+(\d+)\s+baris", text_content)
    failed_matches = re.findall(r"✗\s+(\w+):\s+Gagal total saat insert\s+-\s+Alasan:\s+(.+)", text_content)
    empty_matches = re.findall(r"ℹ️\s+(\w+):\s+DataFrame kosong", text_content)
    
    print("\n--- Summary parsed ---")
    print(f"Parsed Success: {len(success_matches)}")
    print(f"Parsed Failed: {len(failed_matches)}")
    print(f"Parsed Empty: {len(empty_matches)}")
    
    # Print detail of failures
    if failed_matches:
        print("\n--- Failed Tables Details ---")
        for tbl, reason in failed_matches:
            print(f"Table: {tbl}")
            print(f"Reason: {reason.strip()}")
            print("-" * 40)

if __name__ == '__main__':
    main()
