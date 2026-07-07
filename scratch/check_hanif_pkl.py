import pickle
import pandas as pd

def main():
    with open('fase_4/fase_4_hanif.pkl', 'rb') as f:
        data = pickle.load(f)
        
    print("Keys in phase 4 pickle:", data.keys())
    
    for key in ['siswa', 'kursus_siswa', 'siswa_keluar', 'mitra']:
        if key in data:
            df = data[key]
            print(f"\nTable: {key} | Shape: {df.shape}")
            print("Columns:", list(df.columns))
            print(df.head(2))

if __name__ == '__main__':
    main()
