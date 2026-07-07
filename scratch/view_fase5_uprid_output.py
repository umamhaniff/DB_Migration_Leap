import json

def main():
    path = "scratch/temp_insert_handler_fase5_uprid.ipynb"
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code' and 'outputs' in cell:
            for out in cell['outputs']:
                if 'text' in out:
                    text = "".join(out['text'])
                    if any(x in text for x in ['rapor_siswa', 'rapor_siswa_file', 'rapor_lacak', 'Gagal', 'SKIP', 'ERROR']):
                        print(f"--- Cell {idx} Output ---")
                        # print safely in ASCII
                        print(text.encode('ascii', errors='replace').decode('ascii'))

if __name__ == '__main__':
    main()
