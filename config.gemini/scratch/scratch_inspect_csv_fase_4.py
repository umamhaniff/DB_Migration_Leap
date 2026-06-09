import pandas as pd

df_siswa = pd.read_csv("extract/cek_csv/siswa.csv")
df_mitra_progres = pd.read_csv("extract/cek_csv/mitra_progres.csv")

print("=== columns of siswa.csv ===")
print(df_siswa[['id_siswa', 'id_provinsi', 'id_kabupaten', 'id_kecamatan', 'id_kelurahan', 'id_mitra']].dropna(subset=['id_provinsi']).head(5))

print("\n=== columns of mitra_progres.csv ===")
print(df_mitra_progres[['id_progres_mitra', 'id_mitra', 'status_progres_mitra']].head(5))
