# Database Schema Documentation

**Database**: dataleap_v5_example  
**Generated**: 2026-04-21 13:31:08

## Summary
- **Total Tables**: 108
- **Total Rows**: 306296

## Table of Contents

1. [absensi](#absensi)
2. [absensi_note](#absensi_note)
3. [bidang](#bidang)
4. [bidangkategori](#bidangkategori)
5. [bidanglink](#bidanglink)
6. [calon](#calon)
7. [calon_detil](#calon_detil)
8. [calon_pertanyaan](#calon_pertanyaan)
9. [calon_pertanyaan_detil](#calon_pertanyaan_detil)
10. [catatan_kelas](#catatan_kelas)
11. [catatan_kelas_tag](#catatan_kelas_tag)
12. [catatan_mingguan](#catatan_mingguan)
13. [catatan_siswa](#catatan_siswa)
14. [catatan_siswa_follow_up](#catatan_siswa_follow_up)
15. [catatanawal_admin](#catatanawal_admin)
16. [catatanawal_datautama](#catatanawal_datautama)
17. [catatanawal_infolain](#catatanawal_infolain)
18. [catatanawal_tglpenting](#catatanawal_tglpenting)
19. [divisi](#divisi)
20. [docs](#docs)
21. [file_rapor_siswa](#file_rapor_siswa)
22. [form](#form)
23. [form_calon](#form_calon)
24. [form_calon_detil1](#form_calon_detil1)
25. [form_calon_detil2](#form_calon_detil2)
26. [form_calon_detil3](#form_calon_detil3)
27. [form_calon_detil4](#form_calon_detil4)
28. [format_rapor](#format_rapor)
29. [format_rapor_detil](#format_rapor_detil)
30. [format_rapor_detil_rumus](#format_rapor_detil_rumus)
31. [format_rapor_rumus](#format_rapor_rumus)
32. [format_raport_level](#format_raport_level)
33. [hakakses](#hakakses)
34. [histori_pengajuan](#histori_pengajuan)
35. [history_rapor](#history_rapor)
36. [identitas](#identitas)
37. [infrastruktur](#infrastruktur)
38. [jabatan](#jabatan)
39. [jadwal](#jadwal)
40. [jadwal_detil](#jadwal_detil)
41. [jadwal_pengajar](#jadwal_pengajar)
42. [jadwal_siswa](#jadwal_siswa)
43. [jamkerja](#jamkerja)
44. [kabupaten](#kabupaten)
45. [karyawan](#karyawan)
46. [kecamatan](#kecamatan)
47. [keluar](#keluar)
48. [keluarga](#keluarga)
49. [kelurahan](#kelurahan)
50. [kurikulum](#kurikulum)
51. [kurikulum_detil](#kurikulum_detil)
52. [kurikulum_detil_sub](#kurikulum_detil_sub)
53. [kurikulum_kelas](#kurikulum_kelas)
54. [kursus](#kursus)
55. [leapprofil](#leapprofil)
56. [leapverse](#leapverse)
57. [level](#level)
58. [libur](#libur)
59. [libur_pendkursus](#libur_pendkursus)
60. [linkdrive](#linkdrive)
61. [linkform](#linkform)
62. [log](#log)
63. [mitra](#mitra)
64. [mitra_note](#mitra_note)
65. [mitra_users](#mitra_users)
66. [mou](#mou)
67. [mou_histori](#mou_histori)
68. [nowag](#nowag)
69. [parameter_nilai](#parameter_nilai)
70. [pekerjaan](#pekerjaan)
71. [pelamar](#pelamar)
72. [pelamar_note](#pelamar_note)
73. [pelamar_submit](#pelamar_submit)
74. [pelamar_users](#pelamar_users)
75. [pendidikan](#pendidikan)
76. [pendidikankursus](#pendidikankursus)
77. [pengajuan](#pengajuan)
78. [pengumuman](#pengumuman)
79. [perijinan](#perijinan)
80. [perijinan_note](#perijinan_note)
81. [periode](#periode)
82. [pinjam](#pinjam)
83. [presensi_siswa](#presensi_siswa)
84. [problem](#problem)
85. [provinsi](#provinsi)
86. [purchase](#purchase)
87. [purchase_link](#purchase_link)
88. [rapor](#rapor)
89. [role](#role)
90. [role_users](#role_users)
91. [sesi](#sesi)
92. [siswa](#siswa)
93. [siswa_keluar](#siswa_keluar)
94. [siswa_keluar_mitra](#siswa_keluar_mitra)
95. [siswa_keluar_tag](#siswa_keluar_tag)
96. [siswamitra](#siswamitra)
97. [sop](#sop)
98. [sopkategori](#sopkategori)
99. [suratkeluar](#suratkeluar)
100. [suratkeluar_histori](#suratkeluar_histori)
101. [surattugas](#surattugas)
102. [surattugas_users](#surattugas_users)
103. [syarat](#syarat)
104. [tag_keluar](#tag_keluar)
105. [tag_materi_diskusi](#tag_materi_diskusi)
106. [ttd](#ttd)
107. [users](#users)
108. [zoom](#zoom)

---

## absensi

| Property | Value |
|----------|-------|
| **Columns** | 15 |
| **Rows** | 13,444 |

### Columns (15)

| # | Column Name |
|---|-------------|
| 1 | `idabsensi` |
| 2 | `tanggal` |
| 3 | `scanmasuk` |
| 4 | `scankeluar` |
| 5 | `status` |
| 6 | `idkaryawan` |
| 7 | `created_at` |
| 8 | `note1` |
| 9 | `note2` |
| 10 | `verifikasi` |
| 11 | `masuk` |
| 12 | `terlambat` |
| 13 | `keluar` |
| 14 | `cepat` |
| 15 | `FK_absensi_1` |

## absensi_note

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 11 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idnote` |
| 2 | `catatan` |
| 3 | `created_at` |

## bidang

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 4 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `idbidang` |
| 2 | `namabidang` |

## bidangkategori

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 12 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idkatbid` |
| 2 | `namakatbid` |
| 3 | `idbidang` |
| 4 | `FK_bidangkategori_1` |

## bidanglink

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 7 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idformbid` |
| 2 | `namaformbid` |
| 3 | `link` |
| 4 | `idbidang` |
| 5 | `idkatbid` |
| 6 | `share` |
| 7 | `FK_bidanglink_1` |
| 8 | `FK_bidanglink_2` |

## calon

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 4 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `idcalon` |
| 2 | `idpendkursus` |
| 3 | `tlp` |
| 4 | `email` |
| 5 | `nama` |
| 6 | `status` |
| 7 | `FK_calon_pend` |

## calon_detil

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 61 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idcalond` |
| 2 | `idpendkursus` |
| 3 | `idcalon_p` |
| 4 | `jawaban` |
| 5 | `idcalon` |
| 6 | `FK_calon_detil_key` |
| 7 | `FK_calon_detil_pend` |
| 8 | `FK_calon_detil_pertanyaan` |

## calon_pertanyaan

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 229 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idcalon_p` |
| 2 | `idpendkursus` |
| 3 | `pertanyaan` |
| 4 | `mode` |
| 5 | `urutan` |
| 6 | `diisi_oleh` |
| 7 | `pick_target_tb` |
| 8 | `target_tb` |
| 9 | `FK_calon_pendkursus` |

## calon_pertanyaan_detil

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 4,305 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idcalon_pd` |
| 2 | `idcalon_p` |
| 3 | `pertanyaan_detil` |
| 4 | `FK_calon_pertanyaan_detil_key` |

## catatan_kelas

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 12,797 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idcatatan_kelas` |
| 2 | `idjadwal` |
| 3 | `idjadwaldetil` |
| 4 | `catatan` |
| 5 | `materi_diskusi` |
| 6 | `tglcek` |
| 7 | `hasil_konfirm` |
| 8 | `FK_catatan_kelas_jadwal` |
| 9 | `FK_catatan_kelas_jadwaldetil` |

## catatan_kelas_tag

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 999 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idcatatantag` |
| 2 | `idtagmd` |
| 3 | `idcatatan_kelas` |
| 4 | `FK_catatan_kelas_tag_1` |
| 5 | `FK_catatan_kelas_tag_2` |

## catatan_mingguan

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 0 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idcatatanweek` |
| 2 | `catatan` |
| 3 | `materi_diskusi` |
| 4 | `hasil_konfirmasi` |
| 5 | `tglcek` |
| 6 | `idusers` |
| 7 | `tglawal` |
| 8 | `tglakhir` |

## catatan_siswa

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 1,502 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idcatatan_siswa` |
| 2 | `idjadwal` |
| 3 | `idjadwaldetil` |
| 4 | `idsiswa` |
| 5 | `catatan` |
| 6 | `FK_catatan_siswa_jadwal` |
| 7 | `FK_catatan_siswa_jadwaldetil` |
| 8 | `FK_catatan_siswa_siswa` |

## catatan_siswa_follow_up

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 22 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idcs_follow_up` |
| 2 | `idcatatan_siswa` |
| 3 | `tanggal` |
| 4 | `idusers` |
| 5 | `kesimpulan` |
| 6 | `status_follow` |
| 7 | `FK_catatan_siswa_follow_up_catatan` |
| 8 | `FK_catatan_siswa_follow_up_users` |

## catatanawal_admin

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 64 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `idcatatanawal_admin` |
| 2 | `nama` |
| 3 | `tlp` |
| 4 | `email` |
| 5 | `status` |
| 6 | `created_at` |
| 7 | `updated_at` |

## catatanawal_datautama

| Property | Value |
|----------|-------|
| **Columns** | 29 |
| **Rows** | 9 |

### Columns (29)

| # | Column Name |
|---|-------------|
| 1 | `idcatatanawal_datautama` |
| 2 | `pengontak_admin` |
| 3 | `nama_l` |
| 4 | `nama_p` |
| 5 | `jenis_k` |
| 6 | `no_wa_ortu` |
| 7 | `no_wa_anak` |
| 8 | `email` |
| 9 | `pilihan_program` |
| 10 | `jenis_program` |
| 11 | `level_1` |
| 12 | `level_2` |
| 13 | `tujuan_program` |
| 14 | `metode` |
| 15 | `info` |
| 16 | `referensi` |
| 17 | `sby_luarsby` |
| 18 | `kewarganegaraan` |
| 19 | `provinsi` |
| 20 | `kabupaten` |
| 21 | `kecamatan` |
| 22 | `kelurahan` |
| 23 | `alamat_lengkap` |
| 24 | `nama_instansi` |
| 25 | `kurikulum` |
| 26 | `pernah_les` |
| 27 | `kesulitan_pelajaran` |
| 28 | `idcatatanawal_admin` |
| 29 | `catatanawal_datautama_ibfk_1` |

## catatanawal_infolain

| Property | Value |
|----------|-------|
| **Columns** | 15 |
| **Rows** | 64 |

### Columns (15)

| # | Column Name |
|---|-------------|
| 1 | `idcatatanawal_infolain` |
| 2 | `jenis_test` |
| 3 | `keterangan` |
| 4 | `trial` |
| 5 | `hasil_test` |
| 6 | `wawancara` |
| 7 | `catatan_penting` |
| 8 | `diterima_dikelas` |
| 9 | `form_daftar` |
| 10 | `bulan_masuk` |
| 11 | `bank` |
| 12 | `wag_lv` |
| 13 | `pic` |
| 14 | `idcatatanawal_admin` |
| 15 | `fk_idcatatan_infolain` |

## catatanawal_tglpenting

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 10 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idcatatanawal_tglpenting` |
| 2 | `kontakA_date` |
| 3 | `wawancara_date` |
| 4 | `trial_date` |
| 5 | `tglbayar_date` |
| 6 | `tglmasuk_date` |
| 7 | `tglkeluar_date` |
| 8 | `idcatatanawal_admin` |
| 9 | `catatanawal_tglpenting_ibfk_1` |

## divisi

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 6 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `iddivisi` |
| 2 | `nama` |

## docs

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `iddoc` |
| 2 | `doc` |
| 3 | `keperluan` |
| 4 | `idkaryawan` |
| 5 | `created_at` |

## file_rapor_siswa

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 1,506 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idfile` |
| 2 | `idjadwal` |
| 3 | `idsiswa` |
| 4 | `path` |
| 5 | `FK_file_rapor_siswa_jadwal` |
| 6 | `FK_file_rapor_siswa_siswa` |

## form

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 1 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idform` |
| 2 | `judul` |
| 3 | `link` |
| 4 | `response` |

## form_calon

| Property | Value |
|----------|-------|
| **Columns** | 38 |
| **Rows** | 184 |

### Columns (38)

| # | Column Name |
|---|-------------|
| 1 | `idcalon` |
| 2 | `fullName` |
| 3 | `email` |
| 4 | `nickName` |
| 5 | `phone1` |
| 6 | `phone2` |
| 7 | `schoolName` |
| 8 | `classLevel` |
| 9 | `gender` |
| 10 | `activities` |
| 11 | `otherActivities` |
| 12 | `curriculum` |
| 13 | `exp` |
| 14 | `diagnostic` |
| 15 | `info` |
| 16 | `class_options` |
| 17 | `officeApp` |
| 18 | `editing` |
| 19 | `custom` |
| 20 | `purpose` |
| 21 | `placement` |
| 22 | `otherDetail` |
| 23 | `computer` |
| 24 | `software` |
| 25 | `hope` |
| 26 | `recom` |
| 27 | `gadget` |
| 28 | `date` |
| 29 | `file` |
| 30 | `kewarganegaraan` |
| 31 | `provinsi` |
| 32 | `kabupaten` |
| 33 | `status` |
| 34 | `keterangan` |
| 35 | `catatanadmin` |
| 36 | `idpendkursus` |
| 37 | `created_at` |
| 38 | `FK_form_calon_pend` |

## form_calon_detil1

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 77 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idcalon_detil1` |
| 2 | `nama_ortu` |
| 3 | `pekerjaan_ortu` |
| 4 | `tempat_lahir` |
| 5 | `tanggal_lahir` |
| 6 | `program` |
| 7 | `idcalon` |
| 8 | `fk_idcalon1` |

## form_calon_detil2

| Property | Value |
|----------|-------|
| **Columns** | 12 |
| **Rows** | 77 |

### Columns (12)

| # | Column Name |
|---|-------------|
| 1 | `idcalon_detil2` |
| 2 | `PIC` |
| 3 | `tgl_trial` |
| 4 | `trial_dimana` |
| 5 | `waktu_test1` |
| 6 | `waktu_test2` |
| 7 | `jenis_test` |
| 8 | `laporan_test` |
| 9 | `laporan_trial` |
| 10 | `diterima` |
| 11 | `idcalon` |
| 12 | `fk_idcalon2` |

## form_calon_detil3

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 77 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idcalon_detil3` |
| 2 | `lokasi` |
| 3 | `status_siswa` |
| 4 | `nomor_invoice` |
| 5 | `bank` |
| 6 | `tanggal_pembayaran` |
| 7 | `bulan_masuk` |
| 8 | `idcalon` |
| 9 | `fk_idcalon3` |

## form_calon_detil4

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 77 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idcalon_detil4` |
| 2 | `followUp1` |
| 3 | `followUp2` |
| 4 | `followUp3` |
| 5 | `keterangan` |
| 6 | `akun_lv` |
| 7 | `idcalon` |
| 8 | `fk_idcalon4` |

## format_rapor

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 45 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idformat_rapor` |
| 2 | `idpendkursus` |
| 3 | `title` |
| 4 | `idpendkursusmitra` |
| 5 | `FK_format_rapor_pendidikankursus` |

## format_rapor_detil

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 129 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idformat_rd` |
| 2 | `idformat_rapor` |
| 3 | `subtitle` |
| 4 | `FK_format_rapor_detil_key` |

## format_rapor_detil_rumus

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 1,650 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idfrdr` |
| 2 | `idformat_rapor` |
| 3 | `idformat_rd` |
| 4 | `param_operator` |
| 5 | `idlevel` |
| 6 | `FK_format_rapor_detil_rumus_head` |
| 7 | `FK_format_rapor_detil_rumus_key` |
| 8 | `FK_format_rapor_detil_rumus_level` |

## format_rapor_rumus

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 3 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idfrr` |
| 2 | `idformat_rapor` |
| 3 | `param_operator` |
| 4 | `FK_format_rapor_rumus_key` |

## format_raport_level

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 348 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idformat_rl` |
| 2 | `idlevel` |
| 3 | `idpendkursus` |
| 4 | `idformat_rapor` |
| 5 | `idpendkursusmitra` |
| 6 | `FK_format_raport_level_key` |
| 7 | `FK_format_raport_level_level` |
| 8 | `FK_format_raport_level_pend` |

## hakakses

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 6 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idhakakses` |
| 2 | `idusers` |
| 3 | `iddivisi` |
| 4 | `pindah` |
| 5 | `status` |
| 6 | `created_at` |
| 7 | `FK_hakakses_1` |
| 8 | `FK_hakakses_2` |

## histori_pengajuan

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 79 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idhistori` |
| 2 | `status` |
| 3 | `catatan` |
| 4 | `idpengajuan` |
| 5 | `created_at` |
| 6 | `FK_histori_pengajuan_1` |

## history_rapor

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 1,366 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idhistori` |
| 2 | `idsiswa` |
| 3 | `idjadwal` |
| 4 | `jadwal` |
| 5 | `tgl` |
| 6 | `status` |
| 7 | `fk_jadwal` |
| 8 | `fk_siswa` |

## identitas

| Property | Value |
|----------|-------|
| **Columns** | 12 |
| **Rows** | 0 |

### Columns (12)

| # | Column Name |
|---|-------------|
| 1 | `kode` |
| 2 | `instansi` |
| 3 | `slogan` |
| 4 | `tahun` |
| 5 | `pimpinan` |
| 6 | `alamat` |
| 7 | `kdpos` |
| 8 | `tlp` |
| 9 | `fax` |
| 10 | `website` |
| 11 | `email` |
| 12 | `logo` |

## infrastruktur

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 1 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idinfrastruktur` |
| 2 | `judul` |
| 3 | `link` |

## jabatan

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 11 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idjabatan` |
| 2 | `jabatan` |
| 3 | `iddivisi` |
| 4 | `induk` |
| 5 | `FK_jabatan_1` |
| 6 | `FK_jabatan_2` |

## jadwal

| Property | Value |
|----------|-------|
| **Columns** | 16 |
| **Rows** | 551 |

### Columns (16)

| # | Column Name |
|---|-------------|
| 1 | `idjadwal` |
| 2 | `groupwa` |
| 3 | `idsesi` |
| 4 | `idpendkursus` |
| 5 | `idperiode` |
| 6 | `hari` |
| 7 | `idlevel` |
| 8 | `idzoom` |
| 9 | `mode_belajar` |
| 10 | `tempat` |
| 11 | `status_archive` |
| 12 | `FK_jadwal_level` |
| 13 | `FK_jadwal_pendidikankursus` |
| 14 | `FK_jadwal_periode` |
| 15 | `FK_jadwal_sesi` |
| 16 | `FK_jadwal_zoom` |

## jadwal_detil

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 17,267 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `idjadwaldetil` |
| 2 | `title` |
| 3 | `description` |
| 4 | `url` |
| 5 | `start` |
| 6 | `end` |
| 7 | `idjadwal` |
| 8 | `color` |
| 9 | `mitra` |
| 10 | `FK_jadwal_detil_key` |

## jadwal_pengajar

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 641 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idpengajar` |
| 2 | `idjadwal` |
| 3 | `idusers` |
| 4 | `idguru` |
| 5 | `FK_jadwal_pengajar_user` |
| 6 | `FK_pengajar_jadwal` |

## jadwal_siswa

| Property | Value |
|----------|-------|
| **Columns** | 15 |
| **Rows** | 3,905 |

### Columns (15)

| # | Column Name |
|---|-------------|
| 1 | `idjadwal_siswa` |
| 2 | `idsiswa` |
| 3 | `idjadwal` |
| 4 | `idjadwaldetil` |
| 5 | `tgl_mulai` |
| 6 | `file_rapor` |
| 7 | `pesan_rapor` |
| 8 | `is_lulus` |
| 9 | `tambahan_sesi` |
| 10 | `tambahan_ket` |
| 11 | `is_keluar` |
| 12 | `tgl_keluar` |
| 13 | `tgl_aktif` |
| 14 | `FK_jadwal_siswa_key` |
| 15 | `FK_jadwal_siswa_siswa` |

## jamkerja

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 3 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idjamkerja` |
| 2 | `namajamkerja` |
| 3 | `jammasuk` |
| 4 | `jampulang` |

## kabupaten

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 521 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idkabupaten` |
| 2 | `idprovinsi` |
| 3 | `name` |
| 4 | `lat` |
| 5 | `lon` |
| 6 | `FK_kabupaten_provinsi` |

## karyawan

| Property | Value |
|----------|-------|
| **Columns** | 31 |
| **Rows** | 51 |

### Columns (31)

| # | Column Name |
|---|-------------|
| 1 | `idkaryawan` |
| 2 | `ktp` |
| 3 | `nickname` |
| 4 | `kota` |
| 5 | `tgl` |
| 6 | `jk` |
| 7 | `goldar` |
| 8 | `agama` |
| 9 | `status` |
| 10 | `alamatktp` |
| 11 | `domisili` |
| 12 | `warga` |
| 13 | `anakke` |
| 14 | `hobi` |
| 15 | `linkedin` |
| 16 | `riwayat` |
| 17 | `email` |
| 18 | `emailkantor` |
| 19 | `telp` |
| 20 | `npwp` |
| 21 | `bpjskerja` |
| 22 | `bpjssehat` |
| 23 | `idusers` |
| 24 | `nama` |
| 25 | `anak` |
| 26 | `rekening` |
| 27 | `moda` |
| 28 | `ig` |
| 29 | `fb` |
| 30 | `link` |
| 31 | `FK_karyawan_1` |

## kecamatan

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 7,269 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idkecamatan` |
| 2 | `idkabupaten` |
| 3 | `nama` |
| 4 | `FK_kecamatan_kabupaten` |

## keluar

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 51 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `idkeluar` |
| 2 | `idusers` |
| 3 | `setuju` |
| 4 | `kirim` |
| 5 | `alasan` |
| 6 | `scan` |
| 7 | `created_at` |
| 8 | `catatan` |
| 9 | `status` |
| 10 | `FK_keluar_1` |

## keluarga

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 64 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `idkeluarga` |
| 2 | `idusers` |
| 3 | `hubungan` |
| 4 | `namalengkap` |
| 5 | `pekerjaan` |
| 6 | `hp` |
| 7 | `FK_keluarga_1` |

## kelurahan

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 83,473 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idkelurahan` |
| 2 | `idkecamatan` |
| 3 | `nama` |
| 4 | `FK_kelurahan_kecamatan` |

## kurikulum

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idkurikulum` |
| 2 | `idlevel` |
| 3 | `judul` |
| 4 | `FK_kurikulum_level` |

## kurikulum_detil

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idkur_det` |
| 2 | `menu` |
| 3 | `idkurikulum` |
| 4 | `FK_kurikulum_detil_key` |

## kurikulum_detil_sub

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 0 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idkur_det_sub` |
| 2 | `kompetensi` |
| 3 | `idkur_det` |
| 4 | `FK_kurikulum_detil_sub_key` |

## kurikulum_kelas

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idkur_kel` |
| 2 | `idkur_det_sub` |
| 3 | `idjadwaldetil` |
| 4 | `FK_kurikulum_kelas_1` |
| 5 | `FK_kurikulum_kelas_2` |

## kursus

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 50 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idkursus` |
| 2 | `nama` |
| 3 | `tanggal` |
| 4 | `deskripsi` |
| 5 | `lokasi` |
| 6 | `nosertifikat` |
| 7 | `idusers` |
| 8 | `FK_kursus_1` |

## leapprofil

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idleap` |
| 2 | `judul` |
| 3 | `link` |

## leapverse

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 365 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idleapverse` |
| 2 | `tgl` |
| 3 | `download` |
| 4 | `aktif` |

## level

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 181 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idlevel` |
| 2 | `level` |
| 3 | `idpendkursus` |
| 4 | `tingkatan` |
| 5 | `mitra` |
| 6 | `FK_level_pendidikan_kursus` |

## libur

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 79 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idlibur` |
| 2 | `title` |
| 3 | `description` |
| 4 | `url` |
| 5 | `start` |
| 6 | `end` |
| 7 | `color` |
| 8 | `libur` |
| 9 | `allprogram` |

## libur_pendkursus

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 2 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idlibur_pddk` |
| 2 | `idpendkursus` |
| 3 | `idlibur` |
| 4 | `fk_libur` |
| 5 | `fk_pendkursus` |

## linkdrive

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idlink` |
| 2 | `link` |
| 3 | `judul` |

## linkform

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 3 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idlink` |
| 2 | `form` |
| 3 | `bidang` |

## log

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 21,887 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `idlog` |
| 2 | `idusers` |
| 3 | `ip` |
| 4 | `browser` |
| 5 | `aktifitas` |
| 6 | `created_at` |
| 7 | `FK_log_1` |

## mitra

| Property | Value |
|----------|-------|
| **Columns** | 26 |
| **Rows** | 22 |

### Columns (26)

| # | Column Name |
|---|-------------|
| 1 | `idmitra` |
| 2 | `nama` |
| 3 | `instansi` |
| 4 | `namasekolah` |
| 5 | `lokasi` |
| 6 | `kepsek` |
| 7 | `cp` |
| 8 | `status` |
| 9 | `visimisi` |
| 10 | `program` |
| 11 | `sdm` |
| 12 | `weakness` |
| 13 | `rekomen` |
| 14 | `created_at` |
| 15 | `jenis` |
| 16 | `provinsi` |
| 17 | `kotkab` |
| 18 | `jml` |
| 19 | `bidang` |
| 20 | `leapverse` |
| 21 | `kemitraan` |
| 22 | `tahun` |
| 23 | `jeniskemitraan` |
| 24 | `elsa` |
| 25 | `classin` |
| 26 | `mitraleap` |

## mitra_note

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 296 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `idmnote` |
| 2 | `idmitra` |
| 3 | `note` |
| 4 | `idusers` |
| 5 | `created_at` |
| 6 | `status` |
| 7 | `startdate` |
| 8 | `enddate` |
| 9 | `FK_mitra_note_1` |
| 10 | `FK_mitra_note_2` |

## mitra_users

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 228 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idmusers` |
| 2 | `idmnote` |
| 3 | `idusers` |
| 4 | `FK_mitra_users_1` |
| 5 | `FK_mitra_users_2` |

## mou

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 2 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idmou` |
| 2 | `kebutuhan` |
| 3 | `keterangan` |
| 4 | `idusers` |
| 5 | `status` |
| 6 | `link` |
| 7 | `created_at` |
| 8 | `catatan` |
| 9 | `FK_mou_1` |

## mou_histori

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 10 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idhistori` |
| 2 | `idmou` |
| 3 | `status` |
| 4 | `catatan` |
| 5 | `created_at` |
| 6 | `FK_mou_histori_1` |

## nowag

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 1 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `idno` |
| 2 | `wa` |

## parameter_nilai

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 1,187 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idp_nilai` |
| 2 | `idlevel` |
| 3 | `parameter` |
| 4 | `isnumber` |
| 5 | `FK_parameter_nilai_level` |

## pekerjaan

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 67 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `idpekerjaan` |
| 2 | `namaperusahaan` |
| 3 | `periode` |
| 4 | `jabatan` |
| 5 | `jobdesk` |
| 6 | `idusers` |
| 7 | `FK_pekerjaan_1` |

## pelamar

| Property | Value |
|----------|-------|
| **Columns** | 44 |
| **Rows** | 178 |

### Columns (44)

| # | Column Name |
|---|-------------|
| 1 | `idpelamar` |
| 2 | `email` |
| 3 | `nama` |
| 4 | `panggilan` |
| 5 | `jk` |
| 6 | `ttl` |
| 7 | `domisili` |
| 8 | `alamat` |
| 9 | `wa` |
| 10 | `sosmed` |
| 11 | `linkedin` |
| 12 | `laptop` |
| 13 | `internet` |
| 14 | `kegiatan` |
| 15 | `rencana` |
| 16 | `mobilitas` |
| 17 | `info` |
| 18 | `wfo` |
| 19 | `bergabung` |
| 20 | `jenis` |
| 21 | `created_at` |
| 22 | `status` |
| 23 | `ig` |
| 24 | `fb` |
| 25 | `idpengajuan` |
| 26 | `work` |
| 27 | `ppdk` |
| 28 | `pengalaman` |
| 29 | `wawasan` |
| 30 | `sehat` |
| 31 | `statusnikah` |
| 32 | `ajar` |
| 33 | `app` |
| 34 | `gunalaptop` |
| 35 | `toefl` |
| 36 | `apps` |
| 37 | `gaji` |
| 38 | `link` |
| 39 | `resign` |
| 40 | `hasiliq` |
| 41 | `piciq` |
| 42 | `picminat` |
| 43 | `picpribadi` |
| 44 | `FK_pelamar_1` |

## pelamar_note

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 403 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `idnote` |
| 2 | `idpelamar` |
| 3 | `status` |
| 4 | `note` |
| 5 | `idusers` |
| 6 | `created_at` |
| 7 | `link` |
| 8 | `pertanyaan` |
| 9 | `FK_pelamar_note_1` |
| 10 | `FK_pelamar_note_2` |

## pelamar_submit

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 0 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `idsubmit` |
| 2 | `idpelamar` |
| 3 | `idusers` |
| 4 | `link` |
| 5 | `created_at` |
| 6 | `FK_pelamar_submit_1` |
| 7 | `FK_pelamar_submit_2` |

## pelamar_users

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 281 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idassign` |
| 2 | `idpelamar` |
| 3 | `idusers` |
| 4 | `FK_pelamarusers_1` |
| 5 | `FK_pelamarusers_2` |

## pendidikan

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 53 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idpendidikan` |
| 2 | `sekolah` |
| 3 | `jenjang` |
| 4 | `prodi` |
| 5 | `tahun` |
| 6 | `ipk` |
| 7 | `idusers` |
| 8 | `organisasi` |
| 9 | `FK_pendidikan_1` |

## pendidikankursus

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 21 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idpendkursus` |
| 2 | `nama_kursus` |
| 3 | `keterangan` |
| 4 | `idinduk` |

## pengajuan

| Property | Value |
|----------|-------|
| **Columns** | 11 |
| **Rows** | 33 |

### Columns (11)

| # | Column Name |
|---|-------------|
| 1 | `idpengajuan` |
| 2 | `keterangan` |
| 3 | `syarat` |
| 4 | `pertanyaan` |
| 5 | `alur` |
| 6 | `test` |
| 7 | `status` |
| 8 | `jumlah` |
| 9 | `idusers` |
| 10 | `created_at` |
| 11 | `FK_pengajuan_1` |

## pengumuman

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 1 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `kode` |
| 2 | `judul` |
| 3 | `isi` |
| 4 | `gambar` |
| 5 | `urutan` |

## perijinan

| Property | Value |
|----------|-------|
| **Columns** | 13 |
| **Rows** | 957 |

### Columns (13)

| # | Column Name |
|---|-------------|
| 1 | `idperijinan` |
| 2 | `jenis` |
| 3 | `tanggalmulai` |
| 4 | `tanggalselesai` |
| 5 | `waktumulai` |
| 6 | `waktuselesai` |
| 7 | `keterangan` |
| 8 | `surat` |
| 9 | `idusers` |
| 10 | `created_at` |
| 11 | `status` |
| 12 | `catatan` |
| 13 | `FK_perijinan_1` |

## perijinan_note

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 2,107 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `idnotes` |
| 2 | `idperijinan` |
| 3 | `baca` |
| 4 | `status` |
| 5 | `catatan` |
| 6 | `idjabatan` |
| 7 | `iddivisi` |
| 8 | `FK_perijinan_note_1` |
| 9 | `FK_perijinan_note_3` |
| 10 | `FK_perijinan_note_4` |

## periode

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 93 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `idperiode` |
| 2 | `nama_term` |
| 3 | `tanggal` |
| 4 | `bulan_awal` |
| 5 | `tahun_awal` |
| 6 | `idpendkursus` |
| 7 | `jml_sesi` |
| 8 | `tahun_ajar` |
| 9 | `mitra` |
| 10 | `FK_periode_pendkursus` |

## pinjam

| Property | Value |
|----------|-------|
| **Columns** | 8 |
| **Rows** | 194 |

### Columns (8)

| # | Column Name |
|---|-------------|
| 1 | `idpinjam` |
| 2 | `tglpinjam` |
| 3 | `deskripsi` |
| 4 | `idusers` |
| 5 | `status` |
| 6 | `catatan` |
| 7 | `created_at` |
| 8 | `FK_pinjam_1` |

## presensi_siswa

| Property | Value |
|----------|-------|
| **Columns** | 11 |
| **Rows** | 97,762 |

### Columns (11)

| # | Column Name |
|---|-------------|
| 1 | `idpresensi_siswa` |
| 2 | `idjadwaldetil` |
| 3 | `idsiswa` |
| 4 | `waktu` |
| 5 | `status` |
| 6 | `idjadwal` |
| 7 | `idkur_kel` |
| 8 | `FK_presensi_siswa_jadwal` |
| 9 | `FK_presensi_siswa_jadwaldetil` |
| 10 | `FK_presensi_siswa_kurkel` |
| 11 | `FK_presensi_siswa_siswa` |

## problem

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 160 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idproblem` |
| 2 | `keterangan` |
| 3 | `idusers` |
| 4 | `status` |
| 5 | `created_at` |
| 6 | `solved_at` |
| 7 | `catatan` |
| 8 | `image_path` |
| 9 | `FK_problem_1` |

## provinsi

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 36 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `idprovinsi` |
| 2 | `nama` |

## purchase

| Property | Value |
|----------|-------|
| **Columns** | 10 |
| **Rows** | 110 |

### Columns (10)

| # | Column Name |
|---|-------------|
| 1 | `idbeli` |
| 2 | `deskripsi` |
| 3 | `link` |
| 4 | `idusers` |
| 5 | `status` |
| 6 | `catatan` |
| 7 | `created_at` |
| 8 | `done_at` |
| 9 | `linkpurchase` |
| 10 | `FK_purchase_1` |

## purchase_link

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 1 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `idlink` |
| 2 | `link` |

## rapor

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 22,837 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idrapor` |
| 2 | `idjadwal` |
| 3 | `idsiswa` |
| 4 | `tanggal` |
| 5 | `idp_nilai` |
| 6 | `nilai` |
| 7 | `FK_rapor_jadwal` |
| 8 | `FK_rapor_parameter` |
| 9 | `FK_rapor_siswa` |

## role

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 9 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `idrole` |
| 2 | `nama_role` |

## role_users

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 0 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idru` |
| 2 | `idusers` |
| 3 | `idmitra` |

## sesi

| Property | Value |
|----------|-------|
| **Columns** | 4 |
| **Rows** | 43 |

### Columns (4)

| # | Column Name |
|---|-------------|
| 1 | `idsesi` |
| 2 | `nama_sesi` |
| 3 | `waktu_awal` |
| 4 | `waktu_akhir` |

## siswa

| Property | Value |
|----------|-------|
| **Columns** | 52 |
| **Rows** | 1,469 |

### Columns (52)

| # | Column Name |
|---|-------------|
| 1 | `idsiswa` |
| 2 | `tgl_daftar` |
| 3 | `domisili` |
| 4 | `nama_lengkap` |
| 5 | `panggilan` |
| 6 | `jkel` |
| 7 | `nama_sekolah` |
| 8 | `level_sekolah` |
| 9 | `nama_ortu` |
| 10 | `pekerjaan_ortu` |
| 11 | `tmp_lahir` |
| 12 | `tgl_lahir` |
| 13 | `no_induk` |
| 14 | `email` |
| 15 | `tlp` |
| 16 | `keluar` |
| 17 | `idcalon` |
| 18 | `asal_calon` |
| 19 | `provinsi` |
| 20 | `kabupaten` |
| 21 | `kecamatan` |
| 22 | `kelurahan` |
| 23 | `idmitra` |
| 24 | `nisn` |
| 25 | `nik` |
| 26 | `kewarganegaraan` |
| 27 | `agama` |
| 28 | `rt` |
| 29 | `rw` |
| 30 | `kodepos` |
| 31 | `statussiswa` |
| 32 | `rekomen` |
| 33 | `info` |
| 34 | `pembayaran` |
| 35 | `nama_ayah` |
| 36 | `pekerjaan_ayah` |
| 37 | `jenjang_ayah` |
| 38 | `penghasilan_ayah` |
| 39 | `penghasilan_ibu` |
| 40 | `jenjang_ibu` |
| 41 | `nama_wali` |
| 42 | `pekerjaan_wali` |
| 43 | `jenjang_wali` |
| 44 | `penghasilan_wali` |
| 45 | `wawalmur` |
| 46 | `waadmin` |
| 47 | `wapeserta` |
| 48 | `sts_pengisian` |
| 49 | `nama_ibu` |
| 50 | `bukti` |
| 51 | `lulus` |
| 52 | `created_bukti` |

## siswa_keluar

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 556 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idsiswa_keluar` |
| 2 | `idsiswa` |
| 3 | `alasan` |
| 4 | `tanggal` |
| 5 | `FK_siswa_keluar_siswa` |

## siswa_keluar_mitra

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 0 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idsiswa_keluar` |
| 2 | `idsiswa` |
| 3 | `alasan` |
| 4 | `tanggal` |
| 5 | `FK_siswamitra_keluar_1` |

## siswa_keluar_tag

| Property | Value |
|----------|-------|
| **Columns** | 7 |
| **Rows** | 404 |

### Columns (7)

| # | Column Name |
|---|-------------|
| 1 | `idstag` |
| 2 | `idtag` |
| 3 | `idsiswa` |
| 4 | `idsiswa_keluar` |
| 5 | `FK_siswa_keluar_tag_1` |
| 6 | `FK_siswa_keluar_tag_2` |
| 7 | `FK_siswa_keluar_tag_3` |

## siswamitra

| Property | Value |
|----------|-------|
| **Columns** | 16 |
| **Rows** | 0 |

### Columns (16)

| # | Column Name |
|---|-------------|
| 1 | `idsiswa` |
| 2 | `tgl_daftar` |
| 3 | `domisili` |
| 4 | `nama_lengkap` |
| 5 | `panggilan` |
| 6 | `jkel` |
| 7 | `nama_instansi` |
| 8 | `level_sekolah` |
| 9 | `pekerjaan` |
| 10 | `tmp_lahir` |
| 11 | `tgl_lahir` |
| 12 | `no_induk` |
| 13 | `email` |
| 14 | `tlp` |
| 15 | `keluar` |
| 16 | `idmitra` |

## sop

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 4 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idsop` |
| 2 | `judulsop` |
| 3 | `link` |
| 4 | `created_at` |
| 5 | `idsopkategori` |
| 6 | `FK_sop_1` |

## sopkategori

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 3 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `idsopkategori` |
| 2 | `nama` |

## suratkeluar

| Property | Value |
|----------|-------|
| **Columns** | 9 |
| **Rows** | 213 |

### Columns (9)

| # | Column Name |
|---|-------------|
| 1 | `idsurat` |
| 2 | `keterangan` |
| 3 | `link` |
| 4 | `idusers` |
| 5 | `status` |
| 6 | `created_at` |
| 7 | `nosurat` |
| 8 | `catatan` |
| 9 | `FK_suratkeluar_1` |

## suratkeluar_histori

| Property | Value |
|----------|-------|
| **Columns** | 6 |
| **Rows** | 477 |

### Columns (6)

| # | Column Name |
|---|-------------|
| 1 | `idstatus` |
| 2 | `idsurat` |
| 3 | `status` |
| 4 | `catatan` |
| 5 | `created_at` |
| 6 | `fk_suratkeluarhistori_idsurat` |

## surattugas

| Property | Value |
|----------|-------|
| **Columns** | 17 |
| **Rows** | 135 |

### Columns (17)

| # | Column Name |
|---|-------------|
| 1 | `idsurat` |
| 2 | `acara` |
| 3 | `undangan` |
| 4 | `waktu` |
| 5 | `lokasi` |
| 6 | `jenis` |
| 7 | `status` |
| 8 | `idusers` |
| 9 | `created_at` |
| 10 | `nosurat` |
| 11 | `catatan` |
| 12 | `link` |
| 13 | `linklaporan` |
| 14 | `notelaporan` |
| 15 | `ket` |
| 16 | `notebatal` |
| 17 | `fk_surattugas_idusers` |

## surattugas_users

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 304 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idsu` |
| 2 | `idsurat` |
| 3 | `idusers` |
| 4 | `fk_surattugasusers_idsurat` |
| 5 | `fk_surattugasusers_idusers` |

## syarat

| Property | Value |
|----------|-------|
| **Columns** | 2 |
| **Rows** | 1 |

### Columns (2)

| # | Column Name |
|---|-------------|
| 1 | `idsyarat` |
| 2 | `syarat` |

## tag_keluar

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 11 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idtag` |
| 2 | `tag` |
| 3 | `keterangan` |

## tag_materi_diskusi

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 11 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idtagmd` |
| 2 | `tag` |
| 3 | `keterangan` |

## ttd

| Property | Value |
|----------|-------|
| **Columns** | 3 |
| **Rows** | 1 |

### Columns (3)

| # | Column Name |
|---|-------------|
| 1 | `idttd` |
| 2 | `ttd` |
| 3 | `status` |

## users

| Property | Value |
|----------|-------|
| **Columns** | 26 |
| **Rows** | 51 |

### Columns (26)

| # | Column Name |
|---|-------------|
| 1 | `idusers` |
| 2 | `email` |
| 3 | `pass` |
| 4 | `nama` |
| 5 | `foto` |
| 6 | `idrole` |
| 7 | `wa` |
| 8 | `thnbekerja` |
| 9 | `idjabatan` |
| 10 | `idjamkerja` |
| 11 | `minat` |
| 12 | `status` |
| 13 | `idbidang` |
| 14 | `ispurchase` |
| 15 | `isteaching` |
| 16 | `ishr` |
| 17 | `isga` |
| 18 | `isit` |
| 19 | `ispdd` |
| 20 | `isbusdev` |
| 21 | `ispimpinan` |
| 22 | `ttd` |
| 23 | `expertise` |
| 24 | `FK_users_1` |
| 25 | `FK_users_2` |
| 26 | `FK_users_3` |

## zoom

| Property | Value |
|----------|-------|
| **Columns** | 5 |
| **Rows** | 14 |

### Columns (5)

| # | Column Name |
|---|-------------|
| 1 | `idzoom` |
| 2 | `topic` |
| 3 | `link` |
| 4 | `meeting_id` |
| 5 | `passcode` |

