import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd

# Load Fase 4 data from pickle
data = pd.read_pickle("fase_4/fase_4_hanif.pkl")
df_sk = data.get("siswa_keluar")
df_ks = data.get("kursus_siswa")

print("--- Stats ---")
print(f"Total rows in siswa_keluar: {len(df_sk)}")
print(f"Total rows in kursus_siswa: {len(df_ks)}")

# Count how many siswa_keluar rows have non-null id_kursus
mapped_count = df_sk['id_kursus'].notna().sum()
print(f"Mapped id_kursus count: {mapped_count} out of {len(df_sk)}")

# Print a few mapped rows
print("\n--- Mapped rows in siswa_keluar (first 5) ---")
print(df_sk[df_sk['id_kursus'].notna()].head(5))

# Print a few unmapped rows
print("\n--- Unmapped rows in siswa_keluar (first 5) ---")
print(df_sk[df_sk['id_kursus'].isna()].head(5))
