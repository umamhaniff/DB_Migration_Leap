import os
import pandas as pd

csv_dir = 'extract/cek_csv'
print("=== CSV Row Counts ===")
for f in sorted(os.listdir(csv_dir)):
    if f.endswith('.csv'):
        path = os.path.join(csv_dir, f)
        try:
            df = pd.read_csv(path)
            print(f"{f}: {df.shape[0]} rows, {df.shape[1]} columns")
        except Exception as e:
            print(f"{f}: Error reading - {e}")
