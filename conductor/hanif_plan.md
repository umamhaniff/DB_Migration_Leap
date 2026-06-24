# Hanif's Scripts Migration Plan

**Goal:** Resolve any potential issues in Hanif's migration scripts for Phase 3, 4, and 5 based on `hanif_mapping.md`. Ensure the logic is fully implemented and test the notebooks for runtime execution errors.

**Background & Motivation:**
The user requested to audit the column mapping implementation from `hanif_mapping.md` in `fase_3`, `fase_4`, and `fase_5` notebooks, and fix any potential issues. Static analysis shows that `update_notebooks.py` has already injected the mapping logic (e.g., date parsing, enum normalization, foreign key lookups). However, "potential issues" (masalah yang kemungkinan terjadi) usually surface as Pandas runtime errors (KeyError, TypeError) due to messy actual database values.

**Scope & Impact:**
- **Fase 3 (`script_hanif.ipynb`)**: CRM, Recruitment & Sarpras.
- **Fase 4 (`script_hanif.ipynb`)**: Students & Partners.
- **Fase 5 (`script_hanif.ipynb`)**: Grading & Finalization.

**Implementation Steps:**

- [x] **Step 1: Execute & Debug Fase 3**
  - Run `fase_3/script_hanif.ipynb` via Python or `nbconvert`.
  - Verify that `extract_date`, `parse_date`, and `clean_currency` handle all existing data without throwing exceptions.
  - If errors occur, patch `fase_3/script_hanif.ipynb`.

- [x] **Step 2: Execute & Debug Fase 4**
  - Run `fase_4/script_hanif.ipynb`.
  - Validate `detect_tag` and enum mappings (`agama`, `pekerjaan_ayah`, etc.).
  - Check if empty tables `siswa_mitra` and `siswa_mitra_keluar` cause any pipeline breaks downstream.
  - Fix any runtime errors.

- [x] **Step 3: Execute & Debug Fase 5**
  - Run `fase_5/script_hanif.ipynb`.
  - Verify that the updated lookup logic (using `merge` instead of dictionary mapping for `rapor_siswa_file` and `rapor_lacak`) correctly joins the data.
  - Fix any runtime errors.

**Verification:**
After executing all three notebooks successfully, we will verify the resulting `.pkl` files are valid.

---

## Update Rencana & Penyelesaian Masalah (24 Juni 2026)

### 🚨 Tantangan Lapangan Baru yang Ditemukan saat Proses Pengunggahan (Insert) Aktual:
1. **Error Truncated Data (WA)**: Panjang data nomor WhatsApp pada kolom `wa_siswa`, `wa_ortu`, dan `wa_administrasi` melebihi batas skema baru `VARCHAR(20)` karena adanya nomor ganda/catatan teks di database lama.
2. **FK Mismatch (Kursus & Siswa)**: 
   * `id_kursus` ter-extract menjadi integer padahal tipe data primary key `kursus` di database baru adalah string (varchar).
   * `id_siswa` di database baru menggunakan tipe data integer auto-increment, sehingga ID baru yang di-generate MySQL (`1, 2, 3, dst.`) tidak sinkron dengan data foreign key di tabel anak yang sebelumnya dipetakan menggunakan `extract_int(idsiswa)` yang memiliki celah (*gaps*).
3. **Pembersihan Pelamar**: Kolom skor TOEFL mengandung data string kotor (seperti `'asd'`) dan kolom `created_at` yang kosong diisi `'1970-01-01'` sehingga memicu error *out of range* akibat konversi zona waktu lokal ke UTC.

### 🛠️ Langkah Mitigasi & Eksekusi Penyelesaian (Selesai):
* [x] **Mitigasi 1: Pembersihan No WA** — Menambahkan fungsi pembagian berdasarkan slash (`/`), pembersihan non-angka, dan pembatasan panjang nomor telepon maksimal 15 karakter di Fase 4.
* [x] **Mitigasi 2: Pemetaan Auto-Increment Siswa** — Menghapus kolom `id_siswa` dari DataFrame `siswa` (membiarkan MySQL melakukan auto-increment secara natural) dan membuat berkas pemetaan `mapping_siswa.pkl` serta `.csv` berdasarkan urutan baris (`index + 1`).
* [x] **Mitigasi 3: Sinkronisasi Lintas Fase** — Memperbaiki relasi Foreign Key di tabel Fase 4 (`kursus_siswa`, `siswa_keluar`) dan Fase 5 (`rapor_siswa`, `rapor_lacak`) agar menyinkronkan data `id_siswa` menggunakan berkas pemetaan auto-increment yang baru. Memulihkan format `id_kursus` menjadi string.
* [x] **Mitigasi 4: Perbaikan Nilai Default & Pembersihan String Pelamar** — Memperbaiki pengisian default `created_at` ke tanggal aman `'2020-01-01 00:00:00'` dan mengonversi kolom TOEFL/IQ menggunakan `pd.to_numeric` dengan `errors='coerce'`.
* [x] **Mitigasi 5: Penghapusan Seluruh PK Auto-Increment & Pembuatan Pemetaan Induk Lintas Fase** — Menghapus seluruh kolom primary key yang bertipe auto-increment dari DataFrame di Fase 3, 4, dan 5. Menghasilkan berkas pemetaan (`id_lama` ke `id_baru` berupa index + 1) dalam bentuk `.pkl` dan `.csv` untuk seluruh tabel induk: `pelamar`, `pengajuan_karyawan`, `siswa`, `mitra`, `mitra_progres`, `siswa_mitra`, `rapor_siswa`, dan `rapor_siswa_file`. Memetakan kolom foreign key pada seluruh tabel anak (seperti progres pelamar, progres mitra, riwayat sekolah, dan rapor siswa) menggunakan berkas pemetaan secara dinamis dan offline (in-memory).
* [x] **Mitigasi 6: Pembersihan Kolom Alamat Domisili** — Memotong data `domisili` pada koma pertama yang ditemukan dan membatasi teks maksimal 100 karakter untuk menghindari truncation error.
* [x] **Mitigasi 7: Penghapusan PK `id_kursus_siswa` & Proteksi Nilai Default NOT NULL** — Menghapus primary key `id_kursus_siswa` dari target DataFrame `kursus_siswa` untuk menghindari tabrakan auto-increment MySQL. Menambahkan penanganan tangguh untuk semua kolom `NOT NULL` yang kosong/NULL pada tabel `siswa` (seperti `asal_sekolah`, `tingkat_sekolah`, `nama_orang_tua`, `pekerjaan_orang_tua`, `tempat_lahir`, `path_bukti_bayar` diisi `'-'`; `tanggal_lahir` diisi `'1970-01-01'`; dan `tanggal_upload_bukti` diisi `'2020-01-01 00:00:00'`) serta tabel `mitra` (`status_mitra` diisi `'On-going'`; `jenis_mitra` diisi `'Lainnya'`; serta `nama_mitra` dan `nama_instansi` diisi `'-'`). Hal ini sepenuhnya menyelesaikan masalah duplikasi primer dan kegagalan constraint MySQL.
* [x] **Verifikasi & Validasi Sukses** — Menjalankan penyuntingan ulang seluruh notebook secara berurutan dan memvalidasi semuanya via `test_migration_pickles.py` dengan sukses 100%. Melakukan commit dan push ke repositori tanpa menyertakan berkas milik rekan tim (Cimut/Afrida) sesuai arahan.
