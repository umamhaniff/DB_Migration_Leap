# Hanif Mapping Updates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement applicant ID mapping changes in Fase 3, student registration status mapping in Fase 4, audit partner mapping completeness in Fase 4, and perform a code audit for report card file mapping in Fase 5.

**Architecture:** We will create a test script to validate the output pickle data formats. Then, we will create a python patching script to programmatically and safely update the Jupyter Notebook cells (avoiding JSON formatting issues). Finally, we will execute the notebooks and verify the output pickles.

**Tech Stack:** Python 3.10, Pandas, Jupyter (nbformat), Git.

---

### Task 1: Create Validation Test Script

**Files:**
- Create: `config.gemini/test_migration_pickles.py`

- [ ] **Step 1: Write the validation tests**
  Create a test script that validates the keys, columns, and types in `fase_3_hanif.pkl` and `fase_4_hanif.pkl`.

  ```python
  import os
  import pandas as pd

  def test_fase_3_pickle():
      path = "fase_3/fase_3_hanif.pkl"
      if not os.path.exists(path):
          print(f"Skipping {path} as it does not exist yet.")
          return
      data = pd.read_pickle(path)
      
      # 1. Check pelamar
      df_p = data.get("pelamar")
      assert df_p is not None, "pelamar table missing"
      assert "id_pelamar" in df_p.columns
      assert pd.api.types.is_integer_dtype(df_p["id_pelamar"])
      
      # 2. Check child tables
      child_tables = ["pelamar_kerja", "pelamar_sekolah", "pelamar_kursus", "progres_pelamar", "rekrutmen_pelamar"]
      for t in child_tables:
          df_c = data.get(t)
          assert df_c is not None, f"{t} table missing"
          assert "id_pelamar" in df_c.columns
          assert pd.api.types.is_integer_dtype(df_c["id_pelamar"]) or df_c["id_pelamar"].dtype == "Int64"
      print("✓ Fase 3 Pickle validation passed successfully!")

  def test_fase_4_pickle():
      path = "fase_4/fase_4_hanif.pkl"
      if not os.path.exists(path):
          print(f"Skipping {path} as it does not exist yet.")
          return
      data = pd.read_pickle(path)
      
      # 1. Check siswa
      df_s = data.get("siswa")
      assert df_s is not None, "siswa table missing"
      assert "status_pendaftaran" in df_s.columns
      assert "status_aktif" not in df_s.columns
      assert "status_lulus_siswa" not in df_s.columns
      print("✓ Fase 4 Pickle validation passed successfully!")

  if __name__ == "__main__":
      test_fase_3_pickle()
      test_fase_4_pickle()
  ```

- [ ] **Step 2: Run test to verify it prints info**
  Run: `python config.gemini/test_migration_pickles.py`
  Expected: Prints "Skipping..." since the updated pickles are not generated yet.

- [ ] **Step 3: Commit**
  ```bash
  git add config.gemini/test_migration_pickles.py
  git commit -m "test: add validation tests for migration pickles"
  ```

---

### Task 2: Create Safe Notebook Patching Script

**Files:**
- Create: `config.gemini/apply_migration_updates.py`

- [ ] **Step 1: Write the patching script**
  Create a script that reads, parses, and safely modifies the notebook JSON content.

  ```python
  import json
  import os

  def patch_fase_3():
      path = "fase_3/script_hanif.ipynb"
      if not os.path.exists(path):
          print(f"File {path} not found.")
          return
      with open(path, "r", encoding="utf-8") as f:
          nb = json.load(f)

      for cell in nb["cells"]:
          if cell["cell_type"] == "code" and "# 3. pelamar -> pelamar" in "".join(cell["source"]):
              source = "".join(cell["source"])
              
              # Replace Pelamar transformation logic to generate integer IDs
              old_pelamar_code = """    # 3. pelamar -> pelamar
      if 'pelamar' in raw_data:
          df = pd.DataFrame(raw_data['pelamar'])
          df['tempat_lahir'] = df['ttl'].apply(extract_place)
          df['tanggal_lahir'] = df['ttl'].apply(extract_date).apply(parse_date)
          
          # enum & data cleaning
          # mapping.md: "Lajang","Belum","Single","x" -> "Belum Menikah"
          def map_nikah(x):
              val = str(x).strip().lower()
              if val in ['menikah', 'nikah', 'kawin']: return 'Menikah'
              if val in ['lajang', 'belum', 'single', 'x', 'none', 'nan', '', '0']: return 'Belum Menikah'
              return 'Belum Menikah'
          
          df['status_pernikahan'] = df['statusnikah'].apply(map_nikah)
          
          # mapping.md: enum('Pernah','Tidak Pernah'); "Ya, Pernah" jd "Pernah"
          df['penggunaan_laptop'] = df['gunalaptop'].apply(lambda x: 'Pernah' if str(x).strip().lower() in ['pernah', 'ya, pernah', 'ya'] else 'Tidak Pernah')
          df['gaji'] = df['gaji'].apply(clean_currency)
          
          mapping = {
              'idpelamar': 'id_pelamar', 'idpengajuan': 'id_pengajuan', 'email': 'email_pelamar',"""
              
              new_pelamar_code = """    # 3. pelamar -> pelamar
      if 'pelamar' in raw_data:
          df = pd.DataFrame(raw_data['pelamar'])
          df['tempat_lahir'] = df['ttl'].apply(extract_place)
          df['tanggal_lahir'] = df['ttl'].apply(extract_date).apply(parse_date)
          
          # enum & data cleaning
          # mapping.md: "Lajang","Belum","Single","x" -> "Belum Menikah"
          def map_nikah(x):
              val = str(x).strip().lower()
              if val in ['menikah', 'nikah', 'kawin']: return 'Menikah'
              if val in ['lajang', 'belum', 'single', 'x', 'none', 'nan', '', '0']: return 'Belum Menikah'
              return 'Belum Menikah'
          
          df['status_pernikahan'] = df['statusnikah'].apply(map_nikah)
          
          # mapping.md: enum('Pernah','Tidak Pernah'); "Ya, Pernah" jd "Pernah"
          df['penggunaan_laptop'] = df['gunalaptop'].apply(lambda x: 'Pernah' if str(x).strip().lower() in ['pernah', 'ya, pernah', 'ya'] else 'Tidak Pernah')
          df['gaji'] = df['gaji'].apply(clean_currency)
          
          # Generate integer ID auto-increment mapping
          df = df.reset_index()
          df['id_pelamar_new'] = df['index'] + 1
          pelamar_id_map = dict(zip(df['idpelamar'], df['id_pelamar_new']))
          df['id_pelamar'] = df['id_pelamar_new']
          
          mapping = {
              'id_pelamar': 'id_pelamar', 'idpengajuan': 'id_pengajuan', 'email': 'email_pelamar',"""
              
              source = source.replace(old_pelamar_code, new_pelamar_code)

              # Replace child tables ID mapping logic
              old_child_code = """    # 4. pekerjaan -> pelamar_kerja
      if 'pekerjaan' in raw_data:
          df = pd.DataFrame(raw_data['pekerjaan'])
          mapping = {
              'idpekerjaan': 'id_pelamar_kerja', 'idusers': 'id_pelamar',
              'namaperusahaan': 'nama_perusahaan', 'periode': 'periode', 'jabatan': 'jabatan',
              'jobdesk': 'deskripsi_kerja'
          }
          transformed_dfs['pelamar_kerja'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
      
      # 5. pendidikan -> pelamar_sekolah
      if 'pendidikan' in raw_data:
          df = pd.DataFrame(raw_data['pendidikan'])
          df['tahun'] = df['tahun'].apply(extract_latest_year)
          df['ipk'] = df['ipk'].apply(clean_ipk)
          mapping = {
              'idpendidikan': 'id_pelamar_sekolah', 'idusers': 'id_pelamar',
              'sekolah': 'nama_sekolah', 'jenjang': 'jenjang', 'prodi': 'prodi',
              'tahun': 'tahun_lulus', 'ipk': 'ipk', 'organisasi': 'organisasi'
          }
          transformed_dfs['pelamar_sekolah'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
      
      # 6. kursus -> pelamar_kursus
      if 'kursus' in raw_data:
          df = pd.DataFrame(raw_data['kursus'])
          df['tanggal'] = df['tanggal'].apply(parse_date)
          mapping = {
              'idkursus': 'id_pelamar_kursus', 'idusers': 'id_pelamar',
              'nama': 'nama_kursus', 'tanggal': 'tanggal', 'deskripsi': 'deskripsi',
              'lokasi': 'lokasi', 'nosertifikat': 'nomor_sertifikat'
          }
          transformed_dfs['pelamar_kursus'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
      
      # 7. pelamar_note -> progres_pelamar
      if 'pelamar_note' in raw_data:
          df = pd.DataFrame(raw_data['pelamar_note'])
          df['status'] = df['status'].replace('baru', 'Baru')
          mapping = {
              'idnote': 'id_progres_pelamar', 'idpelamar': 'id_pelamar',
              'idusers': 'id_user', 'status': 'status_progres_pelamar',
              'note': 'catatan', 'link': 'tautan_file', 'pertanyaan': 'pertanyaan',
              'created_at': 'created_at'
          }
          transformed_dfs['progres_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
      
      # 8. pelamar_users -> rekrutmen_pelamar
      if 'pelamar_users' in raw_data:
          df = pd.DataFrame(raw_data['pelamar_users'])
          mapping = {
              'idassign': 'id_rekrutmen', 'idpelamar': 'id_pelamar', 'idusers': 'id_user'
          }
          transformed_dfs['rekrutmen_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))"""

              new_child_code = """    # 4. pekerjaan -> pelamar_kerja
      if 'pekerjaan' in raw_data:
          df = pd.DataFrame(raw_data['pekerjaan'])
          df['id_pelamar'] = df['idusers'].map(pelamar_id_map).astype('Int64')
          mapping = {
              'idpekerjaan': 'id_pelamar_kerja', 'id_pelamar': 'id_pelamar',
              'namaperusahaan': 'nama_perusahaan', 'periode': 'periode', 'jabatan': 'jabatan',
              'jobdesk': 'deskripsi_kerja'
          }
          transformed_dfs['pelamar_kerja'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
      
      # 5. pendidikan -> pelamar_sekolah
      if 'pendidikan' in raw_data:
          df = pd.DataFrame(raw_data['pendidikan'])
          df['tahun'] = df['tahun'].apply(extract_latest_year)
          df['ipk'] = df['ipk'].apply(clean_ipk)
          df['id_pelamar'] = df['idusers'].map(pelamar_id_map).astype('Int64')
          mapping = {
              'idpendidikan': 'id_pelamar_sekolah', 'id_pelamar': 'id_pelamar',
              'sekolah': 'nama_sekolah', 'jenjang': 'jenjang', 'prodi': 'prodi',
              'tahun': 'tahun_lulus', 'ipk': 'ipk', 'organisasi': 'organisasi'
          }
          transformed_dfs['pelamar_sekolah'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
      
      # 6. kursus -> pelamar_kursus
      if 'kursus' in raw_data:
          df = pd.DataFrame(raw_data['kursus'])
          df['tanggal'] = df['tanggal'].apply(parse_date)
          df['id_pelamar'] = df['idusers'].map(pelamar_id_map).astype('Int64')
          mapping = {
              'idkursus': 'id_pelamar_kursus', 'id_pelamar': 'id_pelamar',
              'nama': 'nama_kursus', 'tanggal': 'tanggal', 'deskripsi': 'deskripsi',
              'lokasi': 'lokasi', 'nosertifikat': 'nomor_sertifikat'
          }
          transformed_dfs['pelamar_kursus'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
      
      # 7. pelamar_note -> progres_pelamar
      if 'pelamar_note' in raw_data:
          df = pd.DataFrame(raw_data['pelamar_note'])
          df['status'] = df['status'].replace('baru', 'Baru')
          df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
          mapping = {
              'idnote': 'id_progres_pelamar', 'id_pelamar': 'id_pelamar',
              'idusers': 'id_user', 'status': 'status_progres_pelamar',
              'note': 'catatan', 'link': 'tautan_file', 'pertanyaan': 'pertanyaan',
              'created_at': 'created_at'
          }
          transformed_dfs['progres_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))
      
      # 8. pelamar_users -> rekrutmen_pelamar
      if 'pelamar_users' in raw_data:
          df = pd.DataFrame(raw_data['pelamar_users'])
          df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
          mapping = {
              'idassign': 'id_rekrutmen', 'id_pelamar': 'id_pelamar', 'idusers': 'id_user'
          }
          transformed_dfs['rekrutmen_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))"""

              source = source.replace(old_child_code, new_child_code)
              cell["source"] = [line + "\n" for line in source.split("\n")]
              if cell["source"][-1] == "\n": cell["source"].pop()
              break

      with open(path, "w", encoding="utf-8") as f:
          json.dump(nb, f, indent=1)
      print("✓ Fase 3 notebook patched successfully!")

  def patch_fase_4():
      path = "fase_4/script_hanif.ipynb"
      if not os.path.exists(path):
          print(f"File {path} not found.")
          return
      with open(path, "r", encoding="utf-8") as f:
          nb = json.load(f)

      for cell in nb["cells"]:
          if cell["cell_type"] == "code" and "# 1. siswa -> siswa" in "".join(cell["source"]):
              source = "".join(cell["source"])
              
              # Replace mapping definition in siswa
              old_mapping = """        'kodepos': 'kode_pos', 'statussiswa': 'status_aktif', 'rekomen': 'rekomendasi',
          'info': 'sumber_info', 'pembayaran': 'metode_pembayaran', 'nama_ayah': 'nama_ayah',
          'pekerjaan_ayah': 'pekerjaan_ayah', 'jenjang_ayah': 'pendidikan_ayah', 
          'penghasilan_ayah': 'penghasilan_ayah', 'nama_ibu': 'nama_ibu', 'penghasilan_ibu': 'penghasilan_ibu',
          'jenjang_ibu': 'pendidikan_ibu', 'nama_wali': 'nama_wali', 'pekerjaan_wali': 'pekerjaan_wali',
          'jenjang_wali': 'pendidikan_wali', 'penghasilan_wali': 'penghasilan_wali',
          'wapeserta': 'wa_siswa', 'wawalmur': 'wa_ortu', 'waadmin': 'wa_administrasi',
          'sts_pengisian': 'status_pengisian', 'bukti': 'path_bukti_bayar', 'lulus': 'status_lulus_siswa',"""

              new_mapping = """        'kodepos': 'kode_pos', 'statussiswa': 'status_pendaftaran', 'rekomen': 'rekomendasi',
          'info': 'sumber_info', 'pembayaran': 'metode_pembayaran', 'nama_ayah': 'nama_ayah',
          'pekerjaan_ayah': 'pekerjaan_ayah', 'jenjang_ayah': 'pendidikan_ayah', 
          'penghasilan_ayah': 'penghasilan_ayah', 'nama_ibu': 'nama_ibu', 'penghasilan_ibu': 'penghasilan_ibu',
          'jenjang_ibu': 'pendidikan_ibu', 'nama_wali': 'nama_wali', 'pekerjaan_wali': 'pekerjaan_wali',
          'jenjang_wali': 'pendidikan_wali', 'penghasilan_wali': 'penghasilan_wali',
          'wapeserta': 'wa_siswa', 'wawalmur': 'wa_ortu', 'waadmin': 'wa_administrasi',
          'sts_pengisian': 'status_pengisian', 'bukti': 'path_bukti_bayar',"""

              source = source.replace(old_mapping, new_mapping)
              cell["source"] = [line + "\n" for line in source.split("\n")]
              if cell["source"][-1] == "\n": cell["source"].pop()
              break

      with open(path, "w", encoding="utf-8") as f:
          json.dump(nb, f, indent=1)
      print("✓ Fase 4 notebook patched successfully!")

  if __name__ == "__main__":
      patch_fase_3()
      patch_fase_4()
  ```

- [ ] **Step 2: Run patch to check if successful**
  Run: `python config.gemini/apply_migration_updates.py`
  Expected: Prints "✓ Fase 3 notebook patched successfully!" and "✓ Fase 4 notebook patched successfully!".

- [ ] **Step 3: Commit**
  ```bash
  git add config.gemini/apply_migration_updates.py
  git commit -m "feat: add notebook patching script"
  ```

---

### Task 3: Execute notebooks and verify Pickles

**Files:**
- Modify: `fase_3/script_hanif.ipynb` (run)
- Modify: `fase_4/script_hanif.ipynb` (run)

- [ ] **Step 1: Execute Fase 3 and Fase 4 Notebooks**
  Run `update_notebooks.py` first if needed to verify sync, then run the patched notebooks programmatically using a python wrapper or manual run.
  Run:
  ```bash
  jupyter nbconvert --to notebook --execute --inplace fase_3/script_hanif.ipynb
  jupyter nbconvert --to notebook --execute --inplace fase_4/script_hanif.ipynb
  ```

- [ ] **Step 2: Run validation tests**
  Run: `python config.gemini/test_migration_pickles.py`
  Expected: Prints:
  "✓ Fase 3 Pickle validation passed successfully!"
  "✓ Fase 4 Pickle validation passed successfully!"

- [ ] **Step 3: Commit**
  ```bash
  git add fase_3/fase_3_hanif.pkl fase_4/fase_4_hanif.pkl
  git commit -m "feat: regenerate migration pickles after mapping updates"
  ```

---

### Task 4: Audit Fase 5 Report Card File

**Files:**
- Create: `config.gemini/audit_fase_5.txt`

- [ ] **Step 1: Document the audit findings**
  Inspect `fase_5/script_hanif.ipynb` and database schemas. Write down findings in `config.gemini/audit_fase_5.txt`.

  File Content:
  ```text
  === FASET 5 AUDIT REPORT: RAPOR_SISWA_FILE ===
  
  1. Target Database Schema (dataleap_v5_migration):
     - Table: `rapor_siswa`
       PK: `id_rapor_siswa` (bigint auto-increment)
     - Table: `rapor_siswa_file`
       FK: `id_rapor_siswa` (bigint, references `rapor_siswa.id_rapor_siswa`)

  2. Problem Identified in script_hanif.ipynb:
     - The transformation code maps the old `idrapor` string (e.g., 'R005457') directly to the `id_rapor_siswa` column.
     - When this data is loaded using INSERT into the target database, MySQL fails to parse 'R005457' as a BIGINT.
     - As a result, the value is cast to NULL or 0 in the database, resulting in all values in `id_rapor_siswa` column being empty/NULL in the `rapor_siswa_file` table.

  3. Recommended Fix:
     - The integration coordinator must either change `rapor_siswa.id_rapor_siswa` to match the old string PKs, OR
     - Provide a mapping table at load-time to translate string IDs to the newly generated bigint auto-increment IDs.
  ```

- [ ] **Step 2: Commit**
  ```bash
  git add config.gemini/audit_fase_5.txt
  git commit -m "docs: add audit findings for Fase 5 report card files"
  ```
