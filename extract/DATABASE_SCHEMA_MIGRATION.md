# Database Schema Documentation - Migration

**Database**: dataleap_v5_migration  
**Generated**: 2026-04-21 13:32:38

## Summary
- **Total Tables**: 104
- **Total Rows**: 91,267

## Table of Contents

1. [absensi](#absensi)
2. [activity_log](#activity_log)
3. [admin_sarpras](#admin_sarpras)
4. [bidang_kategori](#bidang_kategori)
5. [bidang_link](#bidang_link)
6. [busdev_bidang](#busdev_bidang)
7. [cache](#cache)
8. [cache_locks](#cache_locks)
9. [calon_siswa](#calon_siswa)
10. [calon_siswa_akademik](#calon_siswa_akademik)
11. [calon_siswa_bayar](#calon_siswa_bayar)
12. [calon_siswa_jadwal](#calon_siswa_jadwal)
13. [calon_siswa_kursus](#calon_siswa_kursus)
14. [calon_siswa_ortu](#calon_siswa_ortu)
15. [calon_siswa_proses](#calon_siswa_proses)
16. [calon_siswa_status_logs](#calon_siswa_status_logs)
17. [catatan_kelas](#catatan_kelas)
18. [catatan_kelas_tag](#catatan_kelas_tag)
19. [catatan_mingguan](#catatan_mingguan)
20. [catatan_siswa](#catatan_siswa)
21. [division_user](#division_user)
22. [divisions](#divisions)
23. [failed_jobs](#failed_jobs)
24. [followup_cs](#followup_cs)
25. [histori_pengajuan](#histori_pengajuan)
26. [izin_karyawan](#izin_karyawan)
27. [jadwal](#jadwal)
28. [jadwal_detail](#jadwal_detail)
29. [jadwal_detail_logs](#jadwal_detail_logs)
30. [jadwal_hari](#jadwal_hari)
31. [jadwal_pengajar](#jadwal_pengajar)
32. [jadwal_siswa](#jadwal_siswa)
33. [job_batches](#job_batches)
34. [jobs](#jobs)
35. [kabupaten](#kabupaten)
36. [karyawan](#karyawan)
37. [karyawan_resign](#karyawan_resign)
38. [kecamatan](#kecamatan)
39. [keluarga_karyawan](#keluarga_karyawan)
40. [kelurahan](#kelurahan)
41. [kemitraan_verifikator](#kemitraan_verifikator)
42. [kontak_prospek](#kontak_prospek)
43. [kursus](#kursus)
44. [kursus_level](#kursus_level)
45. [kursus_libur](#kursus_libur)
46. [kursus_siswa](#kursus_siswa)
47. [level](#level)
48. [libur](#libur)
49. [log_aktivitas](#log_aktivitas)
50. [migrations](#migrations)
51. [mitra](#mitra)
52. [mitra_progres](#mitra_progres)
53. [model_has_permissions](#model_has_permissions)
54. [model_has_roles](#model_has_roles)
55. [mou](#mou)
56. [parameter_nilai](#parameter_nilai)
57. [password_reset_tokens](#password_reset_tokens)
58. [pelamar](#pelamar)
59. [pelamar_kerja](#pelamar_kerja)
60. [pelamar_kursus](#pelamar_kursus)
61. [pelamar_sekolah](#pelamar_sekolah)
62. [peminjaman](#peminjaman)
63. [pengadaan](#pengadaan)
64. [pengajuan_karyawan](#pengajuan_karyawan)
65. [periode](#periode)
66. [permissions](#permissions)
67. [presensi_siswa](#presensi_siswa)
68. [problem](#problem)
69. [progres_pelamar](#progres_pelamar)
70. [provinsi](#provinsi)
71. [rapor_format](#rapor_format)
72. [rapor_format_formula](#rapor_format_formula)
73. [rapor_format_formula_sub](#rapor_format_formula_sub)
74. [rapor_format_sub](#rapor_format_sub)
75. [rapor_lacak](#rapor_lacak)
76. [rapor_level_config](#rapor_level_config)
77. [rapor_siswa](#rapor_siswa)
78. [rapor_siswa_file](#rapor_siswa_file)
79. [rapor_sub_level](#rapor_sub_level)
80. [rekrutmen_pelamar](#rekrutmen_pelamar)
81. [role_has_permissions](#role_has_permissions)
82. [roles](#roles)
83. [sesi](#sesi)
84. [sessions](#sessions)
85. [shift_kerja](#shift_kerja)
86. [siswa](#siswa)
87. [siswa_keluar](#siswa_keluar)
88. [siswa_mitra](#siswa_mitra)
89. [siswa_mitra_keluar](#siswa_mitra_keluar)
90. [sop](#sop)
91. [sop_kategori](#sop_kategori)
92. [surat_keluar](#surat_keluar)
93. [surat_tugas](#surat_tugas)
94. [surat_tugas_anggota](#surat_tugas_anggota)
95. [syarat_resign](#syarat_resign)
96. [tag_siswa_keluar](#tag_siswa_keluar)
97. [topik_diskusi](#topik_diskusi)
98. [ttd](#ttd)
99. [users](#users)
100. [verifikasi_absensi](#verifikasi_absensi)
101. [verifikasi_izin](#verifikasi_izin)
102. [verifikasi_surat_keluar](#verifikasi_surat_keluar)
103. [web_berita](#web_berita)
104. [web_statistik](#web_statistik)

---

## absensi

| Property | Value |
|----------|-------|
| **Columns** | 15 |
| **Rows** | 0 |

### Columns (15)

| # | Column Name |
|---|-------------|
| 1 | `id_absensi` |
| 2 | `id_karyawan` |
| 3 | `id_izin` |
| 4 | `tanggal` |
| 5 | `jam_masuk` |
| 6 | `jam_keluar` |
| 7 | `catatan_masuk` |
| 8 | `catatan_keluar` |
| 9 | `status_absensi` |
| 10 | `tipe_absensi` |
| 11 | `id_verifikasi_absensi` |
| 12 | `created_at` |
| 13 | `absensi_id_izin_foreign` |
| 14 | `absensi_id_karyawan_foreign` |
| 15 | `absensi_id_verifikasi_absensi_foreign` |

## activity_log

| Property | Value |
|----------|-------|
| **Columns** | 12 |
| **Rows** | 0 |

### Columns (12)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `log_name` |
| 3 | `description` |
| 4 | `subject_type` |
| 5 | `event` |
| 6 | `subject_id` |
| 7 | `causer_type` |
| 8 | `causer_id` |
| 9 | `properties` |
| 10 | `batch_uuid` |
| 11 | `created_at` |
| 12 | `updated_at` |

## admin_sarpras

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 0 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `id_admin_sarpras` |
| 2 | `wa_admin_sarpras` |

## bidang_kategori

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_bidang_kategori` |
| 2 | `nama_kategori_bidang` |
| 3 | `id_bidang` |
| 4 | `bidang_kategori_id_bidang_foreign` |

## bidang_link

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 0 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `id_bidang_link` |
| 2 | `nama_form` |
| 3 | `link_drive` |
| 4 | `id_bidang_kategori` |
| 5 | `status_share` |
| 6 | `bidang_link_id_bidang_kategori_foreign` |

## busdev_bidang

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 0 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `id_bidang` |
| 2 | `nama_bidang` |

## cache

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `key` |
| 2 | `value` |
| 3 | `expiration` |

## cache_locks

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `key` |
| 2 | `owner` |
| 3 | `expiration` |

## calon_siswa

| Property | Value |
|----------|-------|
| **Columns** | 38 |
| **Rows** | 0 |

### Columns (38)

| # | Column Name |
|---|-------------|
| 1 | `id_calon` |
| 2 | `kode_unik` |
| 3 | `nama_lengkap` |
| 4 | `id_kontak_prospek` |
| 5 | `nama_panggilan` |
| 6 | `jenis_kelamin` |
| 7 | `tempat_lahir` |
| 8 | `tanggal_lahir` |
| 9 | `kewarganegaraan` |
| 10 | `email` |
| 11 | `nama_kontak_awal` |
| 12 | `wa_kontak_awal` |
| 13 | `id_provinsi` |
| 14 | `id_kabupaten` |
| 15 | `id_kecamatan` |
| 16 | `id_kelurahan` |
| 17 | `alamat_lengkap` |
| 18 | `wa_siswa` |
| 19 | `wa_ortu` |
| 20 | `wa_administrasi` |
| 21 | `sumber_lead` |
| 22 | `status_pipeline` |
| 23 | `status_updated_at` |
| 24 | `assigned_fo` |
| 25 | `assigned_akademik` |
| 26 | `catatan_awal_fo` |
| 27 | `link_form_sent_at` |
| 28 | `form_completed_at` |
| 29 | `deleted_at` |
| 30 | `created_at` |
| 31 | `updated_at` |
| 32 | `calon_siswa_assigned_akademik_foreign` |
| 33 | `calon_siswa_assigned_fo_foreign` |
| 34 | `calon_siswa_id_kabupaten_foreign` |
| 35 | `calon_siswa_id_kecamatan_foreign` |
| 36 | `calon_siswa_id_kelurahan_foreign` |
| 37 | `calon_siswa_id_kontak_prospek_foreign` |
| 38 | `calon_siswa_id_provinsi_foreign` |

## calon_siswa_akademik

| Property | Value |
|----------|-------|
| **Columns** | 30 |
| **Rows** | 0 |

### Columns (30)

| # | Column Name |
|---|-------------|
| 1 | `id_calon_akademik` |
| 2 | `id_calon` |
| 3 | `nama_sekolah` |
| 4 | `jenjang_kelas_1` |
| 5 | `jenjang_kelas_2` |
| 6 | `kurikulum_sekolah` |
| 7 | `id_kursus` |
| 8 | `id_periode` |
| 9 | `id_level` |
| 10 | `preferensi_metode_belajar` |
| 11 | `riwayat_les` |
| 12 | `kesulitan_belajar` |
| 13 | `kegiatan_sekarang` |
| 14 | `kegiatan_lainnya` |
| 15 | `kemampuan_officeApp` |
| 16 | `kemampuan_editing` |
| 17 | `kemampuan_kustom` |
| 18 | `kemampuan_komputer` |
| 19 | `kemampuan_software` |
| 20 | `penggunaan_gadget` |
| 21 | `sumber_info` |
| 22 | `referensi` |
| 23 | `alasan_daftar` |
| 24 | `alasan_program` |
| 25 | `harapan_program` |
| 26 | `lampiran_file` |
| 27 | `calon_siswa_akademik_id_calon_foreign` |
| 28 | `calon_siswa_akademik_id_kursus_foreign` |
| 29 | `calon_siswa_akademik_id_level_foreign` |
| 30 | `calon_siswa_akademik_id_periode_foreign` |

## calon_siswa_bayar

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_calon_bayar` |
| 2 | `id_calon` |
| 3 | `nomor_invoice` |
| 4 | `bank_pembayaran` |
| 5 | `tanggal_konfirmasi_bayar` |
| 6 | `bulan_mulai_belajar` |
| 7 | `lokasi_belajar` |
| 8 | `status_siswa` |
| 9 | `calon_siswa_bayar_id_calon_foreign` |

## calon_siswa_jadwal

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 0 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `id_calon_jadwal` |
| 2 | `id_calon` |
| 3 | `tanggal_kontak_awal` |
| 4 | `tanggal_wawancara` |
| 5 | `konfirmasi_tes` |
| 6 | `konfirmasi_trial` |
| 7 | `tanggal_pembayaran` |
| 8 | `tanggal_masuk` |
| 9 | `tanggal_keluar` |
| 10 | `calon_siswa_jadwal_id_calon_foreign` |

## calon_siswa_kursus

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 0 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `id_calon_kursus` |
| 2 | `id_calon` |
| 3 | `urutan` |
| 4 | `nama_kursus` |
| 5 | `jenis_program` |
| 6 | `calon_siswa_kursus_id_calon_foreign` |

## calon_siswa_ortu

| Property | Value |
|----------|-------|
| **Columns** | 15 |
| **Rows** | 0 |

### Columns (15)

| # | Column Name |
|---|-------------|
| 1 | `id_calon_ortu` |
| 2 | `id_calon` |
| 3 | `nama_ayah` |
| 4 | `pekerjaan_ayah` |
| 5 | `pendidikan_ayah` |
| 6 | `penghasilan_ayah` |
| 7 | `nama_ibu` |
| 8 | `pekerjaan_ibu` |
| 9 | `pendidikan_ibu` |
| 10 | `penghasilan_ibu` |
| 11 | `nama_wali` |
| 12 | `pekerjaan_wali` |
| 13 | `pendidikan_wali` |
| 14 | `penghasilan_wali` |
| 15 | `calon_siswa_ortu_id_calon_foreign` |

## calon_siswa_proses

| Property | Value |
|----------|-------|
| **Columns** | 28 |
| **Rows** | 0 |

### Columns (28)

| # | Column Name |
|---|-------------|
| 1 | `id_calon_siswa_proses` |
| 2 | `id_calon` |
| 3 | `admin_pengontak` |
| 4 | `penanggung_jawab` |
| 5 | `jenis_trial` |
| 6 | `hasil_trial` |
| 7 | `waktu_trial_1` |
| 8 | `waktu_trial_2` |
| 9 | `tanggal_trial` |
| 10 | `laporan_trial` |
| 11 | `placement_trial` |
| 12 | `lokasi_trial` |
| 13 | `status_siswa` |
| 14 | `status_diterima` |
| 15 | `status_form_pendaftaran` |
| 16 | `hasil_penempatan` |
| 17 | `followup_1` |
| 18 | `followup_2` |
| 19 | `followup_3` |
| 20 | `akun_leapverse` |
| 21 | `wa_grup_leapverse` |
| 22 | `catatan_admin` |
| 23 | `catatan_penting` |
| 24 | `keterangan_tambahan` |
| 25 | `detail_lainnya` |
| 26 | `created_at` |
| 27 | `updated_at` |
| 28 | `calon_siswa_proses_id_calon_foreign` |

## calon_siswa_status_logs

| Property | Value |
|----------|-------|
| **Columns** | 11 |
| **Rows** | 0 |

### Columns (11)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `id_calon` |
| 3 | `status_sebelumnya` |
| 4 | `status_baru` |
| 5 | `diubah_oleh` |
| 6 | `catatan` |
| 7 | `waktu_perubahan` |
| 8 | `created_at` |
| 9 | `updated_at` |
| 10 | `calon_siswa_status_logs_diubah_oleh_foreign` |
| 11 | `calon_siswa_status_logs_id_calon_foreign` |

## catatan_kelas

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_ck` |
| 2 | `id_jadwal` |
| 3 | `id_jadwal_detail` |
| 4 | `catatan_kelas` |
| 5 | `topik_diskusi` |
| 6 | `tanggal_konfirmasi` |
| 7 | `hasil_konfirmasi` |
| 8 | `catatan_kelas_id_jadwal_detail_foreign` |
| 9 | `catatan_kelas_id_jadwal_foreign` |

## catatan_kelas_tag

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_ck_tag` |
| 2 | `id_ck` |
| 3 | `id_topik_diskusi` |
| 4 | `catatan_kelas_tag_id_ck_foreign` |
| 5 | `catatan_kelas_tag_id_topik_diskusi_foreign` |

## catatan_mingguan

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_cm` |
| 2 | `id_user` |
| 3 | `tanggal_mulai_cm` |
| 4 | `tanggal_selesai_cm` |
| 5 | `keterangan_cm` |
| 6 | `keputusan_cm` |
| 7 | `tanggal_verifikasi_cm` |
| 8 | `catatan_mingguan_id_user_foreign` |

## catatan_siswa

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_cs` |
| 2 | `id_jadwal` |
| 3 | `id_jadwal_detail` |
| 4 | `id_siswa` |
| 5 | `catatan_cs` |
| 6 | `catatan_siswa_id_jadwal_detail_foreign` |
| 7 | `catatan_siswa_id_jadwal_foreign` |
| 8 | `catatan_siswa_id_siswa_foreign` |

## division_user

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_division_user` |
| 2 | `id_division` |
| 3 | `id_role` |
| 4 | `created_at` |
| 5 | `updated_at` |
| 6 | `division_user_id_division_foreign` |
| 7 | `division_user_id_division_user_foreign` |
| 8 | `division_user_id_role_foreign` |

## divisions

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_division` |
| 2 | `name_division` |
| 3 | `description` |
| 4 | `is_active` |

## failed_jobs

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `uuid` |
| 3 | `connection` |
| 4 | `queue` |
| 5 | `payload` |
| 6 | `exception` |
| 7 | `failed_at` |

## followup_cs

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_followup_cs` |
| 2 | `id_cs` |
| 3 | `tanggal_followup` |
| 4 | `id_user` |
| 5 | `kesimpulan_followup_cs` |
| 6 | `status_followup` |
| 7 | `followup_cs_id_cs_foreign` |
| 8 | `followup_cs_id_user_foreign` |

## histori_pengajuan

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 0 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `id_verifikasi` |
| 2 | `id_pengajuan` |
| 3 | `status_verifikasi_pengajuan` |
| 4 | `catatan` |
| 5 | `created_at` |
| 6 | `histori_pengajuan_id_pengajuan_foreign` |

## izin_karyawan

| Property | Value |
|----------|-------|
| **Columns** | 11 |
| **Rows** | 0 |

### Columns (11)

| # | Column Name |
|---|-------------|
| 1 | `id_izin` |
| 2 | `id_karyawan` |
| 3 | `jenis_izin` |
| 4 | `tanggal_mulai` |
| 5 | `tanggal_selesai` |
| 6 | `waktu_mulai` |
| 7 | `waktu_selesai` |
| 8 | `keterangan_izin` |
| 9 | `dokumen_lampiran` |
| 10 | `created_at` |
| 11 | `izin_karyawan_id_karyawan_foreign` |

## jadwal

| Property | Value |
|----------|-------|
| **Columns** | 13 |
| **Rows** | 0 |

### Columns (13)

| # | Column Name |
|---|-------------|
| 1 | `id_jadwal` |
| 2 | `id_kursus` |
| 3 | `id_periode` |
| 4 | `id_level` |
| 5 | `id_sesi` |
| 6 | `metode_belajar_jadwal` |
| 7 | `nama_rombel` |
| 8 | `status_arsip` |
| 9 | `tempat` |
| 10 | `jadwal_id_kursus_foreign` |
| 11 | `jadwal_id_level_foreign` |
| 12 | `jadwal_id_periode_foreign` |
| 13 | `jadwal_id_sesi_foreign` |

## jadwal_detail

| Property | Value |
|----------|-------|
| **Columns** | 21 |
| **Rows** | 0 |

### Columns (21)

| # | Column Name |
|---|-------------|
| 1 | `id_jadwal_detail` |
| 2 | `id_jadwal` |
| 3 | `judul` |
| 4 | `deskripsi` |
| 5 | `url_jadwal_detail` |
| 6 | `penanda_mulai` |
| 7 | `penanda_selesai` |
| 8 | `label_warna` |
| 9 | `id_mitra` |
| 10 | `id_sesi_override` |
| 11 | `status_detail` |
| 12 | `source_type` |
| 13 | `original_jadwal_detail_id` |
| 14 | `has_operational_data` |
| 15 | `last_generated_at` |
| 16 | `created_at` |
| 17 | `updated_at` |
| 18 | `jadwal_detail_id_jadwal_foreign` |
| 19 | `jadwal_detail_id_mitra_foreign` |
| 20 | `jadwal_detail_id_sesi_override_foreign` |
| 21 | `jadwal_detail_original_jadwal_detail_id_foreign` |

## jadwal_detail_logs

| Property | Value |
|----------|-------|
| **Columns** | 21 |
| **Rows** | 0 |

### Columns (21)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `id_jadwal_detail` |
| 3 | `id_jadwal` |
| 4 | `action_type` |
| 5 | `scope_type` |
| 6 | `old_tanggal` |
| 7 | `new_tanggal` |
| 8 | `old_id_sesi` |
| 9 | `new_id_sesi` |
| 10 | `reason` |
| 11 | `notes` |
| 12 | `before_payload` |
| 13 | `after_payload` |
| 14 | `changed_by` |
| 15 | `created_at` |
| 16 | `updated_at` |
| 17 | `jadwal_detail_logs_changed_by_foreign` |
| 18 | `jadwal_detail_logs_id_jadwal_detail_foreign` |
| 19 | `jadwal_detail_logs_id_jadwal_foreign` |
| 20 | `jadwal_detail_logs_new_id_sesi_foreign` |
| 21 | `jadwal_detail_logs_old_id_sesi_foreign` |

## jadwal_hari

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_jadwal_hari` |
| 2 | `id_jadwal` |
| 3 | `nama_hari` |
| 4 | `jadwal_hari_id_jadwal_foreign` |

## jadwal_pengajar

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_jadwal_pengajar` |
| 2 | `id_jadwal` |
| 3 | `id_user` |
| 4 | `jadwal_pengajar_id_jadwal_foreign` |
| 5 | `jadwal_pengajar_id_user_foreign` |

## jadwal_siswa

| Property | Value |
|----------|-------|
| **Columns** | 11 |
| **Rows** | 0 |

### Columns (11)

| # | Column Name |
|---|-------------|
| 1 | `id_jadwal_siswa` |
| 2 | `id_siswa` |
| 3 | `id_jadwal` |
| 4 | `tanggal_mulai` |
| 5 | `tambahan_sesi` |
| 6 | `tambahan_keterangan` |
| 7 | `status_keluar` |
| 8 | `tanggal_keluar` |
| 9 | `tanggal_aktif` |
| 10 | `jadwal_siswa_id_jadwal_foreign` |
| 11 | `jadwal_siswa_id_siswa_foreign` |

## job_batches

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 0 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `name` |
| 3 | `total_jobs` |
| 4 | `pending_jobs` |
| 5 | `failed_jobs` |
| 6 | `failed_job_ids` |
| 7 | `options` |
| 8 | `cancelled_at` |
| 9 | `created_at` |
| 10 | `finished_at` |

## jobs

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `queue` |
| 3 | `payload` |
| 4 | `attempts` |
| 5 | `reserved_at` |
| 6 | `available_at` |
| 7 | `created_at` |

## kabupaten

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 514 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_kabupaten` |
| 2 | `id_provinsi` |
| 3 | `nama_kabupaten` |
| 4 | `code` |
| 5 | `kabupaten_id_provinsi_foreign` |

## karyawan

| Property | Value |
|----------|-------|
| **Columns** | 38 |
| **Rows** | 0 |

### Columns (38)

| # | Column Name |
|---|-------------|
| 1 | `id_karyawan` |
| 2 | `id_user` |
| 3 | `nik_ktp` |
| 4 | `nama_lengkap` |
| 5 | `nama_panggilan` |
| 6 | `tempat_lahir` |
| 7 | `tanggal_lahir` |
| 8 | `jenis_kelamin` |
| 9 | `golongan_darah` |
| 10 | `agama` |
| 11 | `status_pernikahan` |
| 12 | `alamat_ktp` |
| 13 | `alamat_domisili` |
| 14 | `kewarganegaraan` |
| 15 | `anak_ke` |
| 16 | `jumlah_anak` |
| 17 | `hobi` |
| 18 | `akun_linkedin` |
| 19 | `email_pribadi` |
| 20 | `email_kantor` |
| 21 | `nomor_telepon` |
| 22 | `nomor_npwp` |
| 23 | `bpjs_ketenagakerjaan` |
| 24 | `bpjs_kesehatan` |
| 25 | `nomor_rekening` |
| 26 | `moda_transportasi` |
| 27 | `akun_instagram` |
| 28 | `akun_facebook` |
| 29 | `link_dokumen_pribadi` |
| 30 | `riwayat_kesehatan` |
| 31 | `tahun_mulai_kerja` |
| 32 | `keahlian` |
| 33 | `id_shift` |
| 34 | `status_aktif` |
| 35 | `foto_profile` |
| 36 | `ttd_digital` |
| 37 | `karyawan_id_shift_foreign` |
| 38 | `karyawan_id_user_foreign` |

## karyawan_resign

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 0 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `id_resign` |
| 2 | `id_karyawan` |
| 3 | `id_user` |
| 4 | `alasan_resign` |
| 5 | `dokumen_pendukung` |
| 6 | `status_persetujuan` |
| 7 | `status_pengiriman` |
| 8 | `created_at` |
| 9 | `karyawan_resign_id_karyawan_foreign` |
| 10 | `karyawan_resign_id_user_foreign` |

## kecamatan

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 7,266 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_kecamatan` |
| 2 | `id_kabupaten` |
| 3 | `nama_kecamatan` |
| 4 | `code` |
| 5 | `kecamatan_id_kabupaten_foreign` |

## keluarga_karyawan

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `id_keluarga` |
| 2 | `id_karyawan` |
| 3 | `hubungan_keluarga` |
| 4 | `nama_lengkap` |
| 5 | `pekerjaan` |
| 6 | `nomor_hp` |
| 7 | `keluarga_karyawan_id_karyawan_foreign` |

## kelurahan

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 83,449 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_kelurahan` |
| 2 | `id_kecamatan` |
| 3 | `nama_kelurahan` |
| 4 | `kode_pos` |
| 5 | `kelurahan_id_kecamatan_foreign` |

## kemitraan_verifikator

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_kemitraan` |
| 2 | `id_progres_mitra` |
| 3 | `id_user` |
| 4 | `kemitraan_verifikator_id_progres_mitra_foreign` |
| 5 | `kemitraan_verifikator_id_user_foreign` |

## kontak_prospek

| Property | Value |
|----------|-------|
| **Columns** | 14 |
| **Rows** | 0 |

### Columns (14)

| # | Column Name |
|---|-------------|
| 1 | `id_kontak_prospek` |
| 2 | `kode_kontak` |
| 3 | `nama_penanya` |
| 4 | `nomor_telepon` |
| 5 | `email` |
| 6 | `sumber_informasi` |
| 7 | `catatan_awal_fo` |
| 8 | `id_admin_fo` |
| 9 | `status_kontak` |
| 10 | `tanggal_kontak_pertama` |
| 11 | `tanggal_kontak_terakhir` |
| 12 | `created_at` |
| 13 | `updated_at` |
| 14 | `kontak_prospek_id_admin_fo_foreign` |

## kursus

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_kursus` |
| 2 | `nama_kursus` |
| 3 | `deskripsi` |
| 4 | `tipe_kursus` |
| 5 | `status_arsip` |

## kursus_level

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_kursus_level` |
| 2 | `id_kursus` |
| 3 | `id_level` |
| 4 | `kursus_level_id_kursus_foreign` |
| 5 | `kursus_level_id_level_foreign` |

## kursus_libur

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_kursus_libur` |
| 2 | `id_kursus` |
| 3 | `id_libur` |
| 4 | `kursus_libur_id_kursus_foreign` |
| 5 | `kursus_libur_id_libur_foreign` |

## kursus_siswa

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_kursus_siswa` |
| 2 | `id_siswa` |
| 3 | `id_kursus` |
| 4 | `tanggal_mulai` |
| 5 | `metode_belajar` |
| 6 | `status_aktif` |
| 7 | `catatan` |
| 8 | `kursus_siswa_id_kursus_foreign` |
| 9 | `kursus_siswa_id_siswa_foreign` |

## level

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `id_level` |
| 2 | `nama_level` |
| 3 | `urutan_level` |

## libur

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_libur` |
| 2 | `nama_event` |
| 3 | `deskripsi_libur` |
| 4 | `sumber` |
| 5 | `tanggal_mulai` |
| 6 | `tanggal_berakhir` |
| 7 | `label_warna` |
| 8 | `status_libur_program` |

## log_aktivitas

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `id_user` |
| 3 | `ip` |
| 4 | `browser` |
| 5 | `aktivitas` |
| 6 | `created_at` |
| 7 | `log_aktivitas_id_user_foreign` |

## migrations

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `migration` |
| 3 | `batch` |

## mitra

| Property | Value |
|----------|-------|
| **Columns** | 29 |
| **Rows** | 0 |

### Columns (29)

| # | Column Name |
|---|-------------|
| 1 | `id_mitra` |
| 2 | `kode_mitra` |
| 3 | `nama_mitra` |
| 4 | `nama_instansi` |
| 5 | `nama_sekolah` |
| 6 | `alamat_mitra` |
| 7 | `nama_pimpinan` |
| 8 | `kontak_mitra` |
| 9 | `status_mitra` |
| 10 | `visi_misi` |
| 11 | `program_mitra` |
| 12 | `info_sdm` |
| 13 | `info_kelemahan` |
| 14 | `rekomendasi_program` |
| 15 | `jenis_mitra` |
| 16 | `provinsi_id` |
| 17 | `kabupaten_id` |
| 18 | `jumlah_siswa_mitra` |
| 19 | `bidang_usaha` |
| 20 | `is_leapverse` |
| 21 | `status_kemitraan` |
| 22 | `tahun_bergabung` |
| 23 | `tipe_kerjasama` |
| 24 | `is_elsa` |
| 25 | `is_classin` |
| 26 | `is_mitra_leap` |
| 27 | `created_at` |
| 28 | `mitra_kabupaten_id_foreign` |
| 29 | `mitra_provinsi_id_foreign` |

## mitra_progres

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 0 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `id_progres_mitra` |
| 2 | `id_mitra` |
| 3 | `catatan_progres_mitra` |
| 4 | `id_user` |
| 5 | `status_progres_mitra` |
| 6 | `kemitraan_mulai` |
| 7 | `kemitraan_berakhir` |
| 8 | `created_at` |
| 9 | `mitra_progres_id_mitra_foreign` |
| 10 | `mitra_progres_id_user_foreign` |

## model_has_permissions

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `permission_id` |
| 2 | `model_type` |
| 3 | `model_id` |
| 4 | `model_has_permissions_permission_id_foreign` |

## model_has_roles

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `role_id` |
| 2 | `model_type` |
| 3 | `model_id` |
| 4 | `model_has_roles_role_id_foreign` |

## mou

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_mou` |
| 2 | `detail_kebutuhan` |
| 3 | `keterangan_tambahan` |
| 4 | `id_user` |
| 5 | `status_persetujuan` |
| 6 | `url_dokumen_mou` |
| 7 | `created_at` |
| 8 | `mou_id_user_foreign` |

## parameter_nilai

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_parameter_nilai` |
| 2 | `id_level` |
| 3 | `nama_parameter` |
| 4 | `status_parameter` |
| 5 | `parameter_nilai_id_level_foreign` |

## password_reset_tokens

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `email` |
| 2 | `token` |
| 3 | `created_at` |

## pelamar

| Property | Value |
|----------|-------|
| **Columns** | 44 |
| **Rows** | 0 |

### Columns (44)

| # | Column Name |
|---|-------------|
| 1 | `id_pelamar` |
| 2 | `id_pengajuan` |
| 3 | `email_pelamar` |
| 4 | `nama_lengkap` |
| 5 | `nama_panggilan` |
| 6 | `jenis_kelamin` |
| 7 | `tempat_lahir` |
| 8 | `tanggal_lahir` |
| 9 | `alamat_ktp` |
| 10 | `alamat_domisili` |
| 11 | `nomor_wa` |
| 12 | `akun_linkedin` |
| 13 | `akun_instagram` |
| 14 | `akun_facebook` |
| 15 | `sosmed_lain` |
| 16 | `spesifikasi_laptop` |
| 17 | `internet` |
| 18 | `kegiatan_sekarang` |
| 19 | `rencana_karir` |
| 20 | `mobilitas` |
| 21 | `sumber_info` |
| 22 | `siap_wfo` |
| 23 | `tanggal_bergabung` |
| 24 | `kategori_pelamar` |
| 25 | `riwayat_kerja` |
| 26 | `riwayat_pendidikan` |
| 27 | `pengalaman_bidang` |
| 28 | `wawasan` |
| 29 | `riwayat_kesehatan` |
| 30 | `status_pernikahan` |
| 31 | `kemampuan_ajar` |
| 32 | `penguasaan_aplikasi` |
| 33 | `aplikasi_lainnya` |
| 34 | `penggunaan_laptop` |
| 35 | `skor_toefl` |
| 36 | `ekspektasi_gaji` |
| 37 | `tautan_berkas` |
| 38 | `alasan_resign` |
| 39 | `skor_iq` |
| 40 | `foto_iq` |
| 41 | `foto_minat` |
| 42 | `foto_kepribadian` |
| 43 | `created_at` |
| 44 | `pelamar_id_pengajuan_foreign` |

## pelamar_kerja

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `id_pelamar_kerja` |
| 2 | `id_pelamar` |
| 3 | `nama_perusahaan` |
| 4 | `periode` |
| 5 | `jabatan` |
| 6 | `deskripsi_kerja` |
| 7 | `pelamar_kerja_id_pelamar_foreign` |

## pelamar_kursus

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_pelamar_kursus` |
| 2 | `id_pelamar` |
| 3 | `nama_kursus` |
| 4 | `tanggal` |
| 5 | `deskripsi` |
| 6 | `lokasi` |
| 7 | `nomor_sertifikat` |
| 8 | `pelamar_kursus_id_pelamar_foreign` |

## pelamar_sekolah

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_pelamar_sekolah` |
| 2 | `id_pelamar` |
| 3 | `nama_sekolah` |
| 4 | `jenjang` |
| 5 | `prodi` |
| 6 | `tahun_lulus` |
| 7 | `ipk` |
| 8 | `organisasi` |
| 9 | `pelamar_sekolah_id_pelamar_foreign` |

## peminjaman

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_pinjam` |
| 2 | `tanggal_pinjam` |
| 3 | `keperluan` |
| 4 | `id_user` |
| 5 | `status_pinjam` |
| 6 | `catatan_sarpras` |
| 7 | `created_at` |
| 8 | `peminjaman_id_user_foreign` |

## pengadaan

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 0 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `id_pengadaan` |
| 2 | `deskripsi` |
| 3 | `url_produk` |
| 4 | `id_user` |
| 5 | `status_pengajuan` |
| 6 | `catatan_admin` |
| 7 | `tanggal_pengajuan` |
| 8 | `tanggal_selesai` |
| 9 | `url_pembelian` |
| 10 | `pengadaan_id_user_foreign` |

## pengajuan_karyawan

| Property | Value |
|----------|-------|
| **Columns** | 11 |
| **Rows** | 0 |

### Columns (11)

| # | Column Name |
|---|-------------|
| 1 | `id_pengajuan` |
| 2 | `id_user` |
| 3 | `posisi` |
| 4 | `jumlah` |
| 5 | `syarat` |
| 6 | `pertanyaan` |
| 7 | `alur_seleksi` |
| 8 | `daftar_tes` |
| 9 | `status` |
| 10 | `created_at` |
| 11 | `pengajuan_karyawan_id_user_foreign` |

## periode

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_periode` |
| 2 | `nama_periode` |
| 3 | `tanggal_mulai` |
| 4 | `id_kursus` |
| 5 | `jumlah_sesi` |
| 6 | `tahun_ajar` |
| 7 | `status` |
| 8 | `is_active` |
| 9 | `periode_id_kursus_foreign` |

## permissions

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `name` |
| 3 | `guard_name` |
| 4 | `created_at` |
| 5 | `updated_at` |

## presensi_siswa

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `id_presensi_siswa` |
| 2 | `id_jadwal_detail` |
| 3 | `id_siswa` |
| 4 | `waktu_presensi` |
| 5 | `status_presensi` |
| 6 | `presensi_siswa_id_jadwal_detail_foreign` |
| 7 | `presensi_siswa_id_siswa_foreign` |

## problem

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_problem` |
| 2 | `detail_masalah` |
| 3 | `id_user` |
| 4 | `status_perbaikan` |
| 5 | `tanggal_lapor` |
| 6 | `tanggal_selesai` |
| 7 | `catatan_teknisi` |
| 8 | `gambar_problem` |
| 9 | `problem_id_user_foreign` |

## progres_pelamar

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 0 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `id_progres_pelamar` |
| 2 | `id_pelamar` |
| 3 | `id_user` |
| 4 | `status_progres_pelamar` |
| 5 | `catatan` |
| 6 | `tautan_file` |
| 7 | `pertanyaan` |
| 8 | `created_at` |
| 9 | `progres_pelamar_id_pelamar_foreign` |
| 10 | `progres_pelamar_id_user_foreign` |

## provinsi

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 38 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `id_provinsi` |
| 2 | `nama_provinsi` |
| 3 | `code` |

## rapor_format

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_format` |
| 2 | `id_kursus` |
| 3 | `judul_rapor` |
| 4 | `rapor_format_id_kursus_foreign` |

## rapor_format_formula

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_format_formula` |
| 2 | `id_rapor_format` |
| 3 | `logika_operator` |
| 4 | `rapor_format_formula_id_rapor_format_foreign` |

## rapor_format_formula_sub

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 0 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_format_formula_sub` |
| 2 | `id_rapor_format_sub` |
| 3 | `logika_operator` |
| 4 | `id_level` |
| 5 | `rapor_format_formula_sub_id_level_foreign` |
| 6 | `rapor_format_formula_sub_id_rapor_format_sub_foreign` |

## rapor_format_sub

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_format_sub` |
| 2 | `id_rapor_format` |
| 3 | `sub_judul_rapor` |
| 4 | `rapor_format_sub_id_rapor_format_foreign` |

## rapor_lacak

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_lacak` |
| 2 | `id_siswa` |
| 3 | `id_jadwal` |
| 4 | `tanggal_terkirim` |
| 5 | `status_pengiriman` |
| 6 | `id_rapor_siswa_file` |
| 7 | `rapor_lacak_id_jadwal_foreign` |
| 8 | `rapor_lacak_id_rapor_siswa_file_foreign` |
| 9 | `rapor_lacak_id_siswa_foreign` |

## rapor_level_config

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_level_config` |
| 2 | `id_level` |
| 3 | `id_kursus` |
| 4 | `id_rapor_format` |
| 5 | `rapor_level_config_id_kursus_foreign` |
| 6 | `rapor_level_config_id_level_foreign` |
| 7 | `rapor_level_config_id_rapor_format_foreign` |

## rapor_siswa

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_siswa` |
| 2 | `id_jadwal` |
| 3 | `id_siswa` |
| 4 | `tanggal_input` |
| 5 | `id_parameter_nilai` |
| 6 | `final_result` |
| 7 | `rapor_siswa_id_jadwal_foreign` |
| 8 | `rapor_siswa_id_parameter_nilai_foreign` |
| 9 | `rapor_siswa_id_siswa_foreign` |

## rapor_siswa_file

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_siswa_file` |
| 2 | `id_rapor_siswa` |
| 3 | `file_rapor_path` |
| 4 | `rapor_siswa_file_id_rapor_siswa_foreign` |

## rapor_sub_level

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_rapor_sub_level` |
| 2 | `id_rapor_format_sub` |
| 3 | `id_level` |
| 4 | `rapor_sub_level_id_level_foreign` |
| 5 | `rapor_sub_level_id_rapor_format_sub_foreign` |

## rekrutmen_pelamar

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_rekrutmen` |
| 2 | `id_pelamar` |
| 3 | `id_user` |
| 4 | `rekrutmen_pelamar_id_pelamar_foreign` |
| 5 | `rekrutmen_pelamar_id_user_foreign` |

## role_has_permissions

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `permission_id` |
| 2 | `role_id` |
| 3 | `role_has_permissions_permission_id_foreign` |
| 4 | `role_has_permissions_role_id_foreign` |

## roles

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `name` |
| 3 | `guard_name` |
| 4 | `created_at` |
| 5 | `updated_at` |

## sesi

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_sesi` |
| 2 | `nama_sesi` |
| 3 | `waktu_mulai` |
| 4 | `waktu_selesai` |

## sessions

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `id` |
| 2 | `user_id` |
| 3 | `ip_address` |
| 4 | `user_agent` |
| 5 | `payload` |
| 6 | `last_activity` |
| 7 | `sessions_user_id_foreign` |

## shift_kerja

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_shift` |
| 2 | `nama_shift` |
| 3 | `jam_masuk` |
| 4 | `jam_pulang` |

## siswa

| Property | Value |
|----------|-------|
| **Columns** | 57 |
| **Rows** | 0 |

### Columns (57)

| # | Column Name |
|---|-------------|
| 1 | `id_siswa` |
| 2 | `tanggal_registrasi` |
| 3 | `domisili` |
| 4 | `nama_lengkap` |
| 5 | `nama_panggilan` |
| 6 | `jenis_kelamin` |
| 7 | `asal_sekolah` |
| 8 | `tingkat_sekolah` |
| 9 | `nama_orang_tua` |
| 10 | `pekerjaan_orang_tua` |
| 11 | `tempat_lahir` |
| 12 | `tanggal_lahir` |
| 13 | `nomor_induk` |
| 14 | `email` |
| 15 | `id_calon` |
| 16 | `id_provinsi` |
| 17 | `id_kabupaten` |
| 18 | `id_kecamatan` |
| 19 | `id_kelurahan` |
| 20 | `id_mitra` |
| 21 | `nisn` |
| 22 | `nik` |
| 23 | `kewarganegaraan` |
| 24 | `agama` |
| 25 | `rt` |
| 26 | `rw` |
| 27 | `kode_pos` |
| 28 | `status_aktif` |
| 29 | `rekomendasi` |
| 30 | `sumber_info` |
| 31 | `metode_pembayaran` |
| 32 | `nama_ayah` |
| 33 | `pekerjaan_ayah` |
| 34 | `pendidikan_ayah` |
| 35 | `penghasilan_ayah` |
| 36 | `nama_ibu` |
| 37 | `penghasilan_ibu` |
| 38 | `pekerjaan_ibu` |
| 39 | `pendidikan_ibu` |
| 40 | `nama_wali` |
| 41 | `pekerjaan_wali` |
| 42 | `pendidikan_wali` |
| 43 | `penghasilan_wali` |
| 44 | `wa_siswa` |
| 45 | `wa_ortu` |
| 46 | `wa_administrasi` |
| 47 | `status_pengisian` |
| 48 | `path_bukti_bayar` |
| 49 | `status_lulus_siswa` |
| 50 | `tanggal_upload_bukti` |
| 51 | `deleted_at` |
| 52 | `siswa_id_calon_foreign` |
| 53 | `siswa_id_kabupaten_foreign` |
| 54 | `siswa_id_kecamatan_foreign` |
| 55 | `siswa_id_kelurahan_foreign` |
| 56 | `siswa_id_mitra_foreign` |
| 57 | `siswa_id_provinsi_foreign` |

## siswa_keluar

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_keluar` |
| 2 | `id_siswa` |
| 3 | `id_kursus` |
| 4 | `alasan_keluar` |
| 5 | `tanggal_keluar` |
| 6 | `id_tag_keluar` |
| 7 | `siswa_keluar_id_kursus_foreign` |
| 8 | `siswa_keluar_id_siswa_foreign` |
| 9 | `siswa_keluar_id_tag_keluar_foreign` |

## siswa_mitra

| Property | Value |
|----------|-------|
| **Columns** | 18 |
| **Rows** | 0 |

### Columns (18)

| # | Column Name |
|---|-------------|
| 1 | `id_sm` |
| 2 | `tanggal_daftar` |
| 3 | `alamat_domisili` |
| 4 | `nama_lengkap` |
| 5 | `nama_panggilan` |
| 6 | `jenis_kelamin` |
| 7 | `nama_instansi` |
| 8 | `tingkat_sekolah` |
| 9 | `pekerjaan_sm` |
| 10 | `tempat_lahir` |
| 11 | `tanggal_lahir` |
| 12 | `nomor_induk_sm` |
| 13 | `email_sm` |
| 14 | `wa_sm` |
| 15 | `status_keluar_sm` |
| 16 | `id_mitra` |
| 17 | `sertifikat_sm` |
| 18 | `siswa_mitra_id_mitra_foreign` |

## siswa_mitra_keluar

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_sm_keluar` |
| 2 | `id_sm` |
| 3 | `alasan_keluar_sm` |
| 4 | `tanggal_keluar_sm` |
| 5 | `siswa_mitra_keluar_id_sm_foreign` |

## sop

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 0 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `id_sop` |
| 2 | `id_sop_kategori` |
| 3 | `judul_sop` |
| 4 | `link_dokumen_sop` |
| 5 | `created_at` |
| 6 | `sop_id_sop_kategori_foreign` |

## sop_kategori

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 0 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `id_sop_kategori` |
| 2 | `nama_kategori_sop` |

## surat_keluar

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_sk` |
| 2 | `id_user` |
| 3 | `keterangan_sk` |
| 4 | `link_dokumen_sk` |
| 5 | `status_sk` |
| 6 | `nomor_sk` |
| 7 | `catatan_sk` |
| 8 | `created_at` |
| 9 | `surat_keluar_id_user_foreign` |

## surat_tugas

| Property | Value |
|----------|-------|
| **Columns** | 17 |
| **Rows** | 0 |

### Columns (17)

| # | Column Name |
|---|-------------|
| 1 | `id_st` |
| 2 | `id_user` |
| 3 | `acara` |
| 4 | `undangan` |
| 5 | `waktu_acara` |
| 6 | `lokasi_acara` |
| 7 | `jenis_kegiatan` |
| 8 | `status_st` |
| 9 | `nomor_st` |
| 10 | `catatan_st` |
| 11 | `link_st` |
| 12 | `link_laporan` |
| 13 | `catatan_laporan` |
| 14 | `keterangan_st` |
| 15 | `catatan_pembatalan` |
| 16 | `created_at` |
| 17 | `surat_tugas_id_user_foreign` |

## surat_tugas_anggota

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_st_anggota` |
| 2 | `id_st` |
| 3 | `id_user` |
| 4 | `surat_tugas_anggota_id_st_foreign` |
| 5 | `surat_tugas_anggota_id_user_foreign` |

## syarat_resign

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 0 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `id_syarat` |
| 2 | `isi_syarat` |

## tag_siswa_keluar

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `id_tag_keluar` |
| 2 | `nama_tag` |
| 3 | `keterangan_keluar` |

## topik_diskusi

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `id_topik_diskusi` |
| 2 | `topik_diskusi` |
| 3 | `deskripsi_topik_diskusi` |

## ttd

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `id_ttd` |
| 2 | `ttd` |
| 3 | `status` |

## users

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `id_user` |
| 2 | `name` |
| 3 | `email` |
| 4 | `email_verified_at` |
| 5 | `password` |
| 6 | `remember_token` |
| 7 | `created_at` |
| 8 | `updated_at` |

## verifikasi_absensi

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_verifikasi_absensi` |
| 2 | `status_verifikasi_absensi` |
| 3 | `catatan_atasan` |
| 4 | `created_at` |

## verifikasi_izin

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 0 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `id_verifikasi_izin` |
| 2 | `id_izin` |
| 3 | `status_verifikasi_izin` |
| 4 | `catatan_verifikator` |
| 5 | `status_baca` |
| 6 | `id_division` |
| 7 | `created_at` |
| 8 | `verifikasi_izin_id_division_foreign` |
| 9 | `verifikasi_izin_id_izin_foreign` |

## verifikasi_surat_keluar

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 0 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `id_verifikasi_surat` |
| 2 | `id_sk` |
| 3 | `status_verifikasi_sk` |
| 4 | `catatan_verifikasi_sk` |
| 5 | `created_at` |
| 6 | `verifikasi_surat_keluar_id_sk_foreign` |

## web_berita

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `id_berita` |
| 2 | `judul_berita` |
| 3 | `konten_berita` |
| 4 | `path_gambar_berita` |
| 5 | `urutan_tampilan_berita` |

## web_statistik

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `id_stat` |
| 2 | `tanggal_stat` |
| 3 | `jumlah_unduhan` |
| 4 | `pengguna_aktif` |

