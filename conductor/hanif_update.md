# Jurnal Log Perkembangan: Hanif - Update

---

## 🎯 Objektivitas & Fungsi Berkas
Dokumen ini berfungsi khusus sebagai **catatan kronologis perkembangan, rincian log pembaruan harian, penyelesaian kendala teknis di lapangan, serta dokumentasi hasil audit harian** untuk seluruh tabel operasional bagian Hanif. Dokumen ini digunakan sebagai jurnal rekam jejak historis pembaruan kode dan data dari awal pengerjaan hingga status final.

---

## 📈 Jurnal Pembaruan Kronologis

### 🟢 Update 3 Juli 2026: Resolusi Siswa Keluar Hilang & Pembaruan Skema Database Baru

Telah diselesaikan masalah hilangnya 47 data siswa yang berstatus keluar (non-aktif) di database baru melalui penelusuran relasi dan sinkronisasi skema:
1. **Investigasi & Validasi Data**:
   * PM melaporkan 47 nama siswa keluar tidak terdaftar di database baru (`db_new`).
   * Melalui script audit in-memory `scratch/check_siswa_keluar.py`, diverifikasi bahwa seluruh 47 data tersebut **ada di database lama (`db_old.siswa`)** dengan flag status `keluar = 1.0` dan log keluar terdaftar lengkap di `siswa_keluar` lama beserta alasan riil.
2. **Penyebab & Sinkronisasi Skema**:
   * Kegagalan migrasi disebabkan database target `dataleap_v5_migration` belum di-patch skema terbarunya. Akibatnya, MySQL menolak insert tabel induk `siswa` karena kolom `status_pendaftaran` (varchar) tidak ada (masih menggunakan skema lama dengan `status_aktif` dan `status_lulus_siswa`).
   * Sukses menjalankan script patcher [patch_db_schema.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/config.gemini/patch_db_schema.py) untuk memperbarui struktur database target baru secara aman.
3. **Eksekusi ETL & Pickle**:
   * Notebook [script_hanif.ipynb](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/fase_4/script_hanif.ipynb) Fase 4 dijalankan ulang untuk memperbarui file binary pickle `fase_4_hanif.pkl`.
   * File `fase_4/insert_handler.ipynb` milik rekan tim yang sempat dikonversi/dieksekusi dikembalikan (*discard change*) sepenuhnya ke kondisi asli menggunakan Git agar tetap bersih dan tidak termodifikasi lokal.
4. **Saran Peningkatan untuk `insert_handler` (Defensive Programming)**:
   * **Masalah**: `insert_handler` saat ini bertindak sangat *strict* (kaku), di mana ia langsung menyusun query insert mentah-mentah dari kolom Pickle dan memicu crash total saat ada kolom ekstra (seperti `status_pendaftaran`) yang belum ditambahkan di database target.
   * **Rekomendasi Solusi**: Disarankan agar `insert_handler` menerapkan *Dynamic Column Filtering* sebelum melakukan insert. Handler sebaiknya melakukan query `DESCRIBE table_name` terlebih dahulu pada database target baru, lalu memfilter Pandas DataFrame secara in-memory agar hanya meng-insert kolom yang terdaftar di database baru. Ini membuat program migrasi menjadi robust dan kebal crash dari perubahan minor struktur kolom.

---

### 🟢 Update 25 Juni 2026 (Siang): Audit Menyeluruh & Eksekusi Sukses Fase 1 - 5

Telah dilakukan eksekusi ulang secara menyeluruh terhadap kelima notebook Jupyter Hanif (`fase_1` sampai `fase_5`) secara berurutan di dalam *virtual environment* menggunakan skrip otomatisasi `scratch/run_all_notebooks.py`. Semua notebook selesai dijalankan dengan **sukses 100% (Exit Code: 0)**.

#### 1. Rekonsiliasi Jumlah Baris (Pickle vs. CSV)
Hasil verifikasi menunjukkan jumlah baris pada berkas Pickle (`.pkl`) kini **100% sinkron** dengan berkas CSV di folder `extract/cek_csv/`:

| Fase | Nama Tabel | Jumlah Baris (Pickle) | Jumlah Baris (CSV) | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Fase 1** | `busdev_bidang` | 4 | 4 | **✓ Sinkron** |
| | `syarat_resign` | 1 | 1 | **✓ Sinkron** |
| | `ttd` | 1 | 1 | **✓ Sinkron** |
| | `tag_siswa_keluar` | 11 | 11 | **✓ Sinkron** |
| **Fase 2** | `division_user` | 6 | 6 | **✓ Sinkron** |
| | `model_has_roles` | 0 | 0 | **✓ Sinkron** |
| | `model_has_permissions` | 0 | 0 | **✓ Sinkron** |
| **Fase 3** | `pengajuan_karyawan` | 33 | 33 | **✓ Sinkron** |
| | `histori_pengajuan` | 79 | 79 | **✓ Sinkron** |
| | `pelamar` | 192 | 192 | **✓ Sinkron** |
| | `pelamar_kerja` | 67 | 67 | **✓ Sinkron** |
| | `pelamar_sekolah` | 53 | 53 | **✓ Sinkron** |
| | `pelamar_kursus` | 50 | 50 | **✓ Sinkron** |
| | `progres_pelamar` | 403 | 403 | **✓ Sinkron** |
| | `rekrutmen_pelamar` | 281 | 281 | **✓ Sinkron** |
| **Fase 4** | `siswa` | 1.469 | 1.469 | **✓ Sinkron** |
| | `kursus_siswa` | 1.769 | 1.769 | **✓ Sinkron** |
| | `siswa_keluar` | 556 | 556 | **✓ Sinkron** |
| | `mitra` | 22 | 22 | **✓ Sinkron** |
| | `mitra_progres` | 296 | 296 | **✓ Sinkron** |
| | `kemitraan_verifikator` | 228 | 228 | **✓ Sinkron** |
| **Fase 5** | `rapor_format` | 41 | 41 | **✓ Sinkron** |
| | `rapor_format_sub` | 121 | 121 | **✓ Sinkron** |
| | `rapor_format_formula` | 3 | 3 | **✓ Sinkron** |
| | `rapor_format_formula_sub` | 1.625 | 1.625 | **✓ Sinkron** |
| | `rapor_level_config` | 340 | 340 | **✓ Sinkron** |
| | `rapor_siswa` | 22.837 | 22.837 | **✓ Sinkron** |
| | `rapor_siswa_file` | 1.499 | 1.499 | **✓ Sinkron** |
| | `rapor_lacak` | 1.366 | 1.366 | **✓ Sinkron** |

#### 2. Analisis Audit Kualitas Data
* **`rekrutmen_pelamar.id_pelamar` (12 Nulls)**: Bersifat nullable (`YES` pada target DB schema), sehingga aman untuk disuntikkan dan tidak akan memicu kegagalan constraint.
* **`rapor_siswa.final_result` (1 Test Comment)**: Komentar uji coba `'cobak ubah cobak ubah...'` berukuran sangat pendek (~60 karakter) dan aman berada di bawah limit `VARCHAR(255)`. Tidak ada komentar yang melebihi batas panjang kolom.
* **Format Penulisan ID/FK**: Bersih dari format desimal `.0` (menggunakan Pandas `Int64` nullable integer), dan nilai kosong dirender sebagai string kosong murni `""` pada berkas CSV.

---

### 🟢 Update 25 Juni 2026 (Pagi - Tahap 2): Pengalihan Pengelolaan Tabel Roles & Kelurahan

Tanggung jawab pengelolaan beberapa tabel master/wilayah secara resmi dialihkan dari Hanif ke anggota tim lainnya:
* **Tabel `roles` (Fase 1)**: Dikeluarkan dari notebook `fase_1/script_hanif.ipynb`. Berkas pickle target `fase_1_hanif.pkl` kini dikemas secara bersih tanpa menyertakan tabel `roles`.
* **Tabel `kelurahan` (Fase 2)**: Dikeluarkan dari notebook `fase_2/script_hanif.ipynb`. Berkas pickle target `fase_2_hanif.pkl` kini dihasilkan tanpa menyertakan tabel `kelurahan`.
* Kedua notebook telah dijalankan ulang secara berurutan dan terbukti berjalan dengan sukses 100% tanpa ada kesalahan.

---

### 🟢 Update 25 Juni 2026 (Pagi - Tahap 1): Resolusi Peringatan & Kegagalan Relasi Rapor Fase 5

Guna melenyapkan seluruh peringatan (*warnings*) dan kegagalan relasi kunci asing (*Foreign Key*) pada penyuntikan data rapor, telah diimplementasikan arsitektur pemetaan yang kokoh dan bebas dari pergeseran (*drift*):
* **Deduplikasi Cartesian Product & Sinkronisasi Urutan**: Penggabungan kolom `urutan` kini diselaraskan secara langsung pada kunci unik `id_rapor_format` (untuk `rapor_format`) dan `id_rapor_format_sub` (untuk `rapor_format_sub`) menggunakan data dari berkas CSV urutan manual. Jumlah baris kembali bersih dan akurat (tepat 41 format utama dan 121 sub-format).
* **Proteksi Nilai Urutan Null**: Kolom `urutan` pada tabel `rapor_format_sub` dijamin aman dari penolakan database (`NOT NULL` violation) dengan menggunakan fungsi `.fillna(0).astype('Int64')` untuk mengisi nilai default `0` jika data urutan manual kosong.
* **Pembersihan Lintas Relasi Kursus Terhapus ('K00017')**: Seluruh baris konfigurasi, formula, dan sub-format yang berafiliasi dengan kursus `'K00017'` dieliminasi secara lokal menggunakan filter Pandas pada `rapor_format` dan menyaring seluruh tabel anak (`rapor_format_sub`, `rapor_format_formula_sub`, `rapor_level_config`) secara bertingkat berdasarkan format induk yang valid.
* **Pembersihan Komentar Guru (Category A & B)**: Komentar guru berkategori A (placeholder seperti *comment*, *test*, *dummy*) pada `rapor_siswa.final_result` dibersihkan menjadi string kosong (`""`), sedangkan komentar berkategori B (riil) dipertahankan utuh di bawah batas panjang 249 karakter (aman masuk skema `VARCHAR(255)` tanpa terpotong).
* **Pemetaan ID Bebas Drift (Drift-Free Auto-Increment)**: Penomoran auto-increment buatan lokal untuk `id_rapor_siswa` and `id_rapor_siswa_file` dilakukan **setelah** seluruh proses penyaringan data selesai dilakukan (*post-filtering reset index*). Relasi anak di `rapor_siswa_file` dan `rapor_lacak` kini dijamin sinkron 100% dengan auto-increment riil database.
* **Validasi Mandiri Offline-First**: Pencocokan ID siswa dan jadwal dialihkan secara mandiri ke berkas pemetaan lokal Fase 4 (`mapping_siswa.pkl` dan `mapping_id_jadwal.pkl`) alih-alih melakukan query langsung ke database target yang kosong, menjamin seluruh data rapor (22.837 baris `rapor_siswa`, 1.499 baris `rapor_siswa_file`, dan 1.366 baris `rapor_lacak`) berhasil diekspor secara utuh secara lokal.

---

### 🟢 Update 24 Juni 2026 (Sore): Fix Data Lapangan Tahap 2
* **Penghapusan Mapping `id_calon` — ⏸️ SKIP**: Kolom `idcalon → id_calon` dihapus dari `patch_fase_4()` karena tabel calon di db_new belum tersedia. Kolom ini nullable → tidak blocking insert. Backlog post-deadline.
* **Perbaikan `nomor_induk` Invalid (`siswa`)**: Fungsi `fix_no_induk` diperbarui: nilai `#N/A`, `0000`, `NODATAYET`, string kosong → `'-'`. Kasus spesifik: `S0000549` dengan `0000` dan `S0000522` dengan `00NF3` → `'-'`.
* **Pembersihan `NODATAYET` di Beberapa Kolom (`siswa`)**: Setelah rename kolom, seluruh nilai `'NODATAYET'` di kolom `domisili`, `asal_sekolah`, `tingkat_sekolah`, `tempat_lahir`, `nomor_induk` diganti `'-'`.
* **Drop Baris Orphan `K00017` di `kursus_siswa` — ✅ SELESAI**: 1 baris `kursus_siswa` merujuk ke `K00017` yang tidak ada di db_new (di-filter Afrida, Fase 1). Solusi: filter `df_ks_raw[df_ks_raw['id_kursus'] != 'K00017']` setelah deduplication.

---

### 🟢 Update 24 Juni 2026 (Siang): Sinkronisasi Tabel Auto-Increment Induk & Pemetaan Offline Lintas Fase

Guna menyelaraskan data dengan sistem auto-increment di database target (`db_new`) serta menyelaraskan pemetaan yang dikerjakan oleh anggota tim lain tanpa bergantung pada koneksi database aktif (*fully offline-friendly*), telah diimplementasikan arsitektur pemetaan ID baru:
* **Penghapusan Kolom PK Auto-Increment pada Seluruh Tabel**: Seluruh kolom Primary Key (PK) asli dari database lama telah dihapus dari DataFrame hasil transformasi di semua notebook Hanif sebelum diekspor ke berkas Pickle (`.pkl`). Hal ini mencegah kegagalan *duplicate key* atau bentrok tipe data saat proses *insert*.
* **Pembuatan Berkas Pemetaan (Mapping Files) untuk Tabel Induk**: Untuk setiap **Tabel Induk (Parent Table)** yang memiliki relasi Foreign Key (FK) ke tabel anak, kita membuat berkas pemetaan (`id_lama` ke `id_baru`) secara dinamis berdasarkan urutan baris (`index + 1`) setelah DataFrame diurutkan secara deterministik.
  * Berkas pemetaan ini disimpan dalam format **Pickle (`.pkl`)** di direktori fase masing-masing untuk digunakan oleh script, dan format **CSV (`.csv`)** di `extract/cek_csv/` untuk keperluan audit manual oleh tim.
* **Penyelarasan FK Lintas Tabel & Lintas Fase Secara Offline (In-Memory)**:
  * **Penyelarasan Lintas Tabel**: Kolom Foreign Key pada seluruh tabel anak (seperti `id_pelamar` pada riwayat pelamar, `id_mitra` pada progres mitra, dan `id_sm` pada progres siswa mitra) kini dipetakan secara dinamis menggunakan dictionary mapping yang dibentuk *in-memory* dari data tabel induk. Ini menjamin relasi antar data tetap utuh 100% saat masuk ke database baru.
  * **Penyelarasan Lintas Fase**: Kolom `id_siswa` pada tabel rapor di Fase 5 (`rapor_siswa`, `rapor_lacak`) kini disinkronkan secara offline dengan memuat berkas pemetaan `../fase_4/mapping_siswa.pkl` pada awal proses transformasi. Hal ini membuat integrasi antar fase sangat kokoh dan tidak bergantung pada apakah data Fase 4 sudah masuk ke database baru atau belum.
* **Pembersihan Kolom Alamat Domisili (`siswa`)**: Diterapkan fungsi pembersihan khusus `clean_domisili` pada Fase 4 yang melakukan pemotongan (*slicing*) data pada karakter koma pertama (`,`) yang ditemukan (untuk mengambil nama wilayah/kota domisili saja), melakukan *strip* spasi, dan membatasi panjang teks maksimal 100 karakter. Ini memastikan data domisili bersih dan dijamin lolos validasi database baru.

---

### 🟢 Update 24 Juni 2026 (Pagi): Sinkronisasi Skema & Validasi Data Lapangan

Guna mengatasi kegagalan integrasi database (*warnings* dan *FK constraint failures*) saat proses *insert* aktual, telah dilakukan pembaruan implementasi pemetaan dan pembersihan data di seluruh notebook Hanif:
* **Pembersihan Khusus No WA Siswa (`siswa`)**:
  * **Masalah**: Kolom `wa_siswa`, `wa_ortu`, dan `wa_administrasi` di database baru dibatasi `VARCHAR(20)`. Data lama mengandung nilai kotor (beberapa nomor digabung dengan slash `/` atau dibubuhi teks deskripsi) yang memicu error *data truncated*.
  * **Solusi**: Diterapkan fungsi pembersih khusus `clean_wa_number` pada Fase 4:
    1. Jika terdapat karakter slash `/`, hanya potongan teks sebelum slash pertama yang diambil.
    2. Karakter non-angka dan non-simbol `+` dibersihkan sepenuhnya.
    3. Hasil akhir dipotong maksimal 15 karakter angka/simbol (sesuai panjang normal nomor telepon lokal/internasional) sehingga dijamin masuk ke kolom `VARCHAR(20)`.
* **Pembersihan Data Pelamar (`pelamar`)**:
  * **Pembersihan Tanggal**: Mengubah nilai pengisian default untuk kolom `created_at` yang kosong dari `'1970-01-01'` menjadi `'2020-01-01 00:00:00'`. Ini mencegah kegagalan konversi zona waktu lokal (WIB/UTC+7) ke UTC yang sebelumnya menghasilkan waktu `'1969-12-31'` (di luar batas minimum tipe data `TIMESTAMP` MySQL).
  * **Pembersihan Nilai Integer**: Kolom `toefl` (skor TOEFL) dan `hasiliq` (skor IQ) dibersihkan secara ketat menggunakan `pd.to_numeric` dengan `errors='coerce'` untuk mengubah string kotor seperti `'asd'` menjadi `NaN` lalu diisi dengan `0` sebelum dikonversi ke tipe integer. Hal ini menghilangkan kegagalan input tipe data pada kolom tujuan.
