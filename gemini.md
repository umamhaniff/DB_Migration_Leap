# 🔄 6Magang — Database Leap Migration

> Konteks teknis untuk sistem migrasi database Leap dari v5 (Lama) ke v5 (Baru).

## 🎯 Fokus Utama
Migrasi data secara bertahap (per fase) untuk menjaga integritas data dan meminimalisir downtime. Sistem menggunakan pendekatan **Notebook-as-a-Script** di mana logika transformasi berada di Jupyter Notebook namun dijalankan secara otomatis oleh controller Python.

## 🏗️ Arsitektur Sistem
- **Controller:** `migrate_db.py` (Menjalankan notebook secara programatik & logging).
- **Config:** `config.py` (Mapping tabel, koneksi DB, dan urutan fase).
- **Templates:** `setup_files_ipynb.py` (Generator template notebook untuk 3 personel: Cimut, Afrida, Hanif).
- **Phases:** Terbagi menjadi 5 Fase (Master Data -> SDM -> CRM -> KBM -> Penilaian).

## 🛠️ Stack Teknologi
- **Core:** Python 3.10+, MySQL/MariaDB.
- **Libraries:** `mysql-connector-python`, `jupyter` (nbconvert/nbformat), `python-dotenv`.
- **Environment:** Menggunakan file `.env` untuk kredensial database.

## 🚀 Alur Kerja (Workflow)
1. **Setup:** `pip install -r requirements.txt` dan sesuaikan `.env`.
2. **Generate:** Jalankan `python setup_files_ipynb.py` jika file fase belum ada.
3. **Develop:** Isi logika SQL & Transform di notebook `fase_X/script_*.ipynb`.
4. **Execute:** Jalankan `python migrate_db.py` untuk mulai migrasi terkontrol.

## 🧠 Aturan Main (Expert)
1. **Validation First:** Setiap notebook harus mengembalikan `migration_result` (JSON) agar controller bisa memvalidasi sukses/tidaknya migrasi fase tersebut.
2. **Surgical Rerun:** Jika gagal di satu fase, perbaiki notebook-nya lalu jalankan `migrate_db.py` pilih opsi "Run satu fase saja".
3. **Memory Management:** Karena limit RAM 8GB, hindari loading seluruh tabel ke DataFrame jika data sangat besar; gunakan batching atau query SQL langsung untuk insert.
4. **Schema Reference:** Cek `extract/DATABASE_SCHEMA.md` untuk perbandingan struktur antar database.
5. **Safe Notebook Editing:** Selalu mengecek hasil eksekusi saat memodifikasi/patching skrip (terutama file `.ipynb`) secara programatik. Pastikan tidak meninggalkan karakter format JSON yang invalid (seperti escape character atau newline yang salah), karena hal itu akan membuat file `.ipynb` menjadi error (corrupt).
6. **Workspace Organization:** Jika membutuhkan script _patching_, _testing_ manual, atau modifikasi sementara, selalu simpan/buat di dalam folder `config.gemini/` agar direktori *root* proyek tetap bersih dan terstruktur.
