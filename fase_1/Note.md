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

