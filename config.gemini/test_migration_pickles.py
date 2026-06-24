import os
import pandas as pd

def test_fase_3_pickle():
    path = "fase_3/fase_3_hanif.pkl"
    if not os.path.exists(path):
        print(f"Skipping {path} as it does not exist yet.")
        return
    data = pd.read_pickle(path)
    
    # 1. Check pelamar
    df_p = data.get("pelamar")
    assert df_p is not None, "pelamar table missing"
    assert "id_pelamar" not in df_p.columns, "id_pelamar PK should be removed to let MySQL auto-increment"
    
    # 2. Check child tables
    child_tables = ["pelamar_kerja", "pelamar_sekolah", "pelamar_kursus", "progres_pelamar", "rekrutmen_pelamar"]
    for t in child_tables:
        df_c = data.get(t)
        assert df_c is not None, f"{t} table missing"
        assert "id_pelamar" in df_c.columns, f"id_pelamar FK missing in {t}"
        assert pd.api.types.is_integer_dtype(df_c["id_pelamar"]) or df_c["id_pelamar"].dtype == "Int64"
        
        # Check that PK columns are removed
        pk_map = {
            "pelamar_kerja": "id_pelamar_kerja",
            "pelamar_sekolah": "id_pelamar_sekolah",
            "pelamar_kursus": "id_pelamar_kursus",
            "progres_pelamar": "id_progres_pelamar",
            "rekrutmen_pelamar": "id_rekrutmen"
        }
        pk_col = pk_map[t]
        assert pk_col not in df_c.columns, f"PK {pk_col} should be removed from {t}"

    # 3. Check pengajuan_karyawan and histori_pengajuan
    df_pk = data.get("pengajuan_karyawan")
    assert df_pk is not None, "pengajuan_karyawan table missing"
    assert "id_pengajuan" not in df_pk.columns, "id_pengajuan PK should be removed from pengajuan_karyawan"
    
    df_hp = data.get("histori_pengajuan")
    assert df_hp is not None, "histori_pengajuan table missing"
    assert "id_verifikasi" not in df_hp.columns, "id_verifikasi PK should be removed from histori_pengajuan"
    assert "id_pengajuan" in df_hp.columns, "id_pengajuan FK missing in histori_pengajuan"
    assert pd.api.types.is_integer_dtype(df_hp["id_pengajuan"]) or df_hp["id_pengajuan"].dtype == "Int64"

    print("OK: Fase 3 Pickle validation passed successfully!")

def test_fase_4_pickle():
    path = "fase_4/fase_4_hanif.pkl"
    if not os.path.exists(path):
        print(f"Skipping {path} as it does not exist yet.")
        return
    data = pd.read_pickle(path)
    
    # 1. Check siswa
    df_s = data.get("siswa")
    assert df_s is not None, "siswa table missing"
    assert "id_siswa" not in df_s.columns, "id_siswa PK should be removed from siswa"
    assert "status_pendaftaran" in df_s.columns
    assert "status_aktif" not in df_s.columns
    assert "status_lulus_siswa" not in df_s.columns
    
    # 2. Check mitra
    df_m = data.get("mitra")
    assert df_m is not None, "mitra table missing"
    assert "id_mitra" not in df_m.columns, "id_mitra PK should be removed from mitra"
    
    # 3. Check mitra_progres
    df_mp = data.get("mitra_progres")
    assert df_mp is not None, "mitra_progres table missing"
    assert "id_progres_mitra" not in df_mp.columns, "id_progres_mitra PK should be removed from mitra_progres"
    assert "id_mitra" in df_mp.columns, "id_mitra FK missing in mitra_progres"
    
    # 4. Check kemitraan_verifikator
    df_kv = data.get("kemitraan_verifikator")
    assert df_kv is not None, "kemitraan_verifikator table missing"
    assert "id_kemitraan" not in df_kv.columns, "id_kemitraan PK should be removed from kemitraan_verifikator"
    assert "id_progres_mitra" in df_kv.columns, "id_progres_mitra FK missing in kemitraan_verifikator"
    
    # 5. Check siswa_mitra
    df_sm = data.get("siswa_mitra")
    assert df_sm is not None, "siswa_mitra table missing"
    assert "id_sm" not in df_sm.columns, "id_sm PK should be removed from siswa_mitra"
    assert "id_mitra" in df_sm.columns, "id_mitra FK missing in siswa_mitra"
    
    # 6. Check siswa_mitra_keluar
    df_smk = data.get("siswa_mitra_keluar")
    assert df_smk is not None, "siswa_mitra_keluar table missing"
    assert "id_sm_keluar" not in df_smk.columns, "id_sm_keluar PK should be removed from siswa_mitra_keluar"
    assert "id_sm" in df_smk.columns, "id_sm FK missing in siswa_mitra_keluar"
    
    # 7. Check siswa_keluar
    df_sk = data.get("siswa_keluar")
    assert df_sk is not None, "siswa_keluar table missing"
    assert "id_keluar" not in df_sk.columns, "id_keluar PK should be removed from siswa_keluar"
    assert "id_siswa" in df_sk.columns, "id_siswa FK missing in siswa_keluar"

    # 8. Check kursus_siswa
    df_ks = data.get("kursus_siswa")
    assert df_ks is not None, "kursus_siswa table missing"
    assert "id_kursus_siswa" not in df_ks.columns, "id_kursus_siswa PK should be removed from kursus_siswa"
    assert "id_siswa" in df_ks.columns, "id_siswa FK missing in kursus_siswa"

    print("OK: Fase 4 Pickle validation passed successfully!")

def test_fase_5_pickle():
    path = "fase_5/fase_5_hanif.pkl"
    if not os.path.exists(path):
        print(f"Skipping {path} as it does not exist yet.")
        return
    data = pd.read_pickle(path)
    
    # Check rapor tables
    tables = ["rapor_siswa", "rapor_siswa_file", "rapor_lacak"]
    for t in tables:
        df = data.get(t)
        assert df is not None, f"{t} table missing in Fase 5 pickle"
        
        # Validate PK is removed
        pk_map = {
            "rapor_siswa": "id_rapor_siswa",
            "rapor_siswa_file": "id_rapor_siswa_file",
            "rapor_lacak": "id_rapor_lacak"
        }
        pk_col = pk_map[t]
        assert pk_col not in df.columns, f"PK {pk_col} should be removed from {t}"
        
        # Validate ID/FK dtypes
        id_cols = [c for c in df.columns if c.startswith('id_') or c.endswith('_id') or c == 'id']
        for col in id_cols:
            dtype_str = str(df[col].dtype)
            assert any(x in dtype_str for x in ['int', 'Int64']), f"Column {col} in {t} has non-integer dtype: {dtype_str}"
            
    # Check formula and level config tables
    other_tables = ["rapor_format_formula", "rapor_format_formula_sub", "rapor_level_config", "rapor_sub_level"]
    for t in other_tables:
        df = data.get(t)
        assert df is not None, f"{t} table missing in Fase 5 pickle"
        
        pk_map = {
            "rapor_format_formula": "id_rapor_format_formula",
            "rapor_format_formula_sub": "id_rapor_format_formula_sub",
            "rapor_level_config": "id_rapor_level_config",
            "rapor_sub_level": "id_rapor_sub_level"
        }
        pk_col = pk_map[t]
        assert pk_col not in df.columns, f"PK {pk_col} should be removed from {t}"

    print("OK: Fase 5 Pickle validation passed successfully!")

if __name__ == "__main__":
    test_fase_3_pickle()
    test_fase_4_pickle()
    test_fase_5_pickle()
