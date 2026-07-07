import pickle

def main():
    path = "fase_5/fase_5_hanif.pkl"
    with open(path, "rb") as f:
        data = pickle.load(f)
    print("Keys in fase_5_hanif.pkl:")
    for k in data.keys():
        df = data[k]
        print(f"- {k}: shape {df.shape if hasattr(df, 'shape') else len(df)}")
        if hasattr(df, 'head') and not df.empty:
            print("  Cols:", list(df.columns))
            print("  First row id_siswa:", df.iloc[0].get('id_siswa'))

if __name__ == '__main__':
    main()
