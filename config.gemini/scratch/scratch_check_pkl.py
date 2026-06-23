import pickle, sys
sys.path.insert(0, '.')

# NOT NULL columns per tabel (dari skema db_new)
NOT_NULL = {
    'pelamar':              ['nama_lengkap','nama_panggilan','jenis_kelamin','tanggal_lahir','bergabung'],
    'pelamar_sekolah':      ['tahun_lulus'],
    'pelamar_kursus':       ['tanggal'],
    'progres_pelamar':      ['pertanyaan','tautan_file'],
    'siswa':                ['jenis_kelamin','tanggal_registrasi'],
    'kursus_siswa':         ['id_siswa','id_kursus'],
    'mitra':                ['kode_mitra','visi_misi','program_mitra'],
    'rapor_siswa':          ['id_siswa','id_parameter_nilai'],
    'rapor_siswa_file':     ['id_rapor_siswa','id_siswa'],
    'rapor_lacak':          ['id_rapor_siswa_file','id_siswa'],
}

PKLS = [
    ('fase_3', 'fase_3/fase_3_hanif.pkl'),
    ('fase_4', 'fase_4/fase_4_hanif.pkl'),
    ('fase_5', 'fase_5/fase_5_hanif.pkl'),
]

for fase, path in PKLS:
    print(f"\n=== {fase} ===")
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
        for tbl, df in data.items():
            critical = NOT_NULL.get(tbl, [])
            bad = {c: int(df[c].isnull().sum()) for c in critical if c in df.columns and df[c].isnull().any()}
            if bad:
                print(f"  [CRITICAL] {tbl}: {len(df)} baris | null -> {bad}")
            else:
                print(f"  [OK]       {tbl}: {len(df)} baris")
    except FileNotFoundError:
        print(f"  (tidak ada file)")
