# DATABASE LEAP MIGRATION - DOKUMENTASI TEKNIS

## Struktur Proyek

```
db_migration_leap/
├── config.py                    # Konfigurasi database & fase
├── migrate_db.py                # Main migration controller
├── setup_files.py               # Generate file .py (legacy)
├── setup_files_ipynb.py         # Generate file .ipynb (Jupyter Notebook)
├── requirements.txt             # Python dependencies
├── migration.log                # Log file (auto-generated)
├── migration_summary_*.json     # Summary hasil migrasi (auto-generated)
│
├── fase_1/                      # 🟢 FASE 1: Persiapan Master Data (Paralel)
│   ├── script_cimut.ipynb       # Sistem & Wilayah Dasar
│   ├── script_afrida.ipynb      # Akademik Dasar
│   └── script_hanif.ipynb       # Role & Sistem
│
├── fase_2/                      # 🔵 FASE 2: Pendataan SDM & Wilayah Detail
│   ├── script_cimut.ipynb       # SDM & Relasi
│   ├── script_afrida.ipynb      # Periode & Wilayah
│   └── script_hanif.ipynb       # Divisi & Kelurahan
│
├── fase_3/                      # 🟡 FASE 3: Operasional, CRM & Pendaftaran
│   ├── script_cimut.ipynb       # CRM & Aset (FOKUS)
│   ├── script_afrida.ipynb      # Dokumentasi & Surat
│   └── script_hanif.ipynb       # Rekrutmen & Mitra
│
├── fase_4/                      # 🔴 FASE 4: Penjadwalan & Siswa Aktif
│   ├── script_cimut.ipynb       # Kehadiran & Izin
│   ├── script_afrida.ipynb      # Jadwal & Catatan (FOKUS)
│   └── script_hanif.ipynb       # Siswa & Mitra (FOKUS)
│
├── fase_5/                      # 🟣 FASE 5: Penilaian & Finalisasi
│   ├── script_cimut.ipynb       # System Logs & Config
│   ├── script_afrida.ipynb      # Presensi & Catatan Siswa
│   └── script_hanif.ipynb       # Rapor & Penilaian (FOKUS)
│
├── extract/                     # Folder untuk extract schema
│   ├── DATABASE_SCHEMA.md       # Schema database lama
│   ├── DATABASE_SCHEMA_MIGRATION.md  # Schema database baru
│   └── ...
│
├── settings/                    # Folder konfigurasi dan panduan
│   └── schema/                  # Diagram migrasi fase (.mmd)
│       ├── DB LEAP Migration's Phases.mmd
│       └── DB LEAP Migration's Phases 2.mmd
```

---

## Alur Migrasi

### Konsep Utama

Database migration dilakukan **PER FASE**, bukan sekaligus semua:

```
┌──────────────────────────────────────────────────────────────┐
│ 🟢 FASE 1: Master Data (PARALEL - Bisa jalan barengan)      │
├──────────────────────────────────────────────────────────────┤
│ Cimut (Sistem): users, divisions, shift_kerja, ...          │
│ Afrida (Akademik): kursus, level, sesi, libur, ...          │
│ Hanif (Role): roles, permissions, busdev_bidang, ...        │
└─ Validate & Save to DB_NEW ───────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ 🔵 FASE 2: SDM & Wilayah (SEQUENSIAL)                       │
├──────────────────────────────────────────────────────────────┤
│ Cimut (SDM): karyawan, keluarga_karyawan, bidang_*          │
│ Afrida (Wilayah): periode, kabupaten, kecamatan, ...        │
│ Hanif (Divisi): division_user, roles, kelurahan, ...        │
└─ Validate & Save to DB_NEW ───────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ 🟡 FASE 3: CRM & Operasional (SEQUENSIAL)                   │
├──────────────────────────────────────────────────────────────┤
│ Cimut (CRM FOKUS): calon_siswa, calon_siswa_*, peminjaman   │
│ Afrida (Surat): sop, surat_keluar, surat_tugas, ...         │
│ Hanif (Rekrutmen): pelamar, pengajuan_karyawan, ...         │
└─ Validate & Save to DB_NEW ───────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ 🔴 FASE 4: KBM & Siswa Aktif (SEQUENSIAL)                   │
├──────────────────────────────────────────────────────────────┤
│ Cimut (Kehadiran): izin_karyawan, absensi, verifikasi_*     │
│ Afrida (Jadwal FOKUS): jadwal, jadwal_*, catatan_kelas     │
│ Hanif (Siswa FOKUS): siswa, kursus_siswa, mitra, ...       │
└─ Validate & Save to DB_NEW ───────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ 🟣 FASE 5: Penilaian & Logs (SEQUENSIAL - SELESAI)         │
├──────────────────────────────────────────────────────────────┤
│ Cimut (Logs): activity_log, log_aktivitas, jadwal_detail_*  │
│ Afrida (Presensi): presensi_siswa, catatan_siswa, followup  │
│ Hanif (Rapor FOKUS): rapor_*, format, sub, formula, ...    │
└─ Validate & Save to DB_NEW ───────────────────────────────┘
        ✅ SELESAI
```

### Flow Detail Per Fase

Untuk setiap fase:

1. **Run 3 Notebooks** (script_cimut, script_afrida, script_hanif) secara **berurutan**
   - Setiap notebook: Ambil data dari DB Lama → Transform → Insert ke DB Baru
   - Setiap notebook return: `migration_result` (JSON format)

2. **Kumpulkan Hasil**
   - migrate_db.py collect output dari 3 orang
   - Validate apakah semua berhasil

3. **Simpan ke Database Baru**
   - Finalize hasil per fase
   - Ready untuk fase berikutnya

4. **Lanjut ke Fase Berikutnya** (dengan konfirmasi user)

---

## File-File Utama

### 1. config.py
Mendefinisikan:
- Database connection string (DB Lama & DB Baru)
- Konfigurasi 4 fase
- Tabel-tabel yang dimigrasikan per fase

```python
get_db_config()  # Return db_old & db_new config
get_fase_config()  # Return fase 1-4 dengan tabel-tabelnya
```

### 2. migrate_db.py
Controller utama yang:
- Menjalankan notebook per orang per fase
- Validate hasil
- Simpan ke DB baru
- Generate log & summary

**Usage:**
```bash
python migrate_db.py
```

Menu:
1. Run semua fase (1-4)
2. Run dari fase tertentu
3. Run satu fase saja
4. Exit

### 3. setup_files_ipynb.py
Generator untuk membuat template Jupyter Notebook files.

**Usage:**
```bash
python setup_files_ipynb.py
```

Membuat 15 files:
- 5 fase × 3 orang = 15 notebook files

Setiap notebook template memiliki section:
1. Header & Deskripsi
2. Import Libraries
3. Connect to DB
4. Ambil Data dari DB Lama
5. Transform Data
6. Insert ke DB Baru
7. Verifikasi Data
8. Return migration_result
9. Close Connection

---

## Cara Menggunakan

### Setup Awal

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Setup environment variables** (buat file `.env`):
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASS=password
DB_OLD=dataleap_v5_example
DB_NEW=dataleap_v5_migration
```

3. **Generate notebook files** (jika belum ada):
```bash
python setup_files_ipynb.py
```

### Menjalankan Migrasi

1. **Start migration:**
```bash
python migrate_db.py
```

2. **Pilih mode:**
   - Mode 1: Semua fase otomatis (dengan konfirmasi di tiap fase)
   - Mode 2: Dari fase tertentu
   - Mode 3: Satu fase saja (untuk testing/debugging)

3. **Isi query di setiap notebook:**
   - Buka `fase_X/script_*.ipynb`
   - Isi bagian TODO:
     - Query ambil data dari DB Lama
     - Transform logic
     - Insert query ke DB Baru

### Output

- **migration.log**: Detailed log of all operations
- **migration_summary_YYYYMMDD_HHMMSS.json**: Summary dalam format JSON

---

## Struktur Fase & Pembagian Personel

### 🟢 FASE 1: Persiapan Master Data (PARALEL)
**Status:** Independent - Bisa jalan barengan!  
**Tujuan:** Membangun fondasi data master

| Personel | Peran | Tabel yang Ditangani |
|----------|------|---------------------|
| **Cimut** | Sistem & Wilayah Dasar | `users`, `divisions`, `shift_kerja`, `admin_sarpras`, `sop_kategori`, `provinsi`, `web_berita`, `web_statistik` |
| **Afrida** | Akademik Dasar | `kursus`, `level`, `sesi`, `libur`, `topik_diskusi`, `kursus_level`, `kursus_libur` |
| **Hanif** | Role & Sistem | `roles`, `permissions`, `role_has_permissions`, `busdev_bidang`, `syarat_resign`, `ttd`, `tag_siswa_keluar` |

**Catatan:** Karena independen, ketiga script bisa dijalankan bersamaan!

---

### 🔵 FASE 2: Pendataan SDM & Wilayah Detail
**Status:** Depends on Fase 1  
**Tujuan:** Menyiapkan profil internal dan lokasi

| Personel | Peran | Tabel yang Ditangani |
|----------|------|---------------------|
| **Cimut** | SDM & Relasi | `karyawan`, `keluarga_karyawan`, `bidang_kategori`, `bidang_link` |
| **Afrida** | Periode & Wilayah | `periode`, `parameter_nilai`, `kabupaten`, `kecamatan` |
| **Hanif** | Divisi & Wilayah | `division_user`, `model_has_roles`, `model_has_permissions`, `kelurahan` |

---

### 🟡 FASE 3: Operasional, CRM & Pendaftaran
**Status:** Depends on Fase 1, 2  
**Tujuan:** Memasukkan data calon siswa dan aset

| Personel | Peran | Tabel yang Ditangani |
|----------|------|---------------------|
| **Cimut** ⭐ | **CRM & Aset (FOKUS UTAMA)** | `kontak_prospek`, `calon_siswa`, `calon_siswa_akademik`, `calon_siswa_ortu`, `calon_siswa_bayar`, `calon_siswa_jadwal`, `calon_siswa_kursus`, `calon_siswa_proses`, `calon_siswa_status_logs`, `peminjaman`, `pengadaan`, `problem` |
| **Afrida** | Dokumentasi & Surat | `sop`, `surat_keluar`, `verifikasi_surat_keluar`, `surat_tugas`, `surat_tugas_anggota` |
| **Hanif** | Rekrutmen & Mitra | `pengajuan_karyawan`, `histori_pengajuan`, `pelamar`, `pelamar_kerja`, `pelamar_sekolah`, `pelamar_kursus`, `progres_pelamar`, `rekrutmen_pelamar` |

---

### 🔴 FASE 4: Penjadwalan & Siswa Aktif
**Status:** Depends on Fase 1, 2, 3  
**Tujuan:** Migrasi data inti KBM

| Personel | Peran | Tabel yang Ditangani |
|----------|------|---------------------|
| **Cimut** | Kehadiran & Izin | `izin_karyawan`, `verifikasi_izin`, `absensi`, `verifikasi_absensi`, `karyawan_resign` |
| **Afrida** ⭐ | **Jadwal & Catatan (FOKUS UTAMA)** | `jadwal`, `jadwal_hari`, `jadwal_detail`, `jadwal_pengajar`, `jadwal_siswa`, `catatan_kelas`, `catatan_kelas_tag`, `catatan_mingguan` |
| **Hanif** ⭐ | **Siswa & Mitra (FOKUS UTAMA)** | `siswa`, `kursus_siswa`, `siswa_keluar`, `mitra`, `mitra_progres`, `kemitraan_verifikator`, `siswa_mitra`, `siswa_mitra_keluar` |

---

### 🟣 FASE 5: Penilaian & Finalisasi (SELESAI)
**Status:** Depends on Fase 1, 2, 3, 4  
**Tujuan:** Memasukkan hasil belajar dan log sistem

| Personel | Peran | Tabel yang Ditangani |
|----------|------|---------------------|
| **Cimut** | System Logs & Config | `activity_log`, `log_aktivitas`, `jadwal_detail_logs`, `password_reset_tokens` |
| **Afrida** | Presensi & Catatan Siswa | `presensi_siswa`, `catatan_siswa`, `followup_cs` |
| **Hanif** ⭐ | **Rapor & Penilaian (FOKUS UTAMA)** | `rapor_format`, `rapor_format_sub`, `rapor_format_formula`, `rapor_format_formula_sub`, `rapor_level_config`, `rapor_sub_level`, `rapor_siswa`, `rapor_siswa_file`, `rapor_lacak` |

---

## Troubleshooting

### Error: Database connection failed
- Check `.env` file konfigurasi
- Pastikan MySQL service running
- Verify credentials

### Error: Notebook not found
- Run `python setup_files_ipynb.py` untuk generate files
- Check folder structure

### Error: Table already exists
- Truncate atau drop tabel di DB Baru sebelum rerun
- Atau run migrate_db.py dengan fase dari ulang

### Partial migration
- Cek `migration.log` untuk detail error
- Fix issue di notebook yang error
- Run dari fase yang error menggunakan Mode 3

---

## Notes

- Setiap notebook **independent** (bisa dirun manual dari Jupyter atau via migrate_db.py)
- Query di notebook bersifat **template** - perlu di-customize sesuai struktur tabel
- migration_result harus di-return setiap notebook untuk tracking
- Validasi dilakukan **per fase**, bukan per person
- Database **harus dijaga consistency** antar tabel (foreign key, unique key)

---

**Last Updated:** 2026-04-21  
**Version:** 1.0
