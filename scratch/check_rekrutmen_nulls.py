import pickle
import pandas as pd

with open("fase_3/fase_3_hanif.pkl", "rb") as f:
    data = pickle.load(f)

df = data.get("rekrutmen_pelamar")
if df is not None:
    nulls = df[df["id_pelamar"].isna()]
    print(f"Total nulls in id_pelamar: {len(nulls)}")
    print("Rows with null id_pelamar:")
    print(nulls.to_string())
else:
    print("Table rekrutmen_pelamar not found in pickle")
