import pickle
import pandas as pd
import re
import html

# Load the transformed data for Fase 4
pkl_path = "fase_4/fase_4_hanif.pkl"
with open(pkl_path, "rb") as f:
    fase4_data = pickle.load(f)

# Email anomaly check
email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

# Let's define standard valid abbreviations in educational/recruitment context
valid_abbreviations = {
    "s1", "s2", "s3", "d1", "d2", "d3", "d4", "sd", "smp", "sma", "smk", 
    "tk", "paud", "pg", "kb", "it", "hr", "hrd", "mt", "wfo", "wfh", "wa", "hp",
    "b2b", "b2c", "cv", "live", "co", "bni", "bsi", "bca", "bri", "pns", "bumn", "spae",
    "ig", "fb", "yt", "li", "ttc", "cca", "cap", "tkl", "cdx", "tkm", "nf", "cl", "be",
    "m1", "m2", "be1", "be2", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "dii"
}

# Common double-syllable nicknames in Indonesia/English to ignore as false positives
common_nicknames = {
    "lala", "sasa", "rara", "gaga", "anna", "jeje", "keke", "nana", "yaya", "jojo", 
    "fefe", "mimi", "iin", "ara", "ana", "rere", "caca", "kiki", "lili", "didi", 
    "vivi", "tata", "cici", "bobi", "gigi", "zaza", "wawa", "ava", "ata", "keke", "el", "jo", "al"
}

def get_clean_text(val_str):
    # Strip HTML tags
    clean = re.sub(r"<[^>]*>", "", val_str)
    # Unescape HTML entities
    clean = html.unescape(clean).strip()
    return clean

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def check_anomaly(val_str, col_name, row_id):
    val_clean = get_clean_text(val_str)
    val_lower = val_clean.lower()
    
    # Skip numeric column checks
    if is_number(val_clean):
        phone_keywords = [r"\bwa\b", r"\bhp\b", r"\btelp\b", r"\bphone\b", "nomor_wa", "no_wa", "nomor_hp", "no_hp", "telepon"]
        is_phone = any(re.search(kw, col_name.lower()) for kw in phone_keywords)
        if is_phone:
            digits_only = re.sub(r"\D", "", val_clean)
            if len(digits_only) < 7 and digits_only != "":
                return {
                    "Kategori": "Nomor Kontak Aneh",
                    "Alasan": f"Nomor kontak terlalu pendek ({len(digits_only)} digit): '{val_str}'"
                }
        if "email" in col_name.lower() and val_clean in ["0", "0.0"]:
            return {
                "Kategori": "Format Email / Testing Email",
                "Alasan": f"Email bernilai numerik default: '{val_str}'"
            }
        return None

    # 1. Check for real gibberish/dummy values (exact match or very short trials)
    gibberish_terms = {
        "asd", "asdasd", "asda", "sad", "testing", "test", "trial", "dummy", 
        "coba", "cobak", "coba ya", "aku coba", "x", "xx", "ya", "ay", 
        "zgdh", "vfg", "fxzg", "zxfxgf", "gaje", "null", "none", "nan", "nodatayet"
    }
    if val_lower in gibberish_terms:
        return {
            "Kategori": "Programmer Trial / Dummy",
            "Alasan": f"Kolom berisi teks uji coba/gibberish pendek: '{val_clean}'"
        }
        
    # Check if string is composed of repeating characters or single letter (excluding abbreviations/names)
    if len(val_clean) > 0 and len(set(val_lower.replace(" ", ""))) <= 2:
        if val_lower not in valid_abbreviations and val_lower not in common_nicknames and val_clean not in ["-", "0", "."]:
            phone_keywords = [r"\bwa\b", r"\bhp\b", r"\btelp\b", r"\bphone\b", "nomor_wa", "no_wa", "nomor_hp", "no_hp", "telepon"]
            is_phone = any(re.search(kw, col_name.lower()) for kw in phone_keywords)
            # Skip checking RT, RW, and school class columns for repeating/short chars
            is_address_detail = col_name.lower() in ["rt", "rw", "tingkat_sekolah", "domisili", "pendidikan_ayah", "pendidikan_ibu"]
            if not is_phone and not is_address_detail:
                return {
                    "Kategori": "Programmer Trial / Dummy (Gibberish)",
                    "Alasan": f"Teks berisi karakter berulang atau acak: '{val_clean}'"
                }
            
    # 2. Check for suspicious emails
    if "email" in col_name.lower():
        if not email_pattern.match(val_str) or "test" in val_lower or "example" in val_lower:
            return {
                "Kategori": "Format Email / Testing Email",
                "Alasan": f"Format email tidak valid atau email uji coba: '{val_str}'"
            }

    # 3. Check for phone number validation
    phone_keywords = [r"\bwa\b", r"\bhp\b", r"\btelp\b", r"\bphone\b", "nomor_wa", "no_wa", "nomor_hp", "no_hp", "telepon"]
    is_phone = any(re.search(kw, col_name.lower()) for kw in phone_keywords)
    if is_phone and val_clean != "":
        digits_only = re.sub(r"\D", "", val_clean)
        if len(digits_only) < 7 and digits_only != "":
            if val_clean not in ["0", "-"]:
                return {
                    "Kategori": "Nomor Kontak Aneh",
                    "Alasan": f"Nomor kontak terlalu pendek ({len(digits_only)} digit): '{val_str}'"
                }
        elif re.search(r"[a-zA-Z]", val_clean):
            return {
                "Kategori": "Nomor Kontak Aneh",
                "Alasan": f"Nomor kontak mengandung karakter huruf: '{val_str}'"
            }

    # 4. Check for placeholder values like "-" on columns that are usually mandatory
    mandatory_cols = ["nama_lengkap", "nama_panggilan", "tempat_lahir", "alamat_ktp", "alamat_domisili", "wa_siswa", "email"]
    if col_name in mandatory_cols:
        if val_clean in ["-", "0", "0.0", "1970-01-01", "2020-01-01"]:
            return {
                "Kategori": "Nilai Default / Placeholder",
                "Alasan": f"Kolom wajib '{col_name}' berisi placeholder/default: '{val_str}'"
            }
            
    return None

report_data = {}

for table_name, df in fase4_data.items():
    if table_name.startswith("mapping_") or "mapping" in table_name:
        continue
        
    print(f"Auditing table: {table_name} ({len(df)} rows)")
    table_anomalies = []
    
    for idx, row in df.iterrows():
        # Get a meaningful row identifier
        row_id = f"Index: {idx}"
        for col_id_candidate in ["id", "id_siswa", "idsiswa", "id_mitra", "id_karyawan"]:
            if col_id_candidate in row and pd.notna(row[col_id_candidate]):
                row_id = f"{col_id_candidate}: {row[col_id_candidate]}"
                break
                
        for col in df.columns:
            val = row[col]
            if pd.isna(val):
                continue
                
            val_str = str(val).strip()
            if val_str == "":
                continue
                
            anomaly = check_anomaly(val_str, col, row_id)
            if anomaly:
                table_anomalies.append({
                    "ID": row_id,
                    "Kolom": col,
                    "Nilai": val_str,
                    "Kategori": anomaly["Kategori"],
                    "Alasan": anomaly["Alasan"]
                })
                    
    if table_anomalies:
        report_data[table_name] = table_anomalies

# Write Markdown report
with open("extract/fase4_anomalies_clean.md", "w", encoding="utf-8") as out:
    out.write("# 🔍 Laporan Audit Anomali & Data Cleaning Fase 4 (Refined)\n\n")
    out.write("Laporan ini berisi hasil pemindaian langsung pada data Fase 4 yang dihasilkan oleh `script_hanif.ipynb`.\n")
    out.write("Laporan ini **mengecualikan** temuan yang murni berupa tag HTML (karena tag HTML digunakan untuk kebutuhan pemanggilan di web),\n")
    out.write("serta **mengecualikan** kata/abreviasi valid (seperti 'S1', 'SMA', 'Tahap Test', dll.) dan nilai numerik murni.\n")
    out.write("Laporan ini berfokus pada data aneh, uji coba programmer (trial/dummy/gibberish), format email/HP salah, serta placeholder pada kolom wajib.\n\n")
    
    if not report_data:
        out.write("### ✅ Tidak ditemukan anomali data di luar tag HTML yang valid!\n")
    else:
        for t_name, anomalies in report_data.items():
            out.write(f"## 📋 Tabel: `{t_name}` ({len(anomalies)} temuan)\n\n")
            out.write("| ID Baris | Kolom | Nilai Saat Ini | Kategori | Detail Alasan |\n")
            out.write("|---|---|---|---|---|\n")
            for item in anomalies:
                val_escaped = item["Nilai"].replace("|", "\\|").replace("\n", "<br>")
                out.write(f"| `{item['ID']}` | `{item['Kolom']}` | `{val_escaped}` | {item['Kategori']} | {item['Alasan']} |\n")
            out.write("\n---\n\n")

print("Markdown report written to extract/fase4_anomalies_clean.md")
with open("scratch/fase4_anomalies_refined.pkl", "wb") as f:
    pickle.dump(report_data, f)
