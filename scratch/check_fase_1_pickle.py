import pickle

def main():
    path = "fase_1/fase_1_hanif.pkl"
    with open(path, "rb") as f:
        data = pickle.load(f)
    print("Keys in fase_1_hanif.pkl:")
    for k in data.keys():
        print(f"- {k}: {data[k].shape if hasattr(data[k], 'shape') else len(data[k])}")

if __name__ == '__main__':
    main()
