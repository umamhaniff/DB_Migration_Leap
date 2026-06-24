import os
import pandas as pd

# 1. Clean fase_3_cimut.pkl
f3_path = "fase_3/fase_3_cimut.pkl"
if os.path.exists(f3_path):
    print(f"--- CLEANING {f3_path} ---")
    data = pd.read_pickle(f3_path)
    print(f"Original keys ({len(data)}): {list(data.keys())}")
    
    # We keep only CRM tables for Cimut in Fase 3
    keep_prefixes = ['calon_siswa', 'kontak_prospek', 'mapping_id_']
    new_data = {}
    for k, v in data.items():
        # Keep only if it starts with one of our prefixes
        if any(k.startswith(p) for p in keep_prefixes):
            new_data[k] = v
            
    print(f"Cleaned keys ({len(new_data)}): {list(new_data.keys())}")
    pd.to_pickle(new_data, f3_path)
    print("Saved successfully!")
else:
    print(f"{f3_path} not found.")

# 2. Clean fase_4_cimut.pkl
f4_path = "fase_4/fase_4_cimut.pkl"
if os.path.exists(f4_path):
    print(f"\n--- CLEANING {f4_path} ---")
    data = pd.read_pickle(f4_path)
    print(f"Original keys ({len(data)}): {list(data.keys())}")
    
    # We keep only Perizinan & Kepegawaian tables for Cimut in Fase 4
    keep_keys = [
        'izin_karyawan', 
        'verifikasi_izin', 
        'absensi', 
        'verifikasi_absensi', 
        'karyawan_resign', 
        'mapping_id_izin'
    ]
    new_data = {}
    for k, v in data.items():
        if k in keep_keys:
            new_data[k] = v
            
    print(f"Cleaned keys ({len(new_data)}): {list(new_data.keys())}")
    pd.to_pickle(new_data, f4_path)
    print("Saved successfully!")
else:
    print(f"{f4_path} not found.")
