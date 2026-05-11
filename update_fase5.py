import json

file_path = 'fase_5/script_hanif.ipynb'
with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update Imports
nb['cells'][1]['source'] = [
    "import sys\n",
    "import os\n",
    "import mysql.connector\n",
    "import pandas as pd\n",
    "import re\n",
    "from datetime import datetime\n",
    "import pickle\n",
    "import json\n",
    "sys.path.append(os.path.abspath('..'))\n",
    "from config import get_db_config\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
]

# 2. Update Transformation Cell (index 4)
transformation_source = [
    "transformed_dfs = {}\n",
    "\n",
    "# --- TRANSFORMATION ---\n",
    "\n",
    "# 1. format_rapor -> rapor_format\n",
    "if 'format_rapor' in raw_data:\n",
    "    df = pd.DataFrame(raw_data['format_rapor'])\n",
    "    mapping = {\n",
    "        'idformat_rapor': 'id_rapor_format',\n",
    "        'idpendkursus': 'id_kursus', 'title': 'judul_rapor'\n",
    "    }\n",
    "    transformed_dfs['rapor_format'] = df.rename(columns=mapping)[list(mapping.values())]\n",
    "\n",
    "# 2. format_rapor_detil -> rapor_format_sub\n",
    "if 'format_rapor_detil' in raw_data:\n",
    "    df = pd.DataFrame(raw_data['format_rapor_detil'])\n",
    "    mapping = {\n",
    "        'idformat_rd': 'id_rapor_format_sub',\n",
    "        'idformat_rapor': 'id_rapor_format', 'subtitle': 'sub_judul_rapor'\n",
    "    }\n",
    "    transformed_dfs['rapor_format_sub'] = df.rename(columns=mapping)[list(mapping.values())]\n",
    "\n",
    "# 3. format_rapor_rumus -> rapor_format_formula\n",
    "if 'format_rapor_rumus' in raw_data:\n",
    "    df = pd.DataFrame(raw_data['format_rapor_rumus'])\n",
    "    mapping = {\n",
    "        'idfrr': 'id_rapor_format_formula',\n",
    "        'idformat_rapor': 'id_rapor_format', 'param_operator': 'logika_operator'\n",
    "    }\n",
    "    transformed_dfs['rapor_format_formula'] = df.rename(columns=mapping)[list(mapping.values())]\n",
    "\n",
    "# 4. format_rapor_detil_rumus -> rapor_format_formula_sub\n",
    "if 'format_rapor_detil_rumus' in raw_data:\n",
    "    df = pd.DataFrame(raw_data['format_rapor_detil_rumus'])\n",
    "    mapping = {\n",
    "        'idfrdr': 'id_rapor_format_formula_sub',\n",
    "        'idformat_rd': 'id_rapor_format_sub', 'param_operator': 'logika_operator',\n",
    "        'idlevel': 'id_level'\n",
    "    }\n",
    "    transformed_dfs['rapor_format_formula_sub'] = df.rename(columns=mapping)[list(mapping.values())]\n",
    "\n",
    "# 5. format_raport_level -> rapor_level_config\n",
    "if 'format_raport_level' in raw_data:\n",
    "    df = pd.DataFrame(raw_data['format_raport_level'])\n",
    "    mapping = {\n",
    "        'idformat_rl': 'id_rapor_level_config', 'idlevel': 'id_level',\n",
    "        'idpendkursus': 'id_kursus', 'idformat_rapor': 'id_rapor_format'\n",
    "    }\n",
    "    transformed_dfs['rapor_level_config'] = df.rename(columns=mapping)[list(mapping.values())]\n",
    "\n",
    "# 6. rapor_sub_level (Tabel Baru)\n",
    "transformed_dfs['rapor_sub_level'] = pd.DataFrame(columns=['id_rapor_sub_level', 'id_rapor_format_sub', 'id_level'])\n",
    "\n",
    "# 7. rapor -> rapor_siswa\n",
    "if 'rapor' in raw_data:\n",
    "    df = pd.DataFrame(raw_data['rapor'])\n",
    "    mapping = {\n",
    "        'idrapor': 'id_rapor_siswa', 'idjadwal': 'id_jadwal', 'idsiswa': 'id_siswa',\n",
    "        'tanggal': 'tanggal_input', 'idp_nilai': 'id_parameter_nilai', 'nilai': 'final_result'\n",
    "    }\n",
    "    # Note: tanggal direct mapping\n",
    "    transformed_dfs['rapor_siswa'] = df.rename(columns=mapping)[list(mapping.values())]\n",
    "\n",
    "# 8. file_rapor_siswa -> rapor_siswa_file\n",
    "if 'file_rapor_siswa' in raw_data:\n",
    "    df = pd.DataFrame(raw_data['file_rapor_siswa'])\n",
    "    # Logic: cari id_rapor_siswa di rapor_siswa (db_new)\n",
    "    # Jika idsiswa di file_rapor_siswa adalah idrapor di rapor (old), maka direct mapping.\n",
    "    mapping = {\n",
    "        'idfile': 'id_rapor_siswa_file', 'idsiswa': 'id_rapor_siswa', 'path': 'file_rapor_path'\n",
    "    }\n",
    "    transformed_dfs['rapor_siswa_file'] = df.rename(columns=mapping)[list(mapping.values())]\n",
    "\n",
    "# 9. history_rapor -> rapor_lacak\n",
    "if 'history_rapor' in raw_data:\n",
    "    df = pd.DataFrame(raw_data['history_rapor'])\n",
    "    # Enum normalization\n",
    "    df['status'] = df['status'].replace({'Terkirim': 'Terkirim', 'Gagal': 'Gagal'})\n",
    "    \n",
    "    mapping = {\n",
    "        'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa',\n",
    "        'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'\n",
    "    }\n",
    "    df_final = df.rename(columns=mapping)\n",
    "    # id_rapor_siswa_file: cari di rapor_siswa_file\n",
    "    df_final['id_rapor_siswa_file'] = None\n",
    "    transformed_dfs['rapor_lacak'] = df_final[list(mapping.values()) + ['id_rapor_siswa_file']]\n",
    "\n",
    "print(f\"✓ Transformasi {len(transformed_dfs)} tabel Fase 5 selesai.\")"
]
nb['cells'][7]['source'] = transformation_source

# 3. Add Verification Cells
verif_header_idx = -1
export_header_idx = -1

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and '## 3.1 Verifikasi Hasil Transformasi' in ''.join(cell['source']):
        verif_header_idx = i
    if cell['cell_type'] == 'markdown' and '## 4. Export ke Pickle' in ''.join(cell['source']):
        export_header_idx = i

if verif_header_idx != -1 and export_header_idx != -1:
    summary_counts_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# 3.1.1 Ringkasan Jumlah Baris\n",
            "print(\"\ud83d\udcca RINGKASAN MIGRASI (RECORDS COUNT)\")\n",
            "print(\"=\"*70)\n",
            "summary_list = []\n",
            "for old_t, new_t in hanif_tables_map:\n",
            "    old_c = len(raw_data.get(old_t, []))\n",
            "    new_c = len(transformed_dfs.get(new_t, []))\n",
            "    summary_list.append({\n",
            "        'Tabel Lama': old_t,\n",
            "        'Tabel Baru': new_t,\n",
            "        'Old Recs': old_c,\n",
            "        'New Recs': new_c,\n",
            "        'Diff': new_c - old_c,\n",
            "        'Status': \"\u2705 OK\" if old_c == new_c else \"\u26a0\ufe0f Cek\"\n",
            "    })\n",
            "display(pd.DataFrame(summary_list))\n",
            "\n",
            "total_old_all = sum(len(records) for records in raw_data.values())\n",
            "total_new_all = sum(len(df) for df in transformed_dfs.values())\n",
            "print(f\"\\n\ud83d\udce2 TOTAL REKAPITULASI: {total_old_all} (Old) \u2794 {total_new_all} (New)\")\n",
            "if total_old_all == total_new_all: print(\"\u2705 SEMUA DATA TERANGKUT\")\n",
            "else: print(f\"\u26a0\ufe0f ADA SELISIH: {total_new_all - total_old_all} baris\")"
        ]
    }

    specific_checks_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# 3.1.2 Output Pengecekan Kolom Spesifik (KETERANGAN mapping.md)\n",
            "print(\"\\n\ud83d\udd0d PENGECEKAN TRANSFORMASI SPESIFIK (KETERANGAN mapping.md)\")\n",
            "print(\"=\"*70)\n",
            "\n",
            "# 1. Pengecekan Tanggal Input (Rapor Siswa)\n",
            "if 'rapor_siswa' in transformed_dfs:\n",
            "    print(\"\\n[RAPOR_SISWA] Pengecekan tanggal_input (Direct Mapping):\")\n",
            "    display(transformed_dfs['rapor_siswa'][['id_rapor_siswa', 'tanggal_input']].head(5))\n",
            "\n",
            "# 2. Pengecekan Rapor Lacak (Enum Status)\n",
            "if 'rapor_lacak' in transformed_dfs:\n",
            "    print(\"\\n[RAPOR_LACAK] Pengecekan Normalisasi Status Pengiriman:\")\n",
            "    display(transformed_dfs['rapor_lacak']['status_pengiriman'].value_counts())\n",
            "\n",
            "# 3. Pengecekan Rapor Siswa File\n",
            "if 'rapor_siswa_file' in transformed_dfs:\n",
            "    print(\"\\n[RAPOR_SISWA_FILE] Pengecekan path file:\")\n",
            "    display(transformed_dfs['rapor_siswa_file'][['id_rapor_siswa', 'file_rapor_path']].head(5))"
        ]
    }

    detailed_checks_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# 3.1.3 Detail Perbandingan Kolom & Tipe Data (Side-by-Side)\n",
            "print(\"\\n\ud83d\udd0d PERBANDINGAN TIPE DATA SIDE-BY-SIDE\")\n",
            "for old_t, new_t in hanif_tables_map:\n",
            "    print(f\"\\n{'='*15} {old_t.upper()} \u2794 {new_t.upper()} {'='*15}\")\n",
            "    \n",
            "    df_old = pd.DataFrame(raw_data.get(old_t, []))\n",
            "    df_new = transformed_dfs.get(new_t, pd.DataFrame())\n",
            "    \n",
            "    if not df_new.empty or not df_old.empty:\n",
            "        comparison = []\n",
            "        table_mapping = {}\n",
            "        if old_t == 'format_rapor': table_mapping = {'idformat_rapor': 'id_rapor_format', 'idpendkursus': 'id_kursus', 'title': 'judul_rapor'}\n",
            "        elif old_t == 'format_rapor_detil': table_mapping = {'idformat_rd': 'id_rapor_format_sub', 'idformat_rapor': 'id_rapor_format', 'subtitle': 'sub_judul_rapor'}\n",
            "        elif old_t == 'format_rapor_rumus': table_mapping = {'idfrr': 'id_rapor_format_formula', 'idformat_rapor': 'id_rapor_format', 'param_operator': 'logika_operator'}\n",
            "        elif old_t == 'format_rapor_detil_rumus': table_mapping = {'idfrdr': 'id_rapor_format_formula_sub', 'idformat_rd': 'id_rapor_format_sub', 'param_operator': 'logika_operator', 'idlevel': 'id_level'}\n",
            "        elif old_t == 'format_raport_level': table_mapping = {'idformat_rl': 'id_rapor_level_config', 'idlevel': 'id_level', 'idpendkursus': 'id_kursus', 'idformat_rapor': 'id_rapor_format'}\n",
            "        elif old_t == 'rapor': table_mapping = {'idrapor': 'id_rapor_siswa', 'idjadwal': 'id_jadwal', 'idsiswa': 'id_siswa', 'tanggal': 'tanggal_input', 'idp_nilai': 'id_parameter_nilai', 'nilai': 'final_result'}\n",
            "        elif old_t == 'file_rapor_siswa': table_mapping = {'idfile': 'id_rapor_siswa_file', 'idsiswa': 'id_rapor_siswa', 'path': 'file_rapor_path'}\n",
            "        elif old_t == 'history_rapor': table_mapping = {'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa', 'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'}\n",
            "\n",
            "        for old_col, new_col in table_mapping.items():\n",
            "            comparison.append({\n",
            "                'Old Column': old_col,\n",
            "                'Old Type': str(df_old[old_col].dtype) if not df_old.empty and old_col in df_old.columns else \"N/A\",\n",
            "                '\u2794': '\u2794',\n",
            "                'New Column': new_col,\n",
            "                'New Type': str(df_new[new_col].dtype) if not df_new.empty and new_col in df_new.columns else \"N/A\"\n",
            "            })\n",
            "        \n",
            "        # Cek kolom baru\n",
            "        if not df_new.empty:\n",
            "            for col in df_new.columns:\n",
            "                if col not in table_mapping.values():\n",
            "                    comparison.append({\n",
            "                        'Old Column': '(KOLOM BARU / CUSTOM)',\n",
            "                        'Old Type': '-',\n",
            "                        '\u2794': '\u2794',\n",
            "                        'New Column': col,\n",
            "                        'New Type': str(df_new[col].dtype)\n",
            "                    })\n",
            "        \n",
            "        display(pd.DataFrame(comparison))\n",
            "        if not df_new.empty:\n",
            "            print(f\"\\n--- SAMPLE DATA NEW (2 Baris) ---\")\n",
            "            display(df_new.head(2))\n",
            "    else:\n",
            "        print(f\"\u26a0\ufe0f Tabel {new_t} kosong.\")"
        ]
    }

    new_cells = nb['cells'][:verif_header_idx + 1]
    new_cells.append(summary_counts_cell)
    new_cells.append(specific_checks_cell)
    new_cells.append(detailed_checks_cell)
    new_cells.extend(nb['cells'][export_header_idx:])
    
    nb['cells'] = new_cells
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Notebook Fase 5 updated successfully.")
else:
    print("Required headers not found in Fase 5 notebook.")
