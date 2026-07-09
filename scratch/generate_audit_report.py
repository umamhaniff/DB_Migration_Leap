import sys
import os
import pickle
import mysql.connector
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def load_all_pickle_data():
    all_data = {}
    
    # Cimut
    p1 = "fase_3/fase_3_cimut.pkl"
    if os.path.exists(p1):
        with open(p1, 'rb') as f:
            all_data.update(pickle.load(f))
            
    # Afrida
    p2 = "fase_3/fase_3_afrida.pkl"
    if os.path.exists(p2):
        with open(p2, 'rb') as f:
            all_data.update(pickle.load(f))
            
    # Hanif
    p3 = "fase_3/fase_3_hanif.pkl"
    if os.path.exists(p3):
        with open(p3, 'rb') as f:
            all_data.update(pickle.load(f))
            
    return all_data

def main():
    # 1. Load all tables sent via pickles
    all_pickles = load_all_pickle_data()
    
    # Define our targeted tables and their owners
    blocks = {
        'Hanif (Blok A)': [
            'pelamar', 'pelamar_kerja', 'pelamar_sekolah', 'pelamar_kursus', 
            'progres_pelamar', 'rekrutmen_pelamar', 'pengajuan_karyawan', 'histori_pengajuan'
        ],
        'Afrida (Blok B)': [
            'sop', 'surat_keluar', 'verifikasi_surat_keluar', 'surat_tugas', 
            'surat_tugas_anggota', 'sop_kategori'
        ],
        'Cimut (Blok C & D)': [
            'kontak_prospek', 'calon_siswa', 'calon_siswa_ortu', 'calon_siswa_akademik',
            'calon_siswa_bayar', 'calon_siswa_jadwal', 'calon_siswa_kursus', 
            'calon_siswa_proses', 'calon_siswa_status_logs', 'pengadaan', 
            'peminjaman', 'problem'
        ]
    }
    
    # Connect to db_new to get actual counts
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_new'])
    cursor = conn.cursor()
    
    # Load raw notebook log to extract failed reasons
    log_path = "scratch/fase3_run_outputs.log"
    log_text = ""
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            log_text = f.read()
            
    # Read failed reasons
    failed_reasons = {}
    import re
    # Extract sections like: 🚨 [🔴 DIAGNOSTIK TABEL ERROR: TABLE_NAME] 🚨\nAlasan MySQL Menolak: ...
    # And stop before the next section
    pattern = r"🚨 \[🔴 DIAGNOSTIK TABEL ERROR: ([A-Z_]+)\] 🚨\s*\nAlasan MySQL Menolak: ([^\n]+)"
    matches = re.findall(pattern, log_text)
    for tbl, reason in matches:
        failed_reasons[tbl.lower()] = reason.strip()
        
    report = []
    report.append("# 📊 Audit Laporan Migrasi Data Fase 3")
    report.append(f"Tanggal Audit: 2026-07-09\n")
    report.append("| Nama Tabel | Pemilik Blok | Dikirim (Pickle) | Masuk (Database) | Status | Keterangan / Detail Kendala |")
    report.append("|---|---|---|---|---|---|")
    
    for block_name, tables in blocks.items():
        for table in tables:
            # Get pickle count
            df = all_pickles.get(table)
            pkl_count = len(df) if df is not None else 0
            
            # Get db count
            db_count = 0
            status = "✓ Sukses"
            detail = "Semua baris ter-insert dengan bersih."
            
            try:
                cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
                db_count = cursor.fetchone()[0]
            except Exception as e:
                db_count = 0
                status = "✗ Error"
                detail = f"Gagal membaca tabel: {e}"
                
            # If there was a failure reported in logs
            if table in failed_reasons:
                status = "✗ Gagal total"
                detail = failed_reasons[table]
            elif pkl_count == 0:
                status = "ℹ️ Kosong"
                detail = "DataFrame kosong (0 baris)."
            elif db_count < pkl_count:
                # If some rows were skipped
                skipped = pkl_count - db_count
                status = "⚠️ Ter-skip sebagian"
                detail = f"{skipped} baris ter-skip/di-ignore MySQL (cek warning)."
                
            report.append(f"| `{table}` | {block_name} | {pkl_count} | {db_count} | {status} | {detail} |")
            
    conn.close()
    
    # Save report as artifact
    report_content = "\n".join(report)
    with open("scratch/laporan_diagnostik_fase3.md", "w", encoding="utf-8") as f_rep:
        f_rep.write(report_content)
        
    print("\nReport generated successfully at scratch/laporan_diagnostik_fase3.md")

if __name__ == '__main__':
    main()
