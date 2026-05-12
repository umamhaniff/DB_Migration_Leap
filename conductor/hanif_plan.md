# Hanif's Scripts Migration Plan

**Goal:** Resolve any potential issues in Hanif's migration scripts for Phase 3, 4, and 5 based on `hanif_mapping.md`. Ensure the logic is fully implemented and test the notebooks for runtime execution errors.

**Background & Motivation:**
The user requested to audit the column mapping implementation from `hanif_mapping.md` in `fase_3`, `fase_4`, and `fase_5` notebooks, and fix any potential issues. Static analysis shows that `update_notebooks.py` has already injected the mapping logic (e.g., date parsing, enum normalization, foreign key lookups). However, "potential issues" (masalah yang kemungkinan terjadi) usually surface as Pandas runtime errors (KeyError, TypeError) due to messy actual database values.

**Scope & Impact:**
- **Fase 3 (`script_hanif.ipynb`)**: CRM, Recruitment & Sarpras.
- **Fase 4 (`script_hanif.ipynb`)**: Students & Partners.
- **Fase 5 (`script_hanif.ipynb`)**: Grading & Finalization.

**Implementation Steps:**

- [ ] **Step 1: Execute & Debug Fase 3**
  - Run `fase_3/script_hanif.ipynb` via Python or `nbconvert`.
  - Verify that `extract_date`, `parse_date`, and `clean_currency` handle all existing data without throwing exceptions.
  - If errors occur, patch `fase_3/script_hanif.ipynb`.

- [ ] **Step 2: Execute & Debug Fase 4**
  - Run `fase_4/script_hanif.ipynb`.
  - Validate `detect_tag` and enum mappings (`agama`, `pekerjaan_ayah`, etc.).
  - Check if empty tables `siswa_mitra` and `siswa_mitra_keluar` cause any pipeline breaks downstream.
  - Fix any runtime errors.

- [ ] **Step 3: Execute & Debug Fase 5**
  - Run `fase_5/script_hanif.ipynb`.
  - Verify that the updated lookup logic (using `merge` instead of dictionary mapping for `rapor_siswa_file` and `rapor_lacak`) correctly joins the data.
  - Fix any runtime errors.

**Verification:**
After executing all three notebooks successfully, we will verify the resulting `.pkl` files are valid.
