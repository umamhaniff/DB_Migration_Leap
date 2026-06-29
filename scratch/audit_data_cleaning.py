import os
import pickle
import pandas as pd
import numpy as np
import re

def is_weird_email(email):
    if pd.isna(email): return False
    email = str(email).strip().lower()
    if email in ('-', '', 'none', 'null', '<na>'): return False
    if '@' not in email or '.' not in email:
        return True
    if any(x in email for x in ['tidakada', 'dummy', 'test@', 'none@', 'dummy@', 'abc@', 'testing@']):
        return True
    return False

def is_weird_phone(phone):
    if pd.isna(phone): return False
    phone = str(phone).strip()
    if phone in ('-', '', 'none', 'null', '0', '<na>'): return False
    # If contains letters
    if any(c.isalpha() for c in phone):
        return True
    # Clean digits
    clean_phone = ''.join(c for c in phone if c.isdigit())
    if len(clean_phone) < 8 or len(clean_phone) > 15:
        return True
    return False

def is_weird_name(name):
    if pd.isna(name): return False
    name = str(name).strip()
    if name in ('-', '', 'none', 'null', '<na>'): return False
    if any(c in name for c in ['<', '>', '/', '\\', '*', '=', '+']):
        return True
    if any(c.isdigit() for c in name):
        return True
    if len(name) < 2:
        return True
    return False

def contains_html(text):
    if pd.isna(text): return False
    text = str(text)
    if any(tag in text for tag in ['<p>', '</p>', '<br>', '&nbsp;', 'href=', '</div>', '<table>']):
        return True
    return False

def is_gibberish(text):
    if pd.isna(text): return False
    text = str(text).strip().lower()
    if text in ('asdf', 'qwerty', 'testing', 'coba', 'test', '123456', 'xyz', 'hjhj', 'klkl'):
        return True
    return False

def audit_phase_data():
    base_dir = r"D:\_CampusLife\ProjectCampus\6Magang\db_migration_leap"
    report_path = os.path.join(base_dir, "extract", "laporan_pemeriksaan_cleaning.md")
    
    # Load mapping files to map new rows back to old IDs
    maps = {}
    try:
        maps['pelamar'] = pd.read_pickle(os.path.join(base_dir, "fase_3", "mapping_pelamar.pkl"))
    except: pass
    try:
        maps['siswa'] = pd.read_pickle(os.path.join(base_dir, "fase_4", "mapping_siswa.pkl"))
    except: pass
    try:
        maps['mitra'] = pd.read_pickle(os.path.join(base_dir, "fase_4", "mapping_mitra.pkl"))
    except: pass
    try:
        maps['mitra_progres'] = pd.read_pickle(os.path.join(base_dir, "fase_4", "mapping_mitra_progres.pkl"))
    except: pass
    try:
        maps['siswa_mitra'] = pd.read_pickle(os.path.join(base_dir, "fase_4", "mapping_siswa_mitra.pkl"))
    except: pass
    try:
        maps['rapor_siswa'] = pd.read_pickle(os.path.join(base_dir, "fase_5", "mapping_rapor_siswa.pkl"))
    except: pass
    try:
        maps['rapor_siswa_file'] = pd.read_pickle(os.path.join(base_dir, "fase_5", "mapping_rapor_siswa_file.pkl"))
    except: pass

    # Phase files
    phases = {
        3: os.path.join(base_dir, "fase_3", "fase_3_hanif.pkl"),
        4: os.path.join(base_dir, "fase_4", "fase_4_hanif.pkl"),
        5: os.path.join(base_dir, "fase_5", "fase_5_hanif.pkl")
    }

    report_lines = []
    report_lines.append("# 🔍 LAPORAN DETAIL PEMERIKSAAN & DATA CLEANING (FASE 3 - 5)\n")
    report_lines.append(f"Laporan ini berisi rincian data baris demi baris yang mengandung nilai placeholder (`-`), tanggal default (`1970-01-01` / `2020-01-01`), angka default (`0` / `0.0` / `2000`), nilai kosong (`None` / `NaN`), serta **nilai aneh / anomali** (format email salah, HP mengandung huruf, teks mengandung tag HTML, nilai gaji tidak wajar, atau teks uji coba/gibberish).\n")
    report_lines.append("---\n")

    for phase_num, file_path in phases.items():
        if not os.path.exists(file_path):
            report_lines.append(f"## ⚠️ FASE {phase_num}: File pickle tidak ditemukan di {file_path}\n")
            continue
            
        report_lines.append(f"## 📦 FASE {phase_num}\n")
        
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            
        for table_name, df in data.items():
            if table_name.startswith('mapping_') or df is None or df.empty:
                continue
                
            report_lines.append(f"### 📋 Tabel: `{table_name}` ({len(df)} total baris)\n")
            
            # Find old ID mapping helper
            id_map_df = maps.get(table_name)
            
            # Identify columns to check
            cols_to_check = df.columns
            
            table_findings = []
            
            for idx, row in df.iterrows():
                # Determine Old ID
                old_id_val = "N/A"
                if id_map_df is not None:
                    new_id_col = id_map_df.columns[1] # e.g., id_siswa_baru
                    old_id_col = id_map_df.columns[0] # e.g., idsiswa_lama
                    
                    match = id_map_df[id_map_df[new_id_col] == (idx + 1)]
                    if not match.empty:
                        old_id_val = str(match.iloc[0][old_id_col])
                
                if old_id_val == "N/A":
                    id_cols = [c for c in df.columns if c.startswith('id_') or c.endswith('_id') or c == 'id']
                    if id_cols:
                        old_id_val = f"Index {idx} ({id_cols[0]}: {row[id_cols[0]]})"
                    else:
                        old_id_val = f"Row Index {idx}"
                
                # Scan columns
                for col in cols_to_check:
                    val = row[col]
                    is_placeholder = False
                    reason = ""
                    
                    # 1. Null / Empty
                    if pd.isna(val) or val is None or str(val).strip() in ('None', 'NaN', 'NaT', '<NA>', 'nan'):
                        is_placeholder = True
                        reason = "NULL / Kosong"
                    
                    # 2. Placeholders
                    elif str(val).strip() == '-':
                        is_placeholder = True
                        reason = "Placeholder Strip ('-')"
                    elif str(val).strip() == 'NODATAYET':
                        is_placeholder = True
                        reason = "Placeholder 'NODATAYET'"
                    elif str(val).strip() in ('1970-01-01', '1970-01-01 00:00:00'):
                        is_placeholder = True
                        reason = "Tanggal Default Unix ('1970-01-01')"
                    elif str(val).strip() in ('2020-01-01', '2020-01-01 00:00:00'):
                        is_placeholder = True
                        reason = "Tanggal Default System ('2020-01-01')"
                    
                    # 3. Weird Emails
                    elif 'email' in col and is_weird_email(val):
                        is_placeholder = True
                        reason = "⚠️ Email Aneh / Dummy"
                        
                    # 4. Weird Phones
                    elif col in ('nomor_wa', 'wa_siswa', 'wa_ortu', 'wa_administrasi', 'kontak_mitra') and is_weird_phone(val):
                        is_placeholder = True
                        reason = "⚠️ Nomor HP/WA Aneh / Mengandung Huruf"
                        
                    # 5. Weird Names
                    elif any(n_term in col for n_term in ['nama_lengkap', 'nama_ayah', 'nama_ibu', 'nama_wali']) and is_weird_name(val):
                        is_placeholder = True
                        reason = "⚠️ Nama Aneh / Mengandung Angka/Simbol"
                        
                    # 6. HTML Tags in Text Fields
                    elif col not in ('riwayat_kerja', 'riwayat_pendidikan', 'catatan', 'catatan_progres_mitra') and contains_html(val):
                        is_placeholder = True
                        reason = "⚠️ Mengandung Tag HTML"
                        
                    # 7. Gibberish
                    elif is_gibberish(val):
                        is_placeholder = True
                        reason = "⚠️ Teks Uji Coba (Gibberish)"
                        
                    # 8. Numeric range fallbacks
                    elif col == 'ekspektasi_gaji':
                        if val == 0:
                            is_placeholder = True
                            reason = "Ekspektasi Gaji bernilai 0 (Default)"
                        elif 0 < val < 100000:
                            is_placeholder = True
                            reason = "⚠️ Ekspektasi Gaji tidak wajar (Terlalu Kecil)"
                    elif col == 'skor_iq' and val == 0:
                        is_placeholder = True
                        reason = "Skor IQ bernilai 0 (Default)"
                    elif col == 'skor_toefl' and val == 0:
                        is_placeholder = True
                        reason = "Skor TOEFL bernilai 0 (Default)"
                    elif col == 'tahun_lulus' and val == 2000:
                        is_placeholder = True
                        reason = "Tahun Lulus bernilai 2000 (Default)"
                    elif col == 'ipk':
                        if val == 0.0:
                            is_placeholder = True
                            reason = "IPK bernilai 0.0 (Default)"
                        elif val > 4.0:
                            is_placeholder = True
                            reason = "⚠️ IPK tidak wajar (> 4.0)"
                    elif col == 'jumlah_siswa_mitra' and val == 0:
                        is_placeholder = True
                        reason = "Jumlah siswa mitra bernilai 0 (Default)"
                        
                    if is_placeholder:
                        table_findings.append({
                            'id': old_id_val,
                            'col': col,
                            'val': str(val),
                            'reason': reason
                        })
            
            if table_findings:
                report_lines.append(f"| ID Lama (Source ID) | Nama Kolom | Nilai Saat Ini | Alasan / Kategori |")
                report_lines.append(f"|---|---|---|---|")
                limit = 150
                for f_item in table_findings[:limit]:
                    # Escape pipe character in values to avoid breaking markdown tables
                    escaped_val = f_item['val'].replace('|', '\\|').replace('\n', ' ').replace('\r', ' ')
                    report_lines.append(f"| `{f_item['id']}` | `{f_item['col']}` | `{escaped_val}` | {f_item['reason']} |")
                
                if len(table_findings) > limit:
                    report_lines.append(f"| ... | ... | ... | *Dan {len(table_findings) - limit} temuan lainnya pada tabel ini* |")
                report_lines.append(f"\n💡 **Total temuan pembersihan pada tabel `{table_name}`:** {len(table_findings)} kolom bermasalah.\n")
            else:
                report_lines.append(f"✅ Tidak ditemukan data placeholder, kosong, atau anomali pada tabel ini.\n")
            report_lines.append("---\n")
            
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))
    print(f"Laporan audit berhasil ditulis ke: {report_path}")

if __name__ == '__main__':
    audit_phase_data()
