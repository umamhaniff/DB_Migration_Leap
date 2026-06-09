import pandas as pd

data = pd.read_pickle("fase_4/fase_4_hanif.pkl")
df_sk = data.get("siswa_keluar")

print("--- Row at index 1 in pickle ---")
print(df_sk.iloc[1])

print("\n--- Row at index 1 type and dictionary format ---")
print(df_sk.iloc[1].to_dict())
