# 📊 DATABASE COLUMN MAPPING REFERENCE

Database lama: `dataleap_v5_example` (108 tabel)  
Database baru: `dataleap_v5_migration` (104 tabel)

---

## FASE 1: Master & Wilayah

### Tabel: PROVINSI
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

## FASE 2: SDM & Karyawan

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

## FASE 3: CRM, Rekrutmen & Sarpras

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

## FASE 4: KBM & Rapor

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

*Reference Guide for DB Migration Column Mapping*  
*Version 1.0 - 2026-04-21*
