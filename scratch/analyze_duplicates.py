import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from config import get_db_config

def main():
    cfg = get_db_config()
    conn = mysql.connector.connect(**cfg['db_old'])
    cursor = conn.cursor()
    
    # 1. Duplicate emails with IDs
    query_dup = """
        SELECT email, COUNT(*), GROUP_CONCAT(idpelamar) 
        FROM pelamar 
        GROUP BY email 
        HAVING COUNT(*) > 1
        ORDER BY COUNT(*) DESC
    """
    cursor.execute(query_dup)
    dups = cursor.fetchall()
    
    # 2. wfo values > 50 chars
    query_wfo = """
        SELECT idpelamar, email, wfo, LENGTH(wfo) 
        FROM pelamar 
        WHERE LENGTH(wfo) > 50
        ORDER BY LENGTH(wfo) DESC
    """
    cursor.execute(query_wfo)
    wfos = cursor.fetchall()
    
    # Generate markdown report
    output = []
    output.append("# 📋 Data Detail Anomali Pelamar (Database Lama)\n")
    
    output.append("## ✉️ 1. Daftar Email Duplikat")
    output.append("Berikut adalah daftar email yang memiliki lebih dari satu record pelamar di database lama:\n")
    output.append("| No | Email Pelamar | Jumlah | ID Pelamar Lama (`idpelamar`) |")
    output.append("|---|---|---|---|")
    for idx, dup in enumerate(dups):
        output.append(f"| {idx+1} | `{dup[0]}` | {dup[1]} | {dup[2]} |")
        
    output.append("\n## 📝 2. Jawaban WFO yang Terlalu Panjang (> 50 Karakter)")
    output.append("Berikut adalah teks kolom `wfo` di database lama yang melebihi batas 50 karakter target kolom `siap_wfo`:\n")
    output.append("| No | ID Pelamar Lama (`idpelamar`) | Email | Panjang Teks | Isi Teks `wfo` |")
    output.append("|---|---|---|---|---|")
    for idx, wfo in enumerate(wfos):
        # Escape any pipe chars in text to avoid breaking markdown table
        text_escaped = str(wfo[2]).replace('|', '\\|').replace('\n', ' ').strip()
        output.append(f"| {idx+1} | `{wfo[0]}` | `{wfo[1]}` | {wfo[3]} karakter | {text_escaped} |")
        
    conn.close()
    
    report_content = "\n".join(output)
    report_path = "scratch/detail_anomali_pelamar.md"
    with open(report_path, "w", encoding="utf-8") as f_out:
        f_out.write(report_content)
    print(f"Detail report written to {report_path}")

if __name__ == '__main__':
    main()
