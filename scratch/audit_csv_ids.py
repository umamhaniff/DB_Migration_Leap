import os
import pandas as pd
import glob
import re
import sys

# Ensure UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

csv_files = glob.glob("conductor/cek_csv/*.csv")
print(f"Auditing {len(csv_files)} CSV files in conductor/cek_csv...")

failures = 0
for file_path in csv_files:
    filename = os.path.basename(file_path)
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"[ERROR] {filename}: Error reading file: {e}")
        continue
    
    # Identify columns that are likely IDs or FKs
    id_cols = [col for col in df.columns if col.startswith('id_') or col.endswith('_id') or col == 'id' or 'id_' in col or '_id_' in col]
    
    print(f"\nFILE: {filename}")
    print(f"  Total rows: {len(df)}")
    print(f"  ID/FK columns found: {id_cols}")
    
    for col in id_cols:
        non_null = df[col].dropna()
        if non_null.empty:
            print(f"    - {col}: all nulls/empty (OK)")
            continue
        
        # Check values
        str_vals = non_null.astype(str)
        has_decimal = str_vals.str.contains(r'\.0$', regex=True).any()
        is_all_digits = str_vals.str.contains(r'^\d+(\.0)?$', regex=True).all()
        
        if has_decimal:
            print(f"    - [FAIL] {col}: Has decimal formatting (e.g., {str_vals.iloc[0]})")
            failures += 1
        else:
            print(f"    - [OK] {col}: Pure integer representation")

print(f"\nAudit complete. Total formatting failures: {failures}")
