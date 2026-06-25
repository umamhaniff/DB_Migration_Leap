import pandas as pd
import os

def main():
    pkl_path = 'fase_4/mapping_id_jadwal.pkl'
    if os.path.exists(pkl_path):
        d = pd.read_pickle(pkl_path)
        print(f"Loaded schedule mapping: type {type(d)}, length {len(d)}")
        print("First 10 items:")
        for idx, (k, v) in enumerate(list(d.items())[:10]):
            print(f"  {repr(k)} -> {repr(v)}")
    else:
        print("Schedule mapping pickle not found!")

if __name__ == '__main__':
    main()
