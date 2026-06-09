"""
fix_rapor_sub_join.py
Fix join block #2 rapor_format_sub — ganti dari numeric conversion
ke direct string join karena id_rapor_format di old DB juga format 'F00001'.
"""
import json

path = "fase_5/script_hanif.ipynb"
nb = json.load(open(path, "r", encoding="utf-8"))

old_block = (
    "    df_rfs = df.rename(columns=mapping)[list(mapping.values())]\n"
    "    # Merge kolom urutan dari rapor_format_sub_import.csv (sudah diurutkan manual)\n"
    "    # id_rapor_format di import CSV: format 'F00001' -> ambil digit -> int untuk join\n"
    "    df_urutan_rfs = pd.read_csv('rapor_format_sub_import.csv')\n"
    "    df_urutan_rfs['_rf_key'] = df_urutan_rfs['id_rapor_format'].str.extract(r'(\\d+)', expand=False).astype(int)\n"
    "    df_urutan_rfs = df_urutan_rfs[['_rf_key', 'sub_judul_rapor', 'urutan']]\n"
    "    df_rfs = df_rfs.copy()\n"
    "    df_rfs['_rf_key'] = pd.to_numeric(df_rfs['id_rapor_format'], errors='coerce').astype('Int64')\n"
    "    df_urutan_rfs['_rf_key'] = df_urutan_rfs['_rf_key'].astype('Int64')\n"
    "    df_rfs = df_rfs.merge(df_urutan_rfs, on=['_rf_key', 'sub_judul_rapor'], how='left').drop(columns=['_rf_key'])\n"
    "    df_rfs['urutan'] = df_rfs['urutan'].astype('Int64')  # cegah float karena NaN\n"
    "    transformed_dfs['rapor_format_sub'] = df_rfs\n"
)

new_block = (
    "    df_rfs = df.rename(columns=mapping)[list(mapping.values())]\n"
    "    # Merge kolom urutan dari rapor_format_sub_import.csv (sudah diurutkan manual)\n"
    "    # id_rapor_format di KEDUA sisi pakai format string yg sama (misal 'F00001') -> join langsung\n"
    "    df_urutan_rfs = pd.read_csv('rapor_format_sub_import.csv')[['id_rapor_format', 'sub_judul_rapor', 'urutan']]\n"
    "    df_rfs = df_rfs.merge(df_urutan_rfs, on=['id_rapor_format', 'sub_judul_rapor'], how='left')\n"
    "    df_rfs['urutan'] = df_rfs['urutan'].astype('Int64')  # cegah float karena NaN\n"
    "    transformed_dfs['rapor_format_sub'] = df_rfs\n"
)

fixed = False
for cell in nb["cells"]:
    if cell["cell_type"] != "code":
        continue
    source = "".join(cell["source"])
    if old_block in source:
        source = source.replace(old_block, new_block)
        cell["source"] = [line + "\n" for line in source.split("\n")]
        if cell["source"] and cell["source"][-1] == "\n":
            cell["source"].pop()
        fixed = True
        break

if fixed:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print("OK: block #2 rapor_format_sub join disederhanakan ke direct string match.")
else:
    print("Info: old_block tidak ditemukan — mungkin sudah dipatch atau state notebook berbeda.")
    print("Cek manual: cari baris '_rf_key' di transform cell.")
