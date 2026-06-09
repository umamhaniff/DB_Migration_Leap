"""
fix_urutan_int64.py
One-shot: tambah baris .astype('Int64') ke kolom urutan di
rapor_format (block #1) dan rapor_format_sub (block #2)
di fase_5/script_hanif.ipynb yang sudah di-patch sebelumnya.
"""
import json

path = "fase_5/script_hanif.ipynb"
nb = json.load(open(path, "r", encoding="utf-8"))

# --- target baris lama -> baris baru ---
REPLACEMENTS = [
    # Block #1 rapor_format: insert Int64 setelah merge
    (
        "    df_rf = df_rf.merge(df_urutan_rf, on='judul_rapor', how='left')\n"
        "    transformed_dfs['rapor_format'] = df_rf\n",

        "    df_rf = df_rf.merge(df_urutan_rf, on='judul_rapor', how='left')\n"
        "    df_rf['urutan'] = df_rf['urutan'].astype('Int64')  # cegah float karena NaN\n"
        "    transformed_dfs['rapor_format'] = df_rf\n",
    ),
    # Block #2 rapor_format_sub: insert Int64 setelah merge
    (
        "    df_rfs = df_rfs.merge(df_urutan_rfs, on=['_rf_key', 'sub_judul_rapor'], how='left').drop(columns=['_rf_key'])\n"
        "    transformed_dfs['rapor_format_sub'] = df_rfs\n",

        "    df_rfs = df_rfs.merge(df_urutan_rfs, on=['_rf_key', 'sub_judul_rapor'], how='left').drop(columns=['_rf_key'])\n"
        "    df_rfs['urutan'] = df_rfs['urutan'].astype('Int64')  # cegah float karena NaN\n"
        "    transformed_dfs['rapor_format_sub'] = df_rfs\n",
    ),
]

fixed_count = 0
for cell in nb["cells"]:
    if cell["cell_type"] != "code":
        continue
    source = "".join(cell["source"])
    changed = False
    for old, new in REPLACEMENTS:
        if old in source:
            source = source.replace(old, new)
            fixed_count += 1
            changed = True
    if changed:
        cell["source"] = [line + "\n" for line in source.split("\n")]
        if cell["source"] and cell["source"][-1] == "\n":
            cell["source"].pop()

if fixed_count > 0:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print(f"OK: {fixed_count} replacement(s) applied. urutan kolom sekarang pakai Int64.")
else:
    print("Info: Tidak ada yang diubah — sudah dipatch atau baris target tidak ditemukan.")
