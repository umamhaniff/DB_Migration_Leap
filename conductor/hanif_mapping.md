# Spesifikasi Pemetaan Kolom: Hanif - Mapping

---

## 🎯 Objektivitas & Fungsi Berkas
Dokumen ini berfungsi khusus sebagai **referensi teknis pemetaan kolom dan tabel (mapping spec)** dari database versi lama (`dataleap_v5_example`) ke database versi baru (`dataleap_v5_migration`) untuk seluruh tabel operasional bagian Hanif pada Fase 3, 4, dan 5. Dokumen ini digunakan sebagai panduan penulisan query rename, tipe data tujuan, dan transformasi tingkat kolom pada notebook.

---

## 🗂️ List Tabel Operasional (Hanif)

### Fase 3: CRM Pelamar & Rekrutmen
* `pelamar`
* `pelamar_kerja`
* `pelamar_sekolah`
* `pelamar_kursus`
* `rekrutmen_pelamar`
* `progres_pelamar`
* `pengajuan_karyawan`
* `histori_pengajuan`

### Fase 4: Siswa & Kemitraan
* `siswa`
* `kursus_siswa`
* `siswa_keluar`
* `mitra`
* `mitra_progres`
* `kemitraan_verifikator`
* `siswa_mitra`
* `siswa_mitra_keluar`

### Fase 5: Penilaian & Evaluasi Rapor
* `rapor_format`
* `rapor_format_sub`
* `rapor_format_formula`
* `rapor_format_formula_sub`
* `rapor_level_config`
* `rapor_sub_level`
* `rapor_siswa`
* `rapor_siswa_file`
* `rapor_lacak`

---

## 🗺️ Skema Detail Pemetaan (Fase 3 - 5)

### 🟢 Fase 3: CRM Pelamar & Rekrutmen

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru | Keterangan & Transformasi Kolom |
| :--- | :--- | :--- | :--- | :--- |
| pengajuan | idpengajuan | pengajuan_karyawan | id_pengajuan | PK asli dibuang pada pickle (auto-increment) |
| pengajuan | idusers | pengajuan_karyawan | id_user | |
| pengajuan | keterangan | pengajuan_karyawan | posisi | |
| pengajuan | jumlah | pengajuan_karyawan | jumlah | |
| pengajuan | syarat | pengajuan_karyawan | syarat | |
| pengajuan | pertanyaan | pengajuan_karyawan | pertanyaan | |
| pengajuan | alur | pengajuan_karyawan | alur_seleksi | |
| pengajuan | test | pengajuan_karyawan | daftar_tes | |
| pengajuan | status | pengajuan_karyawan | status | enum('Diajukan','Revisi','Sudah Revisi','Diterima','Disetujui','Ditolak'); "Sudah Direvisi" -> "Sudah Revisi" |
| pengajuan | created_at | pengajuan_karyawan | created_at | Direct mapping datetime |
| | | | | |
| histori_pengajuan | idhistori | histori_pengajuan | id_verifikasi | PK asli dibuang pada pickle (auto-increment) |
| histori_pengajuan | idpengajuan | histori_pengajuan | id_pengajuan | Dipetakan menggunakan mapping_pengajuan_karyawan |
| histori_pengajuan | status | histori_pengajuan | status_verifikasi_pengajuan | enum('Diajukan','Revisi','Sudah Revisi','Diterima','Disetujui','Ditolak'); "Sudah Direvisi" -> "Sudah Revisi" |
| histori_pengajuan | catatan | histori_pengajuan | catatan | |
| histori_pengajuan | created_at | histori_pengajuan | created_at | Direct mapping datetime |
| | | | | |
| pelamar | idpelamar | pelamar | id_pelamar | PK asli dibuang pada pickle (auto-increment) |
| pelamar | idpengajuan | pelamar | id_pengajuan | Dipetakan menggunakan mapping_pengajuan_karyawan |
| pelamar | email | pelamar | email_pelamar | |
| pelamar | nama | pelamar | nama_lengkap | |
| pelamar | panggilan | pelamar | nama_panggilan | |
| pelamar | jk | pelamar | jenis_kelamin | enum('Laki-laki','Perempuan') |
| pelamar | | pelamar | tempat_lahir | Ambil string sebelum koma dari kolom `ttl` |
| pelamar | ttl | pelamar | tanggal_lahir | Ambil string tanggal dari kolom `ttl`, ubah ke tipe `date` |
| pelamar | alamat | pelamar | alamat_ktp | |
| pelamar | domisili | pelamar | alamat_domisili | |
| pelamar | wa | pelamar | nomor_wa | |
| pelamar | linkedin | pelamar | akun_linkedin | |
| pelamar | ig | pelamar | akun_instagram | |
| pelamar | fb | pelamar | akun_facebook | |
| pelamar | sosmed | pelamar | sosmed_lain | |
| pelamar | laptop | pelamar | spesifikasi_laptop | |
| pelamar | internet | pelamar | internet | |
| pelamar | kegiatan | pelamar | kegiatan_sekarang | |
| pelamar | rencana | pelamar | rencana_karir | |
| pelamar | mobilitas | pelamar | mobilitas | |
| pelamar | info | pelamar | sumber_info | |
| pelamar | wfo | pelamar | siap_wfo | |
| pelamar | bergabung | pelamar | tanggal_bergabung | Direct mapping date |
| pelamar | jenis | pelamar | kategori_pelamar | |
| pelamar | work | pelamar | riwayat_kerja | |
| pelamar | ppdk | pelamar | riwayat_pendidikan | |
| pelamar | pengalaman | pelamar | pengalaman_bidang | |
| pelamar | wawasan | pelamar | wawasan | |
| pelamar | sehat | pelamar | riwayat_kesehatan | |
| pelamar | statusnikah | pelamar | status_pernikahan | enum('Menikah','Belum Menikah'); "Lajang","Belum","Single" -> "Belum Menikah" |
| pelamar | ajar | pelamar | kemampuan_ajar | |
| pelamar | app | pelamar | penguasaan_aplikasi | |
| pelamar | apps | pelamar | aplikasi_lainnya | |
| pelamar | gunalaptop | pelamar | penggunaan_laptop | enum('Pernah','Tidak Pernah'); "Ya, Pernah" -> "Pernah" |
| pelamar | toefl | pelamar | skor_toefl | Bersihkan string kotor, cast ke integer murni (default 0) |
| pelamar | gaji | pelamar | ekspektasi_gaji | Bersihkan karakter Rp dan spasi, cast ke bigint |
| pelamar | link | pelamar | tautan_berkas | |
| pelamar | resign | pelamar | alasan_resign | |
| pelamar | hasiliq | pelamar | skor_iq | Bersihkan string kotor, cast ke integer (default 0) |
| pelamar | piciq | pelamar | foto_iq | |
| pelamar | picminat | pelamar | foto_minat | |
| pelamar | picpribadi | pelamar | foto_kepribadian | |
| pelamar | created_at | pelamar | created_at | Fallback ke '2020-01-01 00:00:00' jika kosong |
| | | | | |
| pekerjaan | idpekerjaan | pelamar_kerja | id_pelamar_kerja | PK asli dibuang pada pickle (auto-increment) |
| pekerjaan | idusers | pelamar_kerja | id_pelamar | Dipetakan menggunakan mapping_pelamar (via idusers) |
| pekerjaan | namaperusahaan | pelamar_kerja | nama_perusahaan | |
| pekerjaan | periode | pelamar_kerja | periode | |
| pekerjaan | jabatan | pelamar_kerja | jabatan | |
| pekerjaan | jobdesk | pelamar_kerja | deskripsi_kerja | |
| | | | | |
| pendidikan | idpendidikan | pelamar_sekolah | id_pelamar_sekolah | PK asli dibuang pada pickle (auto-increment) |
| pendidikan | idusers | pelamar_sekolah | id_pelamar | Dipetakan menggunakan mapping_pelamar (via idusers) |
| pendidikan | sekolah | pelamar_sekolah | nama_sekolah | |
| pendidikan | jenjang | pelamar_sekolah | jenjang | |
| pendidikan | prodi | pelamar_sekolah | prodi | |
| pendidikan | tahun | pelamar_sekolah | tahun_lulus | Ambil tahun terbaru jika isi berupa rentang |
| pendidikan | ipk | pelamar_sekolah | ipk | Cast ke decimal |
| pendidikan | organisasi | pelamar_sekolah | organisasi | |
| | | | | |
| kursus | idkursus | pelamar_kursus | id_pelamar_kursus | PK asli dibuang pada pickle (auto-increment) |
| kursus | idusers | pelamar_kursus | id_pelamar | Dipetakan menggunakan mapping_pelamar (via idusers) |
| kursus | nama | pelamar_kursus | nama_kursus | |
| kursus | tanggal | pelamar_kursus | tanggal | Parsing format tanggal manual per baris -> date |
| kursus | deskripsi | pelamar_kursus | deskripsi | |
| kursus | lokasi | pelamar_kursus | lokasi | |
| kursus | nosertifikat | pelamar_kursus | nomor_sertifikat | |
| | | | | |
| pelamar_note | idnote | progres_pelamar | id_progres_pelamar | PK asli dibuang pada pickle (auto-increment) |
| pelamar_note | idpelamar | progres_pelamar | id_pelamar | Dipetakan menggunakan mapping_pelamar (via idpelamar) |
| pelamar_note | idusers | progres_pelamar | id_user | |
| pelamar_note | status | progres_pelamar | status_progres_pelamar | enum('Baru','Tahap Test','Interview','Ditolak','Diterima'); "baru" -> "Baru" |
| pelamar_note | note | progres_pelamar | catatan | |
| pelamar_note | link | progres_pelamar | tautan_file | |
| pelamar_note | pertanyaan | progres_pelamar | pertanyaan | |
| pelamar_note | created_at | progres_pelamar | created_at | |
| | | | | |
| pelamar_users | idassign | rekrutmen_pelamar | id_rekrutmen | PK asli dibuang pada pickle (auto-increment) |
| pelamar_users | idpelamar | rekrutmen_pelamar | id_pelamar | Dipetakan menggunakan mapping_pelamar (via idpelamar) (nullable) |
| pelamar_users | idusers | rekrutmen_pelamar | id_user | |

---

### 🔵 Fase 4: Siswa & Kemitraan

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru | Keterangan & Transformasi Kolom |
| :--- | :--- | :--- | :--- | :--- |
| siswa | idsiswa | siswa | id_siswa | PK asli dibuang pada pickle (auto-increment) |
| siswa | tgl_daftar | siswa | tanggal_registrasi | |
| siswa | domisili | siswa | domisili | Potong spasi, slice pada koma pertama (max 100 char) |
| siswa | nama_lengkap | siswa | nama_lengkap | |
| siswa | panggilan | siswa | nama_panggilan | |
| siswa | jkel | siswa | jenis_kelamin | enum('Laki-laki','Perempuan') |
| siswa | nama_sekolah | siswa | asal_sekolah | |
| siswa | level_sekolah | siswa | tingkat_sekolah | |
| siswa | nama_ortu | siswa | nama_orang_tua | |
| siswa | pekerjaan_ortu | siswa | pekerjaan_orang_tua | |
| siswa | tmp_lahir | siswa | tempat_lahir | |
| siswa | tgl_lahir | siswa | tanggal_lahir | |
| siswa | no_induk | siswa | nomor_induk | Konversi `#N/A`, `0000`, `NODATAYET` -> `'-'` |
| siswa | email | siswa | email | |
| siswa | idcalon | siswa | ~~id_calon~~ | ⏸️ **SKIP** — Kolom FK ke tabel calon dihapus (nullable) |
| siswa | provinsi | siswa | id_provinsi | Nama -> FK ID lookup via nama provinsi (Int64) |
| siswa | kabupaten | siswa | id_kabupaten | Nama -> FK ID lookup via nama kabupaten (Int64) |
| siswa | kecamatan | siswa | id_kecamatan | Nama -> FK ID lookup via nama kecamatan (Int64) |
| siswa | kelurahan | siswa | id_kelurahan | Nama -> FK ID lookup via nama kelurahan (Int64) |
| siswa | idmitra | siswa | id_mitra | extract_int(idmitra) -> Int64 |
| siswa | nisn | siswa | nisn | |
| siswa | nik | siswa | nik | |
| siswa | kewarganegaraan | siswa | kewarganegaraan | |
| siswa | agama | siswa | agama | enum('Islam','Kristen Protestan','Katolik','Hindu','Buddha','Konghucu') |
| siswa | rt | siswa | rt | |
| siswa | rw | siswa | rw | |
| siswa | kodepos | siswa | kode_pos | |
| siswa | statussiswa | siswa | status_pendaftaran | Memetakan dari kolom statussiswa (varchar) |
| siswa | rekomen | siswa | rekomendasi | |
| siswa | info | siswa | sumber_info | |
| siswa | pembayaran | siswa | metode_pembayaran | |
| siswa | nama_ayah | siswa | nama_ayah | |
| siswa | pekerjaan_ayah | siswa | pekerjaan_ayah | Ke enum standar |
| siswa | jenjang_ayah | siswa | pendidikan_ayah | |
| siswa | penghasilan_ayah | siswa | penghasilan_ayah | Ke enum standar |
| siswa | nama_ibu | siswa | nama_ibu | |
| siswa | penghasilan_ibu | siswa | penghasilan_ibu | Ke enum standar |
| | | siswa | pekerjaan_ibu | Kolom baru target, diisi default `NULL` |
| siswa | jenjang_ibu | siswa | pendidikan_ibu | |
| siswa | nama_wali | siswa | nama_wali | |
| siswa | pekerjaan_wali | siswa | pekerjaan_wali | Ke enum standar |
| siswa | jenjang_wali | siswa | pendidikan_wali | |
| siswa | penghasilan_wali | siswa | penghasilan_wali | Ke enum standar |
| siswa | wapeserta | siswa | wa_siswa | Bersihkan non-angka/+, pisah slash, batasi max 15 char |
| siswa | wawalmur | siswa | wa_ortu | Bersihkan non-angka/+, pisah slash, batasi max 15 char |
| siswa | waadmin | siswa | wa_administrasi | Bersihkan non-angka/+, pisah slash, batasi max 15 char |
| siswa | sts_pengisian | siswa | status_pengisian | enum('Belum Lengkap','Sudah Lengkap') |
| siswa | bukti | siswa | path_bukti_bayar | |
| siswa | created_bukti | siswa | tanggal_upload_bukti | |
| | | | | |
| jadwal_siswa + jadwal | idsiswa | kursus_siswa | id_kursus_siswa | PK asli dibuang pada pickle (auto-increment) |
| jadwal_siswa | idsiswa | kursus_siswa | id_siswa | Dipetakan menggunakan mapping_siswa (via idsiswa) |
| jadwal + jadwal_siswa | idjadwal | kursus_siswa | id_kursus | String ID asli (seperti `'K00001'`), drop orphan `'K00017'` |
| jadwal_siswa | tgl_mulai | kursus_siswa | tanggal_mulai | parsed ke date |
| jadwal | mode_belajar | kursus_siswa | metode_belajar | Normalisasi -> Online/Offline/Hybrid |
| siswa | lulus | kursus_siswa | status_lulus | lulus == 1.0 -> 1, else 0 |
| | | kursus_siswa | catatan | default `NULL` |
| | | | | |
| siswa_keluar | idsiswa_keluar | siswa_keluar | id_keluar | PK asli dibuang pada pickle (auto-increment) |
| siswa_keluar | idsiswa | siswa_keluar | id_siswa | Dipetakan menggunakan mapping_siswa (via idsiswa) |
| kursus_siswa | (via id_siswa) | siswa_keluar | id_kursus | Mengambil relasi id_kursus dari kursus_siswa |
| siswa_keluar | alasan | siswa_keluar | alasan_keluar | |
| siswa_keluar | tanggal | siswa_keluar | tanggal_keluar | |
| siswa_keluar | alasan_keluar | siswa_keluar | id_tag_keluar | Heuristic detect_tag() berdasarkan kata kunci |
| | | | | |
| mitra | idmitra | mitra | id_mitra | PK asli dibuang pada pickle (auto-increment) |
| mitra | | mitra | kode_mitra | Ambil karakter huruf depan dari idmitra lama |
| mitra | nama | mitra | nama_mitra | |
| mitra | instansi | mitra | nama_instansi | |
| ... | ... | ... | ... | ... (Direct mapping & konversi boolean Ya/Tidak -> 1/0) |
| | | | | |
| mitra_note | idmnote | mitra_progres | id_progres_mitra | PK asli dibuang pada pickle (auto-increment) |
| mitra_note | idmitra | mitra_progres | id_mitra | Dipetakan menggunakan mapping_mitra |
| mitra_note | note | mitra_progres | catatan_progres_mitra | |
| mitra_note | idusers | mitra_progres | id_user | |
| mitra_note | status | mitra_progres | status_progres_mitra | Ke enum standar |
| ... | ... | ... | ... | ... |
| | | | | |
| mitra_users | idmusers | kemitraan_verifikator | id_kemitraan | PK asli dibuang pada pickle (auto-increment) |
| mitra_users | idmnote | kemitraan_verifikator | id_progres_mitra | Dipetakan menggunakan mapping_mitra_progres |
| mitra_users | idusers | kemitraan_verifikator | id_user | |

---

### 🟢 Fase 5: Penilaian & Evaluasi Rapor

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru | Keterangan & Transformasi Kolom |
| :--- | :--- | :--- | :--- | :--- |
| format_rapor | idformat_rapor | rapor_format | id_rapor_format | String ID (PK dipertahankan karena berupa master) |
| format_rapor | idpendkursus | rapor_format | id_kursus | Drop baris yang berafiliasi dengan kursus `'K00017'` |
| format_rapor | title | rapor_format | judul_rapor | |
| | | rapor_format | urutan | Gabung dari `rapor_format_import.csv` via `id_rapor_format` |
| | | | | |
| format_rapor_detil | idformat_rd | rapor_format_sub | id_rapor_format_sub | String ID (PK dipertahankan) |
| format_rapor_detil | idformat_rapor | rapor_format_sub | id_rapor_format | Drop baris berafiliasi dengan format `'K00017'` |
| format_rapor_detil | subtitle | rapor_format_sub | sub_judul_rapor | |
| | | rapor_format_sub | urutan | Gabung via `id_rapor_format_sub` (fillna 0, cast Int64) |
| | | | | |
| format_rapor_rumus | idfrr | rapor_format_formula | id_rapor_format_formula | PK asli dibuang pada pickle (auto-increment) |
| format_rapor_rumus | idformat_rapor | rapor_format_formula | id_rapor_format | Filter format valid |
| format_rapor_rumus | param_operator | rapor_format_formula | logika_operator | |
| | | | | |
| format_rapor_detil_rumus | idfrdr | rapor_format_formula_sub | id_rapor_format_formula_sub | PK asli dibuang pada pickle (auto-increment) |
| format_rapor_detil_rumus | idformat_rd | rapor_format_formula_sub | id_rapor_format_sub | Filter sub-format valid |
| format_rapor_detil_rumus | param_operator | rapor_format_formula_sub | logika_operator | |
| format_rapor_detil_rumus | idlevel | rapor_format_formula_sub | id_level | |
| | | | | |
| format_raport_level | idformat_rl | rapor_level_config | id_rapor_level_config | PK asli dibuang pada pickle (auto-increment) |
| format_raport_level | idlevel | rapor_level_config | id_level | |
| format_raport_level | idpendkursus | rapor_level_config | id_kursus | Filter kursus valid |
| format_raport_level | idformat_rapor | rapor_level_config | id_rapor_format | Filter format valid |
| | | | | |
| | | rapor_sub_level | id_rapor_sub_level | Tabel baru, dibiarkan kosong (0 baris) |
| | | | | |
| rapor | idrapor | rapor_siswa | id_rapor_siswa | PK asli dibuang pada pickle (auto-increment) |
| rapor | idjadwal | rapor_siswa | id_jadwal | Dipetakan menggunakan `mapping_id_jadwal.pkl` (Fase 4) |
| rapor | idsiswa | rapor_siswa | id_siswa | Dipetakan menggunakan `mapping_siswa.pkl` (Fase 4) |
| rapor | tanggal | rapor_siswa | tanggal_input | Direct mapping date |
| rapor | idp_nilai | rapor_siswa | id_parameter_nilai | Dipetakan secara sekuensial dari ID string `'Pxxxxx'` |
| rapor | nilai | rapor_siswa | final_result | Hapus komentar sampah, batasi komentar riil max 249 char |
| | | | | |
| file_rapor_siswa | idfile | rapor_siswa_file | id_rapor_siswa_file | PK asli dibuang pada pickle (auto-increment) |
| file_rapor_siswa | idsiswa | rapor_siswa_file | id_rapor_siswa | Dicari dari relasi (idsiswa, idjadwal) di rapor_siswa |
| file_rapor_siswa | path | rapor_siswa_file | file_rapor_path | |
| | | | | |
| history_rapor | idhistori | rapor_lacak | id_rapor_lacak | PK asli dibuang pada pickle (auto-increment) |
| history_rapor | idsiswa | rapor_lacak | id_siswa | Dipetakan menggunakan `mapping_siswa.pkl` (Fase 4) |
| history_rapor | idjadwal | rapor_lacak | id_jadwal | Dipetakan menggunakan `mapping_id_jadwal.pkl` (Fase 4) |
| history_rapor | tgl | rapor_lacak | tanggal_terkirim | Direct mapping date |
| history_rapor | status | rapor_lacak | status_pengiriman | enum('Terkirim','Gagal') |
| history_rapor | | rapor_lacak | id_rapor_siswa_file | Dicari dari relasi `id_rapor_siswa_file` di rapor_siswa_file |
