import os
import pandas as pd

for person in ['cimut', 'afrida', 'hanif']:
    path = f"fase_4/fase_4_{person}.pkl"
    if os.path.exists(path):
        print(f"\n--- {path.upper()} ---")
        try:
            data = pd.read_pickle(path)
            if isinstance(data, dict):
                print("Keys:")
                for k, df in data.items():
                    if isinstance(df, pd.DataFrame):
                        print(f"  - {k}: {df.shape[0]} rows x {df.shape[1]} columns")
                    else:
                        print(f"  - {k}: type={type(df)}")
            else:
                print(f"Data is not a dict, type={type(data)}")
        except Exception as e:
            print(f"Error loading {path}: {e}")
    else:
        print(f"File {path} does not exist.")
