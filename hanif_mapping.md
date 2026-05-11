# Hanif - Mapping

## Fase 3

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

## Fase 4

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
| siswa | provinsi | siswa | id_provinsi | |
| siswa | kabupaten | siswa | id_kabupaten | |
| siswa | kecamatan | siswa | id_kecamatan | |
| siswa | kelurahan | siswa | id_kelurahan | |
| siswa | idmitra | siswa | id_mitra | ambil nilai int nya di db_old |
| siswa | nisn | siswa | nisn | |
| siswa | nik | siswa | nik | |
| siswa | kewarganegaraan | siswa | kewarganegaraan | |
| siswa | agama | siswa | agama | enum('Islam','Kristen Protestan','Katolik','Hindu','Buddha','Konghucu') |
| siswa | rt | siswa | rt | |
| siswa | rw | siswa | rw | |
| siswa | kodepos | siswa | kode_pos | |
| siswa | keluar | siswa | status_aktif | |
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
| siswa | lulus | siswa | status_lulus_siswa | |
| siswa | created_bukti | siswa | tanggal_upload_bukti | |
| | | siswa | deleted_at | kolom baru |
| | | | | |
| | | kursus_siswa | id_kursus_siswa | tabel baru |
| | | kursus_siswa | id_siswa | tabel baru |
| | | kursus_siswa | id_kursus | tabel baru |
| | | kursus_siswa | tanggal_mulai | tabel baru |
| | | kursus_siswa | metode_belajar | tabel baru |
| | | kursus_siswa | status_aktif | tabel baru |
| | | kursus_siswa | catatan | tabel baru |
| | | | | |
| siswa_keluar | idsiswa_keluar | siswa_keluar | id_keluar | |
| siswa_keluar | idsiswa | siswa_keluar | id_siswa | |
| | | siswa_keluar | id_kursus | kolom baru |
| siswa_keluar | alasan | siswa_keluar | alasan_keluar | |
| siswa_keluar | tanggal | siswa_keluar | tanggal_keluar | |
| | | siswa_keluar | id_tag_keluar | cek kolom alasan_keluar & keterangan_keluar |
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

## Fase 5

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| format_rapor | idformat_rapor | rapor_format | id_rapor_format | |
| format_rapor | idpendkursus | rapor_format | id_kursus | |
| format_rapor | title | rapor_format | judul_rapor | |
| | | | | |
| format_rapor_detil | idformat_rd | rapor_format_sub | id_rapor_format_sub | |
| format_rapor_detil | idformat_rapor | rapor_format_sub | id_rapor_format | |
| format_rapor_detil | subtitle | rapor_format_sub | sub_judul_rapor | |
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
