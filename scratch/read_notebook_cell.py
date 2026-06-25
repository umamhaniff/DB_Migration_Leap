import json

def main():
    path = 'fase_5/script_hanif.ipynb'
    nb = json.load(open(path, 'r', encoding='utf-8'))
    
    print("=== READING NOTEBOOK CELLS IN SCRIPT_HANIF.IPYNB ===")
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            if "# 1. format_rapor -> rapor_format" in source:
                print(f"\nCell {idx} contains '# 1. format_rapor -> rapor_format':")
                print("----------------------------------------")
                print(source)
                print("----------------------------------------")
                
            if "# 7. rapor -> rapor_siswa" in source:
                print(f"\nCell {idx} contains '# 7. rapor -> rapor_siswa':")
                print("----------------------------------------")
                # print first 30 lines
                lines = source.split('\n')
                print('\n'.join(lines[:30]))
                print("...")
                print("----------------------------------------")

if __name__ == '__main__':
    main()
