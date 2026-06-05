# ♊ Design Specification: Database Migration Mapping Updates (Hanif)

**Date:** 2026-06-05  
**Author:** Hanif (Pair-programmed with Antigravity)  
**Status:** Approved by User  
**Scope:** Fase 3 (Pelamar & Child Tables), Fase 4 (Siswa & Mitra), Fase 5 (Rapor Siswa File)

---

## 🎯 1. Objective
Update and refine the ETL pipeline notebooks (`script_hanif.ipynb`) for Fase 3, Fase 4, and Fase 5 to align with database constraint changes and fix data integrity issues identified in the target database (`dataleap_v5_migration`).

---

## 🏗️ 2. Detailed Technical Design

### 🟢 2.1 Fase 3: Applicant ID Auto-Increment Mapping
* **Target Notebook:** `fase_3/script_hanif.ipynb`
* **Goal:** Convert string `idpelamar` (e.g., `'PLM001'`) into integer auto-increment PK (`id_pelamar`) and cascade changes to 5 child tables: `pelamar_kerja`, `pelamar_sekolah`, `pelamar_kursus`, `progres_pelamar`, and `rekrutmen_pelamar`.
* **Transformation Logic:**
  1. Generate `id_pelamar_new` in `pelamar` DataFrame using `reset_index().index + 1`.
  2. Build mapping dictionary: `pelamar_id_map = dict(zip(df['idpelamar'], df['id_pelamar_new']))`.
  3. Rename columns using the mapping.
  4. In all child tables, map the old string ID column to the new `id_pelamar` using `pelamar_id_map`.
  5. Convert `id_pelamar` in child tables to Pandas `Int64` (nullable integer) type to handle potential `NaN` values safely.

---

### 🔴 2.2 Fase 4: Student & Partner Updates
* **Target Notebook:** `fase_4/script_hanif.ipynb`
* **Goal:** Implement the new `status_pendaftaran` column for students and ensure complete data migration for partners.
* **Student Transformation Logic (`siswa`):**
  1. Remove `status_aktif` and `status_lulus_siswa` from column mapping.
  2. Add new column `status_pendaftaran`.
  3. Map `status_pendaftaran` directly from column `statussiswa` (varchar) in the old database.
* **Partner Transformation Logic (`mitra`):**
  1. Audit mapping of all columns in `mitra` to ensure complete data extraction (such as address, contact, dsb.).
  2. Update the insert handler (`fase_4/insert_handler.ipynb`) to execute a `DELETE` query for any partial/testing data in the target `mitra` table before inserting the migrated rows.

---

### 🟣 2.3 Fase 5: Report Card File Mapping
* **Target Notebook:** `fase_5/script_hanif.ipynb`
* **Goal:** Resolve `NULL` values in the `id_rapor_siswa` column in `rapor_siswa_file` table.
* **Transformation Logic:**
  1. Fetch the newly inserted `rapor_siswa` records (containing columns: `id_rapor_siswa` [bigint auto-increment], `id_siswa`, and `id_jadwal`) from the target database (`db_new`).
  2. In `script_hanif.ipynb`, merge the old `file_rapor_siswa` DataFrame with the fetched `rapor_siswa` table on `id_siswa` and `id_jadwal` to resolve the valid `id_rapor_siswa` integer.
  3. Save the mapped records to `fase_5_hanif.pkl`.

---

## 🛠️ 4. Execution & Validation Plan
1. Apply changes programmatically to `fase_3/script_hanif.ipynb`, `fase_4/script_hanif.ipynb`, and `fase_5/script_hanif.ipynb`.
2. Run notebook cells and generate new Pickle files (`fase_3_hanif.pkl`, `fase_4_hanif.pkl`, `fase_5_hanif.pkl`).
3. Verify that all mapped IDs are correctly populated and no runtime errors occur.
