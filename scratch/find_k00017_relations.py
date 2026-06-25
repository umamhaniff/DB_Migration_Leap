import sys
import os
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    print("=== FINDING REFERENCES TO COURSE K00017 IN OLD DB ===")
    
    # 1. format_rapor
    cursor_old.execute("SELECT idformat_rapor, title FROM format_rapor WHERE idpendkursus = 'K00017'")
    formats = cursor_old.fetchall()
    format_ids = [f['idformat_rapor'] for f in formats]
    print(f"\n1. Table 'format_rapor' (Formats for K00017): {len(formats)} records")
    for f in formats:
        print(f"   ID: {f['idformat_rapor']} | Title: {f['title']}")
        
    # 2. format_rapor_detil (sub-formats)
    sub_formats = []
    if format_ids:
        format_placeholders = ", ".join(["%s"] * len(format_ids))
        cursor_old.execute(f"SELECT idformat_rd, idformat_rapor, subtitle FROM format_rapor_detil WHERE idformat_rapor IN ({format_placeholders})", tuple(format_ids))
        sub_formats = cursor_old.fetchall()
    sub_format_ids = [sf['idformat_rd'] for sf in sub_formats]
    print(f"\n2. Table 'format_rapor_detil' (Sub-formats referencing K00017 formats): {len(sub_formats)} records")
    for sf in sub_formats[:15]:
        print(f"   Sub-Format ID: {sf['idformat_rd']} | Parent Format ID: {sf['idformat_rapor']} | Sub-Title: {sf['subtitle']}")
    if len(sub_formats) > 15:
        print(f"   ... and {len(sub_formats) - 15} more records")

    # 3. format_rapor_rumus (formulas)
    formulas = []
    if format_ids:
        format_placeholders = ", ".join(["%s"] * len(format_ids))
        cursor_old.execute(f"SELECT idfrr, idformat_rapor, param_operator FROM format_rapor_rumus WHERE idformat_rapor IN ({format_placeholders})", tuple(format_ids))
        formulas = cursor_old.fetchall()
    print(f"\n3. Table 'format_rapor_rumus' (Formulas referencing K00017 formats): {len(formulas)} records")
    for f in formulas:
        print(f"   Formula ID: {f['idfrr']} | Parent Format ID: {f['idformat_rapor']} | Operator: {f['param_operator']}")

    # 4. format_rapor_detil_rumus (sub-formulas)
    sub_formulas = []
    if sub_format_ids:
        sub_format_placeholders = ", ".join(["%s"] * len(sub_format_ids))
        cursor_old.execute(f"SELECT idfrdr, idformat_rd, param_operator, idlevel FROM format_rapor_detil_rumus WHERE idformat_rd IN ({sub_format_placeholders})", tuple(sub_format_ids))
        sub_formulas = cursor_old.fetchall()
    print(f"\n4. Table 'format_rapor_detil_rumus' (Sub-formulas referencing K00017 sub-formats): {len(sub_formulas)} records")
    for sf in sub_formulas[:15]:
        print(f"   Sub-Formula ID: {sf['idfrdr']} | Sub-Format ID: {sf['idformat_rd']} | Operator: {sf['param_operator']} | Level: {sf['idlevel']}")
    if len(sub_formulas) > 15:
        print(f"   ... and {len(sub_formulas) - 15} more records")

    # 5. format_raport_level (level configurations)
    cursor_old.execute("SELECT idformat_rl, idlevel, idformat_rapor FROM format_raport_level WHERE idpendkursus = 'K00017'")
    levels = cursor_old.fetchall()
    print(f"\n5. Table 'format_raport_level' (Level configs for K00017): {len(levels)} records")
    for l in levels[:15]:
        print(f"   Level Config ID: {l['idformat_rl']} | Level: {l['idlevel']} | Format ID: {l['idformat_rapor']}")
    if len(levels) > 15:
        print(f"   ... and {len(levels) - 15} more records")

    conn_old.close()

if __name__ == '__main__':
    main()
