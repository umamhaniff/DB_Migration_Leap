import pickle

def main():
    path = "fase_2/fase_2_hanif.pkl"
    try:
        with open(path, "rb") as f:
            data = pickle.load(f)
        print("Keys in fase_2_hanif.pkl:")
        for k in data.keys():
            df = data[k]
            print(f"- {k}: shape {df.shape if hasattr(df, 'shape') else len(df)}")
    except Exception as e:
        print(f"Error reading {path}: {e}")

if __name__ == '__main__':
    main()
