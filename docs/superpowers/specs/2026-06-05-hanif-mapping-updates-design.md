# ♊ Design Specification: Database Migration Mapping Updates (Hanif)

**Date:** 2026-06-05  
**Author:** Hanif (Pair-programmed with Antigravity)  
**Status:** Under Review  
**Scope:** Fase 3 (Pelamar & Child Tables), Fase 4 (Siswa & Mitra), Fase 5 (Rapor Siswa File Audit)

---

## 🎯 1. Objective
Update and refine the ETL pipeline notebooks (`script_hanif.ipynb`) for Fase 3 and Fase 4 to align with database constraint changes. Additionally, audit the Fase 5 notebook to identify why `id_rapor_siswa` in `rapor_siswa_file` fails to populate (NULL) in the target database (`dataleap_v5_migration`).

---

## 🏗️ 2. Detailed Technical Design & Audit

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
* **Goal:** Implement the new `status_pendaftaran` column for students and verify the completeness of columns for partners.
* **Student Transformation Logic (`siswa`):**
  1. Remove `status_aktif` and `status_lulus_siswa` from column mapping.
  2. Add new column `status_pendaftaran`.
  3. Map `status_pendaftaran` directly from column `statussiswa` (varchar) in the old database.
* **Partner Transformation Logic (`mitra`):**
  1. Audit mapping of all columns in `mitra` to ensure complete data extraction (such as address, contact, dsb.). *Note: Data insertion handler fixes are handled by the coordinator/integration team, not in Hanif's script.*

---

### 🟣 2.3 Fase 5: Report Card File Code Audit
* **Target Notebook:** `fase_5/script_hanif.ipynb`
* **Goal:** Audit the transformation logic to identify why `id_rapor_siswa` in `rapor_siswa_file` is populated as NULL in `db_new`.
* **Findings & Diagnoses:**
  1. In the target database (`db_new`), the column `id_rapor_siswa` in table `rapor_siswa` is defined as a `bigint(20) AUTO_INCREMENT` (integer).
  2. In `fase_5/script_hanif.ipynb`, the transformation code maps `idrapor` (which has string values like `'R005457'`) directly to `id_rapor_siswa` in both `rapor_siswa` and `rapor_siswa_file`.
  3. When inserting `'R005457'` into the target `bigint` columns, MySQL fails to cast the string to an integer, resulting in NULL values (or 0) for the foreign key.
* **Recommendation:**
  * Report these findings to the database administrator or integration coordinator. The database table `rapor_siswa` must either maintain the original string PKs, or the integration coordinator needs to provide a mapping table to translate string IDs to the newly generated bigint auto-increment IDs.

---

## 🛠️ 3. Execution & Validation Plan
1. Apply changes programmatically to `fase_3/script_hanif.ipynb` and `fase_4/script_hanif.ipynb`.
2. Run notebook cells and generate new Pickle files (`fase_3_hanif.pkl`, `fase_4_hanif.pkl`).
3. Document audit findings for Fase 5 in the project logs.
