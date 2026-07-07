import pickle
import os

def check_pkl(filename):
    path = os.path.join('fase_4', filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        print(f"\nPickle: {filename}")
        print("Keys:", list(data.keys()))
        for k, v in data.items():
            if hasattr(v, 'shape'):
                print(f"  {k}: DataFrame shape {v.shape}")
            else:
                print(f"  {k}: {type(v)}")
    else:
        print(f"\n{filename} does not exist.")

def main():
    check_pkl('fase_4_cimut.pkl')
    check_pkl('fase_4_afrida.pkl')
    check_pkl('fase_4_hanif.pkl')

if __name__ == '__main__':
    main()
