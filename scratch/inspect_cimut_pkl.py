import pickle
import pandas as pd

def main():
    with open('fase_4/fase_4_cimut.pkl', 'rb') as f:
        cimut_data = pickle.load(f)
        
    if 'kursus_siswa' in cimut_data:
        df_ks = cimut_data['kursus_siswa']
        print("fase_4_cimut.pkl 'kursus_siswa' Shape:", df_ks.shape)
        print("fase_4_cimut.pkl 'kursus_siswa' Columns:", list(df_ks.columns))
        print("First 10 rows:")
        print(df_ks.head(10))

if __name__ == '__main__':
    main()
