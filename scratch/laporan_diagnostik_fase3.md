# 📊 Audit Laporan Migrasi Data Fase 3
Tanggal Audit: 2026-07-09

| Nama Tabel | Pemilik Blok | Dikirim (Pickle) | Masuk (Database) | Status | Keterangan / Detail Kendala |
|---|---|---|---|---|---|
| `pelamar` | Hanif (Blok A) | 192 | 192 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `pelamar_kerja` | Hanif (Blok A) | 67 | 67 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `pelamar_sekolah` | Hanif (Blok A) | 53 | 53 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `pelamar_kursus` | Hanif (Blok A) | 50 | 50 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `progres_pelamar` | Hanif (Blok A) | 403 | 403 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `rekrutmen_pelamar` | Hanif (Blok A) | 281 | 281 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `pengajuan_karyawan` | Hanif (Blok A) | 33 | 66 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `histori_pengajuan` | Hanif (Blok A) | 79 | 158 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `sop` | Afrida (Blok B) | 4 | 8 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `surat_keluar` | Afrida (Blok B) | 231 | 231 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `verifikasi_surat_keluar` | Afrida (Blok B) | 513 | 1062 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `surat_tugas` | Afrida (Blok B) | 139 | 139 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `surat_tugas_anggota` | Afrida (Blok B) | 319 | 638 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `sop_kategori` | Afrida (Blok B) | 2 | 2 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `kontak_prospek` | Cimut (Blok C & D) | 194 | 194 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `calon_siswa` | Cimut (Blok C & D) | 166 | 0 | ✗ Gagal total | ✗ calon_siswa: Gagal total saat insert - Alasan: 1054 (42S22): Unknown column 'fo_status' in 'field list' |
| `calon_siswa_ortu` | Cimut (Blok C & D) | 166 | 0 | ✗ Gagal total | ✗ calon_siswa_ortu: Gagal total saat insert - Alasan: 1054 (42S22): Unknown column 'tempat_lahir_ayah' in 'field list' |
| `calon_siswa_akademik` | Cimut (Blok C & D) | 166 | 0 | ✗ Gagal total | ✗ calon_siswa_akademik: Gagal total saat insert - Alasan: 1054 (42S22): Unknown column 'submission_state' in 'field list' |
| `calon_siswa_bayar` | Cimut (Blok C & D) | 166 | 0 | ✗ Gagal total | ✗ calon_siswa_bayar: Gagal total saat insert - Alasan: 1054 (42S22): Unknown column 'id_calon_akademik' in 'field list' |
| `calon_siswa_jadwal` | Cimut (Blok C & D) | 166 | 0 | ✗ Gagal total | ✗ calon_siswa_jadwal: Gagal total saat insert - Alasan: 1054 (42S22): Unknown column 'id_calon_akademik' in 'field list' |
| `calon_siswa_kursus` | Cimut (Blok C & D) | 166 | 166 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `calon_siswa_proses` | Cimut (Blok C & D) | 166 | 0 | ✗ Gagal total | ✗ calon_siswa_proses: Gagal total saat insert - Alasan: 1054 (42S22): Unknown column 'id_calon_akademik' in 'field list' |
| `calon_siswa_status_logs` | Cimut (Blok C & D) | 0 | 0 | ℹ️ Kosong | DataFrame kosong (0 baris). |
| `pengadaan` | Cimut (Blok C & D) | 110 | 110 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `peminjaman` | Cimut (Blok C & D) | 194 | 194 | ✓ Sukses | Semua baris ter-insert dengan bersih. |
| `problem` | Cimut (Blok C & D) | 160 | 160 | ✓ Sukses | Semua baris ter-insert dengan bersih. |