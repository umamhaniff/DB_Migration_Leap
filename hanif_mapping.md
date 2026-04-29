# Hanif - Mapping

## Fase 3

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru |
| :--- | :--- | :--- | :--- |
| pengajuan | idpengajuan | pengajuan_karyawan | id_pengajuan |
| pengajuan | idusers | pengajuan_karyawan | id_user |
| pengajuan | keterangan | pengajuan_karyawan | posisi |
| pengajuan | jumlah | pengajuan_karyawan | jumlah |
| pengajuan | syarat | pengajuan_karyawan | syarat |
| pengajuan | pertanyaan | pengajuan_karyawan | pertanyaan |
| pengajuan | alur | pengajuan_karyawan | alur_seleksi |
| pengajuan | test | pengajuan_karyawan | daftar_tes |
| pengajuan | status | pengajuan_karyawan | status |
| pengajuan | created_at | pengajuan_karyawan | created_at |
| histori_pengajuan | idhistori | histori_pengajuan | id_verifikasi |
| histori_pengajuan | idpengajuan | histori_pengajuan | id_pengajuan |
| histori_pengajuan | status | histori_pengajuan | status_verifikasi_pengajuan |
| histori_pengajuan | catatan | histori_pengajuan | catatan |
| histori_pengajuan | created_at | histori_pengajuan | created_at |
| pelamar | idpelamar | pelamar | id_pelamar |
| pelamar | idpengajuan | pelamar | id_pengajuan |
| pelamar | email | pelamar | email_pelamar |
| pelamar | nama | pelamar | nama_lengkap |
| pelamar | panggilan | pelamar | nama_panggilan |
| pelamar | jk | pelamar | jenis_kelamin |
| pelamar | | pelamar | tempat_lahir |
| pelamar | ttl | pelamar | tanggal_lahir |
| pelamar | alamat | pelamar | alamat_ktp |
| pelamar | domisili | pelamar | alamat_domisili |
| pelamar | wa | pelamar | nomor_wa |
| pelamar | linkedin | pelamar | akun_linkedin |
| pelamar | ig | pelamar | akun_instagram |
| pelamar | fb | pelamar | akun_facebook |
| pelamar | sosmed | pelamar | sosmed_lain |
| pelamar | laptop | pelamar | spesifikasi_laptop |
| pelamar | internet | pelamar | internet |
| pelamar | kegiatan | pelamar | kegiatan_sekarang |
| pelamar | rencana | pelamar | rencana_karir |
| pelamar | mobilitas | pelamar | mobilitas |
| pelamar | info | pelamar | sumber_info |
| pelamar | wfo | pelamar | siap_wfo |
| pelamar | bergabung | pelamar | tanggal_bergabung |
| pelamar | jenis | pelamar | kategori_pelamar |
| pelamar | work | pelamar | riwayat_kerja |
| pelamar | ppdk | pelamar | riwayat_pendidikan |
| pelamar | pengalaman | pelamar | pengalaman_bidang |
| pelamar | wawasan | pelamar | wawasan |
| pelamar | sehat | pelamar | riwayat_kesehatan |
| pelamar | statusnikah | pelamar | status_pernikahan |
| pelamar | ajar | pelamar | kemampuan_ajar |
| pelamar | app | pelamar | penguasaan_aplikasi |
| pelamar | apps | pelamar | aplikasi_lainnya |
| pelamar | gunalaptop | pelamar | penggunaan_laptop |
| pelamar | toefl | pelamar | skor_toefl |
| pelamar | gaji | pelamar | ekspektasi_gaji |
| pelamar | link | pelamar | tautan_berkas |
| pelamar | resign | pelamar | alasan_resign |
| pelamar | hasiliq | pelamar | skor_iq |
| pelamar | piciq | pelamar | foto_iq |
| pelamar | picminat | pelamar | foto_minat |
| pelamar | picpribadi | pelamar | foto_kepribadian |
| pelamar | created_at | pelamar | created_at |
| pekerjaan | idpekerjaan | pelamar_kerja | id_pelamar_kerja |
| pekerjaan | idusers | pelamar_kerja | id_pelamar |
| pekerjaan | namaperusahaan | pelamar_kerja | nama_perusahaan |
| pekerjaan | periode | pelamar_kerja | periode |
| pekerjaan | jabatan | pelamar_kerja | jabatan |
| pekerjaan | jobdesk | pelamar_kerja | deskripsi_kerja |
| pendidikan | idpendidikan | pelamar_sekolah | id_pelamar_sekolah |
| pendidikan | idusers | pelamar_sekolah | id_pelamar |
| pendidikan | sekolah | pelamar_sekolah | nama_sekolah |
| pendidikan | jenjang | pelamar_sekolah | jenjang |
| pendidikan | prodi | pelamar_sekolah | prodi |
| pendidikan | tahun | pelamar_sekolah | tahun_lulus |
| pendidikan | ipk | pelamar_sekolah | ipk |
| pendidikan | organisasi | pelamar_sekolah | organisasi |
| kursus | idkursus | pelamar_kursus | id_pelamar_kursus |
| kursus | idusers | pelamar_kursus | id_pelamar |
| kursus | nama | pelamar_kursus | nama_kursus |
| kursus | tanggal | pelamar_kursus | tanggal |
| kursus | deskripsi | pelamar_kursus | deskripsi |
| kursus | lokasi | pelamar_kursus | lokasi |
| kursus | nosertifikat | pelamar_kursus | nomor_sertifikat |
| pelamar_note | idnote | progres_pelamar | id_progres_pelamar |
| pelamar_note | idpelamar | progres_pelamar | id_pelamar |
| pelamar_note | idusers | progres_pelamar | id_user |
| pelamar_note | status | progres_pelamar | status_progres_pelamar |
| pelamar_note | note | progres_pelamar | catatan |
| pelamar_note | link | progres_pelamar | tautan_file |
| pelamar_note | pertanyaan | progres_pelamar | pertanyaan |
| pelamar_note | created_at | progres_pelamar | created_at |
| pelamar_users | idassign | rekrutmen_pelamar | id_rekrutmen |
| pelamar_users | idpelamar | rekrutmen_pelamar | id_pelamar |
| pelamar_users | idusers | rekrutmen_pelamar | id_user |

---

## Fase 4

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru |
| :--- | :--- | :--- | :--- |
| siswa | idsiswa | siswa | id_siswa |
| siswa | tgl_daftar | siswa | tanggal_registrasi |
| siswa | domisili | siswa | domisili |
| siswa | nama_lengkap | siswa | nama_lengkap |
| siswa | panggilan | siswa | nama_panggilan |
| siswa | jkel | siswa | jenis_kelamin |
| siswa | nama_sekolah | siswa | asal_sekolah |
| siswa | level_sekolah | siswa | tingkat_sekolah |
| siswa | nama_ortu | siswa | nama_orang_tua |
| siswa | pekerjaan_ortu | siswa | pekerjaan_orang_tua |
| siswa | tmp_lahir | siswa | tempat_lahir |
| siswa | tgl_lahir | siswa | tanggal_lahir |
| siswa | no_induk | siswa | nomor_induk |
| siswa | email | siswa | email |
| siswa | idcalon | siswa | id_calon |
| siswa | provinsi | siswa | id_provinsi |
| siswa | kabupaten | siswa | id_kabupaten |
| siswa | kecamatan | siswa | id_kecamatan |
| siswa | kelurahan | siswa | id_kelurahan |
| siswa | idmitra | siswa | id_mitra |
| siswa | nisn | siswa | nisn |
| siswa | nik | siswa | nik |
| siswa | kewarganegaraan | siswa | kewarganegaraan |
| siswa | agama | siswa | agama |
| siswa | rt | siswa | rt |
| siswa | rw | siswa | rw |
| siswa | kodepos | siswa | kode_pos |
| siswa | statussiswa | siswa | status_aktif |
| siswa | rekomen | siswa | rekomendasi |
| siswa | info | siswa | sumber_info |
| siswa | pembayaran | siswa | metode_pembayaran |
| siswa | nama_ayah | siswa | nama_ayah |
| siswa | pekerjaan_ayah | siswa | pekerjaan_ayah |
| siswa | jenjang_ayah | siswa | pendidikan_ayah |
| siswa | penghasilan_ayah | siswa | penghasilan_ayah |
| siswa | nama_ibu | siswa | nama_ibu |
| siswa | penghasilan_ibu | siswa | penghasilan_ibu |
| siswa | | siswa | pekerjaan_ibu |
| siswa | jenjang_ibu | siswa | pendidikan_ibu |
| siswa | nama_wali | siswa | nama_wali |
| siswa | pekerjaan_wali | siswa | pekerjaan_wali |
| siswa | jenjang_wali | siswa | pendidikan_wali |
| siswa | penghasilan_wali | siswa | penghasilan_wali |
| siswa | wapeserta | siswa | wa_siswa |
| siswa | wawalmur | siswa | wa_ortu |
| siswa | waadmin | siswa | wa_administrasi |
| siswa | sts_pengisian | siswa | status_pengisian |
| siswa | bukti | siswa | path_bukti_bayar |
| siswa | lulus | siswa | status_lulus_siswa |
| siswa | created_bukti | siswa | tanggal_upload_bukti |
| siswa | | siswa | deleted_at |
| | | kursus_siswa | id_kursus_siswa |
| | | kursus_siswa | id_siswa |
| | | kursus_siswa | id_kursus |
| | | kursus_siswa | tanggal_mulai |
| | | kursus_siswa | metode_belajar |
| | | kursus_siswa | status_aktif |
| | | kursus_siswa | catatan |
| siswa_keluar | idsiswa_keluar | siswa_keluar | id_keluar |
| siswa_keluar | idsiswa | siswa_keluar | id_siswa |
| siswa_keluar | | siswa_keluar | id_kursus |
| siswa_keluar | alasan | siswa_keluar | alasan_keluar |
| siswa_keluar | tanggal | siswa_keluar | tanggal_keluar |
| siswa_keluar | | siswa_keluar | id_tag_keluar |
| mitra | idmitra | mitra | id_mitra |
| mitra | | mitra | kode_mitra |
| mitra | nama | mitra | nama_mitra |
| mitra | instansi | mitra | nama_instansi |
| mitra | namasekolah | mitra | nama_sekolah |
| mitra | lokasi | mitra | alamat_mitra |
| mitra | kepsek | mitra | nama_pimpinan |
| mitra | cp | mitra | kontak_mitra |
| mitra | status | mitra | status_mitra |
| mitra | visimisi | mitra | visi_misi |
| mitra | program | mitra | program_mitra |
| mitra | sdm | mitra | info_sdm |
| mitra | weakness | mitra | info_kelemahan |
| mitra | rekomen | mitra | rekomendasi_program |
| mitra | jenis | mitra | jenis_mitra |
| mitra | provinsi | mitra | provinsi_id |
| mitra | kotkab | mitra | kabupaten_id |
| mitra | jml | mitra | jumlah_siswa_mitra |
| mitra | bidang | mitra | bidang_usaha |
| mitra | leapverse | mitra | is_leapverse |
| mitra | kemitraan | mitra | status_kemitraan |
| mitra | tahun | mitra | tahun_bergabung |
| mitra | jeniskemitraan | mitra | tipe_kerjasama |
| mitra | elsa | mitra | is_elsa |
| mitra | classin | mitra | is_classin |
| mitra | mitraleap | mitra | is_mitra_leap |
| mitra | created_at | mitra | created_at |
| mitra_note | idmnote | mitra_progres | id_progres_mitra |
| mitra_note | idmitra | mitra_progres | id_mitra |
| mitra_note | note | mitra_progres | catatan_progres_mitra |
| mitra_note | idusers | mitra_progres | id_user |
| mitra_note | status | mitra_progres | status_progres_mitra |
| mitra_note | startdate | mitra_progres | kemitraan_mulai |
| mitra_note | enddate | mitra_progres | kemitraan_berakhir |
| mitra_note | created_at | mitra_progres | created_at |
| mitra_users | idmusers | kemitraan_verifikator | id_kemitraan |
| mitra_users | idnote | kemitraan_verifikator | id_progres_mitra |
| mitra_users | idusers | kemitraan_verifikator | id_user |
| siswamitra | idsiswa | siswa_mitra | id_sm |
| siswamitra | tgl_daftar | siswa_mitra | tanggal_daftar |
| siswamitra | domisili | siswa_mitra | alamat_domisili |
| siswamitra | nama_lengkap | siswa_mitra | nama_lengkap |
| siswamitra | panggilan | siswa_mitra | nama_panggilan |
| siswamitra | jkel | siswa_mitra | jenis_kelamin |
| siswamitra | nama_instansi | siswa_mitra | nama_instansi |
| siswamitra | level_sekolah | siswa_mitra | tingkat_sekolah |
| siswamitra | pekerjaan | siswa_mitra | pekerjaan_sm |
| siswamitra | tmp_lahir | siswa_mitra | tempat_lahir |
| siswamitra | tgl_lahir | siswa_mitra | tanggal_lahir |
| siswamitra | no_induk | siswa_mitra | nomor_induk_sm |
| siswamitra | email | siswa_mitra | email_sm |
| siswamitra | tlp | siswa_mitra | wa_sm |
| siswamitra | keluar | siswa_mitra | status_keluar_sm |
| siswamitra | idmitra | siswa_mitra | id_mitra |
| siswamitra | | siswa_mitra | sertifikat_sm |
| siswa_keluar_mitra | idsiswa_keluar | siswa_mitra_keluar | id_sm_keluar |
| siswa_keluar_mitra | idsiswa | siswa_mitra_keluar | id_sm |
| siswa_keluar_mitra | alasan | siswa_mitra_keluar | alasan_keluar_sm |
| siswa_keluar_mitra | tanggal | siswa_mitra_keluar | tanggal_keluar_sm |

---

## Fase 5

| Tabel Lama | Kolom Lama | Tabel Baru | Kolom Baru |
| :--- | :--- | :--- | :--- |
| format_rapor | idformat_rapor | rapor_format | id_rapor_format |
| format_rapor | idpendkursus | rapor_format | id_kursus |
| format_rapor | title | rapor_format | judul_rapor |
| format_rapor_detil | idformat_rd | rapor_format_sub | id_rapor_format_sub |
| format_rapor_detil | idformat_rapor | rapor_format_sub | id_rapor_format |
| format_rapor_detil | subtitle | rapor_format_sub | sub_judul_rapor |
| format_rapor_rumus | idfrr | rapor_format_formula | id_rapor_format_formula |
| format_rapor_rumus | idformat_rapor | rapor_format_formula | id_rapor_format |
| format_rapor_rumus | param_operator | rapor_format_formula | logika_operator |
| format_rapor_detil_rumus | idfrdr | rapor_format_formula_sub | id_rapor_format_formula_sub |
| format_rapor_detil_rumus | idformat_rd | rapor_format_formula_sub | id_rapor_format_sub |
| format_rapor_detil_rumus | param_operator | rapor_format_formula_sub | logika_operator |
| format_rapor_detil_rumus | idlevel | rapor_format_formula_sub | id_level |
| format_raport_level | idformat_rl | rapor_level_config | id_rapor_level_config |
| format_raport_level | idlevel | rapor_level_config | id_level |
| format_raport_level | idpendkursus | rapor_level_config | id_kursus |
| format_raport_level | idformat_rapor | rapor_level_config | id_rapor_format |
| | | rapor_sub_level | id_rapor_sub_level |
| | | rapor_sub_level | id_rapor_format_sub |
| | | rapor_sub_level | id_level |
| rapor | idrapor | rapor_siswa | id_rapor_siswa |
| rapor | idjadwal | rapor_siswa | id_jadwal |
| rapor | idsiswa | rapor_siswa | id_siswa |
| rapor | tanggal | rapor_siswa | tanggal_input |
| rapor | idp_nilai | rapor_siswa | id_parameter_nilai |
| rapor | nilai | rapor_siswa | final_result |
| file_rapor_siswa | idfile | rapor_siswa_file | id_rapor_siswa_file |
| file_rapor_siswa | idsiswa | rapor_siswa_file | id_rapor_siswa |
| file_rapor_siswa | path | rapor_siswa_file | file_rapor_path |
| history_rapor | idhistori | rapor_lacak | id_rapor_lacak |
| history_rapor | idsiswa | rapor_lacak | id_siswa |
| history_rapor | idjadwal | rapor_lacak | id_jadwal |
| history_rapor | tgl | rapor_lacak | tanggal_terkirim |
| history_rapor | status | rapor_lacak | status_pengiriman |
| history_rapor | | rapor_lacak | id_rapor_siswa_file |

---
