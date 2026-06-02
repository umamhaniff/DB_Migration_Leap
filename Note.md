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
- kode_pos this is all null, then what for? #programmer


================================================
        FASE 3 - THE THINGS WE SHOULD CHANGE
================================================

TABEL: PELAMAR

cuz this table cant in into the database please update the id_pelamar into auto increment then update the child table too.
        - pelamar_kerja (id_pelamar)
        - pelamar_kursus (id_pelamar)
        - pelamar_sekolah (id_pelamar)
        - progres_pelamar (id_pelamar)
        - rekrutmen_pelamar (id_pelamar)

================================================

TABEL: KONTAK_PROSPEK
- delete column created_at and updated_at
- column nama_penanya kosong ga ada datanya (not null)
- column status_kontak (not null)

TABEL: CALON_SISWA
- Delete column sumber_lead (are you sure this is erase) #programmer, status_pipeline, status_updated_at 
- Add column agama, fo_status, fo_status_updated_at, handover_at, latest_submitted_at, first_submitted_at 
- why we need this (fo_status, fo_status_updated_at, handover_at) when the table already connect into table KONTAK_PROSPEK #programmer
- anw this column wa_kontak_awal should be deleted cuz already in table KONTAK_PROSPEK
- on this column jenis_kelamin they are a few table who empty but not missing value
- ga di ambil buat table 
        - calon_siswa_bayar (id_calon)
        - calon_siswa_jadwal (id_calon)
        - calon_siswa_proses (id_calon)

TABEL: CALON_SISWA_AKADEMIK
- why this table id_calon_akademik connect into so many othey table #programmer
        - calon_siswa_bayar (id_calon_akademik)
        - calon_siswa_jadwal (id_calon_akademik)
        - calon_siswa_proses (id_calon_akademik)
        - calon_siswa_proses_logs (id_calon_akademik)
- add new colomn submission_state (not null) but idk what should i add in this column #programmer
- add new colomn submitted_at
- Bersihin jenjang_kelas_1 and jenjang_kelas_2
- is that okkey for column id_kursus to be index not fk? #programmer

TABEL: CALON_SISWA_ORTU
- add column tempat_lahir_ayah, tanggal_lahir_ayah, tempat_lahir_ibu, tanggal_lahir_ibu, tempat_lahir_wali, tanggal_lahir_wali.
- Update enum penghasilan from Kurang dari 1 Juta,1 Juta - 3 Juta,3 Juta - 5 Juta,Lebih dari 5 Juta into 	kurang_1jt,1jt_3jt,3jt_5jt,lebih_5jt

TABEL: CALON_SISWA_BAYAR
- column id_calon change into column id_calon_akademik
- delete column status_siswa why? #programmer

TABEL: CALON_SISWA_JADWAL
- column id_calon change into column id_calon_akademik
- delete column konfirmasi_tes, konfirmasi_trial why? #programmer

TABEL: CALON_SISWA_PROSES
- column id_calon change into column id_calon_akademik (tapi ga nyambung ke tablenya wtf)
- this column admin_pengontak should be deleted cuz in table kontak_prospek already has it.
- delete column status_siswa why? #programmer
- add new column sumber_lead, status_updated_at
- delete column updated_at, created_at

TABEL: VERIFIKASI_SURAT_KELUAR
- in db_future this column catatan_verifikasi_sk was 🛑 NOT NULL (Wajib Isi) and i think this should be null. #programmer

TABEL: SURAT_TUGAS
- add new column periode

================================================

TABEL: CALON_SISWA_KURSUS
- column jenis_program emg kosong kah?

================================================
        FASE 4 - THE THINGS WE SHOULD CHANGE
================================================

TABEL: IZIN_KARYAWAN
- column id_karyawan update colomn ini jadi int

TABEL: ABSENSI
- column id_karyawan update colomn ini jadi int

TABEL: KARYAWAN_RESIGN
- column id_karyawan update colomn ini jadi int

TABEL: JADWAL_DETAIL
- add colomn presensi_disimpan_at

TABEL: JADWAL_SISWA
- add column is_acc_rapor, status_ketuntasan, catatan_ketuntasan_guru, catatan_ketuntasan_admin, ketuntasan_diperbarui_oleh, ketuntasan_diperbarui_pada

TABEL: CATATAN_KELAS
- add column id_karyawan

TABEL: SISWA
- delete column status_aktif, status_lulus_siswa
- new column status_pendaftaran

TABEL: KURSUS_SISWA
- new column status_lulus

================================================

TABEL: MITRA
- ada isinya, kok bisa?? tapi cuma 1 just asking

================================================
        FASE 5 - THE THINGS WE SHOULD CHANGE
================================================

TABEL: RAPOR_FORMAT
- add column urutan

TABEL: RAPOR_FORMAT_SUB
- add column urutan

TABEL: RAPOR_FORMAT_FORMULA_SUB
- add column urutan

TABEL: RAPOR_LEVEL_CONFIG
- column id_rapor_format, id_level just index need check

TABEL: CATATAN_SISWA
- add column id_karyawan, tanggal

================================================

TABEL: RAPOR_SISWA_FILE
- all row in column id_rapor_siswa was null

================================================
        TABLE BARU 
================================================
catatan_remidi_siswa 
siswa_keluar_feedbacks 

