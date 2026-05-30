================================================
        FASE 1 - THE THINGS WE SHOULD CHANGE
================================================

TABEL: LIBUR
- delete column sumber
- Update urutan id varchar
Question
- label_warna emang kosong kah? soalnya di db old fc-event-default

TABEL: ROLES
- add column id_division 
Qe=uestion
- Did in the db old have information about this if they dont. that should be fine if we just insert the data we have rn - so the id_division was null

================================================

TABEL: USERS
- Fill this column (email_verified_at, created_at, updated_at) into current time 
- Update urutan id varchar

================================================
        FASE 2 - THE THINGS WE SHOULD CHANGE
================================================

TABEL: KARYAWAN
- Kolom tahun_mulai_kerja dihapus dan diganti menjadi tanggal_bergabung (date)
- The enum change from Laki-laki,Perempuan into Laki laki,Perempuan
- Move the data in column id_karyawan into column kode_karyawan.
- Nama Lengkap was null
- status_pernikahan was blank but not missing value/null bcs the column settings was 🛑 NOT NULL (Wajib Isi) we should change it.

TABEL: KELUARGA_KARYAWAN
- change the id_karyawan cuz after this, this gonna be auto increment

================================================

TABEL: KELURAHAN
- kode_pos this is all null, then what for?