import pickle
import pandas as pd
import re
import html

# Load the transformed data for Fase 5
pkl_path = "fase_5/fase_5_hanif.pkl"
with open(pkl_path, "rb") as f:
    fase5_data = pickle.load(f)

# Let's define standard valid abbreviations/terms in educational context
valid_abbreviations = {
    "s1", "s2", "s3", "d1", "d2", "d3", "d4", "sd", "smp", "sma", "smk", 
    "tk", "paud", "pg", "kb", "it", "hr", "hrd", "mt", "wfo", "wfh", "wa", "hp",
    "b2b", "b2c", "cv", "live", "co", "bni", "bsi", "bca", "bri", "pns", "bumn",
    "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi"
}

# Educational phrases that contain 'test' or 'coba' but are completely valid
valid_educational_phrases = [
    r"placement\s+test", r"pre\s*-?\s*test", r"post\s*-?\s*test", 
    r"unit\s+test", r"test\s+unit", r"progress\s+test", r"final\s+test",
    r"speaking\s+test", r"listening\s+test", r"reading\s+test", r"writing\s+test",
    r"test\s+speaking", r"test\s+listening", r"test\s+reading", r"test\s+writing",
    r"grammar\s+test", r"vocabulary\s+test", r"test\s+report",
    r"uji\s+coba", r"percobaan", r"coba\s+lagi", r"dicoba"
]

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
        return None

    # Check for valid educational phrases containing 'test' or 'coba'
    for phrase in valid_educational_phrases:
        if re.search(phrase, val_lower):
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
        
    # Check if string is composed of repeating characters or single letter (excluding abbreviations)
    if len(val_clean) > 0 and len(set(val_lower.replace(" ", ""))) <= 2:
        if val_lower not in valid_abbreviations and val_clean not in ["-", "0", "."]:
            # Skip checking formulas and report card final grades ('A', 'B', etc.) for short/repeating characters
            is_formula_or_grade = col_name.lower() in ["logika_operator", "final_result", "sub_judul_rapor", "judul_rapor"]
            if not is_formula_or_grade:
                return {
                    "Kategori": "Programmer Trial / Dummy (Gibberish)",
                    "Alasan": f"Teks berisi karakter berulang atau acak: '{val_clean}'"
                }

    # 2. Check for dummy file paths
    if "path" in col_name.lower() or "file" in col_name.lower():
        if any(term in val_lower for term in ["test", "dummy", "coba", "asd", "trial"]):
            return {
                "Kategori": "Path Berkas Dummy / Percobaan",
                "Alasan": f"Path file mengindikasikan file uji coba/dummy: '{val_str}'"
            }
            
    return None

report_data = {}

for table_name, df in fase5_data.items():
    if table_name.startswith("mapping_") or "mapping" in table_name:
        continue
        
    print(f"Auditing table: {table_name} ({len(df)} rows)")
    table_anomalies = []
    
    for idx, row in df.iterrows():
        # Get a meaningful row identifier
        row_id = f"Index: {idx}"
        for col_id_candidate in ["id", "id_rapor_siswa", "id_rapor_siswa_file", "id_rapor_lacak", "id_rapor_format"]:
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
with open("extract/fase5_anomalies_clean.md", "w", encoding="utf-8") as out:
    out.write("# 🔍 Laporan Audit Anomali & Data Cleaning Fase 5 (Refined)\n\n")
    out.write("Laporan ini berisi hasil pemindaian langsung pada data Fase 5 yang dihasilkan oleh `script_hanif.ipynb`.\n")
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

print("Markdown report written to extract/fase5_anomalies_clean.md")
with open("scratch/fase5_anomalies_refined.pkl", "wb") as f:
    pickle.dump(report_data, f)
