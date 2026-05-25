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

## 🛠️ Cara Kerja Transformasi & Sinkronisasi Notebook

* File `.ipynb` dimodifikasi secara terprogram menggunakan script pendukung **`update_notebooks.py`**.
* Setelah `update_notebooks.py` dijalankan, notebook Jupyter terkait akan terperbaharui secara otomatis tanpa merusak struktur internal JSON notebook.
