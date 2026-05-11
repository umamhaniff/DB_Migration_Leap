import mysql.connector, os, pandas as pd, re
from dotenv import load_dotenv
load_dotenv()
c=mysql.connector.connect(host=os.getenv('DB_HOST'), port=int(os.getenv('DB_PORT')), user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), database=os.getenv('DB_OLD'), collation='utf8mb4_general_ci')
cur=c.cursor(dictionary=True)
cur.execute('SELECT * FROM siswa')
raw_data = {'siswa': cur.fetchall()}
c.close()
transformed_dfs = {}
transformed_dfs = {}

# --- HELPER FUNCTIONS ---
def extract_int(s):
    if pd.isna(s) or not str(s).strip(): return None
    nums = re.findall(r'\\d+', str(s))
    return int(nums[0]) if nums else None

def extract_chars(s):
    if pd.isna(s) or not str(s).strip(): return None
    return re.sub(r'\\d+', '', str(s)).strip()

def convert_ya_tidak(s):
    if pd.isna(s): return 0
    val = str(s).strip().lower()
    return 1 if val == 'ya' else 0

# --- TRANSFORMATION ---

# 1. siswa -> siswa
if 'siswa' in raw_data:
    df = pd.DataFrame(raw_data['siswa'])
    df['idmitra_int'] = df['idmitra'].apply(extract_int)
    
    # Normalisasi Agama
    agama_map = {
        'kristen': 'Kristen Protestan', 'protestan': 'Kristen Protestan', 
        'katholik': 'Katolik', 'budha': 'Buddha', 'khonghucu': 'Konghucu'
    }
    def normalize_agama(a):
        if pd.isna(a): return 'Islam'
        a_clean = str(a).strip()
        for k, v in agama_map.items():
            if k in a_clean.lower(): return v
        return a_clean
    df['agama'] = df['agama'].apply(normalize_agama)

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

    # Normalisasi Pekerjaan
    def normalize_pekerjaan(p):
        if pd.isna(p) or str(p).strip() in ('', '-', 'NO DATA', '0'): return 'Lainnya'
        s = str(p).strip().lower()
        if 'pegawai_swasta' in s or 'karyawan swasta' in s or 'karyawan' in s: return 'Pegawai Swasta'
        if 'wiraswasta' in s: return 'Wiraswasta'
        if 'aparatur_pejabat_negara' in s or 'tni' in s or 'pns' in s: return 'Aparatur/Pejabat Negara'
        if 'tenaga_kesehatan' in s: return 'Tenaga Kesehatan'
        if 'belum_tidak_bekerja' in s or 'tidak bekerja' in s: return 'Belum/Tidak Bekerja'
        if 'pensiunan' in s: return 'Pensiunan'
        if 'tenaga_pengajar' in s or 'guru' in s or 'dosen' in s: return 'Tenaga Pengajar'
        if 'agama_kepercayaan' in s: return 'Agama dan Kepercayaan'
        if 'pelajar_mahasiswa' in s or 'pelajar' in s: return 'Pelajar/Mahasiswa'
        if 'nelayan' in s: return 'Nelayan'
        if 'pertanian_peternakan' in s or 'tani' in s: return 'Pertanian/Peternakan'
        return 'Lainnya'
        
    df['pekerjaan_ayah'] = df['pekerjaan_ayah'].apply(normalize_pekerjaan)
    df['pekerjaan_wali'] = df['pekerjaan_wali'].apply(normalize_pekerjaan)
    if 'pekerjaan_ortu' in df.columns:
        df['pekerjaan_ortu'] = df['pekerjaan_ortu'].apply(normalize_pekerjaan)
        
    # Normalisasi Penghasilan
    def normalize_penghasilan(p):
        if pd.isna(p) or str(p).strip() in ('', '-', 'NO DATA', '0'): return None
        s = str(p).strip()
        if s in ('kurang_1jt', '1jt_3jt', '3jt_5jt', 'lebih_5jt'): return s
        return None
        
    df['penghasilan_ayah'] = df['penghasilan_ayah'].apply(normalize_penghasilan)
    df['penghasilan_ibu'] = df['penghasilan_ibu'].apply(normalize_penghasilan)
    df['penghasilan_wali'] = df['penghasilan_wali'].apply(normalize_penghasilan)
    
    df_final = df.rename(columns=mapping)
    df_final['pekerjaan_ibu'] = 'Lainnya'
    df_final['deleted_at'] = None
    target_cols = [c for c in list(mapping.values()) if c in df_final.columns] + ['pekerjaan_ibu', 'deleted_at']
    transformed_dfs['siswa'] = df_final[target_cols]


print(transformed_dfs['siswa']['id_mitra'].notna().sum())
