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
├── fase_1/                      # 🟢 FASE 1: Master & Wilayah
│   ├── script_cimut.ipynb
│   ├── script_afrida.ipynb
│   └── script_hanif.ipynb
│
├── fase_2/                      # 🔵 FASE 2: SDM & Karyawan
│   ├── script_cimut.ipynb
│   ├── script_afrida.ipynb
│   └── script_hanif.ipynb
│
├── fase_3/                      # 🟡 FASE 3: CRM, Rekrutmen & Sarpras
│   ├── script_cimut.ipynb
│   ├── script_afrida.ipynb
│   └── script_hanif.ipynb
│
├── fase_4/                      # 🔴 FASE 4: KBM & Rapor
│   ├── script_cimut.ipynb
│   ├── script_afrida.ipynb
│   └── script_hanif.ipynb
│
├── extract/                     # Folder untuk extract schema
│   ├── DATABASE_SCHEMA.md       # Schema database lama
│   ├── DATABASE_SCHEMA_MIGRATION.md  # Schema database baru
│   └── ...
│
└── schema/                      # Diagram migrasi fase
    ├── DB LEAP Migration's Phases.mmd
    └── DB LEAP Migration's Phases 2.mmd
```

---

## Alur Migrasi

### Konsep Utama

Database migration dilakukan **PER FASE**, bukan sekaligus semua:

```
┌─────────────────────────────────────────────────────────────┐
│ FASE 1: Master & Wilayah (Independent)                      │
│ ├─ script_cimut.ipynb  → Transform data                     │
│ ├─ script_afrida.ipynb → Transform data                     │
│ └─ script_hanif.ipynb  → Transform data                     │
└─ Save Result to DB_NEW ────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ FASE 2: SDM & Karyawan (Depends on Fase 1)                 │
│ ├─ script_cimut.ipynb  → Transform data                     │
│ ├─ script_afrida.ipynb → Transform data                     │
│ └─ script_hanif.ipynb  → Transform data                     │
└─ Save Result to DB_NEW ────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ FASE 3: CRM, Rekrutmen & Sarpras (Depends on Fase 1,2)     │
│ ├─ script_cimut.ipynb  → Transform data                     │
│ ├─ script_afrida.ipynb → Transform data                     │
│ └─ script_hanif.ipynb  → Transform data                     │
└─ Save Result to DB_NEW ────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ FASE 4: KBM & Rapor (Depends on Fase 1,2,3)               │
│ ├─ script_cimut.ipynb  → Transform data                     │
│ ├─ script_afrida.ipynb → Transform data                     │
│ └─ script_hanif.ipynb  → Transform data                     │
└─ Save Result to DB_NEW ────────────────────────────────────┘
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

## Struktur Fase

### 🟢 FASE 1: Master & Wilayah
**Status:** Independent (tidak bergantung fase lain)
**Tabel:** Wilayah, System Setup, Akademik Dasar
- provinsi, kabupaten, kecamatan, kelurahan
- roles, permissions, divisions
- kursus, level, sesi, libur, topik_diskusi

### 🔵 FASE 2: SDM & Karyawan
**Status:** Depends on Fase 1
**Tabel:** Users, Karyawan, Kehadiran
- users, shift_kerja, karyawan
- division_user, model_has_roles
- absensi, izin_karyawan, catatan_mingguan

### 🟡 FASE 3: CRM, Rekrutmen & Sarpras
**Status:** Depends on Fase 1, 2
**Tabel:** CRM, Rekrutmen, Admin, Sarpras
- calon_siswa (dengan sub-table)
- pelamar, progres_pelamar
- mitra, surat_keluar, peminjaman, pengadaan

### 🔴 FASE 4: KBM & Rapor
**Status:** Depends on Fase 1, 2, 3
**Tabel:** Siswa Aktif, Jadwal, Presensi, Rapor, Logs
- siswa, kursus_siswa, periode
- jadwal, jadwal_detail, jadwal_pengajar
- presensi_siswa, catatan_kelas, catatan_siswa
- rapor_format, rapor_siswa, rapor_lacak
- activity_log, log_aktivitas

---

## Kontribusi Orang-Orang

Setiap orang (script_cimut, script_afrida, script_hanif) bertanggung jawab:

1. **Mengisi query** di notebook yang ditugaskan
2. **Testing** setiap notebook secara manual
3. **Transform data** sesuai kebutuhan
4. **Verify hasil** di DB Baru

Contoh pembagian (dapat disesuaikan):
- **script_cimut**: Master data & sistem
- **script_afrida**: SDM & kehadiran
- **script_hanif**: Siswa & akademik

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
