import pickle
import pandas as pd

with open("fase_5/fase_5_hanif.pkl", "rb") as f:
    data = pickle.load(f)

df = data.get("rapor_siswa")
if df is not None:
    # Check for placeholder garbage
    garbage_keywords = ['comment', 'coba', 'test', 'dummy']
    garbage_rows = df[df['final_result'].str.lower().str.contains('|'.join(garbage_keywords), na=False)]
    print(f"Total garbage comments: {len(garbage_rows)}")
    print(garbage_rows[['id_siswa', 'id_jadwal', 'final_result']])
else:
    print("Table rapor_siswa not found in pickle")
