import os
import pandas as pd

pkl_path = "fase_4/fase_4_hanif.pkl"
if not os.path.exists(pkl_path):
    print(f"File {pkl_path} not found.")
    exit(1)

print(f"--- INSPECTING PICKLE FILE: {pkl_path} ---")
data = pd.read_pickle(pkl_path)

print("Keys in pickle:")
for k in data.keys():
    df = data[k]
    if isinstance(df, pd.DataFrame):
        print(f"  - {k}: {df.shape[0]} rows x {df.shape[1]} columns")
    else:
        print(f"  - {k}: not a DataFrame (type={type(df)})")

if 'siswa' in data:
    df_s = data['siswa']
    print(f"\nTotal rows in siswa DataFrame: {len(df_s)}")
    
    # Check duplicates on nomor_induk
    df_s['ni_clean'] = df_s['nomor_induk'].astype(str).str.strip()
    duplicates = df_s[df_s.duplicated(subset=['ni_clean'], keep=False)]
    print(f"Duplicate nomor_induk in pickle's siswa: {len(duplicates)}")
    if len(duplicates) > 0:
        print("First 20 duplicate rows:")
        print(duplicates[['nama_lengkap', 'nomor_induk', 'ni_clean']].sort_values(by='ni_clean').head(20))
        
    # Check specific duplicates from warning
    print("\nSpecific checks in pickle's siswa:")
    for specific in ['20220000080', '20220000293', 'TEMP-S0000009']:
        matches = df_s[df_s['nomor_induk'].astype(str).str.contains(specific, na=False)]
        print(f"Matches for '{specific}':")
        print(matches[['nama_lengkap', 'nomor_induk']])

if 'mitra' in data:
    df_m = data['mitra']
    print(f"\nTotal rows in mitra DataFrame: {len(df_m)}")
    print("generated_kode in pickle's mitra:")
    print(df_m[['nama_mitra', 'kode_mitra']])
    
    duplicates_mitra = df_m[df_m.duplicated(subset=['kode_mitra'], keep=False)]
    print(f"Duplicate kode_mitra in pickle's mitra: {len(duplicates_mitra)}")
    if len(duplicates_mitra) > 0:
         print(duplicates_mitra[['nama_mitra', 'kode_mitra']])
