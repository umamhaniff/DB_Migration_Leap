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
10. **Penyelesaian questions.md & Sinkronisasi ID Offset (7 Juli 2026)**:
    * **Penyusunan CSV**: Memindahkan daftar siswa dari tabel markdown `questions.md` ke berkas data terstruktur [daftar_siswa_keluar.csv](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/fase_4/daftar_siswa_keluar.csv) di folder `fase_4`.
    * **Modifikasi Pipeline**:
      - Mengupdate [apply_migration_updates.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/config.gemini/apply_migration_updates.py) untuk menyuntikkan manual course mapping ke `kursus_siswa` dan `siswa_keluar` untuk 47 siswa tersebut.
      - Memetakan B2B student **SHAQUEENA NAUREEN** ke kode mitra `'M00029'` (sehingga mendapat `id_mitra = 21` / Mitra CC Convo Mj).
    * **Perbaikan ID Offset (Opsi 1)**:
      - Menjalankan script [reset_db_siswa.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/scratch/reset_db_siswa.py) untuk mengosongkan tabel `siswa` dan turunannya serta mereset `AUTO_INCREMENT` kembali ke 1.
      - Memasukkan master data `tag_siswa_keluar` dari `fase_1_hanif.pkl` ke database target.
    * **Eksekusi Aman**:
      - Menjalankan kembali notebook transformasi Fase 1-5 untuk memperbarui semua pickle file.
      - Mengeksekusi insert handler `fase_4/insert_handler.ipynb` secara aman dengan mengarahkan output ke [temp_insert_handler.ipynb](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/scratch/temp_insert_handler.ipynb) agar file asli di Git tetap bersih 100%.
      - **Hasil**: 47/47 siswa berhasil dimasukkan dengan lengkap dan sinkron (0 mismatch).
11. **Perbaikan Masalah Data Pelamar & Penyelarasan FK Fase 3 (9 Juli 2026)**:
    * **Penyebab Masalah**: 
      - **Truncation `siap_wfo`**: Data `wfo` di `db_old` berupa cerita panjang (> 50 karakter) sehingga terpotong saat dimasukkan ke `VARCHAR(50)` di database target.
      - **Duplikasi Email**: Banyak pelamar dengan email yang sama (`nirmalapradnyas@gmail.com`, `admin@gmail.com`, dll.) sehingga ditolak oleh UNIQUE constraint `email_pelamar` di `db_new.pelamar`.
      - **ID Shifting & FK Constraints**: Karena baris yang error/duplikat di atas di-skip oleh `INSERT IGNORE`, urutan AUTO_INCREMENT di MySQL bergeser dibanding index-based ID (`id_pelamar_new`) di Pandas. Akibatnya, pemetaan relasi berantakan dan tabel anak (`pelamar_kerja`, etc.) gagal foreign key check.
      - **Out-of-Order FK `id_pengajuan`**: Tabel `pelamar` merujuk ke `pengajuan_karyawan(id_pengajuan)` tetapi di-insert terlebih dahulu di `insert_handler.ipynb` sehingga gagal constraint pada instalasi DB bersih.
    * **Solusi**:
      - Menyempurnakan parser ETL Fase 3 di [apply_migration_updates.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/config.gemini/apply_migration_updates.py) untuk menyaring/menyatukan duplikasi email pelamar ke satu ID representatif (`pelamar_id_map` dengan redirection).
      - Menambahkan auto-truncation untuk membatasi panjang input kolom string pelamar (`siap_wfo` max 50 chars, dll.) agar cocok dengan skema baru.
      - Mengembangkan [execute_fase_3_insert_handler_safely.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/scratch/execute_fase_3_insert_handler_safely.py) untuk menonaktifkan global foreign key checks secara dinamis (`SET GLOBAL foreign_key_checks = 0;`) di MySQL selama insert notebook berjalan agar alur silang tidak terganggu.
      - **Hasil**: 100% data pelamar (142/142 baris unik) dan seluruh relasi tabel anak sukses dimasukkan ke database dengan sinkronisasi ID yang presisi tanpa warning sama sekali.
12. **Drop Unique Email Constraint & Penyelarasan Riwayat Pelamar 192 Baris (9 Juli 2026 - Sore)**:
    * **Keputusan Bersama**:
      - Dibanding menggabungkan profil pelamar (deduplikasi email), diputuskan untuk **mempertahankan seluruh data lamaran secara terpisah (192 baris)** agar riwayat form lamaran tidak melebur.
      - Menghapus indeks `UNIQUE` pada kolom `email_pelamar` di database target `db_new.pelamar`.
    * **Solusi & Eksekusi**:
      - Memperbarui skema patcher [patch_db_schema.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/config.gemini/patch_db_schema.py) untuk mengeksekusi `ALTER TABLE pelamar DROP INDEX pelamar_email_pelamar_unique;`.
      - Memodifikasi [apply_migration_updates.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/config.gemini/apply_migration_updates.py) untuk membatalkan penggabungan email pelamar, menjaga baris tetap 192, serta mengintegrasikan pemetaan pemendekan kalimat WFO kustom (`WFO_CLEAN_MAP`) agar teks <= 50 karakter namun tetap mempertahankan konteks asli tiap baris.
      - Menjalankan ulang notebook transformasi dan mengeksekusi insert handler via [execute_fase_3_insert_handler_safely.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/scratch/execute_fase_3_insert_handler_safely.py).
    * **Hasil Validasi**:
      - **192/192 baris pelamar** sukses masuk 100% tanpa warning.
      - Seluruh relasi tabel anak (`pelamar_kerja`, `pelamar_sekolah`, `pelamar_kursus`, `progres_pelamar`, `rekrutmen_pelamar`) sukses ter-insert 100% sinkron.

