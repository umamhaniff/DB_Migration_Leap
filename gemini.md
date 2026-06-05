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

---

* File `.ipynb` dimodifikasi secara terprogram menggunakan script pendukung **`update_notebooks.py`** dan script patching khusus **`config.gemini/apply_migration_updates.py`**.
* Setelah `apply_migration_updates.py` dijalankan, notebook Jupyter terkait akan terperbaharui secara otomatis tanpa merusak struktur internal JSON notebook.

---

## 📈 Perkembangan Terakhir (Per 5 Juni 2026)

1. **Fase 3 (Selesai)**:
   * Mengubah `id_pelamar` di tabel `pelamar` menjadi integer auto-increment.
   * Memetakan kolom `id_pelamar` di 5 tabel anak (`pelamar_kerja`, `pelamar_sekolah`, `pelamar_kursus`, `progres_pelamar`, `rekrutmen_pelamar`) menjadi tipe data `Int64` yang sinkron dengan ID induk baru.
2. **Fase 4 (Selesai)**:
   * Menambahkan kolom `status_pendaftaran` pada tabel `siswa` langsung dari kolom `statussiswa` (varchar) database lama, serta menghapus kolom `status_aktif` dan `status_lulus_siswa` dari mapping.
   * Mengubah looping mapping kelurahan yang lambat menjadi vectorized `.merge()` (memangkas durasi ETL dari jam-jaman menjadi kurang dari 15 detik).
   * Melakukan audit kelengkapan kolom pada tabel `mitra`.
3. **Fase 5 (Selesai)**:
   * Menyelesaikan masalah nilai `id_rapor_siswa` yang NULL pada tabel `rapor_siswa_file` dan `id_rapor_siswa_file` yang NULL di `rapor_lacak` dengan pemetaan ID integer lokal di python sebelum ekspor Pickle.
4. **Validasi & Sinkronisasi**:
   * Menambahkan test suite [test_migration_pickles.py](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/config.gemini/test_migration_pickles.py) untuk memastikan file Pickle hasil regenerasi (`fase_3_hanif.pkl`, `fase_4_hanif.pkl`, `fase_5_hanif.pkl`) valid 100%.
   * Laporan detail audit Fase 5 disimpan di [config.gemini/audit_fase_5.txt](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/config.gemini/audit_fase_5.txt).

