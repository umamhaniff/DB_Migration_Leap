# 🔍 Laporan Audit Anomali & Data Cleaning Fase 4 (Refined)

Laporan ini berisi hasil pemindaian langsung pada data Fase 4 yang dihasilkan oleh `script_hanif.ipynb`.
Laporan ini **mengecualikan** temuan yang murni berupa tag HTML (karena tag HTML digunakan untuk kebutuhan pemanggilan di web),
serta **mengecualikan** kata/abreviasi valid (seperti 'S1', 'SMA', 'Tahap Test', dll.) dan nilai numerik murni.
Laporan ini berfokus pada data aneh, uji coba programmer (trial/dummy/gibberish), format email/HP salah, serta placeholder pada kolom wajib.

## 📋 Tabel: `siswa` (1867 temuan)

| ID Baris | Kolom | Nilai Saat Ini | Kategori | Detail Alasan |
|---|---|---|---|---|
| `Index: 0` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 2` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 2` | `email` | `0` | Format Email / Testing Email | Email bernilai numerik default: '0' |
| `Index: 2` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 4` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 8` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 10` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 10` | `nomor_induk` | `--1` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--1' |
| `Index: 10` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 12` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 15` | `nomor_induk` | `--2` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--2' |
| `Index: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 17` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 17` | `nomor_induk` | `--3` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--3' |
| `Index: 17` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 18` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 18` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 19` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 19` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 20` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 21` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 24` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 24` | `nomor_induk` | `--4` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--4' |
| `Index: 24` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 25` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 26` | `asal_sekolah` | `====` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '====' |
| `Index: 26` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 26` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 29` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 29` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 32` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 32` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 33` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 34` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 34` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 37` | `nomor_induk` | `--5` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--5' |
| `Index: 37` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 38` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 40` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 40` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 41` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 41` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 42` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 42` | `nomor_induk` | `--6` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--6' |
| `Index: 42` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 50` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 50` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 52` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 55` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 56` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 57` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 57` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 59` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 61` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 62` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 62` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 63` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 67` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 67` | `nomor_induk` | `--7` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--7' |
| `Index: 67` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 68` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 69` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 69` | `email` | `MIMMA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'MIMMA' |
| `Index: 69` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 71` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 73` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 77` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 77` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 81` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 83` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 84` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 84` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 85` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 91` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 91` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 92` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 92` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 93` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 93` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 95` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 95` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 97` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 97` | `nomor_induk` | `--8` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--8' |
| `Index: 97` | `email` | `SYIFA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'SYIFA' |
| `Index: 97` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 100` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 100` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 102` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 102` | `nomor_induk` | `--9` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--9' |
| `Index: 102` | `email` | `TAMMY` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'TAMMY' |
| `Index: 102` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 105` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 108` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 109` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 110` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 110` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 112` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 112` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 113` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 113` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 115` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 115` | `email` | `VERO` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'VERO' |
| `Index: 115` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 117` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 118` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 118` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 120` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 123` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 124` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 124` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 126` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 126` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 127` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 130` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 130` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 132` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 135` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 135` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 18` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 137` | `email` | `GAGA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'GAGA' |
| `Index: 137` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 141` | `email` | `NADRIA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NADRIA' |
| `Index: 141` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 142` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 143` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 144` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 144` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 145` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 147` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 147` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 148` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 152` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 155` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 156` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 159` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 160` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 160` | `nomor_induk` | `--11` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--11' |
| `Index: 160` | `email` | `SAFINA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'SAFINA' |
| `Index: 160` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 165` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 166` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 166` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 166` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 168` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 169` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 170` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 170` | `email` | `SANDRA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'SANDRA' |
| `Index: 170` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 171` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 171` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 173` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 173` | `email` | `AZZAM` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'AZZAM' |
| `Index: 173` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 175` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 176` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 179` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 181` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 185` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 188` | `nama_ayah` | `aa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aa' |
| `Index: 188` | `nama_ibu` | `aa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aa' |
| `Index: 190` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 191` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 191` | `email` | `ANZO` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'ANZO' |
| `Index: 191` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 193` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 194` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 194` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 195` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 195` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 197` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 197` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 200` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 200` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 202` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 202` | `email` | `BILA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'BILA' |
| `Index: 202` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 204` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 205` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 205` | `email` | `RAFA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'RAFA' |
| `Index: 205` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 209` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 211` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 211` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 212` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 213` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 222` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 222` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 227` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 232` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 232` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 232` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 233` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 236` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 236` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 237` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 237` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 240` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 242` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 243` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 243` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 244` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 244` | `email` | `ARSYAD` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'ARSYAD' |
| `Index: 244` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 245` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 247` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 249` | `rekomendasi` | `--` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--' |
| `Index: 251` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 252` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 252` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 255` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 256` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 256` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 257` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 257` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 258` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 258` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 259` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 259` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 260` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 260` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 261` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 261` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 262` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 266` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 269` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 269` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 270` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 270` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 271` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 272` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 272` | `email` | `RASYA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'RASYA' |
| `Index: 272` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 273` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 273` | `email` | `REHAN` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'REHAN' |
| `Index: 273` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 274` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 274` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 275` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 276` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 276` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 277` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 277` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 279` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 281` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 281` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 282` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 285` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 287` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 287` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 289` | `nama_wali` | `?` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '?' |
| `Index: 292` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 292` | `nomor_induk` | `--22` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--22' |
| `Index: 292` | `email` | `YASMIN` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'YASMIN' |
| `Index: 292` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 293` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 293` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 294` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 294` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 296` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 296` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 300` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 300` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 301` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 301` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 303` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 305` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 306` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 306` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 307` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 308` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 309` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 310` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 310` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 312` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 312` | `email` | `CHARITY` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'CHARITY' |
| `Index: 312` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 313` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 313` | `email` | `JOCELYN` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'JOCELYN' |
| `Index: 313` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 315` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 317` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 318` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 319` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 320` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 321` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 321` | `email` | `SAMIR` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'SAMIR' |
| `Index: 321` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 327` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 327` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 328` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 330` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 331` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 333` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 333` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 335` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 335` | `email` | `ACHA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'ACHA' |
| `Index: 335` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 336` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 336` | `email` | `NAUREEN` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NAUREEN' |
| `Index: 336` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 337` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 337` | `email` | `XINXIN` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'XINXIN' |
| `Index: 337` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 339` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 340` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 341` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 341` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 342` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 342` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 344` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 344` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 345` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 346` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 347` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 349` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 349` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 350` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 351` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 351` | `email` | `RAJAB` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'RAJAB' |
| `Index: 351` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 354` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 359` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 361` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 361` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 362` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 363` | `email` | `NINDYA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NINDYA' |
| `Index: 363` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 365` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 371` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 372` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 373` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 373` | `email` | `ALIF` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'ALIF' |
| `Index: 373` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 376` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 377` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 377` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 378` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 378` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 380` | `tempat_lahir` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 380` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 385` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 386` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 386` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 389` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 391` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 392` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 393` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 394` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 394` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 395` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 396` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 396` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 397` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 397` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 398` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 399` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 399` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 400` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 401` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 401` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 402` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 402` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 403` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 403` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 405` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 405` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 406` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 406` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 407` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 407` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 407` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 408` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 408` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 410` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 410` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 413` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 413` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 415` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 415` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 418` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 418` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 419` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 419` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 421` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 422` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 422` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 424` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 424` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 426` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 426` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 427` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 427` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 428` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 429` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 430` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 8` | `email` | `NF Miss Fita` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NF Miss Fita' |
| `id_mitra: 8` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 8` | `email` | `NF Miss Firoh` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NF Miss Firoh' |
| `id_mitra: 8` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 8` | `email` | `NF Miss Niar` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NF Miss Niar' |
| `id_mitra: 8` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 8` | `email` | `NF Miss Syibti` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NF Miss Syibti' |
| `id_mitra: 8` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 8` | `email` | `NF Miss Darwati` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NF Miss Darwati' |
| `id_mitra: 8` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 8` | `email` | `NF Miss Siska` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NF Miss Siska' |
| `id_mitra: 8` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Afni` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Afni' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Artha` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Artha' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Agus` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Agus' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Rubben` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Rubben' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Almun` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Almun' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Agnes` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Agnes' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Firda` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Firda' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Fiona` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Fiona' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Angga` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Angga' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 1` | `email` | `Nur` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Nur' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 1` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 453` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 453` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 454` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 454` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 456` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 456` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 457` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 458` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 459` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 459` | `nomor_induk` | `--33` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--33' |
| `Index: 459` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 461` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 461` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 463` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 463` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 464` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 467` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 467` | `email` | `REYNA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'REYNA' |
| `Index: 467` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 471` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 471` | `email` | `MUHAMAD INDIARDI` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'MUHAMAD INDIARDI' |
| `Index: 471` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 475` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 482` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 486` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 486` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 488` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 488` | `email` | `ALYA` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'ALYA' |
| `Index: 488` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 491` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 491` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 493` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 496` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 496` | `email` | `NAZNIN` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'NAZNIN' |
| `Index: 496` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 497` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 497` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 498` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 498` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 502` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 502` | `email` | `Dea` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Dea' |
| `Index: 502` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 503` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 503` | `email` | `Robby` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Robby' |
| `Index: 503` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 504` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 504` | `email` | `Giovanni` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Giovanni' |
| `Index: 504` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 505` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 505` | `email` | `Aisyah` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'Aisyah' |
| `Index: 505` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 506` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 506` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 508` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 510` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 511` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 511` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 515` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 516` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 516` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 517` | `asal_sekolah` | `NO` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'NO' |
| `Index: 517` | `tempat_lahir` | `NO` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'NO' |
| `Index: 517` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 520` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_panggilan` | `MEE` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'MEE' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 538` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 540` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 542` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 543` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 544` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 544` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 545` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 545` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 546` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 546` | `tempat_lahir` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 546` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 548` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 548` | `tempat_lahir` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 548` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 549` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 550` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 551` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 551` | `tempat_lahir` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 551` | `email` | `REYNARD` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'REYNARD' |
| `Index: 551` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 552` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 553` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 555` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 555` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 555` | `tempat_lahir` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 555` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 558` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 558` | `tempat_lahir` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 558` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 559` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 561` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 569` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 570` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 572` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 575` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 576` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 577` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 578` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 580` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 581` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 582` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 588` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 588` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 589` | `email` | `GALUH` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'GALUH' |
| `Index: 589` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 590` | `rekomendasi` | `None` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'None' |
| `Index: 590` | `nama_ayah` | `P` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'P' |
| `Index: 590` | `nama_ibu` | `B` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'B' |
| `Index: 590` | `nama_wali` | `C` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'C' |
| `Index: 590` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 591` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 592` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 596` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 596` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 597` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 597` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 599` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 601` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 603` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 604` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 607` | `rekomendasi` | `Kakak` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'Kakak' |
| `Index: 612` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 613` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 616` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 616` | `email` | `ZELIG` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'ZELIG' |
| `Index: 616` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 617` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 617` | `email` | `ZELENE` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'ZELENE' |
| `Index: 617` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 620` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 620` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 624` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 624` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 625` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 626` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 627` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 628` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 629` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 6` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 6` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 668` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 670` | `asal_sekolah` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 670` | `tempat_lahir` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 670` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 671` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 672` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 674` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 683` | `nama_orang_tua` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 684` | `nama_orang_tua` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `Index: 685` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 685` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 685` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 692` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 692` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 692` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 692` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 693` | `nama_ayah` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 693` | `nama_ibu` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 698` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 698` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 698` | `nama_ayah` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 698` | `nama_ibu` | `X` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'X' |
| `Index: 699` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 699` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 699` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 699` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 700` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 700` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 700` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 700` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 3` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 3` | `email` | `DESAK` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'DESAK' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 754` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 755` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 755` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 755` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 757` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 4` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 4` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 4` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 4` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 4` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 4` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 4` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 4` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 4` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 5` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 5` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 7` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 7` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 7` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 7` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 7` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 7` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 2` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 2` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 805` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 2` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 2` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 2` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 2` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 2` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 3` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 3` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 835` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 835` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 9` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 9` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 857` | `nama_wali` | `n` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'n' |
| `Index: 860` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 861` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 863` | `rekomendasi` | `kakak` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'kakak' |
| `Index: 869` | `nama_ayah` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 869` | `nama_ibu` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 874` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 879` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 879` | `nama_ayah` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 879` | `nama_ibu` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 880` | `nama_lengkap` | `QO QO` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'QO QO' |
| `Index: 880` | `asal_sekolah` | `fdfdfdf` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'fdfdfdf' |
| `Index: 880` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 880` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 18` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 884` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 884` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 884` | `nama_ayah` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 884` | `nama_ibu` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 885` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 885` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 885` | `nama_ayah` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 885` | `nama_ibu` | `XX` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'XX' |
| `Index: 888` | `nama_panggilan` | `AXXA` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'AXXA' |
| `Index: 890` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 892` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 892` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 892` | `nama_ayah` | `xx` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `Index: 892` | `nama_ibu` | `xx` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `Index: 895` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 18` | `asal_sekolah` | `E` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'E' |
| `id_mitra: 18` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `id_mitra: 18` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 900` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 900` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 902` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 903` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 903` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 903` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 903` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 903` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 904` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 904` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 904` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 904` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 913` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 915` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 915` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 915` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 915` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 916` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 917` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 922` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 922` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 922` | `nama_ayah` | `aaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaa' |
| `Index: 922` | `nama_ibu` | `aaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaa' |
| `Index: 922` | `nama_wali` | `aaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaa' |
| `Index: 923` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 924` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 925` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 930` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 934` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 935` | `email` | `test@gmail.com` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'test@gmail.com' |
| `Index: 935` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 937` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 937` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 937` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 937` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 938` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 939` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 939` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 939` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 939` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 941` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 942` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 942` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 942` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 942` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 947` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 947` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 947` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 947` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 948` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 948` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 955` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 956` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 956` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 956` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 956` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 958` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 958` | `nama_ayah` | `A` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'A' |
| `Index: 958` | `nama_ibu` | `A` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'A' |
| `Index: 958` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 959` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 959` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 959` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 959` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 961` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 961` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 961` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 961` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 962` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 962` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 962` | `nama_ayah` | `xx` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `Index: 962` | `nama_ibu` | `xx` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `Index: 962` | `nama_wali` | `xx` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'xx' |
| `Index: 963` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 964` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 965` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 965` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 965` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 965` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 965` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 966` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 966` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 966` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 966` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 966` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 969` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 970` | `nama_ayah` | `aaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaa' |
| `Index: 970` | `nama_ibu` | `aaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaa' |
| `Index: 970` | `nama_wali` | `aaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaa' |
| `Index: 974` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 975` | `nomor_induk` | `--44` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--44' |
| `id_mitra: 18` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 978` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 978` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 978` | `nama_ayah` | `aaaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaaa' |
| `Index: 978` | `nama_ibu` | `aaaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaaa' |
| `Index: 978` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 980` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 980` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 980` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 980` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 980` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 984` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 984` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 984` | `nama_ayah` | `A` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'A' |
| `Index: 984` | `nama_ibu` | `A` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'A' |
| `Index: 984` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 985` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 985` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 985` | `nama_ayah` | `AA` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'AA' |
| `Index: 985` | `nama_ibu` | `AAAA` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'AAAA' |
| `Index: 985` | `nama_wali` | `AAAAA` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'AAAAA' |
| `Index: 986` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 988` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 990` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 990` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 990` | `nama_ayah` | `A` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'A' |
| `Index: 990` | `nama_ibu` | `A` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'A' |
| `Index: 990` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 991` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 991` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 991` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 991` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 991` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 995` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 995` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 996` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 998` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 999` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1001` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1001` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1001` | `nama_ayah` | `aaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaa' |
| `Index: 1001` | `nama_ibu` | `aaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaa' |
| `Index: 1003` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1005` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1005` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1005` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1006` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1006` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1006` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1007` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1007` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1007` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1008` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1008` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1008` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1009` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1009` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1009` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1010` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1010` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1010` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1011` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1011` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1011` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1012` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1012` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1012` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1013` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1013` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1013` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1014` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1014` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1014` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1015` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1015` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1015` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1016` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1016` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1016` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1017` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1017` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1017` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1018` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1018` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1018` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1019` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1019` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1019` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1020` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1020` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1020` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1021` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1021` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1021` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1022` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1022` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1022` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1023` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1023` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1023` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1024` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1024` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1024` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1025` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1025` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1025` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1026` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1026` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1026` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1027` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1027` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1027` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1033` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1033` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1033` | `nama_ayah` | `aaaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaaa' |
| `Index: 1033` | `nama_ibu` | `aaaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaaa' |
| `Index: 1033` | `nama_wali` | `aaaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaaa' |
| `Index: 1034` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1034` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1034` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1034` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1035` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1035` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1035` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1035` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1036` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1036` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1036` | `nama_ayah` | `aaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaa' |
| `Index: 1036` | `nama_ibu` | `aaaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaaa' |
| `Index: 1037` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1037` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1037` | `nama_ayah` | `aaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaa' |
| `Index: 1037` | `nama_ibu` | `aaaaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaaaa' |
| `Index: 1037` | `nama_wali` | `aaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaa' |
| `Index: 1039` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1039` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1039` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 1039` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 1039` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1042` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1042` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1042` | `nama_ayah` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 1042` | `nama_ibu` | `a` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'a' |
| `Index: 1043` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1044` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1044` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1044` | `nama_ayah` | `aaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaa' |
| `Index: 1044` | `nama_ibu` | `aaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaa' |
| `Index: 1044` | `nama_wali` | `aaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaa' |
| `Index: 1045` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1046` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1046` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1046` | `nama_ayah` | `A` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'A' |
| `Index: 1046` | `nama_ibu` | `A` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'A' |
| `Index: 1046` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1049` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1050` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1052` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1053` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1058` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1058` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1058` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1058` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1059` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1059` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1060` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1060` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1061` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1063` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1063` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1064` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1064` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1065` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1065` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1065` | `nama_ayah` | `aaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaa' |
| `Index: 1065` | `nama_ibu` | `aaaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaaa' |
| `Index: 1065` | `nama_wali` | `aaaaa` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'aaaaa' |
| `Index: 1065` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1068` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1068` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1069` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1069` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1071` | `tingkat_sekolah` | `X` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'X' |
| `Index: 1071` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1071` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1075` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1076` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1076` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1077` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 8` | `asal_sekolah` | `qq` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'qq' |
| `id_mitra: 8` | `nama_orang_tua` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `id_mitra: 8` | `tempat_lahir` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `id_mitra: 8` | `email` | `q` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'q' |
| `id_mitra: 8` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1080` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1080` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1081` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1081` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1082` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1082` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1083` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1083` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1084` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1084` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1084` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1084` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1085` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1085` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1085` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1085` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1086` | `nama_lengkap` | `coba` | Programmer Trial / Dummy | Kolom berisi teks uji coba/gibberish pendek: 'coba' |
| `Index: 1086` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1086` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1087` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1087` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1088` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1088` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `tempat_lahir` | `BW` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'BW' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 20` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1269` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1269` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1269` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1270` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1272` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1273` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1274` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1275` | `nama_panggilan` | `qo` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'qo' |
| `Index: 1275` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1275` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 11` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 11` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 11` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 11` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 11` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 11` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 11` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 11` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 11` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 11` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `email` | `putriyantil@gmail,com` | Format Email / Testing Email | Format email tidak valid atau email uji coba: 'putriyantil@gmail,com' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1312` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1312` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1313` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1313` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 12` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 12` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 12` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 12` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 12` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 12` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 12` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 12` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 12` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 12` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 12` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 12` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1359` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1360` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1360` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1361` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 21` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 21` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 21` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 21` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1368` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1368` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1369` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1375` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1376` | `rekomendasi` | `MJ` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'MJ' |
| `Index: 1376` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1377` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1378` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1378` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1379` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1381` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 13` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 14` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 14` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 14` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 11` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 11` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 15` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 15` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 15` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1416` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1416` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1417` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1417` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1420` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1420` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1421` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1423` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1424` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1424` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1425` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1425` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1426` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1426` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1427` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1427` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1428` | `nama_panggilan` | `-` | Nilai Default / Placeholder | Kolom wajib 'nama_panggilan' berisi placeholder/default: '-' |
| `Index: 1428` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1428` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `Index: 1428` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1430` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `nama_panggilan` | `IBI` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'IBI' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 16` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 16` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 12` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 12` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1434` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1436` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1436` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1437` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1437` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1438` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1438` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 13` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1440` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1440` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `id_mitra: 22` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `id_mitra: 22` | `email` | `-` | Format Email / Testing Email | Format email tidak valid atau email uji coba: '-' |
| `id_mitra: 22` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |
| `Index: 1468` | `tempat_lahir` | `-` | Nilai Default / Placeholder | Kolom wajib 'tempat_lahir' berisi placeholder/default: '-' |
| `Index: 1468` | `wa_siswa` | `-` | Nilai Default / Placeholder | Kolom wajib 'wa_siswa' berisi placeholder/default: '-' |

---

## 📋 Tabel: `siswa_keluar` (19 temuan)

| ID Baris | Kolom | Nilai Saat Ini | Kategori | Detail Alasan |
|---|---|---|---|---|
| `id_siswa: 57` | `alasan_keluar` | `--` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--' |
| `id_siswa: 404` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 373` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 131` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 101` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 78` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 253` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 346` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 53` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 144` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 671` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 552` | `alasan_keluar` | `--` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--' |
| `id_siswa: 716` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 425` | `alasan_keluar` | `--` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--' |
| `id_siswa: 33` | `alasan_keluar` | `--` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--' |
| `id_siswa: 546` | `alasan_keluar` | `--` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--' |
| `id_siswa: 590` | `alasan_keluar` | `=` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '=' |
| `id_siswa: 693` | `alasan_keluar` | `==` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '==' |
| `id_siswa: 1414` | `alasan_keluar` | `--` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: '--' |

---

## 📋 Tabel: `mitra` (1 temuan)

| ID Baris | Kolom | Nilai Saat Ini | Kategori | Detail Alasan |
|---|---|---|---|---|
| `Index: 9` | `kode_mitra` | `M` | Programmer Trial / Dummy (Gibberish) | Teks berisi karakter berulang atau acak: 'M' |

---

