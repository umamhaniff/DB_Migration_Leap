import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd

data = pd.read_pickle("fase_3/fase_3_hanif.pkl")
df_pk = data.get("pengajuan_karyawan")
if df_pk is not None:
    print("--- Pickle pengajuan_karyawan (first 10 rows) ---")
    print(df_pk.head(10))
else:
    print("pengajuan_karyawan not found in pickle!")
