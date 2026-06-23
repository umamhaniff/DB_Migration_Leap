# ♊ Design Specification: Database Migration Constraints & Normalization (Hanif)

**Date:** 2026-06-23  
**Author:** Hanif (Pair-programmed with Antigravity)  
**Status:** Approved by User  
**Scope:** Fase 3 (Pelamar & Child Tables) and Fase 4 (Siswa, Kursus Siswa & Mitra)

---

## 🎯 1. Objective
Resolve all MySQL warnings, data truncations, unique key conflicts, and foreign key constraint failures causing skipped rows during database migration in Fase 3 and Fase 4. This spec establishes robust transformation logic in `script_hanif.ipynb` for both phases.

---

## 🏗️ 2. Detailed Technical Design

### 🟡 2.1 Fase 3: Applicant & Child Tables Constraints

#### A. Table `pelamar`
* **Problem**: 50 skipped rows due to `nama_lengkap`, `nama_panggilan`, and `jenis_kelamin` being `NULL`. These columns are `NOT NULL` in the target schema.
* **Gender Enum Normalization**:
  * Normalize `'Laki-laki'` (hyphenated) to `'Laki laki'` (space-separated) to match target `enum('Laki laki','Perempuan')`.
  * For rows where gender is `NULL`/missing (20 old records + 14 unmatched user placeholders), use a manual lookup dictionary:
    * **Perempuan**: Ditari Kurnia, Graciela Evanda Ronadi, Rini Budi Rahayu, Cantika Swasti, Hartatik, Nisrina Dea, Mieke Puspita, Qorin, Miftakhul Jannah, Vivi Pramitha, Eka Nur, Siti Uswatun, Maria Florencia, Getari Adyagarini, Intan Safitri, Ra Putri, Gistara Azzahra, Nimas Buwana, Erfiadyn Tahzanin, Ficca Ayu, Putri Rahayu, Shania Febriana, Habibah.
    * **Laki laki**: Agung Wijayanto, Trio Fajar Cahyanto, Tedi Alvianto, Bryant Frederico, Mochamad Saiful, Akin, Ddoanda, Staff HRD.
* **NOT NULL Fallbacks**:
  * **Varchar / Text Columns** (e.g. `nama_lengkap`, `nama_panggilan`, `tempat_lahir`, `alamat_ktp`, `alamat_domisili`, `nomor_wa`, etc.): If null/empty, fill with `'-'`.
  * **Integer / Bigint Columns** (e.g. `skor_toefl`, `ekspektasi_gaji`, `skor_iq`): If null/empty, fill with `0`.
  * **Date Columns** (e.g. `tanggal_lahir`, `tanggal_bergabung`): If null/empty, fill with Unix Epoch date `'1970-01-01'`.
  * **Enum Columns** (`status_pernikahan`): Default to `'Belum Menikah'`.
  * **Enum Columns** (`penggunaan_laptop`): Default to `'Tidak Pernah'`.

#### B. Table `pelamar_sekolah`
* **Problem**: `tahun_lulus` has no default value and is `NOT NULL`.
* **Solusi**: 
  * If `tahun_lulus` is null/empty after extracting the year, default to `2000` (valid MySQL `YEAR(4)` value).
  * Default `ipk` (decimal) to `0.0` if null.
  * Default `organisasi` (text) to `'-'` if null.
  * Default `nama_sekolah`, `jenjang`, `prodi` (varchar) to `'-'` if null.

#### C. Table `pelamar_kursus`
* **Problem**: `tanggal` cannot be null and is `NOT NULL`.
* **Solusi**:
  * If `tanggal` is null/unparseable, default to `'1970-01-01'`.
  * Default `deskripsi`, `lokasi`, `nomor_sertifikat` (varchar/text) to `'-'` if null.

#### D. Table `progres_pelamar`
* **Problem**: `pertanyaan` and `tautan_file` cannot be null and are `NOT NULL`.
* **Solusi**:
  * Default `pertanyaan`, `tautan_file`, and `catatan` to `'-'` if null.

---

### 🔴 2.2 Fase 4: Students & Partners Constraints

#### A. Table `siswa`
* **Gender Enum Normalization**:
  * Normalize `'Laki-laki'` (hyphenated) to `'Laki laki'` (space-separated) to match target `enum('Laki laki','Perempuan')`.
* **Tanggal Registrasi (`tanggal_registrasi`)**:
  * Check the `no_induk` column:
    * If `no_induk` contains a valid year prefix (first 4 digits, e.g. `'2022'`) and the remaining part contains non-zero digits (e.g. `'20220000293'`), construct the date as `'YYYY-07-01'` (e.g. `'2022-07-01'`).
    * If `no_induk` is a dummy number containing only zeros after the year (e.g. `'20200000'`) or is empty/strip (`'-'`), default to Unix Epoch `'1970-01-01'`.

#### B. Table `kursus_siswa`
* **Problem**: Duplicate entries for unique key `(id_siswa, id_kursus)`.
* **Deduplication & Completion**:
  * Group registrations by `['id_siswa', 'id_kursus']` using Pandas `.groupby().first()`. This merges duplicate rows while keeping the first non-null values to complete any missing fields.
  * Recalculate `id_kursus_siswa` sequentially from `1` to `N` after deduplication.

#### C. Table `mitra`
* **Problem**: Duplicate entry `'M'` for `kode_mitra` unique key due to `extract_chars` stripping digits.
* **Deterministic Unique Codes**:
  * Retrieve all partners from `db_old.mitra`, sorted ascending by `created_at` (with `idmitra` as a tie-breaker).
  * For each partner:
    * Extract the alphabetical prefix from their students' `no_induk` (or `'M'` if they have no students/prefixes).
    * Count the occurrences of this prefix.
    * First occurrence gets prefix directly (e.g. `'TKM'`).
    * Subsequent occurrences append a 1-based sequential index (e.g. `'TKM1'`, `'TKM2'`).
  * For `id_mitra` (bigint), convert `idmitra` to integer (e.g. `'M00002'` becomes `2`).
* **Cascade mapping to `mitra_progres`**:
  * Map `id_mitra` in `mitra_progres` directly from the unique `kode_mitra` mapping dictionary built during the `mitra` step, bypassing any letter-stripping functions.
* **NOT NULL Fallbacks**:
  * Default `visi_misi`, `program_mitra`, `info_sdm`, `info_kelemahan`, and `rekomendasi_program` (text) to `'-'` if null.

---

## 🛠️ 3. Execution & Validation Strategy
1. Programmatically patch `config.gemini/apply_migration_updates.py` to insert the new logic.
2. Run notebook updates using `update_notebooks.py` to compile the notebooks and export the `.pkl` files and CSVs to `extract/cek_csv/`.
3. Verify that the output files are free of `NULL` constraint violations and duplicate keys.
4. Run integration insert scripts (executed by the integration team or locally) to verify 100% of rows are successfully loaded into `db_new`.
