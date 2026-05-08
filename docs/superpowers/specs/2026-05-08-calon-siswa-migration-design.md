# Design Doc: Migrasi Calon Siswa & Sub-Tabel (CRM)

**Date**: 2026-05-08
**Topic**: CRM Student Candidate Migration
**Status**: Approved

## 1. Executive Summary
Migrasi data calon siswa dari database lama (v5 Lama) ke database baru (v5 Baru). Proses ini mencakup tabel utama `calon_siswa` dan 6 sub-tabel terkait (`akademik`, `ortu`, `bayar`, `jadwal`, `kursus`, `proses`).

## 2. Technical Strategy

### 2.1. Data Source (Old DB)
- `form_calon`: Tabel data utama calon siswa.
- `form_calon_detil1`: Data orang tua dan program.
- `form_calon_detil2`: Data trial dan penempatan.
- `form_calon_detil3`: Data pembayaran dan lokasi.
- `form_calon_detil4`: Data follow-up dan akun.

### 2.2. Data Target (New DB)
- `calon_siswa`: Tabel utama.
- `calon_siswa_akademik`: Detail sekolah dan akademik.
- `calon_siswa_ortu`: Detail orang tua (Ayah, Ibu, Wali).
- `calon_siswa_bayar`: Status dan detail pembayaran.
- `calon_siswa_jadwal`: Tanggal-tanggal penting proses.
- `calon_siswa_kursus`: Daftar kursus yang diminati.
- `calon_siswa_proses`: Detail proses trial, follow-up, dan catatan admin.

### 2.3. Key Transformation Rules
- **ID Transformation**: `idcalon` (e.g., "C00000017") -> `id_calon` (numeric 17).
- **Prospect Matching**: Menggunakan `nama` dan `email` untuk mencari `id_kontak_prospek` dari `df_kontak_prospek_ready`.
- **Regional Data**: Ambil nilai nama wilayah (string) saja, letakkan di kolom yang relevan tanpa pencocokan ID ke tabel wilayah baru.
- **Sub-table Relation**: Semua sub-tabel menggunakan `id_calon` (numeric) sebagai Foreign Key.

## 3. Implementation Plan (Cell-by-Cell)

### Cell 1: Master Data Preparation
- Load all `form_calon*` tables into separate DataFrames.
- Left join all data into a single `df_calon_master` using `idcalon`.

### Cell 2: Data Cleaning & ID Matching
- Extract numeric ID from `idcalon`.
- Map `id_kontak_prospek` by matching (name, email) with `df_kontak_prospek_ready`.
- Handle potential missing matches by assigning NULL or logging.

### Cell 3: Migration - `calon_siswa`
- Transform `df_calon_master` to match `calon_siswa` schema.
- Perform batch insert into `calon_siswa`.

### Cell 4: Migration - `calon_siswa_akademik` & `calon_siswa_ortu`
- Map academic data (school, level, etc.).
- Map parent data (Ayah, Ibu, Wali).
- Perform batch insert.

### Cell 5: Migration - `calon_siswa_bayar` & `calon_siswa_jadwal`
- Map payment status, invoice, and bank.
- Map dates (contact, interview, trial, payment, etc.).
- Perform batch insert.

### Cell 6: Migration - `calon_siswa_proses` & `calon_siswa_kursus`
- Map trial process, results, follow-up, and admin notes.
- Map interested courses.
- Perform batch insert.

### Cell 7: Final Validation
- Check row counts for all target tables.
- Commit transaction.

## 4. Risks & Mitigations
- **Data Mismatch**: Potential mismatch in name/email for prospect matching. *Mitigation*: Use fuzzy matching or log missed records for manual review.
- **Numeric ID Collision**: Ensure extracted IDs don't collide with existing records. *Mitigation*: Clear target tables before migration if necessary.
