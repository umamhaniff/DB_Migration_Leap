# Spesifikasi Desain: Penyelarasan Koneksi Database Target (db_future)

**Tanggal:** 2026-06-21  
**Status:** Approved  
**Author:** Antigravity  

---

## 1. Latar Belakang & Motivasi
Dalam proyek migrasi database ini, tim menggunakan database target referensi blueprint bernama `db_future` pada `config.py` untuk mendefinisikan skema tabel target yang bersih dan valid. Pada proses akhir di `insert_handler.ipynb` masing-masing fase, data hasil konversi disuntikkan ke dalam `db_future`. 

Untuk menyelaraskan konfigurasi database target antara script milik Hanif (`script_hanif.ipynb`) dengan milik anggota tim lainnya (Cimut dan Afrida), koneksi database target di dalam notebook Hanif (Fase 1 s/d 5) perlu diarahkan untuk menggunakan konfigurasi `db_future` dari `config.py`.

---

## 2. Tujuan & Lingkup Kerja
Mengubah konfigurasi inisialisasi koneksi database target pada seluruh notebook milik Hanif dari `config['db_new']` menjadi `config['db_future']`.

Notebook yang akan dimodifikasi:
1. `fase_1/script_hanif.ipynb`
2. `fase_2/script_hanif.ipynb`
3. `fase_3/script_hanif.ipynb`
4. `fase_4/script_hanif.ipynb`
5. `fase_5/script_hanif.ipynb`

---

## 3. Detail Rancangan Teknis
Untuk menghindari risiko *code churn* (perubahan kode massal) dan potensi bug variabel tidak terdefinisi (`NameError`) pada cell-cell downstream di dalam notebook yang sangat panjang, kita akan menggunakan pendekatan **Opsi A**:
* Mengubah parameter input fungsi koneksi database di **Cell Inisialisasi Koneksi (Cell 2/3)** agar menggunakan konfigurasi `db_future`.
* Tetap mempertahankan penamaan variabel Python `db_new` dan `cursor_new` di dalam notebook agar seluruh kode program di cell berikutnya tetap berjalan normal tanpa modifikasi.

### Contoh Perubahan Kode Cell Koneksi:

**Sebelum:**
```python
# Connect ke DB Baru
db_new = mysql.connector.connect(**config['db_new'])
cursor_new = db_new.cursor(dictionary=True)
print(f'Connected to new database: {config["db_new"]["database"]}')
```

**Sesudah:**
```python
# Connect ke DB Target (Menggunakan konfigurasi db_future agar seragam dengan tim)
db_new = mysql.connector.connect(**config['db_future'])
cursor_new = db_new.cursor(dictionary=True)
print(f'Connected to target database (db_future config): {config["db_future"]["database"]}')
```

---

## 4. Rencana Pengujian
Setelah modifikasi file Jupyter Notebook dilakukan secara programmatik:
1. Jalankan headless execution menggunakan `nbconvert` untuk masing-masing notebook:
   ```bash
   jupyter nbconvert --to notebook --execute --inplace <path_notebook>
   ```
2. Pastikan file `.pkl` yang dihasilkan (`fase_1_hanif.pkl` s/d `fase_5_hanif.pkl`) terisi data DataFrame yang valid.
3. Lakukan verifikasi status Git sebelum push.
