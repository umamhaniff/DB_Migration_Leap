import json
import os

path = 'fase_4/script_hanif.ipynb'
if not os.path.exists(path):
    print("Not found")
    exit(1)

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and '1. siswa -> siswa' in ''.join(cell['source']):
        source = ''.join(cell['source'])
        
        # We need to insert the normalization logic right before `df_final = df.rename(columns=mapping)`
        # Wait, the best way to insert is replacing exactly what is there.
        # Original has:
        #     'sts_pengisian': 'status_pengisian', 'bukti': 'path_bukti_bayar', 'lulus': 'status_lulus_siswa',\n
        #     'created_bukti': 'tanggal_upload_bukti'\n
        # }\n
        # df_final = df.rename(columns=mapping)\n
        # df_final['pekerjaan_ibu'] = None\n
        
        target = "    df_final = df.rename(columns=mapping)\n    df_final['pekerjaan_ibu'] = None"
        
        new_logic = """
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
    df_final['pekerjaan_ibu'] = 'Lainnya'"""
        
        if target in source:
            source = source.replace(target, new_logic)
        
            cell['source'] = [line + '\n' for line in source.split('\n')]
            if cell['source'][-1] == '\n': cell['source'].pop()

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Patch applied")