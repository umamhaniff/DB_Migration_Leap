import pandas as pd

# Load Fase 4 data from pickle
data = pd.read_pickle("fase_4/fase_4_hanif.pkl")
df_mitra = data.get("mitra")
df_mp = data.get("mitra_progres")

print("--- Mitra id_mitra values ---")
print(df_mitra["id_mitra"].unique())

print("\n--- Mitra Progres id_mitra values ---")
print(df_mp["id_mitra"].unique())

# Check if there are any id_mitra in mitra_progres that are not in mitra
mismatches = df_mp[~df_mp["id_mitra"].isin(df_mitra["id_mitra"])]["id_mitra"].dropna().unique()
print("\n--- id_mitra in mitra_progres NOT present in mitra ---")
print(mismatches)
