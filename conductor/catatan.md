# Catatan Migrasi Database & Validasi ETL (Fase 3, 4, & 5) 📝

Berkas ini berisi catatan teknis penting mengenai jalannya migrasi database dari `db_old` (`dataleap_v5_example`) ke `db_new` (`dataleap_v5_migration`).

---

## 📌 Poin-Poin Penting & Logic Implementation

1. **Penyelarasan Folder Ekspor CSV**:
   * Seluruh CSV pengecekan diletakkan di folder [extract/cek_csv/](file:///D:/_CampusLife/ProjectCampus/6Magang/db_migration_leap/extract/cek_csv) secara langsung.
   * Nama file CSV bersih tanpa imbuhan `_export`.

2. **Pembersihan Tipe Data ID/FK (Bebas Desimal `.0`)**:
   * Pandas secara default mengekspor kolom float (yang mengandung nilai kosong/NaN) ke CSV dengan format desimal `.0`.
   * Solusinya: Kami mengintegrasikan fungsi pembersih otomatis pada cell ekspor di akhir jupyter notebook. Fungsi ini menyaring kolom ID/FK (seperti `id_siswa`, `id_mitra`, `id_provinsi`, dll.), membulatkannya, dan meng-cast ke Pandas Nullable Integer `Int64`.
   * Hasil audit membuktikan **100% ID & FK bersih tanpa desimal `.0`** di dalam file raw CSV.

3. **Logic Mapping & Dinamisasi Kelas**:
   * **Fase 3 (Pelamar)**: Mapping `idusers` -> `id_pelamar` baru diselesaikan menggunakan pencocokan bertingkat (tabel pelamar_users -> email bersih -> nama bersih).
   * **Fase 4 (Kursus Siswa)**: Tabel `kursus_siswa` dibangun secara dinamis dengan melakukan join query pada `jadwal_siswa` dan `jadwal` di database lama. Kolom `status_aktif` ditentukan dari `is_keluar` (jika `is_keluar > 0` maka `0`, else `1`), `status_lulus` dari `is_lulus`, dan `catatan` diisi `NULL`.
   * **Fase 4 (Siswa Keluar)**: Kolom `id_kursus` berhasil dipetakan secara dinamis berdasarkan hasil join data siswa ke tabel `kursus_siswa` di atas.
   * **Fase 5 (Rapor)**: Penyelamatan `id_rapor_siswa` yang NULL di `rapor_siswa_file` dan `id_rapor_siswa_file` yang NULL di `rapor_lacak` berhasil diselesaikan dengan query penelusuran relasi `(idsiswa, idjadwal)` pada memory DataFrame Python sebelum diekspor.
   * **Fase 5 (Parameter Nilai)**: Mapping `idp_nilai` string lama (contoh: `'P00745'`) yang memiliki gaps/holes ke integer `id_parameter_nilai` baru (auto-increment) berhasil di-sync berdasarkan urutan default database lama.

---

## ⚙️ Cara Menjalankan Ulang Pipeline & Patching

Jika ada perubahan data di database lama dan Anda ingin memperbarui file Pickle & CSV:
1. Pastikan database MySQL lokal Anda aktif (port `3307`).
2. Jalankan patch notebook untuk memastikan logika terbaru ter-apply:
   ```bash
   venv\Scripts\python config.gemini/apply_migration_updates.py
   ```
3. Eksekusi notebook di masing-masing fase:
   * **Fase 3**:
     ```bash
     venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_3/script_hanif.ipynb
     ```
   * **Fase 4**:
     ```bash
     venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_4/script_hanif.ipynb
     ```
   * **Fase 5**:
     ```bash
     venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace fase_5/script_hanif.ipynb
     ```
4. Jalankan script audit untuk memastikan kebersihan format ID:
   ```bash
   venv\Scripts\python scratch/audit_csv_ids_raw.py
   ```
5. File hasil transformasi Pickle `.pkl` akan ter-update di folder masing-masing fase, dan file CSV pengecekan akan ter-update di `extract/cek_csv/`.
