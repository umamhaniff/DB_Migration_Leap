# Calon Siswa & Sub-Tabel Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrasi data lengkap calon siswa dan 6 sub-tabel terkait dari database lama ke database baru dengan pemetaan ID dan lookup prospek.

**Architecture:** Menggunakan pendekatan Master Join DataFrame untuk menggabungkan 5 tabel sumber, melakukan pembersihan data di memori, dan melakukan insert batch ke 7 tabel target.

**Tech Stack:** Python, Pandas, MySQL Connector.

---

### Task 1: Master Data Preparation & Joining

**Files:**
- Modify: `fase_3/script_cimut.ipynb` (Append new cell)

- [ ] **Step 1: Create Master Join Cell**
  Gabungkan `form_calon` dengan 4 tabel detilnya menggunakan `idcalon`.

```python
# Cell: Master Join
df_calon = df_old['form_calon'].copy()
df_detil1 = df_old['form_calon_detil1'].copy()
df_detil2 = df_old['form_calon_detil2'].copy()
df_detil3 = df_old['form_calon_detil3'].copy()
df_detil4 = df_old['form_calon_detil4'].copy()

# Join all
df_master = df_calon.merge(df_detil1, on='idcalon', how='left') \
                  .merge(df_detil2, on='idcalon', how='left', suffixes=('', '_d2')) \
                  .merge(df_detil3, on='idcalon', how='left', suffixes=('', '_d3')) \
                  .merge(df_detil4, on='idcalon', how='left', suffixes=('', '_d4'))

print(f"Total Master Data: {len(df_master)} rows")
```

- [ ] **Step 2: Run Cell and Verify**
  Pastikan jumlah baris sesuai dengan `form_calon`.

---

### Task 2: Data Cleaning & Regional Names

**Files:**
- Modify: `fase_3/script_cimut.ipynb` (Append new cell)

- [ ] **Step 1: Extract Numeric ID & Map Regional Names**
  Ekstrak ID dari `C00000017` -> `17` dan join nama wilayah.

```python
# Cell: Cleaning & Regional
import re

def extract_id(id_str):
    if pd.isna(id_str): return None
    nums = re.findall(r'\d+', str(id_str))
    return int(nums[0]) if nums else None

df_master['id_calon_new'] = df_master['idcalon'].apply(extract_id)

# Map Regional Names (String only)
prov_map = df_old['provinsi'].set_index('idprovinsi')['nama'].to_dict()
kab_map = df_old['kabupaten'].set_index('idkabupaten')['name'].to_dict()

df_master['nama_provinsi'] = df_master['provinsi'].map(prov_map)
df_master['nama_kabupaten'] = df_master['kabupaten'].map(kab_map)

print(f"Sample Cleaned ID: {df_master['id_calon_new'].head(3).tolist()}")
```

---

### Task 3: Prospect Lookup Matching

**Files:**
- Modify: `fase_3/script_cimut.ipynb` (Append new cell)

- [ ] **Step 1: Match with df_kontak_prospek_ready**
  Gunakan nama dan email untuk mencari `id_kontak_prospek`.

```python
# Cell: Prospect Lookup
# Asumsi df_kontak_prospek_ready sudah ada di memory
if 'df_kontak_prospek_ready' in locals():
    # Buat mapping (nama, email) -> id_kontak_prospek
    prospek_map = df_kontak_prospek_ready.set_index(['nama_penanya', 'email'])['id_kontak_prospek'].to_dict()
    
    def lookup_prospek(row):
        key = (row['fullName'], row['email'])
        return prospek_map.get(key)

    df_master['id_kontak_prospek_new'] = df_master.apply(lookup_prospek, axis=1)
else:
    print("Warning: df_kontak_prospek_ready not found. Using NULL.")
    df_master['id_kontak_prospek_new'] = None

print(f"Matched Prospects: {df_master['id_kontak_prospek_new'].notna().sum()}")
```

---

### Task 4: Insert to `calon_siswa` (Main Table)

**Files:**
- Modify: `fase_3/script_cimut.ipynb` (Append new cell)

- [ ] **Step 1: Prepare and Insert `calon_siswa`**

```python
# Cell: Insert calon_siswa
data_calon = []
for _, row in df_master.iterrows():
    data_calon.append({
        'id_calon': row['id_calon_new'],
        'nama_lengkap': row['fullName'],
        'id_kontak_prospek': row['id_kontak_prospek_new'],
        'nama_panggilan': row['nickName'],
        'email': row['email'],
        'wa_siswa': row['phone1'],
        'wa_ortu': row['phone2'],
        'sumber_lead': row['info'],
        'status_pipeline': row['status'],
        'catatan_awal_fo': row['catatanadmin'],
        'created_at': row['created_at'] if pd.notna(row['created_at']) else datetime.datetime.now(),
        'updated_at': datetime.datetime.now()
    })

# Batch Insert (Helper function assumed available in notebook)
# insert_to_db('calon_siswa', data_calon)
```

---

### Task 5: Insert Sub-Tables (Akademik & Ortu)

**Files:**
- Modify: `fase_3/script_cimut.ipynb` (Append new cell)

- [ ] **Step 1: Insert `calon_siswa_akademik`**
- [ ] **Step 2: Insert `calon_siswa_ortu`**

```python
# Cell: Insert Akademik & Ortu
data_akademik = []
data_ortu = []

for _, row in df_master.iterrows():
    # Akademik
    data_akademik.append({
        'id_calon': row['id_calon_new'],
        'nama_sekolah': row['schoolName'],
        'jenjang_kelas_1': row['classLevel'],
        'kurikulum_sekolah': row['curriculum'] if row['curriculum'] in ['NASIONAL', 'CAMBRIDGE', 'LAINNYA'] else 'LAINNYA',
        'riwayat_les': row['exp'],
        'kesulitan_belajar': row['diagnostic']
    })
    
    # Ortu
    data_ortu.append({
        'id_calon': row['id_calon_new'],
        'nama_ayah': row['nama_ortu'], # Data ortu di detil1 campur
        'pekerjaan_ayah': 'Lainnya',
        'nama_ibu': row['nama_ortu']
    })

# insert_to_db('calon_siswa_akademik', data_akademik)
# insert_to_db('calon_siswa_ortu', data_ortu)
```

---

### Task 6: Insert Sub-Tables (Bayar & Jadwal)

**Files:**
- Modify: `fase_3/script_cimut.ipynb` (Append new cell)

- [ ] **Step 1: Insert `calon_siswa_bayar`**
- [ ] **Step 2: Insert `calon_siswa_jadwal`**

```python
# Cell: Insert Bayar & Jadwal
data_bayar = []
data_jadwal = []

for _, row in df_master.iterrows():
    # Bayar
    data_bayar.append({
        'id_calon': row['id_calon_new'],
        'nomor_invoice': row['nomor_invoice'],
        'bank_pembayaran': row['bank'],
        'bulan_mulai_belajar': row['bulan_masuk'],
        'status_siswa': row['status_siswa'] if row['status_siswa'] in ['Waiting for payment', 'Canceled', 'Done'] else 'Done'
    })
    
    # Jadwal
    data_jadwal.append({
        'id_calon': row['id_calon_new'],
        'tanggal_pembayaran': row['tanggal_pembayaran']
    })

# insert_to_db('calon_siswa_bayar', data_bayar)
# insert_to_db('calon_siswa_jadwal', data_jadwal)
```

---

### Task 7: Insert Sub-Tables (Proses & Kursus)

**Files:**
- Modify: `fase_3/script_cimut.ipynb` (Append new cell)

- [ ] **Step 1: Insert `calon_siswa_proses`**
- [ ] **Step 2: Insert `calon_siswa_kursus`**

```python
# Cell: Insert Proses & Kursus
data_proses = []
data_kursus = []

for _, row in df_master.iterrows():
    # Proses
    data_proses.append({
        'id_calon': row['id_calon_new'],
        'admin_pengontak': row['PIC'],
        'hasil_trial': row['laporan_trial'],
        'status_siswa': row['status_siswa'] if row['status_siswa'] in ['On-progress','Done','Canceled','Follow Up'] else 'Done',
        'catatan_admin': row['catatanadmin']
    })
    
    # Kursus
    data_kursus.append({
        'id_calon': row['id_calon_new'],
        'nama_kursus': row['program']
    })

# insert_to_db('calon_siswa_proses', data_proses)
# insert_to_db('calon_siswa_kursus', data_kursus)
```

---

### Task 8: Validation & Cleanup

**Files:**
- Modify: `fase_3/script_cimut.ipynb` (Append final cell)

- [ ] **Step 1: Row Count Verification**
- [ ] **Step 2: Transaction Commit**

```python
# Cell: Validation
print("Migration Summary:")
# query counts from db_new
# print results
# db_new.commit()
```
