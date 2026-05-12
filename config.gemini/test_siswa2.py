import mysql.connector, os, pandas as pd, re
from dotenv import load_dotenv
load_dotenv()

def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\d+', str(s))
    return int(nums[0]) if nums else None

c = mysql.connector.connect(host=os.getenv('DB_HOST'), port=int(os.getenv('DB_PORT')), user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), database=os.getenv('DB_OLD'), collation='utf8mb4_general_ci')
cur = c.cursor(dictionary=True)
cur.execute('SELECT * FROM siswa')
df = pd.DataFrame(cur.fetchall())
c.close()

print('Initial idmitra (DB_OLD) non-empty:', (df['idmitra'] != '').sum())
df['idmitra_int'] = df['idmitra'].apply(extract_int)
print('After extract_int:', df['idmitra_int'].notna().sum())

mapping = {
    'idsiswa': 'id_siswa', 'tgl_daftar': 'tanggal_registrasi', 'domisili': 'domisili',
    'nama_lengkap': 'nama_lengkap', 'panggilan': 'nama_panggilan', 'jkel': 'jenis_kelamin',
    'nama_sekolah': 'asal_sekolah', 'level_sekolah': 'tingkat_sekolah', 'nama_ortu': 'nama_orang_tua',
    'pekerjaan_ortu': 'pekerjaan_orang_tua', 'tmp_lahir': 'tempat_lahir', 'tgl_lahir': 'tanggal_lahir',
    'no_induk': 'nomor_induk', 'email': 'email', 'idcalon': 'id_calon',
    'provinsi': 'id_provinsi', 'kabupaten': 'id_kabupaten', 'kecamatan': 'id_kecamatan',
    'kelurahan': 'id_kelurahan', 'idmitra_int': 'id_mitra', 'nisn': 'nisn', 'nik': 'nik',
    'kewarganegaraan': 'kewarganegaraan', 'agama': 'agama', 'rt': 'rt', 'rw': 'rw',
    'kodepos': 'kode_pos', 'statussiswa': 'status_aktif', 'rekomen': 'rekomendasi',
    'info': 'sumber_info', 'pembayaran': 'metode_pembayaran', 'nama_ayah': 'nama_ayah',
    'pekerjaan_ayah': 'pekerjaan_ayah', 'jenjang_ayah': 'pendidikan_ayah',        
    'penghasilan_ayah': 'penghasilan_ayah', 'nama_ibu': 'nama_ibu', 'penghasilan_ibu': 'penghasilan_ibu',
    'jenjang_ibu': 'pendidikan_ibu', 'nama_wali': 'nama_wali', 'pekerjaan_wali': 'pekerjaan_wali',
    'jenjang_wali': 'pendidikan_wali', 'penghasilan_wali': 'penghasilan_wali',    
    'wapeserta': 'wa_siswa', 'wawalmur': 'wa_ortu', 'waadmin': 'wa_administrasi', 
    'sts_pengisian': 'status_pengisian', 'bukti': 'path_bukti_bayar', 'lulus': 'status_lulus_siswa',
    'created_bukti': 'tanggal_upload_bukti'
}

df_final = df.rename(columns=mapping)
print('After rename, id_mitra exists:', 'id_mitra' in df_final.columns)
print('After rename, id_mitra notna:', df_final['id_mitra'].notna().sum() if 'id_mitra' in df_final.columns else 'N/A')
