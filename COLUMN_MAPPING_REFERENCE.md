# 📊 DATABASE COLUMN MAPPING REFERENCE

Database lama: `dataleap_v5_example` (108 tabel)  
Database baru: `dataleap_v5_migration` (104 tabel)

---

## 📋 Pembagian Fase & Personel

### 🟢 FASE 1: Persiapan Master Data (PARALEL)

**Cimut - Sistem & Wilayah Dasar:**
- users, divisions, shift_kerja, admin_sarpras, sop_kategori, provinsi, web_berita, web_statistik

**Afrida - Akademik Dasar:**
- kursus, level, sesi, libur, topik_diskusi, kursus_level, kursus_libur

**Hanif - Role & Sistem:**
- roles, permissions, role_has_permissions, busdev_bidang, syarat_resign, ttd, tag_siswa_keluar

---

### 🔵 FASE 2: Pendataan SDM & Wilayah Detail

**Cimut - SDM & Relasi:**
- karyawan, keluarga_karyawan, bidang_kategori, bidang_link

**Afrida - Periode & Wilayah:**
- periode, parameter_nilai, kabupaten, kecamatan

**Hanif - Divisi & Wilayah:**
- division_user, model_has_roles, model_has_permissions, kelurahan

---

### 🟡 FASE 3: Operasional, CRM & Pendaftaran

**Cimut - CRM & Aset (FOKUS UTAMA):**
- kontak_prospek, calon_siswa, calon_siswa_akademik, calon_siswa_ortu, calon_siswa_bayar, calon_siswa_jadwal, calon_siswa_kursus, calon_siswa_proses, calon_siswa_status_logs, peminjaman, pengadaan, problem

**Afrida - Dokumentasi & Surat:**
- sop, surat_keluar, verifikasi_surat_keluar, surat_tugas, surat_tugas_anggota

**Hanif - Rekrutmen & Mitra:**
- pengajuan_karyawan, histori_pengajuan, pelamar, pelamar_kerja, pelamar_sekolah, pelamar_kursus, progres_pelamar, rekrutmen_pelamar

---

### 🔴 FASE 4: Penjadwalan & Siswa Aktif

**Cimut - Kehadiran & Izin:**
- izin_karyawan, verifikasi_izin, absensi, verifikasi_absensi, karyawan_resign

**Afrida - Jadwal & Catatan (FOKUS UTAMA):**
- jadwal, jadwal_hari, jadwal_detail, jadwal_pengajar, jadwal_siswa, catatan_kelas, catatan_kelas_tag, catatan_mingguan

**Hanif - Siswa & Mitra (FOKUS UTAMA):**
- siswa, kursus_siswa, siswa_keluar, mitra, mitra_progres, kemitraan_verifikator, siswa_mitra, siswa_mitra_keluar

---

### 🟣 FASE 5: Penilaian & Finalisasi (SELESAI)

**Cimut - System Logs & Config:**
- activity_log, log_aktivitas, jadwal_detail_logs, password_reset_tokens

**Afrida - Presensi & Catatan Siswa:**
- presensi_siswa, catatan_siswa, followup_cs

**Hanif - Rapor & Penilaian (FOKUS UTAMA):**
- rapor_format, rapor_format_sub, rapor_format_formula, rapor_format_formula_sub, rapor_level_config, rapor_sub_level, rapor_siswa, rapor_siswa_file, rapor_lacak

---

## 📊 COLUMN MAPPING BY PHASE

---

## FASE 1: Persiapan Master Data (PARALEL)
```
DB Lama (dataleap_v5_example)          →  DB Baru (dataleap_v5_migration)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
id                                     →  id_provinsi
name                                   →  nama_provinsi
code (jika ada)                         →  kode_provinsi
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: KABUPATEN
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
id                                     →  id_kabupaten
name                                   →  nama_kabupaten
provinsi_id                            →  id_provinsi (FK)
code (jika ada)                         →  kode_kabupaten
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: KECAMATAN
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
id                                     →  id_kecamatan
name                                   →  nama_kecamatan
kabupaten_id                           →  id_kabupaten (FK)
code (jika ada)                         →  kode_kecamatan
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: KELURAHAN
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
id                                     →  id_kelurahan
name                                   →  nama_kelurahan
kecamatan_id                           →  id_kecamatan (FK)
code (jika ada)                         →  kode_kelurahan
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: KURSUS (Akademik Dasar)
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idkursus / id                          →  id_kursus
namakursus / name                      →  nama_kursus
kurjenjang / jenjang_kursus            →  jenjang_kursus
kurkurikulum / kurikulum               →  kurikulum_kursus
status / is_active                     →  status_kursus
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: LEVEL
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idlevel / id                           →  id_level
namalevel / name                       →  nama_level
urutan / sequence                      →  urutan_level
deskripsi / description                →  deskripsi_level
created_at                             →  created_at
updated_at                             →  updated_at
```

---

## FASE 2: Pendataan SDM & Wilayah Detail

### Tabel: USERS
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idusers / id                           →  id_user
email                                  →  email
password                               →  password
name                                   →  nama_lengkap
username                               →  username
status / is_active                     →  status_user
email_verified_at                      →  email_verified_at
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: KARYAWAN
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idkaryawan / id                        →  id_karyawan
idusers                                →  id_user (FK)
nama_lengkap                           →  nama_lengkap
nik                                    →  nik
jenis_kelamin                          →  jenis_kelamin
tempat_lahir                           →  tempat_lahir
tanggal_lahir                          →  tanggal_lahir
alamat_lengkap                         →  alamat_lengkap
no_telepon                             →  no_telepon
id_jabatan                             →  id_jabatan (FK)
id_divisi                              →  id_division (FK)
status_karyawan                        →  status_karyawan
tanggal_masuk                          →  tanggal_masuk
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: ABSENSI
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idabsensi / id                         →  id_absensi
idkaryawan                             →  id_karyawan (FK)
tanggal                                →  tanggal
scanmasuk / jam_masuk                  →  jam_masuk
scankeluar / jam_keluar                →  jam_keluar
status                                 →  status_absensi
note1 / catatan_masuk                  →  catatan_masuk
note2 / catatan_keluar                 →  catatan_keluar
created_at                             →  created_at
```

---

## FASE 3: Operasional, CRM & Pendaftaran

### Tabel: CALON_SISWA (CRM)
```
DB Lama (calon_siswa* tables)          →  DB Baru (calon_siswa)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idcalon / id                           →  id_calon
idpendkursus                           →  id_kontak_prospek (FK)
nama                                   →  nama_lengkap
email                                  →  email
tlp                                    →  wa_siswa
status                                 →  status_pipeline
created_at                             →  created_at
updated_at                             →  updated_at
(Lanjutkan mapping untuk sub-table)
```

### Tabel: PELAMAR (Rekrutmen)
```
DB Lama (pelamar*)                     →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idpelamar / id                         →  id_pelamar
nama                                   →  nama_lengkap
email                                  →  email
no_hp / telepon                        →  no_telepon
status                                 →  status_pelamar
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: MITRA
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idmitra / id                           →  id_mitra
nama_mitra                             →  nama_mitra
alamat_mitra                           →  alamat_mitra
no_telepon                             →  no_telepon
email                                  →  email
pic_mitra                              →  pic_mitra
status_mitra                           →  status_mitra
created_at                             →  created_at
updated_at                             →  updated_at
```

---

## FASE 4: Penjadwalan & Siswa Aktif

### Tabel: SISWA
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idsiswa / id                           →  id_siswa
idcalon / id_calon                     →  id_calon (FK)
namasiswa / nama_lengkap               →  nama_lengkap
email                                  →  email
no_hp / telepon                        →  no_telepon
status_siswa                           →  status_siswa
tanggal_daftar                         →  tanggal_daftar
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: JADWAL
```
DB Lama                                →  DB Baru
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idjadwal / id                          →  id_jadwal
idkursus                               →  id_kursus (FK)
idperiode / id_periode                 →  id_periode (FK)
idlevel                                →  id_level (FK)
tglmulai / tanggal_mulai               →  tanggal_mulai
tglselesai / tanggal_selesai           →  tanggal_selesai
status_jadwal                          →  status_jadwal
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: JADWAL_DETAIL
```
DB Lama (jadwal_detil)                 →  DB Baru (jadwal_detail)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idjadwaldetil / id                     →  id_jadwal_detail
idjadwal                               →  id_jadwal (FK)
hari / day                             →  hari_pembelajaran
jam_mulai                              →  jam_mulai
jam_selesai                            →  jam_selesai
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: RAPOR_SISWA
```
DB Lama (rapor)                        →  DB Baru (rapor_siswa)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idrapor / id                           →  id_rapor_siswa
idsiswa                                →  id_siswa (FK)
idjadwal                               →  id_jadwal (FK)
nilai_akhir / final_score              →  nilai_akhir
grade                                  →  grade
created_at                             →  created_at
updated_at                             →  updated_at
```

---

## FASE 5: Penilaian & Finalisasi (SELESAI)

### Tabel: PRESENSI_SISWA
```
DB Lama (presensi_siswa)               →  DB Baru (presensi_siswa)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idpresensi / id                        →  id_presensi_siswa
idjadwaldetil                          →  id_jadwal_detail (FK)
idsiswa                                →  id_siswa (FK)
tanggal                                →  tanggal_presensi
status_presensi                        →  status_presensi
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: RAPOR_FORMAT
```
DB Lama (format_rapor)                 →  DB Baru (rapor_format)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idformat_rapor / id                    →  id_rapor_format
idpendkursus                           →  id_kursus (FK)
title / nama_format                    →  nama_format_rapor
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: RAPOR_SISWA
```
DB Lama (rapor)                        →  DB Baru (rapor_siswa)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idrapor / id                           →  id_rapor_siswa
idsiswa                                →  id_siswa (FK)
idjadwal                               →  id_jadwal (FK)
nilai_akhir / final_score              →  nilai_akhir
grade                                  →  grade
created_at                             →  created_at
updated_at                             →  updated_at
```

### Tabel: ACTIVITY_LOG
```
DB Lama (log)                          →  DB Baru (activity_log)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
idlog / id                             →  id
log_name                               →  log_name
description                           →  description
subject_type                          →  subject_type
subject_id                            →  subject_id
causer_id                             →  causer_id
properties                            →  properties (JSON)
created_at                            →  created_at
updated_at                            →  updated_at
```

---

## ⚠️ PENTING: Notes untuk Transform

1. **Date Format**: Pastikan format date/datetime sama
2. **NULL Values**: Handle NULL untuk kolom yang di-map
3. **Foreign Keys**: Sesuaikan ID reference antara lama dan baru
4. **Status Mapping**: Konversi status string jika berbeda format
5. **Unicode**: Pastikan encoding UTF-8 untuk data non-ASCII
6. **Decimal/Float**: Hati-hati dengan precision pada angka

---

## 🔍 Query Template untuk Transform

```python
# CONTOH: Transform data kabupaten
kabupaten_transformed = []
for row in kabupaten_old:
    transformed = {
        'id_kabupaten': row.get('id'),              # Direct mapping
        'nama_kabupaten': row.get('name'),          # Rename column
        'id_provinsi': row.get('provinsi_id'),      # Foreign key reference
        'kode_kabupaten': row.get('code'),          # Optional field
        'created_at': row.get('created_at') or datetime.now(),  # Default if NULL
        'updated_at': datetime.now()                 # Current timestamp
    }
    kabupaten_transformed.append(transformed)

# CONTOH: Insert ke DB Baru
insert_query = """INSERT INTO kabupaten 
    (id_kabupaten, nama_kabupaten, id_provinsi, kode_kabupaten, created_at, updated_at) 
    VALUES (%s, %s, %s, %s, %s, %s)"""

for record in kabupaten_transformed:
    cursor_new.execute(insert_query, (
        record['id_kabupaten'],
        record['nama_kabupaten'],
        record['id_provinsi'],
        record.get('kode_kabupaten'),
        record['created_at'],
        record['updated_at']
    ))
db_new.commit()
```

---
## 🔍 Query Template untuk Transform

```python
# CONTOH: Transform data kabupaten
kabupaten_transformed = []
for row in kabupaten_old:
    transformed = {
        'id_kabupaten': row.get('id'),              # Direct mapping
        'nama_kabupaten': row.get('name'),          # Rename column
        'id_provinsi': row.get('provinsi_id'),      # Foreign key reference
        'kode_kabupaten': row.get('code'),          # Optional field
        'created_at': row.get('created_at') or datetime.now(),  # Default if NULL
        'updated_at': datetime.now()                 # Current timestamp
    }
    kabupaten_transformed.append(transformed)

# CONTOH: Insert ke DB Baru
insert_query = """INSERT INTO kabupaten 
    (id_kabupaten, nama_kabupaten, id_provinsi, kode_kabupaten, created_at, updated_at) 
    VALUES (%s, %s, %s, %s, %s, %s)"""

for record in kabupaten_transformed:
    cursor_new.execute(insert_query, (
        record['id_kabupaten'],
        record['nama_kabupaten'],
        record['id_provinsi'],
        record.get('kode_kabupaten'),
        record['created_at'],
        record['updated_at']
    ))
db_new.commit()
```

---

## 📌 Catatan Fase 5 (Finalisasi)

**Fase 5 adalah fase terakhir yang meliputi:**
- **Cimut**: System logs & configuration (4 tabel)
- **Afrida**: Student attendance & notes (3 tabel)
- **Hanif**: Report cards & assessment (9 tabel) - **FOKUS UTAMA**

Pastikan:
1. Semua data dari fase 1-4 sudah tersimpan dengan baik
2. Foreign key consistency sudah terjaga
3. Rapor (report) punya semua dependency terpenuhi sebelum di-insert
4. Activity log harus di-populate terakhir (untuk tracking lengkap)

---

*Reference Guide for DB Migration Column Mapping*  
*Version 2.0 - 2026-04-22*  
*Updated: 5 Phase Migration with Personnel Assignment*
