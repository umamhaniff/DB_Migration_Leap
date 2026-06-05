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
    assert "id_pelamar" in df_p.columns
    assert pd.api.types.is_integer_dtype(df_p["id_pelamar"])
    
    # 2. Check child tables
    child_tables = ["pelamar_kerja", "pelamar_sekolah", "pelamar_kursus", "progres_pelamar", "rekrutmen_pelamar"]
    for t in child_tables:
        df_c = data.get(t)
        assert df_c is not None, f"{t} table missing"
        assert "id_pelamar" in df_c.columns
        assert pd.api.types.is_integer_dtype(df_c["id_pelamar"]) or df_c["id_pelamar"].dtype == "Int64"
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
    assert "status_pendaftaran" in df_s.columns
    assert "status_aktif" not in df_s.columns
    assert "status_lulus_siswa" not in df_s.columns
    print("OK: Fase 4 Pickle validation passed successfully!")

if __name__ == "__main__":
    test_fase_3_pickle()
    test_fase_4_pickle()
