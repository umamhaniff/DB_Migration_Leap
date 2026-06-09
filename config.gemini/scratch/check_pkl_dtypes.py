import pickle
import pandas as pd

def check_pkl_dtypes(path):
    print(f"\n=== {path} ===")
    with open(path, "rb") as f:
        data = pickle.load(f)
    for tbl, df in data.items():
        print(f"Tabel: {tbl}")
        for col in df.columns:
            if 'id' in col or col.startswith('id_') or col.endswith('_id'):
                print(f"  - {col}: {df[col].dtype}")

check_pkl_dtypes("fase_3/fase_3_hanif.pkl")
check_pkl_dtypes("fase_4/fase_4_hanif.pkl")
check_pkl_dtypes("fase_5/fase_5_hanif.pkl")
