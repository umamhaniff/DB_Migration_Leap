import os
import glob
import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

csv_files = glob.glob("conductor/cek_csv/*.csv")
print(f"Auditing {len(csv_files)} CSV files in conductor/cek_csv (RAW TEXT MODE)...")

failures = 0
for file_path in csv_files:
    filename = os.path.basename(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            continue
            
        # Identify columns that are likely IDs or FKs
        id_indices = []
        id_names = []
        for idx, h in enumerate(headers):
            h_lower = h.lower()
            if h_lower.startswith('id_') or h_lower.endswith('_id') or h_lower == 'id' or 'id_' in h_lower or '_id_' in h_lower:
                id_indices.append(idx)
                id_names.append(h)
                
        if not id_indices:
            continue
            
        print(f"\nFILE: {filename}")
        print(f"  ID/FK columns: {id_names}")
        
        # Track if any ID column has a decimal format in the file
        decimal_cols = {idx: False for idx in id_indices}
        sample_vals = {idx: None for idx in id_indices}
        
        row_count = 0
        for row in reader:
            row_count += 1
            for idx in id_indices:
                if idx < len(row):
                    val = row[idx].strip()
                    if val:
                        # Check if matches digits followed by .0 or decimal point
                        if '.' in val:
                            parts = val.split('.')
                            if len(parts) == 2 and parts[1] == '0':
                                decimal_cols[idx] = True
                                sample_vals[idx] = val
                            elif len(parts) == 2 and parts[1] == '':
                                decimal_cols[idx] = True
                                sample_vals[idx] = val
        
        for idx, name in zip(id_indices, id_names):
            if decimal_cols[idx]:
                print(f"    - [FAIL] {name}: Has physical decimal format (e.g., '{sample_vals[idx]}')")
                failures += 1
            else:
                print(f"    - [OK] {name}: Pure integer / clean in raw CSV")

print(f"\nAudit complete. Total physical formatting failures: {failures}")
