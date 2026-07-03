# 🔍 Laporan Audit Anomali & Data Cleaning Fase 3 (Refined)

Laporan ini berisi hasil pemindaian langsung pada data Fase 3 yang dihasilkan oleh `script_hanif.ipynb`.
Laporan ini **mengecualikan** temuan yang murni berupa tag HTML (karena tag HTML digunakan untuk kebutuhan pemanggilan di web),
serta **mengecualikan** kata/abreviasi valid (seperti 'S1', 'SMA', 'Tahap Test', dll.) dan nilai numerik murni.
Laporan ini berfokus pada data aneh, uji coba programmer (trial/dummy/gibberish), format email/HP salah, serta placeholder pada kolom wajib.

## 📋 Tabel: `pengajuan_karyawan` (14 temuan)

| ID Baris | Kolom | Nilai Saat Ini | Kategori | Detail Alasan |
|---|---|---|---|---|
| `id_user: U00020` | `daftar_tes` | `<p>....</p>` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '....' |
| `id_user: U00016` | `pertanyaan` | `<p>none</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'none' |
| `id_user: U00016` | `alur_seleksi` | `<p>none</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'none' |
| `id_user: U00016` | `daftar_tes` | `<p>none</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'none' |
| `id_user: U00016` | `pertanyaan` | `<p>none</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'none' |
| `id_user: U00016` | `alur_seleksi` | `<p>none</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'none' |
| `id_user: U00016` | `daftar_tes` | `<p>none</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'none' |
| `id_user: U00016` | `syarat` | `<p>xx</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `id_user: U00016` | `pertanyaan` | `<p>&nbsp;xx</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `id_user: U00016` | `alur_seleksi` | `<p>&nbsp;xx</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `id_user: U00016` | `daftar_tes` | `<p>&nbsp;xx</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `id_user: U00016` | `pertanyaan` | `<p>x</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `id_user: U00016` | `alur_seleksi` | `<p>&nbsp;x</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `id_user: U00016` | `daftar_tes` | `<p>&nbsp;x</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |

---

## 📋 Tabel: `pelamar` (312 temuan)

| ID Baris | Kolom | Nilai Saat Ini | Kategori | Detail Alasan |
|---|---|---|---|---|
| `Index: 0` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 0` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 0` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 0` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 0` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 0` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 2` | `tempat_lahir` | `asd` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'asd' |
| `Index: 2` | `alamat_ktp` | `asd` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'asd' |
| `Index: 2` | `alamat_domisili` | `asda` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'asda' |
| `Index: 2` | `kegiatan_sekarang` | `ZX` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'ZX' |
| `Index: 2` | `rencana_karir` | `ZX` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'ZX' |
| `Index: 2` | `riwayat_kerja` | `sad` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'sad' |
| `Index: 2` | `riwayat_pendidikan` | `asd` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'asd' |
| `Index: 2` | `pengalaman_bidang` | `<p>asdasd</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'asdasd' |
| `Index: 2` | `wawasan` | `asda` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'asda' |
| `Index: 2` | `riwayat_kesehatan` | `asd` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'asd' |
| `Index: 2` | `aplikasi_lainnya` | `ZX` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'ZX' |
| `Index: 6` | `nama_lengkap` | `gg` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'gg' |
| `Index: 6` | `nama_panggilan` | `t` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 't' |
| `Index: 7` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 9` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 9` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 9` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 9` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 9` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 9` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 14` | `nama_lengkap` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 14` | `nama_panggilan` | `f` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'f' |
| `Index: 14` | `kegiatan_sekarang` | `v` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'v' |
| `Index: 14` | `rencana_karir` | `v` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'v' |
| `Index: 16` | `nama_lengkap` | `mj` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'mj' |
| `Index: 16` | `nama_panggilan` | `mj` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'mj' |
| `Index: 16` | `akun_linkedin` | `li` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'li' |
| `Index: 16` | `akun_instagram` | `ig` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'ig' |
| `Index: 16` | `akun_facebook` | `fb` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'fb' |
| `Index: 16` | `kegiatan_sekarang` | `yj` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'yj' |
| `Index: 16` | `rencana_karir` | `yj` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'yj' |
| `Index: 16` | `riwayat_kerja` | `ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'ya' |
| `Index: 16` | `riwayat_pendidikan` | `ay` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'ay' |
| `Index: 16` | `pengalaman_bidang` | `<p>ay</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'ay' |
| `Index: 16` | `wawasan` | `ay` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'ay' |
| `Index: 16` | `riwayat_kesehatan` | `ay` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'ay' |
| `Index: 16` | `aplikasi_lainnya` | `ay` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'ay' |
| `Index: 18` | `nama_lengkap` | `s` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 's' |
| `Index: 18` | `nama_panggilan` | `s` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 's' |
| `Index: 18` | `tempat_lahir` | `s` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 's' |
| `Index: 18` | `alamat_ktp` | `s` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 's' |
| `Index: 18` | `alamat_domisili` | `s` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 's' |
| `Index: 18` | `akun_linkedin` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `akun_instagram` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `akun_facebook` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `kegiatan_sekarang` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `rencana_karir` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `riwayat_kerja` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `riwayat_pendidikan` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `pengalaman_bidang` | `<p>x</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `wawasan` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `riwayat_kesehatan` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 18` | `aplikasi_lainnya` | `x` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'x' |
| `Index: 20` | `nama_lengkap` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 20` | `nama_panggilan` | `f` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'f' |
| `Index: 20` | `riwayat_kerja` | `fxzg` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'fxzg' |
| `Index: 20` | `riwayat_pendidikan` | `vfg` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'vfg' |
| `Index: 20` | `wawasan` | `zgdh` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'zgdh' |
| `Index: 20` | `riwayat_kesehatan` | `zxfxgf` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'zxfxgf' |
| `Index: 23` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 23` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 23` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 23` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 23` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 23` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `id_pengajuan: 5` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 31` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 31` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 31` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 31` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 31` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 31` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 36` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 36` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 36` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 36` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 36` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 36` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 38` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 38` | `alasan_resign` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `id_pengajuan: 7` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `id_pengajuan: 7` | `alasan_resign` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `id_pengajuan: 1` | `akun_linkedin` | `None` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'None' |
| `Index: 44` | `nama_lengkap` | `edd` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'edd' |
| `Index: 44` | `akun_linkedin` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `akun_instagram` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `akun_facebook` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `kegiatan_sekarang` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `rencana_karir` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `riwayat_kerja` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `riwayat_pendidikan` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `pengalaman_bidang` | `<p>dd</p>` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'dd' |
| `Index: 44` | `wawasan` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `riwayat_kesehatan` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `Index: 44` | `aplikasi_lainnya` | `d` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'd' |
| `id_pengajuan: 12` | `nama_panggilan` | `Ana` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'Ana' |
| `id_pengajuan: 13` | `siap_wfo` | `ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'ya' |
| `id_pengajuan: 13` | `alasan_resign` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 60` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 60` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 60` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 60` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 60` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 60` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `id_pengajuan: 13` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 66` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 66` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 66` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 66` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 66` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 66` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `id_pengajuan: 14` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `id_pengajuan: 14` | `alasan_resign` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 71` | `riwayat_pendidikan` | `MA` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'MA' |
| `Index: 72` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 72` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 72` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 72` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 72` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 72` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `id_pengajuan: 15` | `riwayat_pendidikan` | `MA` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'MA' |
| `id_pengajuan: 14` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 78` | `tempat_lahir` | `Gu` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'Gu' |
| `id_pengajuan: 15` | `tempat_lahir` | `Gu` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'Gu' |
| `Index: 83` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 83` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 83` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 83` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 83` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 83` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `id_pengajuan: 16` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `id_pengajuan: 16` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `id_pengajuan: 16` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `id_pengajuan: 16` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 90` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 90` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 90` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 90` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 90` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 90` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 97` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 97` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 97` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 97` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 97` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 97` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `id_pengajuan: 16` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `id_pengajuan: 16` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `id_pengajuan: 16` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 101` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 102` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 102` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 102` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 102` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 102` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 102` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 103` | `nama_lengkap` | `mj` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'mj' |
| `Index: 103` | `nama_panggilan` | `mj` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'mj' |
| `Index: 103` | `akun_linkedin` | `asss` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'asss' |
| `Index: 105` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 105` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 105` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 105` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 105` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 105` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 115` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 115` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 115` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 115` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 115` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 115` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `id_pengajuan: 1` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `id_pengajuan: 1` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 125` | `nama_lengkap` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `nama_panggilan` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `tempat_lahir` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `alamat_ktp` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `alamat_domisili` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `akun_linkedin` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 125` | `kegiatan_sekarang` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `rencana_karir` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `riwayat_kerja` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `riwayat_pendidikan` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `pengalaman_bidang` | `<p>q</p>` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `wawasan` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `riwayat_kesehatan` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 125` | `aplikasi_lainnya` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `Index: 134` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 134` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 134` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 134` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 134` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 134` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 142` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `id_pengajuan: 30` | `nama_panggilan` | `Err` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'Err' |
| `id_pengajuan: 30` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `id_pengajuan: 30` | `alasan_resign` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 150` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 150` | `alasan_resign` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 151` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 151` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 151` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 151` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 151` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 151` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 152` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 152` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 152` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 152` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 152` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 152` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 154` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 154` | `alasan_resign` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 160` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 160` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 160` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 160` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 160` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 160` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 163` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 163` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 163` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 163` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 163` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 163` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 164` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 171` | `nama_lengkap` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_lengkap' berisi placeholder/default: '-' |
| `Index: 171` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 171` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 171` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 171` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 171` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `id_pengajuan: 30` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 176` | `nama_panggilan` | `Mumu` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'Mumu' |
| `Index: 176` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 177` | `siap_wfo` | `Ya` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'Ya' |
| `Index: 178` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 178` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 178` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 178` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 178` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 179` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 179` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 179` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 179` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 179` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 180` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 180` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 180` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 180` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 180` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 181` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 181` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 181` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 181` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 181` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 182` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 182` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 182` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 182` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 182` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 183` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 183` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 183` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 183` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 183` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 184` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 184` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 184` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 184` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 184` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 185` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 185` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 185` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 185` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 185` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 186` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 186` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 186` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 186` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 186` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 187` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 187` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 187` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 187` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 187` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 188` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 188` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 188` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 188` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 188` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 189` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 189` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 189` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 189` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 189` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 190` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 190` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 190` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 190` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 190` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |
| `Index: 191` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 191` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 191` | `alamat_ktp` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_ktp' berisi placeholder/default: '-' |
| `Index: 191` | `alamat_domisili` | `-` | Nilai Default / Placeholder | Kolom wajib 'alamat_domisili' berisi placeholder/default: '-' |
| `Index: 191` | `nomor_wa` | `-` | Nilai Default / Placeholder | Kolom wajib 'nomor_wa' berisi placeholder/default: '-' |

---

## 📋 Tabel: `progres_pelamar` (5 temuan)

| ID Baris | Kolom | Nilai Saat Ini | Kategori | Detail Alasan |
|---|---|---|---|---|
| `id_pelamar: 177` | `catatan` | `<p>testing</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'testing' |
| `id_pelamar: 177` | `catatan` | `<p>aku coba</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'aku coba' |
| `id_pelamar: 177` | `catatan` | `<p>test</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'test' |
| `id_pelamar: 178` | `catatan` | `<p>haha</p>` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'haha' |
| `id_pelamar: 12` | `catatan` | `<p>coba ya</p><br><p>&nbsp;</p>` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'coba ya' |

---

