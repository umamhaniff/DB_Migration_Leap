# Strategi & Pengelolaan Migrasi: Hanif - Plan

---

## 🎯 Objektivitas & Fungsi Berkas
Dokumen ini berfungsi sebagai **panduan manajemen proyek, strategi umum, arsitektur pipa data (pipeline), dan batasan proyek (constraints)** untuk seluruh rangkaian migrasi database bagian Hanif. Dokumen ini mendefinisikan *bagaimana* migrasi dirancang secara konsep, batasan-batasan teknis yang harus dipatuhi, serta pengelolaan backlog dan sisa pekerjaan pasca-migrasi.

---

## 🏗️ Arsitektur & Alur Kerja ETL Migrasi

Proses migrasi data dirancang menggunakan arsitektur offline-first dengan tiga tahapan utama:

1. **Extract**: Data mentah diekstrak dari database lama (`db_old`) secara terprogram di dalam notebook menggunakan kueri SQL.
2. **Transform**: Pembersihan, penyesuaian tipe data, normalisasi enum, pembersihan nomor telepon/alamat kotor, dan lookup kunci asing dilakukan menggunakan library Pandas di Jupyter Notebook.
   * Hasil transformasi disimpan ke dalam berkas binary **Pickle (`.pkl`)** untuk menjaga keutuhan tipe data Pandas.
   * Hasil transformasi juga diekspor ke berkas **CSV (`.csv`)** di folder `extract/cek_csv/` untuk keperluan verifikasi manual dan audit visual oleh tim.
3. **Insert (Load)**: Berkas Pickle dibaca oleh skrip penyuntik (*insert handler*) untuk dimasukkan secara bersih ke database baru (`db_new`).

---

## 🛑 Batasan & Aturan Teknis Proyek (Project Constraints)

Rangkaian skrip dan notebook migrasi harus tunduk pada 4 aturan utama berikut:

1. 🛑 **DILARANG MENGUBAH DATA MASTER/WILAYAH DI DB_NEW**: Tabel referensi wilayah (`provinsi`, `kabupaten`, `kecamatan`, `kelurahan`) di `db_new` bersifat final. Kita hanya diperbolehkan mencari ID wilayah berdasarkan nama wilayah secara hierarkis (*Hierarchical Matching*) dan menyimpannya sebagai Foreign Key (FK) di tabel anak.
2. 🚫 **DILARANG KERAS MENGUBAH `insert_handler.ipynb`**: Berkas skrip penyuntikan (*insert*) dikelola secara eksklusif oleh rekan tim lain. Jangan pernah memodifikasi, mem-patch, atau menulis ulang berkas `insert_handler.ipynb` mana pun.
3. 🔌 **Offline-First & Database Independence**: Skrip transformasi tidak boleh bergantung pada koneksi aktif ke database target baru (`db_new`) yang kosong. Semua lookup relasi lintas tabel dan lintas fase harus diselesaikan secara offline menggunakan berkas pemetaan (`mapping_xxxx.pkl`) yang telah dihasilkan pada fase sebelumnya.
4. 🔢 **Auto-Increment & Drift-Free Mapping**: Kolom Primary Key (PK) yang bertipe auto-increment pada database baru harus dihapus dari DataFrame transformasi agar dikelola secara alami oleh MySQL. Seluruh tabel anak dipetakan secara dinamis menggunakan berkas pemetaan ID baru (`id_lama -> id_baru`) yang dihitung secara *drift-free* setelah proses penyaringan data selesai (*post-filtering reset index*).

---

## 📋 Rencana Eksekusi Tingkat Tinggi (High-Level Steps)

* [x] **Fase 1 & Fase 2 (Master & SDM)**:
  * Pembersihan skrip `script_hanif.ipynb` pada Fase 1 dan Fase 2 untuk mengeluarkan pengelolaan tabel `roles` dan `kelurahan`.
  * Eksekusi ulang dan pembuatan Pickle Fase 1 & 2 yang bersih.
* [x] **Fase 3 (CRM & Rekrutmen)**:
  * Implementasi auto-increment pelamar.
  * Pemetaan FK pelamar bertingkat via tabel `pelamar_users` -> email -> nama lengkap.
* [x] **Fase 4 (Siswa & Kemitraan)**:
  * Pembersihan nomor WA (max 15 karakter) dan domisili (max 100 karakter).
  * Penyusunan relasi kelas B2C `kursus_siswa` secara dinamis.
  * Penyaringan baris kursus terhapus `'K00017'`.
* [x] **Fase 5 (Rapor & Evaluasi)**:
  * Sinkronisasi urutan format tanpa Cartesian product.
  * Penanganan nilai default `urutan` untuk kolom NOT NULL.
  * Pembersihan komentar guru kategori A dan pembatasan kategori B.
  * Pemetaan ID bebas drift (drift-free auto-increment).
* [x] **Validasi & Verifikasi Akhir**:
  * Eksekusi ulang kelima notebook secara berurutan dan otomatis.
  * Audit menyeluruh terhadap seluruh berkas Pickle dan CSV yang dihasilkan.

---

## 🗃️ Pengelolaan Backlog & Masalah Diketahui (Backlog & Known Issues)

### 1. ⏸️ SKIP — Kolom `id_calon` pada tabel `siswa`
* **Status**: Ditunda (nullable).
* **Konteks**: Kolom `idcalon` di database lama seharusnya merujuk ke tabel calon siswa di `db_new`. Namun, tabel calon siswa belum selesai dimigrasikan oleh rekan tim.
* **Tindakan ke Depan**: Setelah tabel calon siswa selesai di-insert ke `db_new`, buat berkas pemetaan ID calon siswa, kemudian lakukan integrasi kueri lookup pada `siswa` (Fase 4).
* **Prioritas**: Rendah (tidak menghambat proses insert karena kolom bersifat nullable).

### 2. ⚠️ Overlapping Tabel pada File Ekspor `.pkl` Rekan Tim
* **Konteks**: Hasil analisis berkas Pickle menunjukkan bahwa beberapa berkas `.pkl` milik Cimut (`fase_3_cimut.pkl`, `fase_4_cimut.pkl`) mengandung tabel-tabel operasional yang juga diekspor oleh Hanif (seperti `siswa`, `mitra`, `rekrutmen_pelamar`, dll.).
* **Mitigasi**: Pastikan saat menjalankan skrip insert handler utama, tabel operasional yang disuntikkan ke database merujuk secara konsisten ke berkas Pickle milik Hanif (`fase_3_hanif.pkl`, `fase_4_hanif.pkl`, `fase_5_hanif.pkl`) karena berkas milik Hanif telah melalui proses pembersihan tipe data, panjang kolom, dan perbaikan integritas relasi secara ketat.
