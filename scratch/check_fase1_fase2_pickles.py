import pickle
import pandas as pd

def check_pickle(file_path):
    print(f"\n=== Checking {file_path} ===")
    try:
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        print(f"Type: {type(data)}")
        if isinstance(data, dict):
            print(f"Keys: {list(data.keys())}")
            for k, v in data.items():
                if isinstance(v, pd.DataFrame):
                    print(f"  - Key '{k}': DataFrame shape={v.shape}, columns={list(v.columns)}")
                else:
                    print(f"  - Key '{k}': {type(v)}")
        else:
            print(f"Data: {data}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

check_pickle('fase_1/fase_1_hanif.pkl')
check_pickle('fase_2/fase_2_hanif.pkl')
