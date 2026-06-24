# Hanif - Mapping

---

## List Tabel
Fase 3:
- `pelamar`
- `pelamar_kerja`
- `pelamar_sekolah`
- `pelamar_kursus`
- `rekrutmen_pelamar`
- `progres_pelamar`
- `pengajuan_karyawan`
- `histori_pengajuan`

Fase 4:
- `siswa`
- `kursus_siswa`
- `siswa_keluar`
- `mitra`
- `mitra_progres`
- `kemitraan_verifikator`
- `siswa_mitra`
- `siswa_mitra_keluar`

Fase 5:
- `rapor_format`
- `rapor_format_sub`
- `rapor_format_formula`
- `rapor_format_formula_sub`
- `rapor_level_config`
- `rapor_sub_level`
- `rapor_siswa`
- `rapor_siswa_file`
- `rapor_lacak`

---

## Mapping Tabel

### Fase 3

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| pengajuan | idpengajuan | pengajuan_karyawan | id_pengajuan | |
| pengajuan | idusers | pengajuan_karyawan | id_user | |
| pengajuan | keterangan | pengajuan_karyawan | posisi | |
| pengajuan | jumlah | pengajuan_karyawan | jumlah | |
| pengajuan | syarat | pengajuan_karyawan | syarat | |
| pengajuan | pertanyaan | pengajuan_karyawan | pertanyaan | |
| pengajuan | alur | pengajuan_karyawan | alur_seleksi | |
| pengajuan | test | pengajuan_karyawan | daftar_tes | |
| pengajuan | status | pengajuan_karyawan | status | enum('Diajukan','Revisi','Sudah Revisi','Diterima','Disetujui','Ditolak'); "Sudah Direvisi" di db old jd "Sudah Revisi" di db new |
| pengajuan | created_at | pengajuan_karyawan | created_at | jangan buat timestamp nya tp direct mapping ajaa |
| | | | | |
| histori_pengajuan | idhistori | histori_pengajuan | id_verifikasi | |
| histori_pengajuan | idpengajuan | histori_pengajuan | id_pengajuan | |
| histori_pengajuan | status | histori_pengajuan | status_verifikasi_pengajuan | enum('Diajukan','Revisi','Sudah Revisi','Diterima','Disetujui','Ditolak'); "Sudah Direvisi" di db old jd "Sudah Revisi" di db new |
| histori_pengajuan | catatan | histori_pengajuan | catatan | |
| histori_pengajuan | created_at | histori_pengajuan | created_at | jangan buat timestamp nya tp direct mapping ajaa |
| | | | | |
| pelamar | idpelamar | pelamar | id_pelamar | |
| pelamar | idpengajuan | pelamar | id_pengajuan | |
| pelamar | email | pelamar | email_pelamar | |
| pelamar | nama | pelamar | nama_lengkap | |
| pelamar | panggilan | pelamar | nama_panggilan | |
| pelamar | jk | pelamar | jenis_kelamin | enum('Laki-laki','Perempuan') |
| pelamar | | pelamar | tempat_lahir | ambil nilai selain tanggal di db_old kolom ttl (disebelum koma) |
| pelamar | ttl | pelamar | tanggal_lahir | ambil nilai tanggal nya sajaa ubah ke tipe date karna di db_new tipe nya date |
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
| pelamar | bergabung | pelamar | tanggal_bergabung | jangan buat timestamp nya tp direct mapping ajaa |
| pelamar | jenis | pelamar | kategori_pelamar | |
| pelamar | work | pelamar | riwayat_kerja | |
| pelamar | ppdk | pelamar | riwayat_pendidikan | |
| pelamar | pengalaman | pelamar | pengalaman_bidang | |
| pelamar | wawasan | pelamar | wawasan | |
| pelamar | sehat | pelamar | riwayat_kesehatan | |
| pelamar | statusnikah | pelamar | status_pernikahan | enum('Menikah','Belum Menikah'); "Lajang","Belum","Single","x" di db old jd "Belum Menikah" di db new |
| pelamar | ajar | pelamar | kemampuan_ajar | |
| pelamar | app | pelamar | penguasaan_aplikasi | |
| pelamar | apps | pelamar | aplikasi_lainnya | |
| pelamar | gunalaptop | pelamar | penggunaan_laptop | enum('Pernah','Tidak Pernah'); "Ya, Pernah" di db old jd "Pernah" di db new |
| pelamar | toefl | pelamar | skor_toefl | |
| pelamar | gaji | pelamar | ekspektasi_gaji | di db_old itu format rupiah tp di db_new jd bigint jd langsung ambil nilai int nyaa ajaa |
| pelamar | link | pelamar | tautan_berkas | |
| pelamar | resign | pelamar | alasan_resign | |
| pelamar | hasiliq | pelamar | skor_iq | |
| pelamar | piciq | pelamar | foto_iq | |
| pelamar | picminat | pelamar | foto_minat | |
| pelamar | picpribadi | pelamar | foto_kepribadian | |
| pelamar | created_at | pelamar | created_at | jangan buat timestamp nya tp direct mapping ajaa |
| | | | | |
| pekerjaan | idpekerjaan | pelamar_kerja | id_pelamar_kerja | |
| pekerjaan | idusers | pelamar_kerja | id_pelamar | |
| pekerjaan | namaperusahaan | pelamar_kerja | nama_perusahaan | |
| pekerjaan | periode | pelamar_kerja | periode | |
| pekerjaan | jabatan | pelamar_kerja | jabatan | |
| pekerjaan | jobdesk | pelamar_kerja | deskripsi_kerja | |
| | | | | |
| pendidikan | idpendidikan | pelamar_sekolah | id_pelamar_sekolah | |
| pendidikan | idusers | pelamar_sekolah | id_pelamar | |
| pendidikan | sekolah | pelamar_sekolah | nama_sekolah | |
| pendidikan | jenjang | pelamar_sekolah | jenjang | |
| pendidikan | prodi | pelamar_sekolah | prodi | |
| pendidikan | tahun | pelamar_sekolah | tahun_lulus | karna di db old di kolom tahun nya banyak maka ngambil tahun terbaru aja |
| pendidikan | ipk | pelamar_sekolah | ipk | di db_old itu varchar tapi isi nya decimal, di db_new itu tipe nyaa decimal |
| pendidikan | organisasi | pelamar_sekolah | organisasi | |
| | | | | |
| kursus | idkursus | pelamar_kursus | id_pelamar_kursus | |
| kursus | idusers | pelamar_kursus | id_pelamar | |
| kursus | nama | pelamar_kursus | nama_kursus | |
| kursus | tanggal | pelamar_kursus | tanggal | dari varchar ke date, harus melakukan pengubahan format per baris |
| kursus | deskripsi | pelamar_kursus | deskripsi | |
| kursus | lokasi | pelamar_kursus | lokasi | |
| kursus | nosertifikat | pelamar_kursus | nomor_sertifikat | |
| | | | | |
| pelamar_note | idnote | progres_pelamar | id_progres_pelamar | |
| pelamar_note | idpelamar | progres_pelamar | id_pelamar | |
| pelamar_note | idusers | progres_pelamar | id_user | |
| pelamar_note | status | progres_pelamar | status_progres_pelamar | enum('Baru','Tahap Test','Interview','Ditolak','Diterima'); "baru" di db lama jd "Baru" |
| pelamar_note | note | progres_pelamar | catatan | |
| pelamar_note | link | progres_pelamar | tautan_file | |
| pelamar_note | pertanyaan | progres_pelamar | pertanyaan | |
| pelamar_note | created_at | progres_pelamar | created_at | jangan buat timestamp nya tp direct mapping ajaa |
| | | | | |
| pelamar_users | idassign | rekrutmen_pelamar | id_rekrutmen | |
| pelamar_users | idpelamar | rekrutmen_pelamar | id_pelamar | |
| pelamar_users | idusers | rekrutmen_pelamar | id_user | |

---

### Fase 4

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| siswa | idsiswa | siswa | id_siswa | |
| siswa | tgl_daftar | siswa | tanggal_registrasi | |
| siswa | domisili | siswa | domisili | |
| siswa | nama_lengkap | siswa | nama_lengkap | |
| siswa | panggilan | siswa | nama_panggilan | |
| siswa | jkel | siswa | jenis_kelamin | enum('Laki-laki','Perempuan') |
| siswa | nama_sekolah | siswa | asal_sekolah | |
| siswa | level_sekolah | siswa | tingkat_sekolah | |
| siswa | nama_ortu | siswa | nama_orang_tua | |
| siswa | pekerjaan_ortu | siswa | pekerjaan_orang_tua | |
| siswa | tmp_lahir | siswa | tempat_lahir | |
| siswa | tgl_lahir | siswa | tanggal_lahir | |
| siswa | no_induk | siswa | nomor_induk | |
| siswa | email | siswa | email | |
| siswa | idcalon | siswa | id_calon | |
| siswa | provinsi | siswa | id_provinsi | nama → id FK lookup ke db_new (Int64) |
| siswa | kabupaten | siswa | id_kabupaten | nama → id FK lookup ke db_new (Int64) |
| siswa | kecamatan | siswa | id_kecamatan | nama → id FK lookup ke db_new (Int64) |
| siswa | kelurahan | siswa | id_kelurahan | nama → id FK lookup ke db_new (Int64) |
| siswa | idmitra | siswa | id_mitra | extract_int(idmitra) → Int64 |
| siswa | nisn | siswa | nisn | |
| siswa | nik | siswa | nik | |
| siswa | kewarganegaraan | siswa | kewarganegaraan | |
| siswa | agama | siswa | agama | enum('Islam','Kristen Protestan','Katolik','Hindu','Buddha','Konghucu') |
| siswa | rt | siswa | rt | |
| siswa | rw | siswa | rw | |
| siswa | kodepos | siswa | kode_pos | |
| siswa | statussiswa | siswa | status_pendaftaran | dari kolom statussiswa (varchar) db_old |
| siswa | rekomen | siswa | rekomendasi | |
| siswa | info | siswa | sumber_info | |
| siswa | pembayaran | siswa | metode_pembayaran | |
| siswa | nama_ayah | siswa | nama_ayah | |
| siswa | pekerjaan_ayah | siswa | pekerjaan_ayah | enum('Belum/Tidak Bekerja','Pegawai Swasta', dsb) |
| siswa | jenjang_ayah | siswa | pendidikan_ayah | |
| siswa | penghasilan_ayah | siswa | penghasilan_ayah | enum('kurang_1jt','1jt_3jt','3jt_5jt','lebih_5jt') |
| siswa | nama_ibu | siswa | nama_ibu | |
| siswa | penghasilan_ibu | siswa | penghasilan_ibu | enum('kurang_1jt','1jt_3jt','3jt_5jt','lebih_5jt') |
| | | siswa | pekerjaan_ibu | kolom baru |
| siswa | jenjang_ibu | siswa | pendidikan_ibu | |
| siswa | nama_wali | siswa | nama_wali | |
| siswa | pekerjaan_wali | siswa | pekerjaan_wali | enum('pegawai_swasta','wiraswasta', dsb) |
| siswa | jenjang_wali | siswa | pendidikan_wali | |
| siswa | penghasilan_wali | siswa | penghasilan_wali | enum('kurang_1jt','1jt_3jt','3jt_5jt','lebih_5jt') |
| siswa | wapeserta | siswa | wa_siswa | |
| siswa | wawalmur | siswa | wa_ortu | |
| siswa | waadmin | siswa | wa_administrasi | |
| siswa | sts_pengisian | siswa | status_pengisian | enum('Belum Lengkap','Sudah Lengkap') |
| siswa | bukti | siswa | path_bukti_bayar | |
| siswa | lulus | kursus_siswa | status_lulus | dipindah ke kursus_siswa (kolom status_lulus_siswa di siswa dihapus) |
| siswa | created_bukti | siswa | tanggal_upload_bukti | |
| | | siswa | deleted_at | kolom baru |
| | | | | |
| jadwal_siswa + jadwal | idsiswa | kursus_siswa | id_kursus_siswa | auto-increment, tabel baru dari join jadwal_siswa |
| jadwal_siswa | idsiswa | kursus_siswa | id_siswa | extract_int(idsiswa) → Int64 |
| jadwal + jadwal_siswa | idjadwal | kursus_siswa | id_kursus | via idpendkursus dari join |
| jadwal_siswa | tgl_mulai | kursus_siswa | tanggal_mulai | parsed ke date |
| jadwal | mode_belajar | kursus_siswa | metode_belajar | normalize → Online/Offline/Hybrid |
| siswa | lulus | kursus_siswa | status_lulus | lulus==1 → 1, else 0 |
| | | kursus_siswa | catatan | default NULL |
| | | | | |
| siswa_keluar | idsiswa_keluar | siswa_keluar | id_keluar | extract_int |
| siswa_keluar | idsiswa | siswa_keluar | id_siswa | extract_int |
| kursus_siswa | (via id_siswa) | siswa_keluar | id_kursus | lookup kursus_siswa.id_siswa → id_kursus |
| siswa_keluar | alasan | siswa_keluar | alasan_keluar | |
| siswa_keluar | tanggal | siswa_keluar | tanggal_keluar | |
| siswa_keluar | alasan_keluar | siswa_keluar | id_tag_keluar | detect_tag() heuristic: 9 kategori keyword (lulus/jadwal/biaya/lokasi/motivasi/akademik/guru/teknologi/keluarga) + DB lookup siswa_keluar_tag |
| | | | | |
| mitra | idmitra | mitra | id_mitra | ambil nilai int nya di db_old |
| mitra | | mitra | kode_mitra | ambil karakter selain int di db_old kolom idmitra |
| mitra | nama | mitra | nama_mitra | |
| mitra | instansi | mitra | nama_instansi | |
| mitra | namasekolah | mitra | nama_sekolah | |
| mitra | lokasi | mitra | alamat_mitra | |
| mitra | kepsek | mitra | nama_pimpinan | |
| mitra | cp | mitra | kontak_mitra | |
| mitra | status | mitra | status_mitra | enum('On-going','Done') |
| mitra | visimisi | mitra | visi_misi | |
| mitra | program | mitra | program_mitra | |
| mitra | sdm | mitra | info_sdm | |
| mitra | weakness | mitra | info_kelemahan | |
| mitra | rekomen | mitra | rekomendasi_program | |
| mitra | jenis | mitra | jenis_mitra | enum('Corporate','Sekolah','Lainnya') |
| mitra | provinsi | mitra | provinsi_id | |
| mitra | kotkab | mitra | kabupaten_id | |
| mitra | jml | mitra | jumlah_siswa_mitra | |
| mitra | bidang | mitra | bidang_usaha | |
| mitra | leapverse | mitra | is_leapverse | Ya/Tidak -> 1/0 |
| mitra | kemitraan | mitra | status_kemitraan | Ya/Tidak -> 1/0 |
| mitra | tahun | mitra | tahun_bergabung | |
| mitra | jeniskemitraan | mitra | tipe_kerjasama | enum('Perluasan Bisnis','Layanan Training') |
| mitra | elsa | mitra | is_elsa | Ya/Tidak -> 1/0 |
| mitra | classin | mitra | is_classin | Ya/Tidak -> 1/0 |
| mitra | mitraleap | mitra | is_mitra_leap | Ya/Tidak -> 1/0 |
| mitra | created_at | mitra | created_at | jangan buat timestamp nya tp direct mapping ajaa |
| | | | | |
| mitra_note | idmnote | mitra_progres | id_progres_mitra | |
| mitra_note | idmitra | mitra_progres | id_mitra | |
| mitra_note | note | mitra_progres | catatan_progres_mitra | |
| mitra_note | idusers | mitra_progres | id_user | |
| mitra_note | status | mitra_progres | status_progres_mitra | enum('On-going','Transfer','Connect','Done') |
| mitra_note | startdate | mitra_progres | kemitraan_mulai | |
| mitra_note | enddate | mitra_progres | kemitraan_berakhir | |
| mitra_note | created_at | mitra_progres | created_at | jangan buat timestamp nya tp direct mapping ajaa |
| | | | | |
| mitra_users | idmusers | kemitraan_verifikator | id_kemitraan | |
| mitra_users | idmnote | kemitraan_verifikator | id_progres_mitra | |
| mitra_users | idusers | kemitraan_verifikator | id_user | |
| | | | | |
| siswamitra | idsiswa | siswa_mitra | id_sm | kosong |
| siswamitra | tgl_daftar | siswa_mitra | tanggal_daftar | kosong |
| siswamitra | domisili | siswa_mitra | alamat_domisili | kosong |
| siswamitra | nama_lengkap | siswa_mitra | nama_lengkap | kosong |
| siswamitra | panggilan | siswa_mitra | nama_panggilan | kosong |
| siswamitra | jkel | siswa_mitra | jenis_kelamin | kosong |
| siswamitra | nama_instansi | siswa_mitra | nama_instansi | kosong |
| siswamitra | level_sekolah | siswa_mitra | tingkat_sekolah | kosong |
| siswamitra | pekerjaan | siswa_mitra | pekerjaan_sm | kosong |
| siswamitra | tmp_lahir | siswa_mitra | tempat_lahir | kosong |
| siswamitra | tgl_lahir | siswa_mitra | tanggal_lahir | kosong |
| siswamitra | no_induk | siswa_mitra | nomor_induk_sm | kosong |
| siswamitra | email | siswa_mitra | email_sm | kosong |
| siswamitra | tlp | siswa_mitra | wa_sm | kosong |
| siswamitra | keluar | siswa_mitra | status_keluar_sm | kosong |
| siswamitra | idmitra | siswa_mitra | id_mitra | kosong |
| | | siswa_mitra | sertifikat_sm | kosong |
| | | | | |
| siswa_keluar_mitra | idsiswa_keluar | siswa_mitra_keluar | id_sm_keluar | kosong |
| siswa_keluar_mitra | idsiswa | siswa_mitra_keluar | id_sm | kosong |
| siswa_keluar_mitra | alasan | siswa_mitra_keluar | alasan_keluar_sm | kosong |
| siswa_keluar_mitra | tanggal | siswa_mitra_keluar | tanggal_keluar_sm | kosong |

---

### Fase 5

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| format_rapor | idformat_rapor | rapor_format | id_rapor_format | |
| format_rapor | idpendkursus | rapor_format | id_kursus | |
| format_rapor | title | rapor_format | judul_rapor | |
| | | rapor_format | urutan | dari rapor_format_import.csv (left join on judul_rapor, cast Int64) |
| | | | | |
| format_rapor_detil | idformat_rd | rapor_format_sub | id_rapor_format_sub | |
| format_rapor_detil | idformat_rapor | rapor_format_sub | id_rapor_format | |
| format_rapor_detil | subtitle | rapor_format_sub | sub_judul_rapor | |
| | | rapor_format_sub | urutan | dari rapor_format_sub_import.csv (left join on id_rapor_format + sub_judul_rapor, cast Int64) |
| | | | | |
| format_rapor_rumus | idfrr | rapor_format_formula | id_rapor_format_formula | |
| format_rapor_rumus | idformat_rapor | rapor_format_formula | id_rapor_format | |
| format_rapor_rumus | param_operator | rapor_format_formula | logika_operator | |
| | | | | |
| format_rapor_detil_rumus | idfrdr | rapor_format_formula_sub | id_rapor_format_formula_sub | |
| format_rapor_detil_rumus | idformat_rd | rapor_format_formula_sub | id_rapor_format_sub | |
| format_rapor_detil_rumus | param_operator | rapor_format_formula_sub | logika_operator | |
| format_rapor_detil_rumus | idlevel | rapor_format_formula_sub | id_level | |
| | | | | |
| format_raport_level | idformat_rl | rapor_level_config | id_rapor_level_config | |
| format_raport_level | idlevel | rapor_level_config | id_level | |
| format_raport_level | idpendkursus | rapor_level_config | id_kursus | |
| format_raport_level | idformat_rapor | rapor_level_config | id_rapor_format | |
| | | | | |
| | | rapor_sub_level | id_rapor_sub_level | tabel baru |
| | | rapor_sub_level | id_rapor_format_sub | tabel baru |
| | | rapor_sub_level | id_level | tabel baru |
| | | | | |
| rapor | idrapor | rapor_siswa | id_rapor_siswa | |
| rapor | idjadwal | rapor_siswa | id_jadwal | |
| rapor | idsiswa | rapor_siswa | id_siswa | |
| rapor | tanggal | rapor_siswa | tanggal_input | jangan buat timestamp nya tp direct mapping ajaa |
| rapor | idp_nilai | rapor_siswa | id_parameter_nilai | |
| rapor | nilai | rapor_siswa | final_result | |
| | | | | |
| file_rapor_siswa | idfile | rapor_siswa_file | id_rapor_siswa_file | |
| file_rapor_siswa | idsiswa | rapor_siswa_file | id_rapor_siswa | cari id_rapor_siswa di rapor_siswa (db_new) |
| file_rapor_siswa | path | rapor_siswa_file | file_rapor_path | |
| | | | | |
| history_rapor | idhistori | rapor_lacak | id_rapor_lacak | |
| history_rapor | idsiswa | rapor_lacak | id_siswa | |
| history_rapor | idjadwal | rapor_lacak | id_jadwal | |
| history_rapor | tgl | rapor_lacak | tanggal_terkirim | jangan buat waktu nya tp direct mapping ajaa |
| history_rapor | status | rapor_lacak | status_pengiriman | enum('Terkirim','Gagal') |
| history_rapor | | rapor_lacak | id_rapor_siswa_file | cari id_rapor_siswa_file di rapor_siswa_file |

---

## Catatan Perubahan & Penyelesaian Kendala (Sesuai Kondisi Script Aktual)

Semua kendala mapping operasional yang sebelumnya terhambat kini telah diselesaikan 100% pada notebook Jupyter (`script_hanif.ipynb`) di masing-masing fase:

### 🟢 Fase 3: Pemetaan & Auto-Increment Pelamar
* **Tabel Pelamar (`id_pelamar`)**: Mengubah tipe kolom `id_pelamar` menjadi integer auto-increment untuk mengatasi kegagalan integrasi database.
* **Tabel Anak (`pelamar_kerja`, `pelamar_kursus`, `pelamar_sekolah`, `progres_pelamar`, `rekrutmen_pelamar`)**: Kolom `id_pelamar` yang baru berhasil dipetakan secara akurat dari `idusers` lama melalui:
  1. Relasi tabel `pelamar_users` di database lama.
  2. Pencocokan fallback berdasarkan email bersih (`email_clean`).
  3. Pencocokan fallback berdasarkan normalisasi nama lengkap (`clean_name_without_titles`).
* Seluruh foreign key `id_pelamar` dikonversi ke tipe data integer nullable (`Int64`) untuk memastikan konsistensi relasi tanpa desimal.

### 🟢 Fase 4: Struktur Tabel Siswa, Kursus Siswa, & Mitra
* **Tabel `siswa`**:
  * Kolom `status_aktif` dan `status_lulus_siswa` dihapus dari mapping (tidak digunakan lagi di tabel target ini).
  * Menambahkan kolom `status_pendaftaran` yang diambil langsung dari kolom `statussiswa` (varchar) pada database lama.
  * Normalisasi data string pada kolom `agama` (misal 'kristen' -> 'Kristen Protestan', 'katolik' -> 'Katolik', dsb.) dan `pekerjaan_ayah` / `pekerjaan_wali` (ke kategori enum standar seperti 'Pegawai Swasta', 'Wiraswasta', dll.).
* **Tabel `kursus_siswa` (Tabel Baru)**:
  * Berhasil dibangun secara dinamis dengan melakukan join antara tabel `jadwal_siswa` dan `jadwal` di database lama (`db_old`) untuk mendapatkan relasi B2C yang tepat.
  * Kolom `status_lulus` dipetakan dari kolom `lulus` di `db_old.siswa` (jika `lulus == 1.0` -> `1`, selain itu `0`).
  * Kolom `catatan` diisi default `NULL`.
  * *Catatan Skema*: Kolom `status_aktif` tidak dimasukkan ke dalam mapping script `script_hanif.ipynb` (omitted), meskipun ada di skema database target.
* **Tabel `siswa_keluar`**:
  * Kolom `id_kursus` yang sebelumnya kosong kini berhasil diisi secara dinamis dengan mencocokkan `id_siswa` dengan relasi yang terbentuk di tabel `kursus_siswa` di atas.
  * Kolom `id_tag_keluar` berhasil dipetakan menggunakan fungsi `detect_tag()` yang menyeleksi 9 kategori alasan keluar (lulus, jadwal, biaya, domisili, motivasi, akademik, guru, teknologi, keluarga) berdasarkan kata kunci di kolom `alasan`, dikombinasikan dengan data dari tabel `siswa_keluar_tag` lama.
* **Tabel `mitra`**:
  * Kolom bertipe boolean (`leapverse`, `kemitraan`, `elsa`, `classin`, `mitraleap`) dikonversi secara bersih dari format string Ya/Tidak menjadi integer `1`/`0`.
  * `id_mitra` menyimpan nilai integer dari `idmitra` lama, sementara `kode_mitra` menyimpan prefiks karakternya (misalnya `'M0001'` -> `id_mitra = 1`, `kode_mitra = 'M'`).
  * Relasi wilayah `provinsi_id` dan `kabupaten_id` dipetakan melalui pencocokan nama wilayah secara hierarkis (*Clean-Name Hierarchical Matching*) ke ID baru.
* **Tabel `mitra_progres`**:
  * Menghubungkan progres ke tabel `mitra` dengan mencocokkan `kode_mitra` ke data `id_mitra` hasil migrasi.
  * Menangani nilai `NULL` pada kolom wajib isi `kemitraan_mulai` dan `kemitraan_berakhir` dengan fallback logis ke tanggal pembuatan data (`created_at`) atau default `2023-01-01`.

### 🟢 Fase 5: Sinkronisasi Rapor & Relasi Dokumen
* **Tabel `rapor_format` & `rapor_format_sub`**:
  * Kolom `urutan` berhasil ditambahkan dengan melakukan merge data dari file CSV urutan manual (`rapor_format_import.csv` & `rapor_format_sub_import.csv`) menggunakan tipe data `Int64`.
* **Tabel `rapor_format_formula_sub`**:
  * Kolom `urutan` tidak ditransformasikan di dalam script `script_hanif.ipynb` (omitted), meskipun ada di skema database target.
* **Tabel `rapor_siswa_file` & `rapor_lacak`**:
  * Mengatasi kendala nilai `id_rapor_siswa` dan `id_rapor_siswa_file` yang NULL. Solusinya adalah dengan melakukan pencocokan data `idsiswa` & `idjadwal` dari tabel file ke mapping ID rapor yang digenerate sebelum ekspor data.
  * Mengonversi string ID lama berformat `'Pxxxxx'` (misal `'P00745'`) di kolom `idp_nilai` ke auto-increment `id_parameter_nilai` baru secara berurutan sesuai urutan di database lama agar sinkron dengan tabel parameter nilai Fase 2.
  * Mengonversi string ID berformat `'Hxxxxx'` pada `idhistori` ke integer murni menggunakan fungsi `extract_int`.

### 🧹 Format Output Ekspor CSV & Pickle
* Seluruh file ekspor CSV untuk proses verifikasi (25 tabel) disimpan langsung ke folder `extract/cek_csv/` tanpa imbuhan kata `_export` pada nama file atau direktori.
* Seluruh kolom ID/FK (seperti `id_siswa`, `id_mitra`, `id_provinsi`, dll.) dibersihkan secara otomatis di akhir notebook dengan melakukan cast ke tipe data Pandas `Int64` untuk menghilangkan desimal `.0` (misal `1.0` -> `1`) dan memastikan nilai kosong ter-render sebagai string kosong murni (`""`) pada file CSV.
* Seluruh tipe data string Pandas (`string` / `string[python]`) di-cast ke tipe data `object` sebelum proses penyimpanan Pickle untuk memastikan kompatibilitas penuh dengan serializer Python 3.13.

---

### 🟢 Update 24 Juni 2026: Sinkronisasi Skema & Validasi Data Lapangan

Guna mengatasi kegagalan integrasi database (*warnings* dan *FK constraint failures*) saat proses *insert* aktual, telah dilakukan pembaruan implementasi pemetaan dan pembersihan data di seluruh notebook Hanif:

#### 1. Pembersihan Khusus No WA Siswa (`siswa`)
* **Masalah**: Kolom `wa_siswa`, `wa_ortu`, dan `wa_administrasi` di database baru dibatasi `VARCHAR(20)`. Data lama mengandung nilai kotor (beberapa nomor digabung dengan slash `/` atau dibubuhi teks deskripsi) yang memicu error *data truncated*.
* **Solusi**: Diterapkan fungsi pembersih khusus `clean_wa_number` pada Fase 4:
  1. Jika terdapat karakter slash `/`, hanya potongan teks sebelum slash pertama yang diambil.
  2. Karakter non-angka dan non-simbol `+` dibersihkan sepenuhnya.
  3. Hasil akhir dipotong maksimal 15 karakter angka/simbol (sesuai panjang normal nomor telepon lokal/internasional) sehingga dijamin masuk ke kolom `VARCHAR(20)`.

#### 2. Auto-Increment & Pemetaan Dinamis ID Siswa (`mapping_siswa`)
* **Masalah**: Kolom `id_siswa` di database baru (`db_new.siswa`) bertipe integer auto-increment, sehingga database akan menghasilkan nilai `1, 2, 3, dst.` secara otomatis sesuai urutan sisipan. Pemetaan sebelumnya menggunakan `extract_int(idsiswa)` yang memicu ketidaksinronan relasi dengan tabel anak karena adanya celah (*gaps*) nomor pada ID lama.
* **Solusi**:
  1. Kolom `id_siswa` dihapus dari DataFrame `siswa` di berkas ekspor `fase_4_hanif.pkl`. Hal ini membiarkan MySQL mengelola nilai auto-increment secara natural.
  2. Berkas pemetaan (`idsiswa_lama` ke `id_siswa_baru`) dibuat secara dinamis menggunakan urutan baris (`index + 1`) DataFrame siswa (misal: `'S0000007'` sebagai baris pertama dipetakan ke ID baru `1`).
  3. Hasil pemetaan diekspor secara terpisah ke `fase_4/mapping_siswa.pkl` (juga disisipkan dalam dictionary utama berkas `.pkl`) dan `extract/cek_csv/mapping_siswa.csv` untuk keperluan audit manual.
| siswa | lulus | kursus_siswa | status_lulus | lulus==1 → 1, else 0 |
| | | kursus_siswa | catatan | default NULL |
| | | | | |
| siswa_keluar | idsiswa_keluar | siswa_keluar | id_keluar | extract_int |
| siswa_keluar | idsiswa | siswa_keluar | id_siswa | extract_int |
| kursus_siswa | (via id_siswa) | siswa_keluar | id_kursus | lookup kursus_siswa.id_siswa → id_kursus |
| siswa_keluar | alasan | siswa_keluar | alasan_keluar | |
| siswa_keluar | tanggal | siswa_keluar | tanggal_keluar | |
| siswa_keluar | alasan_keluar | siswa_keluar | id_tag_keluar | detect_tag() heuristic: 9 kategori keyword (lulus/jadwal/biaya/lokasi/motivasi/akademik/guru/teknologi/keluarga) + DB lookup siswa_keluar_tag |
| | | | | |
| mitra | idmitra | mitra | id_mitra | ambil nilai int nya di db_old |
| mitra | | mitra | kode_mitra | ambil karakter selain int di db_old kolom idmitra |
| mitra | nama | mitra | nama_mitra | |
| mitra | instansi | mitra | nama_instansi | |
| mitra | namasekolah | mitra | nama_sekolah | |
| mitra | lokasi | mitra | alamat_mitra | |
| mitra | kepsek | mitra | nama_pimpinan | |
| mitra | cp | mitra | kontak_mitra | |
| mitra | status | mitra | status_mitra | enum('On-going','Done') |
| mitra | visimisi | mitra | visi_misi | |
| mitra | program | mitra | program_mitra | |
| mitra | sdm | mitra | info_sdm | |
| mitra | weakness | mitra | info_kelemahan | |
| mitra | rekomen | mitra | rekomendasi_program | |
| mitra | jenis | mitra | jenis_mitra | enum('Corporate','Sekolah','Lainnya') |
| mitra | provinsi | mitra | provinsi_id | |
| mitra | kotkab | mitra | kabupaten_id | |
| mitra | jml | mitra | jumlah_siswa_mitra | |
| mitra | bidang | mitra | bidang_usaha | |
| mitra | leapverse | mitra | is_leapverse | Ya/Tidak -> 1/0 |
| mitra | kemitraan | mitra | status_kemitraan | Ya/Tidak -> 1/0 |
| mitra | tahun | mitra | tahun_bergabung | |
| mitra | jeniskemitraan | mitra | tipe_kerjasama | enum('Perluasan Bisnis','Layanan Training') |
| mitra | elsa | mitra | is_elsa | Ya/Tidak -> 1/0 |
| mitra | classin | mitra | is_classin | Ya/Tidak -> 1/0 |
| mitra | mitraleap | mitra | is_mitra_leap | Ya/Tidak -> 1/0 |
| mitra | created_at | mitra | created_at | jangan buat timestamp nya tp direct mapping ajaa |
| | | | | |
| mitra_note | idmnote | mitra_progres | id_progres_mitra | |
| mitra_note | idmitra | mitra_progres | id_mitra | |
| mitra_note | note | mitra_progres | catatan_progres_mitra | |
| mitra_note | idusers | mitra_progres | id_user | |
| mitra_note | status | mitra_progres | status_progres_mitra | enum('On-going','Transfer','Connect','Done') |
| mitra_note | startdate | mitra_progres | kemitraan_mulai | |
| mitra_note | enddate | mitra_progres | kemitraan_berakhir | |
| mitra_note | created_at | mitra_progres | created_at | jangan buat timestamp nya tp direct mapping ajaa |
| | | | | |
| mitra_users | idmusers | kemitraan_verifikator | id_kemitraan | |
| mitra_users | idmnote | kemitraan_verifikator | id_progres_mitra | |
| mitra_users | idusers | kemitraan_verifikator | id_user | |
| | | | | |
| siswamitra | idsiswa | siswa_mitra | id_sm | kosong |
| siswamitra | tgl_daftar | siswa_mitra | tanggal_daftar | kosong |
| siswamitra | domisili | siswa_mitra | alamat_domisili | kosong |
| siswamitra | nama_lengkap | siswa_mitra | nama_lengkap | kosong |
| siswamitra | panggilan | siswa_mitra | nama_panggilan | kosong |
| siswamitra | jkel | siswa_mitra | jenis_kelamin | kosong |
| siswamitra | nama_instansi | siswa_mitra | nama_instansi | kosong |
| siswamitra | level_sekolah | siswa_mitra | tingkat_sekolah | kosong |
| siswamitra | pekerjaan | siswa_mitra | pekerjaan_sm | kosong |
| siswamitra | tmp_lahir | siswa_mitra | tempat_lahir | kosong |
| siswamitra | tgl_lahir | siswa_mitra | tanggal_lahir | kosong |
| siswamitra | no_induk | siswa_mitra | nomor_induk_sm | kosong |
| siswamitra | email | siswa_mitra | email_sm | kosong |
| siswamitra | tlp | siswa_mitra | wa_sm | kosong |
| siswamitra | keluar | siswa_mitra | status_keluar_sm | kosong |
| siswamitra | idmitra | siswa_mitra | id_mitra | kosong |
| | | siswa_mitra | sertifikat_sm | kosong |
| | | | | |
| siswa_keluar_mitra | idsiswa_keluar | siswa_mitra_keluar | id_sm_keluar | kosong |
| siswa_keluar_mitra | idsiswa | siswa_mitra_keluar | id_sm | kosong |
| siswa_keluar_mitra | alasan | siswa_mitra_keluar | alasan_keluar_sm | kosong |
| siswa_keluar_mitra | tanggal | siswa_mitra_keluar | tanggal_keluar_sm | kosong |

---

### Fase 5

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| format_rapor | idformat_rapor | rapor_format | id_rapor_format | |
| format_rapor | idpendkursus | rapor_format | id_kursus | |
| format_rapor | title | rapor_format | judul_rapor | |
| | | rapor_format | urutan | dari rapor_format_import.csv (left join on judul_rapor, cast Int64) |
| | | | | |
| format_rapor_detil | idformat_rd | rapor_format_sub | id_rapor_format_sub | |
| format_rapor_detil | idformat_rapor | rapor_format_sub | id_rapor_format | |
| format_rapor_detil | subtitle | rapor_format_sub | sub_judul_rapor | |
| | | rapor_format_sub | urutan | dari rapor_format_sub_import.csv (left join on id_rapor_format + sub_judul_rapor, cast Int64) |
| | | | | |
| format_rapor_rumus | idfrr | rapor_format_formula | id_rapor_format_formula | |
| format_rapor_rumus | idformat_rapor | rapor_format_formula | id_rapor_format | |
| format_rapor_rumus | param_operator | rapor_format_formula | logika_operator | |
| | | | | |
| format_rapor_detil_rumus | idfrdr | rapor_format_formula_sub | id_rapor_format_formula_sub | |
| format_rapor_detil_rumus | idformat_rd | rapor_format_formula_sub | id_rapor_format_sub | |
| format_rapor_detil_rumus | param_operator | rapor_format_formula_sub | logika_operator | |
| format_rapor_detil_rumus | idlevel | rapor_format_formula_sub | id_level | |
| | | | | |
| format_raport_level | idformat_rl | rapor_level_config | id_rapor_level_config | |
| format_raport_level | idlevel | rapor_level_config | id_level | |
| format_raport_level | idpendkursus | rapor_level_config | id_kursus | |
| format_raport_level | idformat_rapor | rapor_level_config | id_rapor_format | |
| | | | | |
| | | rapor_sub_level | id_rapor_sub_level | tabel baru |
| | | rapor_sub_level | id_rapor_format_sub | tabel baru |
| | | rapor_sub_level | id_level | tabel baru |
| | | | | |
| rapor | idrapor | rapor_siswa | id_rapor_siswa | |
| rapor | idjadwal | rapor_siswa | id_jadwal | |
| rapor | idsiswa | rapor_siswa | id_siswa | |
| rapor | tanggal | rapor_siswa | tanggal_input | jangan buat timestamp nya tp direct mapping ajaa |
| rapor | idp_nilai | rapor_siswa | id_parameter_nilai | |
| rapor | nilai | rapor_siswa | final_result | |
| | | | | |
| file_rapor_siswa | idfile | rapor_siswa_file | id_rapor_siswa_file | |
| file_rapor_siswa | idsiswa | rapor_siswa_file | id_rapor_siswa | cari id_rapor_siswa di rapor_siswa (db_new) |
| file_rapor_siswa | path | rapor_siswa_file | file_rapor_path | |
| | | | | |
| history_rapor | idhistori | rapor_lacak | id_rapor_lacak | |
| history_rapor | idsiswa | rapor_lacak | id_siswa | |
| history_rapor | idjadwal | rapor_lacak | id_jadwal | |
| history_rapor | tgl | rapor_lacak | tanggal_terkirim | jangan buat waktu nya tp direct mapping ajaa |
| history_rapor | status | rapor_lacak | status_pengiriman | enum('Terkirim','Gagal') |
| history_rapor | | rapor_lacak | id_rapor_siswa_file | cari id_rapor_siswa_file di rapor_siswa_file |

---

## Catatan Perubahan & Penyelesaian Kendala (Sesuai Kondisi Script Aktual)

Semua kendala mapping operasional yang sebelumnya terhambat kini telah diselesaikan 100% pada notebook Jupyter (`script_hanif.ipynb`) di masing-masing fase:

### 🟢 Fase 3: Pemetaan & Auto-Increment Pelamar
* **Tabel Pelamar (`id_pelamar`)**: Mengubah tipe kolom `id_pelamar` menjadi integer auto-increment untuk mengatasi kegagalan integrasi database.
* **Tabel Anak (`pelamar_kerja`, `pelamar_kursus`, `pelamar_sekolah`, `progres_pelamar`, `rekrutmen_pelamar`)**: Kolom `id_pelamar` yang baru berhasil dipetakan secara akurat dari `idusers` lama melalui:
  1. Relasi tabel `pelamar_users` di database lama.
  2. Pencocokan fallback berdasarkan email bersih (`email_clean`).
  3. Pencocokan fallback berdasarkan normalisasi nama lengkap (`clean_name_without_titles`).
* Seluruh foreign key `id_pelamar` dikonversi ke tipe data integer nullable (`Int64`) untuk memastikan konsistensi relasi tanpa desimal.

### 🟢 Fase 4: Struktur Tabel Siswa, Kursus Siswa, & Mitra
* **Tabel `siswa`**:
  * Kolom `status_aktif` dan `status_lulus_siswa` dihapus dari mapping (tidak digunakan lagi di tabel target ini).
  * Menambahkan kolom `status_pendaftaran` yang diambil langsung dari kolom `statussiswa` (varchar) pada database lama.
  * Normalisasi data string pada kolom `agama` (misal 'kristen' -> 'Kristen Protestan', 'katolik' -> 'Katolik', dsb.) dan `pekerjaan_ayah` / `pekerjaan_wali` (ke kategori enum standar seperti 'Pegawai Swasta', 'Wiraswasta', dll.).
* **Tabel `kursus_siswa` (Tabel Baru)**:
  * Berhasil dibangun secara dinamis dengan melakukan join antara tabel `jadwal_siswa` dan `jadwal` di database lama (`db_old`) untuk mendapatkan relasi B2C yang tepat.
  * Kolom `status_lulus` dipetakan dari kolom `lulus` di `db_old.siswa` (jika `lulus == 1.0` -> `1`, selain itu `0`).
  * Kolom `catatan` diisi default `NULL`.
  * *Catatan Skema*: Kolom `status_aktif` tidak dimasukkan ke dalam mapping script `script_hanif.ipynb` (omitted), meskipun ada di skema database target.
* **Tabel `siswa_keluar`**:
  * Kolom `id_kursus` yang sebelumnya kosong kini berhasil diisi secara dinamis dengan mencocokkan `id_siswa` dengan relasi yang terbentuk di tabel `kursus_siswa` di atas.
  * Kolom `id_tag_keluar` berhasil dipetakan menggunakan fungsi `detect_tag()` yang menyeleksi 9 kategori alasan keluar (lulus, jadwal, biaya, domisili, motivasi, akademik, guru, teknologi, keluarga) berdasarkan kata kunci di kolom `alasan`, dikombinasikan dengan data dari tabel `siswa_keluar_tag` lama.
* **Tabel `mitra`**:
  * Kolom bertipe boolean (`leapverse`, `kemitraan`, `elsa`, `classin`, `mitraleap`) dikonversi secara bersih dari format string Ya/Tidak menjadi integer `1`/`0`.
  * `id_mitra` menyimpan nilai integer dari `idmitra` lama, sementara `kode_mitra` menyimpan prefiks karakternya (misalnya `'M0001'` -> `id_mitra = 1`, `kode_mitra = 'M'`).
  * Relasi wilayah `provinsi_id` dan `kabupaten_id` dipetakan melalui pencocokan nama wilayah secara hierarkis (*Clean-Name Hierarchical Matching*) ke ID baru.
* **Tabel `mitra_progres`**:
  * Menghubungkan progres ke tabel `mitra` dengan mencocokkan `kode_mitra` ke data `id_mitra` hasil migrasi.
  * Menangani nilai `NULL` pada kolom wajib isi `kemitraan_mulai` dan `kemitraan_berakhir` dengan fallback logis ke tanggal pembuatan data (`created_at`) atau default `2023-01-01`.

### 🟢 Fase 5: Sinkronisasi Rapor & Relasi Dokumen
* **Tabel `rapor_format` & `rapor_format_sub`**:
  * Kolom `urutan` berhasil ditambahkan dengan melakukan merge data dari file CSV urutan manual (`rapor_format_import.csv` & `rapor_format_sub_import.csv`) menggunakan tipe data `Int64`.
* **Tabel `rapor_format_formula_sub`**:
  * Kolom `urutan` tidak ditransformasikan di dalam script `script_hanif.ipynb` (omitted), meskipun ada di skema database target.
* **Tabel `rapor_siswa_file` & `rapor_lacak`**:
  * Mengatasi kendala nilai `id_rapor_siswa` dan `id_rapor_siswa_file` yang NULL. Solusinya adalah dengan melakukan pencocokan data `idsiswa` & `idjadwal` dari tabel file ke mapping ID rapor yang digenerate sebelum ekspor data.
  * Mengonversi string ID lama berformat `'Pxxxxx'` (misal `'P00745'`) di kolom `idp_nilai` ke auto-increment `id_parameter_nilai` baru secara berurutan sesuai urutan di database lama agar sinkron dengan tabel parameter nilai Fase 2.
  * Mengonversi string ID berformat `'Hxxxxx'` pada `idhistori` ke integer murni menggunakan fungsi `extract_int`.

### 🧹 Format Output Ekspor CSV & Pickle
* Seluruh file ekspor CSV untuk proses verifikasi (25 tabel) disimpan langsung ke folder `extract/cek_csv/` tanpa imbuhan kata `_export` pada nama file atau direktori.
* Seluruh kolom ID/FK (seperti `id_siswa`, `id_mitra`, `id_provinsi`, dll.) dibersihkan secara otomatis di akhir notebook dengan melakukan cast ke tipe data Pandas `Int64` untuk menghilangkan desimal `.0` (misal `1.0` -> `1`) dan memastikan nilai kosong ter-render sebagai string kosong murni (`""`) pada file CSV.
* Seluruh tipe data string Pandas (`string` / `string[python]`) di-cast ke tipe data `object` sebelum proses penyimpanan Pickle untuk memastikan kompatibilitas penuh dengan serializer Python 3.13.

---

### 🟢 Update 24 Juni 2026: Sinkronisasi Skema & Validasi Data Lapangan

Guna mengatasi kegagalan integrasi database (*warnings* dan *FK constraint failures*) saat proses *insert* aktual, telah dilakukan pembaruan implementasi pemetaan dan pembersihan data di seluruh notebook Hanif:

#### 1. Pembersihan Khusus No WA Siswa (`siswa`)
* **Masalah**: Kolom `wa_siswa`, `wa_ortu`, dan `wa_administrasi` di database baru dibatasi `VARCHAR(20)`. Data lama mengandung nilai kotor (beberapa nomor digabung dengan slash `/` atau dibubuhi teks deskripsi) yang memicu error *data truncated*.
* **Solusi**: Diterapkan fungsi pembersih khusus `clean_wa_number` pada Fase 4:
  1. Jika terdapat karakter slash `/`, hanya potongan teks sebelum slash pertama yang diambil.
  2. Karakter non-angka dan non-simbol `+` dibersihkan sepenuhnya.
  3. Hasil akhir dipotong maksimal 15 karakter angka/simbol (sesuai panjang normal nomor telepon lokal/internasional) sehingga dijamin masuk ke kolom `VARCHAR(20)`.

#### 2. Auto-Increment & Pemetaan Dinamis ID Siswa (`mapping_siswa`)
* **Masalah**: Kolom `id_siswa` di database baru (`db_new.siswa`) bertipe integer auto-increment, sehingga database akan menghasilkan nilai `1, 2, 3, dst.` secara otomatis sesuai urutan sisipan. Pemetaan sebelumnya menggunakan `extract_int(idsiswa)` yang memicu ketidaksinronan relasi dengan tabel anak karena adanya celah (*gaps*) nomor pada ID lama.
* **Solusi**:
  1. Kolom `id_siswa` dihapus dari DataFrame `siswa` di berkas ekspor `fase_4_hanif.pkl`. Hal ini membiarkan MySQL mengelola nilai auto-increment secara natural.
  2. Berkas pemetaan (`idsiswa_lama` ke `id_siswa_baru`) dibuat secara dinamis menggunakan urutan baris (`index + 1`) DataFrame siswa (misal: `'S0000007'` sebagai baris pertama dipetakan ke ID baru `1`).
  3. Hasil pemetaan diekspor secara terpisah ke `fase_4/mapping_siswa.pkl` (juga disisipkan dalam dictionary utama berkas `.pkl`) dan `extract/cek_csv/mapping_siswa.csv` untuk keperluan audit manual.

#### 3. Penyelarasan Relasi Lintas Tabel & Lintas Fase
* **Fase 4 (`kursus_siswa`, `siswa_keluar`)**: Kolom `id_siswa` yang menjadi Foreign Key kini dipetakan menggunakan `student_id_map` hasil pemetaan auto-increment dinamis di atas. Kolom `id_kursus` dikembalikan ke format string asli (seperti `'K00001'`) untuk mencocokkan tipe data VARCHAR pada skema `kursus` database baru.
* **Fase 5 (`rapor_siswa`, `rapor_lacak`)**: Ditambahkan mekanisme otomatis pada awal proses transformasi untuk memuat berkas pemetaan `../fase_4/mapping_siswa.pkl` secara dinamis. Kolom `id_siswa` pada tabel-tabel rapor ini diselaraskan sepenuhnya dengan ID baru siswa berdasarkan hasil pemetaan tersebut.

#### 4. Pembersihan Data Pelamar (`pelamar`)
* **Pembersihan Tanggal**: Mengubah nilai pengisian default untuk kolom `created_at` yang kosong dari `'1970-01-01'` menjadi `'2020-01-01 00:00:00'`. Ini mencegah kegagalan konversi zona waktu lokal (WIB/UTC+7) ke UTC yang sebelumnya menghasilkan waktu `'1969-12-31'` (di luar batas minimum tipe data `TIMESTAMP` MySQL).
* **Pembersihan Nilai Integer**: Kolom `toefl` (skor TOEFL) dan `hasiliq` (skor IQ) dibersihkan secara ketat menggunakan `pd.to_numeric` dengan `errors='coerce'` untuk mengubah string kotor seperti `'asd'` menjadi `NaN` lalu diisi dengan `0` sebelum dikonversi ke tipe integer. Hal ini menghilangkan kegagalan input tipe data pada kolom tujuan.

---

### 🟢 Update Tambahan 24 Juni 2026: Sinkronisasi Tabel Auto-Increment Induk & Pemetaan Offline Lintas Fase

Guna menyelaraskan data dengan sistem auto-increment di database target (`db_new`) serta menyelaraskan pemetaan yang dikerjakan oleh anggota tim lain tanpa bergantung pada koneksi database aktif (*fully offline-friendly*), telah diimplementasikan arsitektur pemetaan ID baru:

#### 1. Penghapusan Kolom PK Auto-Increment pada Seluruh Tabel
* Berdasarkan aturan bahwa seluruh tabel baru menggunakan primary key auto-increment bertipe integer (yang akan di-assign otomatis oleh MySQL mulai dari `1, 2, 3, dst.`), **seluruh kolom Primary Key (PK) asli dari database lama telah dihapus dari DataFrame hasil transformasi** di semua notebook Hanif sebelum diekspor ke berkas Pickle (`.pkl`). Hal ini mencegah kegagalan *duplicate key* atau bentrok tipe data saat proses *insert*.
* Tabel-tabel yang kolom PK-nya dihapus meliputi:
  * **Fase 3**: `pelamar`, `pelamar_kerja`, `pelamar_sekolah`, `pelamar_kursus`, `progres_pelamar`, `rekrutmen_pelamar`, `pengajuan_karyawan`, `histori_pengajuan`.
  * **Fase 4**: `siswa`, `mitra`, `mitra_progres`, `kemitraan_verifikator`, `siswa_mitra`, `siswa_mitra_keluar`, `siswa_keluar`.
  * **Fase 5**: `rapor_siswa`, `rapor_siswa_file`, `rapor_lacak`, `rapor_format_formula`, `rapor_format_formula_sub`, `rapor_level_config`, `rapor_sub_level`.

#### 2. Pembuatan Berkas Pemetaan (Mapping Files) untuk Tabel Induk
* Untuk setiap **Tabel Induk (Parent Table)** yang memiliki relasi Foreign Key (FK) ke tabel anak, kita membuat berkas pemetaan (`id_lama` ke `id_baru`) secara dinamis berdasarkan urutan baris (`index + 1`) setelah DataFrame diurutkan secara deterministik.
* Berkas pemetaan ini disimpan dalam format **Pickle (`.pkl`)** di direktori fase masing-masing untuk digunakan oleh script, dan format **CSV (`.csv`)** di `extract/cek_csv/` untuk keperluan audit manual oleh tim.
* Daftar berkas pemetaan yang dihasilkan:
  1. **Fase 3**:
     * `fase_3/mapping_pelamar.pkl` / `mapping_pelamar.csv` (untuk tabel `pelamar`)
     * `fase_3/mapping_pengajuan_karyawan.pkl` / `mapping_pengajuan_karyawan.csv` (untuk tabel `pengajuan_karyawan`)
  2. **Fase 4**:
     * `fase_4/mapping_siswa.pkl` / `mapping_siswa.csv` (untuk tabel `siswa`)
     * `fase_4/mapping_mitra.pkl` / `mapping_mitra.csv` (untuk tabel `mitra`)
     * `fase_4/mapping_mitra_progres.pkl` / `mapping_mitra_progres.csv` (untuk tabel `mitra_progres`)
     * `fase_4/mapping_siswa_mitra.pkl` / `mapping_siswa_mitra.csv` (untuk tabel `siswa_mitra`)
  3. **Fase 5**:
     * `fase_5/mapping_rapor_siswa.pkl` / `mapping_rapor_siswa.csv` (untuk tabel `rapor_siswa`)
     * `fase_5/mapping_rapor_siswa_file.pkl` / `mapping_rapor_siswa_file.csv` (untuk tabel `rapor_siswa_file`)

#### 3. Penyelarasan FK Lintas Tabel & Lintas Fase Secara Offline (In-Memory)
* **Penyelarasan Lintas Tabel**: Kolom Foreign Key pada seluruh tabel anak (seperti `id_pelamar` pada riwayat pelamar, `id_mitra` pada progres mitra, dan `id_sm` pada progres siswa mitra) kini dipetakan secara dinamis menggunakan dictionary mapping yang dibentuk *in-memory* dari data tabel induk. Ini menjamin relasi antar data tetap utuh 100% saat masuk ke database baru.
* **Penyelarasan Lintas Fase**: Kolom `id_siswa` pada tabel rapor di Fase 5 (`rapor_siswa`, `rapor_lacak`) kini disinkronkan secara offline dengan memuat berkas pemetaan `../fase_4/mapping_siswa.pkl` pada awal proses transformasi. Hal ini membuat integrasi antar fase sangat kokoh dan tidak bergantung pada apakah data Fase 4 sudah masuk ke database baru atau belum.

#### 4. Pembersihan Kolom Alamat Domisili (`siswa`)
* **Masalah**: Kolom `domisili` pada tabel `siswa` di database baru memiliki batasan panjang karakter. Data lama yang kotor sering kali berisi alamat lengkap beserta keterangan RT/RW atau catatan tambahan yang sangat panjang, memicu error *data truncated*.
* **Solusi**: Diterapkan fungsi pembersihan khusus `clean_domisili` pada Fase 4 yang melakukan pemotongan (*slicing*) data pada karakter koma pertama (`,`) yang ditemukan (untuk mengambil nama wilayah/kota domisili saja), melakukan *strip* spasi, dan membatasi panjang teks maksimal 100 karakter. Ini memastikan data domisili bersih dan dijamin lolos validasi database baru.
