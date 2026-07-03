# ♊ Gemini Project Memory: db_migration_leap

Proyek ini adalah migrasi database terstruktur dari database versi lama (`dataleap_v5_example`) ke database versi baru (`dataleap_v5_migration`) yang dibagi menjadi 5 fase migrasi.

---

## 🗂️ Konseptual & Arsitektur Migrasi

1. **Jalur Pemrosesan (Pipeline)**:
   * **Extract**: Data diekstrak dari database lama (`db_old`).
   * **Transform**: Data ditransformasi secara lokal di Jupyter Notebook (misal `fase_4/script_hanif.ipynb`) menggunakan Pandas DataFrame. Hasil transformasi disimpan dalam bentuk file binary Pickle (`.pkl`).
   * **Insert (Load)**: File Pickle dibaca oleh script/handler insert untuk dimasukkan ke database baru (`db_new`).

2. **Aturan Penting Project (Project Constraints)**:
   * 🛑 **DILARANG MENGUBAH DATA MASTER/WILAYAH DI DB_NEW**: Tabel referensi wilayah (`provinsi`, `kabupaten`, `kecamatan`, `kelurahan`) di `db_new` sudah bersifat final (hasil migrasi Fase 1 & 2). 
   * 🔄 **Hanya Mengubah Foreign Key (FK)**: Selama transformasi data operasional (seperti `siswa` dan `mitra` di Fase 4), kita hanya diperbolehkan mengubah nilai kolom FK (`id_provinsi`, `id_kabupaten`, `etc.`) agar menunjuk ke ID integer auto-increment baru di `db_new`. Pemetaan ini dicapai dengan mencocokkan nama wilayah secara hierarkis (*Clean-Name Hierarchical Matching*).
   * 🚫 **DILARANG KERAS MENGUBAH `insert_handler.ipynb`** (di semua fase): File ini bukan bagian Hanif — dikelola oleh anggota tim lain. Jangan pernah edit, patch, atau regenerate file `insert_handler.ipynb` manapun, termasuk melalui `apply_migration_updates.py` or script patching lain.

---

* File `.ipynb` dimodifikasi secara terprogram menggunakan script pendukung **`update_notebooks.py`** dan script patching khusus **`config.gemini/apply_migration_updates.py`**.
* Setelah `apply_migration_updates.py` dijalankan, notebook Jupyter terkait akan terperbaharui secara otomatis tanpa merusak struktur internal JSON notebook.

---

## 📈 Perkembangan Terakhir (Per 29 Juni 2026)

1. **Fase 3 (Selesai)**:
   * Mengubah `id_pelamar` di tabel `pelamar` menjadi integer auto-increment.
   * Memetakan kolom `id_pelamar` di tabel anak (`pelamar_kerja`, `pelamar_sekolah`, `pelamar_kursus`, `progres_pelamar`, `rekrutmen_pelamar`) dari `idusers` lama secara akurat via pencocokan bertingkat (tabel `pelamar_users` -> email -> normalisasi nama lengkap).
2. **Fase 4 (Selesai)**:
   * Menambahkan kolom `status_pendaftaran` pada tabel `siswa` langsung dari kolom `statussiswa` (varchar) database lama, serta menghapus kolom `status_aktif` dan `status_lulus_siswa` dari mapping.
   * Membangun tabel `kursus_siswa` secara dinamis dari join `jadwal_siswa` dan `jadwal` di `db_old` untuk memetakan kelas siswa B2C secara tepat. Kolom `status_aktif` diturunkan dari `is_keluar` (jika `is_keluar > 0` maka `0`, else `1`), `status_lulus` dari `is_lulus`, dan `catatan` diisi default `NULL`.
   * Memetakan kolom `id_kursus` di `siswa_keluar` secara dinamis dari mapping `kursus_siswa` di atas.
3. **Fase 5 (Selesai)**:
   * Menyelesaikan masalah nilai `id_rapor_siswa` yang NULL pada tabel `rapor_siswa_file` dan `id_rapor_siswa_file` yang NULL di `rapor_lacak` dengan penelusuran relasi `(idsiswa, idjadwal)` pada Python DataFrame sebelum ekspor.
   * Memetakan string `idp_nilai` lama (seperti `'P00745'`) ke new `id_parameter_nilai` secara sekuensial berdasarkan urutan database lama agar sinkron dengan `parameter_nilai` Fase 2.
   * Mengekstrak integer murni dari format ID string (seperti `'H00001'`) ke `id_rapor_lacak` integer murni.
4. **Validasi & Sinkronisasi CSV**:
   * Seluruh CSV verifikasi (25 tabel) diekspor secara bersih ke folder `extract/cek_csv/` tanpa imbuhan `_export`.
   * Mengintegrasikan auto-cast tipe data integer nullable Pandas (`Int64`) pada cell ekspor CSV untuk membersihkan format desimal `.0` pada seluruh kolom ID/FK dan merender nilai kosong/NaN menjadi string kosong murni.
   * Laporan detail kendala migrasi yang terselesaikan di-update di `conductor/laporan_kendala_migrasi.md` dan ringkasan catatan di `conductor/catatan.md`.
5. **Pembaruan Pembagian Kerja (25 Juni 2026)**:
   * Tabel `roles` di Fase 1 dan tabel `kelurahan` di Fase 2 secara resmi dialihkan pengelolaannya dari Hanif ke anggota tim lain.
   * Notebook `fase_1/script_hanif.ipynb` dan `fase_2/script_hanif.ipynb` telah diperbarui dan dijalankan kembali secara bersih untuk menghilangkan pemrosesan kedua tabel tersebut. Berkas pickle (`fase_1_hanif.pkl` dan `fase_2_hanif.pkl`) telah diperbarui untuk mengeluarkan tabel tersebut dengan aman.
6. **Optimasi & Penyesuaian Explicit ID (29 Juni 2026)**:
   * **Fase 4 (Optimasi `kode_mitra`)**: Mengoptimalkan pembuatan `kode_mitra` dengan mengganti loop N+1 query menjadi *single bulk query* ke tabel `siswa`, meningkatkan performa ETL secara signifikan.
   * **Fase 5 (Explicit ID & PK Exclusion)**: 
     * Memetakan foreign key di tabel anak secara presisi menggunakan `file_id_map` hasil pemetaan in-memory.
     * Mengeluarkan kolom Primary Key (`id_rapor_siswa`, `id_rapor_siswa_file`, `id_rapor_lacak`) dari DataFrame di file Pickle agar sesuai dengan spesifikasi insert handler yang mengandalkan `AUTO_INCREMENT` MySQL (lulus uji di `test_migration_pickles.py`).
   * **Audit Data Cleaning (29 Juni 2026)**:
     * Melakukan pemindaian otomatis terhadap nilai placeholder dan anomali di Fase 3, 4, dan 5. Laporan lengkap ditulis di [laporan_pemeriksaan_cleaning.md](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/extract/laporan_pemeriksaan_cleaning.md).
     * Ditemukan 2 anomali riil: Pelamar `64a4ddd6bea4320230705100454` dengan `nomor_wa` = `532453` (terlalu pendek), dan Siswa `S0000009` dengan `email` = `0`. Tindakan pembersihan ditangguhkan menunggu diskusi Hanif dengan PM.
7. **Refined Audit Data Cleaning & Git Untracking (3 Juli 2026)**:
   * **Saringan Bersih (No False Positive)**: Mengoptimalkan regex pemindai data cleaning untuk mengecualikan tag HTML, nama panggilan Indonesia (seperti *Lala*, *Rara*, *Iin*), angka Romawi (kelas & RT/RW), serta singkatan media sosial (*ig*, *fb*, *yt*).
   * **Fase 3**: Audit menghasilkan [fase3_anomalies_clean.md](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/extract/fase3_anomalies_clean.md). Mengidentifikasi 14 anomali di `pengajuan_karyawan`, 312 di `pelamar` (termasuk tester internal & email internal), dan 5 di `progres_pelamar`.
   * **Fase 4**: Audit menghasilkan [fase4_anomalies_clean.md](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/extract/fase4_anomalies_clean.md). Mengidentifikasi 1867 data (mayoritas default WA/Tempat Lahir `-`), 19 alasan keluar dummy di `siswa_keluar`, dan 1 *minor note* di `mitra`.
   * **Fase 5**: Audit menghasilkan [fase5_anomalies_clean.md](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/extract/fase5_anomalies_clean.md). Menemukan 6 path file dummy (`TRIAL01.jpeg`, `coba.jpeg`, etc.) di `rapor_siswa_file`.
   * **Git Untracking**: Menghapus laporan audit dari pemantauan Git (`git rm --cached`) untuk menjaga agar folder `extract/` tetap bersih dan lokal, namun tetap menyimpan skrip pemindai di folder `scratch/`.
8. **Penyelidikan Siswa Keluar Hilang & DB Schema Patch (3 Juli 2026)**:
   * **Audit Mismatch Nama**: Menyelidiki 47 nama siswa keluar yang dilaporkan hilang oleh PM. Menemukan bahwa data mereka lengkap di DB Old (`keluar = 1.0` dan log di `siswa_keluar`), namun gagal ter-insert karena database target baru (`dataleap_v5_migration`) belum di-patch skema terbarunya.
   * **Database Patcher**: Sukses mengeksekusi `config.gemini/patch_db_schema.py` untuk menambahkan kolom `status_pendaftaran` di tabel `siswa`, `status_lulus` di `kursus_siswa`, and alter kolom lainnya yang dibutuhkan.
   * **Regenerasi Notebook**: Menjalankan ulang notebook `fase_4/script_hanif.ipynb` untuk memperbarui pickle `fase_4_hanif.pkl` secara bersih dengan status ✅ OK.
   * **Insert Handler Restoration**: Memulihkan file `fase_4/insert_handler.ipynb` milik teman agar kembali bersih tanpa modifikasi lokal.
9. **Eksekusi Ulang & Validasi Akhir Fase 3 - 5 (3 Juli 2026 - Sore)**:
   * **Notebook Runs**: Menjalankan ulang notebook `script_hanif.ipynb` Fase 3, 4, dan 5 secara penuh dengan sukses (0 error).
   * **Pickle Verification**: Mengonfirmasi kepatuhan skema dan data menggunakan `test_migration_pickles.py` dengan status **Passed**.
   * **Null Constraint Check**: Memverifikasi bahwa 12 baris dengan `id_pelamar` NULL di `rekrutmen_pelamar` aman untuk di-insert karena kolom tersebut nullable di database baru.
   * **Git Sync**: Melakukan commit dan sync (push) seluruh files di Git repository secara bersih (termasuk folder `scratch/`, notebooks, dan file `.pkl`).
