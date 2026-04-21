import os
from dotenv import load_dotenv

load_dotenv()

def get_db_config():
    """
    Konfigurasi database lama dan baru.
    
    Returns:
        dict: Configuration dengan struktur:
            - db_old: Config untuk database lama (dataleap_v5_example)
            - db_new: Config untuk database baru (dataleap_v5_migration)
    """
    return {
        'db_old': {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', 3306)),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASS', ''),
            'database': os.getenv('DB_OLD', 'dataleap_v5_example'),
            'autocommit': True,
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_general_ci'
        },
        'db_new': {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', 3306)),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASS', ''),
            'database': os.getenv('DB_NEW', 'dataleap_v5_migration'),
            'autocommit': True,
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_general_ci'
        }
    }

def get_fase_config():
    """
    Konfigurasi fase migrasi dan tabel-tabel yang akan dimigrasikan.
    
    Returns:
        dict: Mapping fase ke list orang dan tabel-tabel yang ditangani
    """
    return {
        'fase_1': {
            'nama': '🟢 DATA MASTER & WILAYAH',
            'deskripsi': 'Migrasi data master independen dan wilayah',
            'tabel_utama': [
                'provinsi', 'kabupaten', 'kecamatan', 'kelurahan',  # Wilayah
                'roles', 'permissions', 'role_has_permissions',      # Sistem
                'divisions',                                          # Organisasi
                'kursus', 'level', 'sesi', 'libur', 'topik_diskusi',  # Akademik
                'parameter_nilai'
            ],
            'people': ['script_cimut', 'script_afrida', 'script_hanif']
        },
        'fase_2': {
            'nama': '🔵 SDM & PENGGUNA',
            'deskripsi': 'Migrasi users, karyawan, dan pengelolaan kehadiran',
            'tabel_utama': [
                'users', 'shift_kerja', 'karyawan',                  # SDM
                'division_user', 'model_has_roles', 'model_has_permissions',
                'keluarga_karyawan', 'password_reset_tokens',        # Detail SDM
                'verifikasi_absensi', 'izin_karyawan', 'absensi',    # Kehadiran
                'verifikasi_izin', 'catatan_mingguan',
                'karyawan_resign', 'syarat_resign'
            ],
            'people': ['script_cimut', 'script_afrida', 'script_hanif']
        },
        'fase_3': {
            'nama': '🟡 CRM, REKRUTMEN & SARPRAS',
            'deskripsi': 'Migrasi CRM calon siswa, rekrutmen, dan sarpras',
            'tabel_utama': [
                'kontak_prospek', 'calon_siswa',                     # CRM
                'calon_siswa_akademik', 'calon_siswa_ortu', 'calon_siswa_bayar',
                'calon_siswa_jadwal', 'calon_siswa_kursus', 'calon_siswa_proses',
                'calon_siswa_status_logs',
                'pengajuan_karyawan', 'histori_pengajuan',           # Rekrutmen
                'pelamar', 'pelamar_kerja', 'pelamar_sekolah', 'pelamar_kursus',
                'progres_pelamar', 'rekrutmen_pelamar',
                'mitra', 'mitra_progres', 'kemitraan_verifikator',   # Mitra
                'sop_kategori', 'sop', 'mou',                        # Sarpras
                'surat_keluar', 'verifikasi_surat_keluar', 'surat_tugas',
                'surat_tugas_anggota', 'peminjaman', 'pengadaan', 'problem',
                'admin_sarpras'
            ],
            'people': ['script_cimut', 'script_afrida', 'script_hanif']
        },
        'fase_4': {
            'nama': '🔴 OPERASIONAL KBM & RAPOR',
            'deskripsi': 'Migrasi operasional kelas, presensi, dan rapor',
            'tabel_utama': [
                'siswa', 'kursus_siswa', 'tag_siswa_keluar',         # Siswa
                'siswa_keluar', 'periode',
                'jadwal', 'jadwal_hari', 'jadwal_detail',             # Jadwal
                'jadwal_pengajar', 'jadwal_siswa',
                'presensi_siswa',                                    # Penilaian
                'catatan_kelas', 'catatan_kelas_tag', 'catatan_siswa',
                'followup_cs',
                'rapor_format', 'rapor_format_sub', 'rapor_format_formula',
                'rapor_format_formula_sub', 'rapor_level_config', 'rapor_sub_level',
                'rapor_siswa', 'rapor_siswa_file', 'rapor_lacak',
                'activity_log', 'log_aktivitas', 'jadwal_detail_logs',  # Logs
                'sessions', 'jobs', 'job_batches', 'failed_jobs'
            ],
            'people': ['script_cimut', 'script_afrida', 'script_hanif']
        }
    }
