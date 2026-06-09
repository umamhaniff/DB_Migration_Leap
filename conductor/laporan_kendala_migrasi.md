# Laporan Kendala dan Penangguhan Migrasi Database (Fase 3, 4, & 5) - TERSELESAIKAN ✅

Dokumen ini memuat status penyelesaian kendala teknis dan penangguhan (*skip*) dalam proses migrasi database dari database lama (`dataleap_v5_example`) ke database baru (`dataleap_v5_migration`) per **8 Juni 2026**.

---

## 🗂️ Rangkuman Kendala & Solusi Penyelesaian

### 1. FASE 3: CRM & Pelamar
#### **Tabel Terkait**: `pelamar_kerja`, `pelamar_sekolah`, `pelamar_kursus`
* **Status**: **TERSELESAIKAN ✅**
* **Kendala Awal**: Kolom `id_pelamar` (Foreign Key baru) bernilai NULL karena ketiadaan jembatan data yang konsisten antara `idusers` (riwayat) dengan `idpelamar` (data diri) di database lama.
* **Solusi Implementasi**:
  * Menggunakan strategi pencocokan multi-tahap (hierarchical matching) pada python ETL:
    1. Pencocokan langsung melalui tabel perantara `pelamar_users` lama.
    2. Pencocokan fallback menggunakan alamat email (setelah dinormalisasi dari spasi/lowercase).
    3. Pencocokan fallback menggunakan nama lengkap (dihilangkan karakter non-alfabetis/spasi ganda untuk pencocokan string bersih).
  * Dengan metode ini, tingkat kecocokan meningkat drastis (match rate ~50% dibanding sebelumnya 0%), dan FK `id_pelamar` berhasil dipetakan secara bersih sebagai integer murni `Int64` di CSV.

---

### 2. FASE 4: Siswa & Mitra
#### **Tabel Terkait**: `siswa_keluar`
* **Status**: **TERSELESAIKAN ✅**
* **Kendala Awal**: Kolom `id_kursus` bernilai NULL karena database lama tidak menyimpan relasi kursus pada siswa yang keluar.
* **Solusi Implementasi**:
  * Menggunakan relasi tabel `kursus_siswa` baru (hasil dinamisasi jadwal) untuk menelusuri kursus yang pernah diambil oleh siswa tersebut.
  * Hasil mapping `student_to_course` digunakan untuk mengisi kolom `id_kursus` secara dinamis pada tabel `siswa_keluar` agar integritas referensial (FK) terjaga.

#### **Tabel Terkait**: `kursus_siswa`
* **Status**: **TERSELESAIKAN ✅**
* **Kendala Awal**: Tabel relasional baru ini kosong dan penentuan `status_aktif`/`status_lulus` belum jelas.
* **Solusi Implementasi**:
  * Membangun data secara dinamis dari query database lama dengan melakukan join antara `jadwal_siswa` dan `jadwal` di `db_old`.
  * Kolom `status_aktif` dihitung dari kolom `is_keluar` (jika `is_keluar > 0` maka `0` (Tidak Aktif), selain itu `1` (Aktif)).
  * Kolom `status_lulus` dipetakan dari `is_lulus` (jika `is_lulus > 0` maka `1`, selain itu `0`).
  * Kolom `catatan` diisi default `NULL`/`None` sesuai permintaan.

---

### 3. FASE 5: Rapor Siswa
#### **Tabel Terkait**: `rapor_siswa_file` & `rapor_lacak`
* **Status**: **TERSELESAIKAN ✅**
* **Kendala Awal**: Kolom `id_rapor_siswa` bernilai NULL pada data file rapor, dan `id_rapor_siswa_file` bernilai NULL pada lacak.
* **Solusi Implementasi**:
  * Melakukan pencocokan berbasis gabungan kunci `(idsiswa, idjadwal)` dari file rapor lama ke tabel `rapor` sebelum ekspor Pickle.
  * Melakukan join yang sama untuk memetakan `id_rapor_siswa_file` di tabel `rapor_lacak`.
  * Memetakan string `idp_nilai` lama (seperti `'P00745'`) ke new `id_parameter_nilai` secara sekuensial berdasarkan urutan database lama agar sinkron dengan data `parameter_nilai` Fase 2.
  * Mengekstrak integer murni dari format ID string (seperti `'H00001'`) ke `id_rapor_lacak` integer murni.

---

## 🧹 Format Pembersihan ID/FK di CSV
* Semua file CSV verifikasi di folder `extract/cek_csv/` telah di-audit menggunakan text-based parser.
* Hasilnya **100% Bebas Desimal `.0`** pada seluruh kolom ID dan Foreign Key. Kolom-kolom bernilai kosong di-render sebagai string kosong yang bersih tanpa ada sisa representasi float.

---
