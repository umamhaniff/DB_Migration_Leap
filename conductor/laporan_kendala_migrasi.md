# Laporan Kendala dan Penangguhan Migrasi Database (Fase 3, 4, & 5)

Dokumen ini memuat daftar kendala teknis dan penangguhan (*skip*) dalam proses migrasi database dari database lama (`dataleap_v5_example`) ke database baru (`dataleap_v5_migration`). Informasi di bawah ini disusun secara terstruktur agar dapat dilaporkan langsung kepada Project Manager (PM) guna mendapatkan konfirmasi langkah tindak lanjut.

---

## 🗂️ Rangkuman Kendala Berdasarkan Fase & Tabel

### 1. FASE 3: Rekrutmen & Pelamar
#### **Tabel Terkait**: `pelamar_kerja`, `pelamar_sekolah`, `pelamar_kursus`
* **Kendala**: Kolom `id_pelamar` (Foreign Key baru) bernilai **NULL (kosong)** untuk seluruh baris data riwayat pekerjaan, pendidikan, dan kursus pelamar.
* **Penyebab Teknis**:
  * Di database lama (`db_old`), tabel riwayat hidup (`pekerjaan`, `pendidikan`, `kursus`) menggunakan kolom `idusers` (berformat string, contoh: `'U00003'`) untuk menunjukkan kepemilikan data.
  * Sementara itu, tabel utama `pelamar` di database lama menggunakan kolom `idpelamar` (berformat hash string acak/timestamp) dan **TIDAK memiliki kolom `idusers`**.
  * Hubungan antara `idusers` (pada tabel riwayat) dengan `idpelamar` (pada data diri pelamar) hanya dicatat secara parsial di tabel perantara `pelamar_users` (hanya ada 10 user terpetakan dari total 29 user di riwayat).
  * Akibat ketiadaan jembatan data yang konsisten antara tabel utama `pelamar` dengan tabel riwayat hidup di database lama, sistem ETL tidak dapat mencocokkan riwayat kerja/sekolah/kursus ke ID integer pelamar baru (`id_pelamar`).
* **Rekomendasi Tindak Lanjut PM**:
  * Meminta konfirmasi apakah ada tabel referensi lain yang memetakan `idusers` ke `idpelamar` secara lengkap.
  * Jika tidak ada, apakah data riwayat pelamar tanpa pemilik ini diperbolehkan untuk tetap NULL atau diabaikan.

---

### 2. FASE 4: Siswa & Mitra
#### **Tabel Terkait**: `siswa_keluar`
* **Kendala**: Kolom `id_kursus` bernilai **NULL (kosong)**.
* **Penyebab Teknis**:
  * Skema database baru (`db_new.siswa_keluar`) mewajibkan adanya referensi ke program kursus melalui kolom `id_kursus`.
  * Namun, pada database lama (`db_old.siswa_keluar`), pencatatan siswa keluar hanya didasarkan pada ID Siswa, Alasan, dan Tanggal Keluar, tanpa menyimpan data mengenai program kursus mana yang mereka tinggalkan.
* **Rekomendasi Tindak Lanjut PM**:
  * Meminta konfirmasi apakah kolom `id_kursus` pada `siswa_keluar` dapat dibiarkan NULL.
  * Atau, apakah perlu dilakukan penelusuran histori kelas aktif siswa di tabel lain (misal `jadwal_siswa` atau `presensi_siswa`) untuk menebak kursus terakhir yang diikuti siswa sebelum keluar.

#### **Tabel Terkait**: `kursus_siswa`
* **Kendala**: Tabel relasional baru ini **kosong (0 baris)** dan pemetaan kolom baru `status_lulus` ditangguhkan.
* **Penyebab Teknis**:
  * Tabel `kursus_siswa` merupakan tabel baru yang dirancang untuk memisahkan data kursus dari data profil utama siswa.
  * Status kelulusan siswa lama awalnya disimpan di kolom `status_lulus_siswa` pada tabel `siswa` database lama. 
  * Namun, untuk memindahkan data ini ke `kursus_siswa.status_lulus`, sistem memerlukan informasi mengenai relasi `id_kursus` yang diambil siswa. Database lama tidak menyediakan struktur pemetaan langsung siswa lama ke program kursus secara terstruktur di tabel siswa.
* **Rekomendasi Tindak Lanjut PM**:
  * Menanyakan bagaimana aturan pengisian histori kursus siswa lama (`kursus_siswa`). Apakah data ini akan diisi manual pasca-migrasi, atau adakah parameter pemetaan tertentu yang bisa digunakan untuk menentukan kursus default dari masing-masing siswa lama.

---

### 3. FASE 5: Rapor Siswa
#### **Tabel Terkait**: `rapor_format` (asal: `format_rapor`), `rapor_format_sub` (asal: `format_rapor_detil`), dan `rapor_format_formula_sub` (asal: `format_rapor_detil_rumus`)
* **Kendala**: Kolom `urutan` ditangguhkan pengisiannya (bernilai kosong/default).
* **Penyebab Teknis**:
  * Skema database baru menambahkan kolom `urutan` untuk mengatur prioritas tampilan parameter nilai rapor di antarmuka aplikasi.
  * Database lama tidak memiliki kolom atau data yang mencatat urutan/prioritas ini (tampilan sebelumnya kemungkinan hanya mengandalkan urutan baris alami saat query SQL).
* **Rekomendasi Tindak Lanjut PM**:
  * Meminta konfirmasi apakah kolom `urutan` ini dapat diisi dengan nilai default berurutan (misal: 1, 2, 3...) berdasarkan urutan masukan data asli, atau apakah ada aturan khusus pengisian urutan berdasarkan kategori/sub-kategori rapor.

---

## 📈 Status Saat Ini (Summary)
Semua kendala di atas telah diisolasi dengan aman di dalam kode notebook (`script_hanif.ipynb`) di masing-masing folder fase, sehingga **tidak menyebabkan error sistem saat proses ETL dijalankan** (data non-kendala berhasil ditransformasikan 100% dan file Pickle ter-generate dengan sukses).

Tindak lanjut sepenuhnya bergantung pada arahan dan kebijakan Project Manager terkait penanganan integritas data historis tersebut.
