import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd

data = pd.read_pickle("fase_4/fase_4_hanif.pkl")
df_s = data.get("siswa")
if df_s is not None:
    print("--- Pickle siswa columns and types ---")
    print(df_s[['id_siswa', 'id_provinsi', 'id_kabupaten', 'id_kecamatan', 'id_kelurahan', 'id_mitra']].head(10))
    print("\nDtypes in pickle:")
    print(df_s[['id_siswa', 'id_provinsi', 'id_kabupaten', 'id_kecamatan', 'id_kelurahan', 'id_mitra']].dtypes)
else:
    print("siswa not found in pickle!")
