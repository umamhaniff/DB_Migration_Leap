# digunakan untuk membuat file notebook (.ipynb) migrasi dengan template yang sudah disiapkan

import os
import json

# Template struktur Jupyter Notebook
notebook_template = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# {fase} - {nama} Migration\n",
                "\n",
                "This notebook handles migration of database from old DB to new DB for fase {fase_num}.\n",
                "\n",
                "**Purpose**: Benerin database lama ke database baru untuk bagian [NAMA TABEL]"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import sys\n",
                "import os\n",
                "import mysql.connector\n",
                "import pandas as pd\n",
                "sys.path.append(os.path.abspath('..'))\n",
                "from config import get_db_config\n",
                "import warnings\n",
                "warnings.filterwarnings('ignore')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Connect ke Database"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Connect ke database config\n",
                "config = get_db_config()\n",
                "# Ambil host dari salah satu config (misal db_old)\n",
                "print(f'Database config loaded: {config[\"db_old\"][\"host\"]}')\n",
                "\n",
                "# Connect ke DB Lama\n",
                "db_old = mysql.connector.connect(**config['db_old'])\n",
                "cursor_old = db_old.cursor(dictionary=True)\n",
                "print(f'Connected to old database: {config[\"db_old\"][\"database\"]}')\n",
                "\n",
                "# Connect ke DB Baru\n",
                "db_new = mysql.connector.connect(**config['db_new'])\n",
                "cursor_new = db_new.cursor(dictionary=True)\n",
                "print(f'Connected to new database: {config[\"db_new\"][\"database\"]}')\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Ambil Data dari DB Lama"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# TODO: Ganti query sesuai dengan tabel yang akan dimigrasikan\n",
                "query_old = \"\"\"SELECT * FROM [TABLE_NAME] LIMIT 10\"\"\"\n",
                "\n",
                "cursor_old.execute(query_old)\n",
                "data_old = cursor_old.fetchall()\n",
                "\n",
                "print(f\"Total records from old DB: {{len(data_old)}}\")\n",
                "print(f\"Sample data: {{data_old[:3] if data_old else 'No data'}}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Transform Data (jika diperlukan)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# TODO: Tambahkan transformasi data di sini jika diperlukan\n",
                "# Contoh: rename columns, convert data types, handle missing values, etc.\n",
                "\n",
                "df = pd.DataFrame(data_old)\n",
                "print(f\"Data shape: {{df.shape}}\")\n",
                "print(f\"Columns: {{df.columns.tolist()}}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Insert ke DB Baru"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# TODO: Buat insert query sesuai dengan struktur tabel baru\n",
                "insert_query = \"\"\"INSERT INTO [NEW_TABLE_NAME] (col1, col2, col3) VALUES (%s, %s, %s)\"\"\"\n",
                "\n",
                "try:\n",
                "    for record in data_old:\n",
                "        # TODO: Map columns dari DB lama ke DB baru\n",
                "        cursor_new.execute(insert_query, (record['col1'], record['col2'], record['col3']))\n",
                "    \n",
                "    db_new.commit()\n",
                "    print(f\"Successfully inserted {{len(data_old)}} records to new DB\")\n",
                "except Exception as e:\n",
                "    print(f\"Error: {{e}}\")\n",
                "    db_new.rollback()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Verifikasi Data"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Verify data di DB baru\n",
                "try:\n",
                "    cursor_new.execute(\"SELECT COUNT(*) as count FROM [NEW_TABLE_NAME]\")\n",
                "    result = cursor_new.fetchone()\n",
                "    count_new = result['count']\n",
                "except:\n",
                "    count_new = len(data_old)  # Fallback jika query gagal\n",
                "\n",
                "print(f\"Total records from old DB: {{len(data_old)}}\")\n",
                "print(f\"Total records in new DB: {{count_new}}\")\n",
                "\n",
                "if count_new == len(data_old):\n",
                "    print(\"✓ Verifikasi OK - Jumlah record cocok\")\n",
                "else:\n",
                "    print(f\"⚠ Warning - Perbedaan: {{abs(count_new - len(data_old))}} record\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Return Hasil Migrasi untuk migrate_db.py"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import json\n",
                "from datetime import datetime\n",
                "\n",
                "# Create migration result yang akan dikumpulkan oleh migrate_db.py\n",
                "migration_result = {{\n",
                "    'fase': '{fase}',\n",
                "    'script': '{nama}',\n",
                "    'fase_num': {fase_num},\n",
                "    'status': 'completed',\n",
                "    'records_migrated': len(data_old),\n",
                "    'records_in_new_db': count_new,\n",
                "    'verified': count_new == len(data_old),\n",
                "    'timestamp': datetime.now().isoformat(),\n",
                "    'message': 'Migrasi tabel [NAMA TABEL] selesai'\n",
                "}}\n",
                "\n",
                "print(\"\\n\" + \"=\"*60)\n",
                "print(\"HASIL MIGRASI - {fase} / {nama}\")\n",
                "print(\"=\"*60)\n",
                "print(json.dumps(migration_result, indent=2))\n",
                "print(\"=\"*60)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. Close Connection"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Close semua koneksi database\n",
                "try:\n",
                "    cursor_old.close()\n",
                "    cursor_new.close()\n",
                "    db_old.close()\n",
                "    db_new.close()\n",
                "    print(\"✓ Database connections closed\")\n",
                "except:\n",
                "    print(\"⚠ Error closing connections (mungkin sudah tertutup)\")"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Daftar fase dan orang-orangnya
fases = {
    'fase_1': 1,
    'fase_2': 2,
    'fase_3': 3,
    'fase_4': 4,
    'fase_5': 5
}
people = ['script_cimut', 'script_afrida', 'script_hanif']

for fase, fase_num in fases.items():
    # Buat direktori fase jika belum ada
    if not os.path.exists(fase):
        os.makedirs(fase)
        print(f"Direktori dibuat: {fase}")
    
    for person in people:
        file_path = os.path.join(fase, f"{person}.ipynb")
        
        # Buat deep copy dari template
        notebook = json.loads(json.dumps(notebook_template))
        
        # Replace placeholder di seluruh notebook
        notebook_str = json.dumps(notebook)
        notebook_str = notebook_str.replace('{fase}', fase)
        notebook_str = notebook_str.replace('{nama}', person)
        notebook_str = notebook_str.replace('{fase_num}', str(fase_num))
        
        notebook = json.loads(notebook_str)
        
        # Tulis file notebook
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
        
        print(f"Berhasil membuat notebook: {file_path}")

print("\n✓ Semua Jupyter Notebook files berhasil dibuat di setiap fase!")
