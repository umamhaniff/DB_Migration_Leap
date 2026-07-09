import pickle
import os
import pandas as pd

def inspect_pkl(path):
    print(f"\n=== Inspecting {path} ===")
    if not os.path.exists(path):
        print("Does not exist!")
        return
    with open(path, 'rb') as f:
        data = pickle.load(f)
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, pd.DataFrame):
                print(f"Key: {k}, DataFrame shape: {v.shape}")
            else:
                print(f"Key: {k}, Type: {type(v)}")
    else:
        print(f"Root Type: {type(data)}")

def main():
    inspect_pkl("fase_3/fase_3_cimut.pkl")
    inspect_pkl("fase_3/fase_3_afrida.pkl")
    inspect_pkl("fase_3/fase_3_hanif.pkl")

if __name__ == '__main__':
    main()
