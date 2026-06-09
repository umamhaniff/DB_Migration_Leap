import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_new = mysql.connector.connect(**cfg['db_new'])
cursor = conn_new.cursor()

tables = [
    'kontak_prospek', 'calon_siswa', 'calon_siswa_akademik', 'calon_siswa_ortu', 
    'calon_siswa_bayar', 'calon_siswa_jadwal', 'calon_siswa_kursus', 'calon_siswa_proses', 
    'calon_siswa_status_logs', 'pengajuan_karyawan', 'histori_pengajuan', 'pelamar', 
    'pelamar_kerja', 'pelamar_sekolah', 'pelamar_kursus', 'progres_pelamar', 
    'rekrutmen_pelamar', 'mitra', 'mitra_progres', 'kemitraan_verifikator',
    'siswa', 'kursus_siswa', 'siswa_keluar', 'siswa_mitra', 'siswa_mitra_keluar'
]

print("--- Row counts in db_new ---")
for t in tables:
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {t}")
        cnt = cursor.fetchone()[0]
        print(f"{t}: {cnt}")
    except Exception as e:
        print(f"{t}: Error: {e}")

cursor.close()
conn_new.close()
