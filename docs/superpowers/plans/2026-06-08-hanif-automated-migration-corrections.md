# Automated Migration Corrections Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Automate Phase 3 and Phase 4 database migration mapping fixes for Hanif's scripts, including date range parsing, applicant name-matching, exit reason tag mappings, automatic student-course mapping, integer ID conversions, and CSV debugging exports.

**Architecture:** Programmatically patch Jupyter Notebooks (`fase_3/script_hanif.ipynb`, `fase_4/script_hanif.ipynb`, `fase_5/script_hanif.ipynb`) using `config.gemini/apply_migration_updates.py`. Insert ID conversion logic in `fase_4/insert_handler.ipynb` for other team members' pickles.

**Tech Stack:** Python, Pandas, Regex, JSON, Jupyter Notebooks

---

### Task 1: Update Notebook Patching Script (Fase 3 & Fase 4 & Fase 5)

**Files:**
- Modify: `config.gemini/apply_migration_updates.py`

- [ ] **Step 1: Replace Fase 3 patch definitions in `apply_migration_updates.py`**
  Modify `patch_fase_3()` inside `config.gemini/apply_migration_updates.py` to:
  1. Define a robust `parse_date` helper that fixes the regex double-escaping bug (use `\b` instead of `\\\\b`) and parses date ranges by splitting with `-` and taking the last part.
  2. Map `idusers` in child tables `pekerjaan`/`pendidikan`/`kursus` to the new `id_pelamar` integer by fetching `users` from `db_old` and performing advanced name normalization (lowercased, space-free, degree/title removal) and email matching against `pelamar`.
  3. Include a CSV export cell at the end of the notebook to output transformed tables to `extract/cek_csv/`.

- [ ] **Step 2: Replace Fase 4 patch definitions in `apply_migration_updates.py`**
  Modify `patch_fase_4()` inside `config.gemini/apply_migration_updates.py` to:
  1. Convert `id_siswa` in `siswa` and `siswa_keluar` to integer via `extract_int`.
  2. Convert `id_sm` in `siswa_mitra` and `siswa_mitra_keluar` to integer via `extract_int`.
  3. Replace `siswa_keluar`'s `id_tag_keluar` heuristic by fetching `siswa_keluar_tag` from `db_old` and mapping `idsiswa` / `idsiswa_keluar` to the actual `idtag` numbers (1-11), defaulting to `8` (LAINNYA) if unmatched.
  4. Replace `kursus_siswa` initialization with a join of `siswa`, `jadwal_siswa`, and `jadwal` in `db_old` to automatically map B2C students to their courses, start dates, and study methods.
  5. Include a CSV export cell at the end of the notebook to output transformed tables to `extract/cek_csv/`.

- [ ] **Step 3: Replace Fase 5 patch definitions in `apply_migration_updates.py`**
  Modify `patch_fase_5()` inside `config.gemini/apply_migration_updates.py` to:
  1. Convert `id_siswa` to integer in `rapor_siswa` and `rapor_lacak` transformations using `extract_int`.
  2. Include a CSV export cell at the end of the notebook to output transformed tables to `extract/cek_csv/`.

---

### Task 2: Apply Patches and Regenerate Pickles

**Files:**
- Modify: `fase_3/script_hanif.ipynb` (via script)
- Modify: `fase_4/script_hanif.ipynb` (via script)
- Modify: `fase_5/script_hanif.ipynb` (via script)

- [ ] **Step 1: Execute `apply_migration_updates.py`**
  Run the patching script to update the JSON of all three notebooks.
  Command: `venv\Scripts\python config.gemini/apply_migration_updates.py`

- [ ] **Step 2: Regenerate pickles using `update_notebooks.py`**
  Run the update script to run the notebooks and output the updated pickles (`fase_3_hanif.pkl`, `fase_4_hanif.pkl`, `fase_5_hanif.pkl`).
  Command: `venv\Scripts\python update_notebooks.py`

---

### Task 3: Patch Global Insert Handler

**Files:**
- Modify: `fase_4/insert_handler.ipynb`

- [ ] **Step 1: Inject a global `id_siswa` and `id_sm` string-to-integer converter**
  Inject a cleaning step in `fase_4/insert_handler.ipynb` immediately after all pickles are loaded into `all_fase_4_data`. This step must check all DataFrames for `id_siswa`, `id_sm`, or `id_siswa_baru` columns and convert them to integer `Int64` if they are of type object/string. This preserves Afrida's and Cimut's child table relations without modifying their original notebooks.

---

### Task 4: Update Documentation Files

**Files:**
- Modify: `conductor/hanif_mapping.md`
- Modify: `conductor/laporan_kendala_migrasi.md`
- Modify: `conductor/catatan.md`

- [ ] **Step 1: Update `conductor/hanif_mapping.md`**
  Document the automatic mapping rules for `kursus_siswa` and name/email matching for `pelamar_kerja`/`pelamar_sekolah`/`pelamar_kursus`. Also update `id_siswa` to `Int64` types.

- [ ] **Step 2: Update `conductor/laporan_kendala_migrasi.md`**
  Document the resolution of the date range parsing bug, the `siswa_keluar` exit reasons mapping, and the `id_siswa` integer conversion.

- [ ] **Step 3: Update `conductor/catatan.md`**
  Update notes to indicate that `kursus_siswa` is now automated and PM manual input is no longer required unless overridden via `kursus_siswa_import.csv`.

---

### Task 5: Run Verification and Tests

**Files:**
- Test: `config.gemini/test_migration_pickles.py`

- [ ] **Step 1: Run pickle validation tests**
  Command: `venv\Scripts\python config.gemini/test_migration_pickles.py`
  Expected: All checks for Fase 3, Fase 4, and Fase 5 pickles pass.
