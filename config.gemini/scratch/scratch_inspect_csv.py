import pandas as pd

df_pelamar = pd.read_csv("extract/cek_csv/pelamar.csv")
df_pengajuan = pd.read_csv("extract/cek_csv/pengajuan_karyawan.csv")

print("=== columns of pelamar.csv ===")
print(df_pelamar.dtypes)
print(df_pelamar[['id_pelamar', 'id_pengajuan', 'nama_lengkap']].dropna(subset=['id_pengajuan']).head(10))

print("\n=== columns of pengajuan_karyawan.csv ===")
print(df_pengajuan.dtypes)
print(df_pengajuan[['id_pengajuan', 'id_user', 'posisi']].head(10))
