import os
import pandas as pd

if os.path.exists("fase_3/fase_3_afrida.pkl"):
    data_a = pd.read_pickle("fase_3/fase_3_afrida.pkl")
    print("Keys in fase_3_afrida.pkl:", list(data_a.keys()))
else:
    print("fase_3_afrida.pkl does not exist in fase_3/")
