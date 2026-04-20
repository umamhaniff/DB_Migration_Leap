# digunakan untuk membuat file migrasi dengan template yang sudah disiapkan 

import os

template = """# {fase}/{nama}.py
import mysql.connector
from config import get_db_config

def migrate():
    config = get_db_config()
    db = mysql.connector.connect(**config)
    cursor = db.cursor(dictionary=True)
    
    print("Memulai migrasi tabel bagian [NAMA TABEL]...")
    
    # 1. Ambil data dari DB Lama (Ganti dengan kueri sesuai)
    # 2. Transformasi data jika perlu
    # 3. Insert ke DB Baru
    
    print("Migrasi selesai!")
    db.close()

if __name__ == "__main__":
    migrate()
"""

# Daftar fase dan orang-orangnya
fases = ['fase_1', 'fase_2', 'fase_3', 'fase_4', 'fase_5']
people = ['script_cimut', 'script_afrida', 'script_hanif']

for fase in fases:
    # Buat direktori fase jika belum ada
    if not os.path.exists(fase):
        os.makedirs(fase)
        print(f"Direktori dibuat: {fase}")
    
    for person in people:
        file_path = os.path.join(fase, f"{person}.py")
        # Buat/tulis file (tidak perlu cek apakah ada)
        with open(file_path, "w") as f:
            # Mengisi template ke dalam file, mengganti {fase} dan {nama} secara dinamis
            f.write(template.format(fase=fase, nama=person))
        print(f"Berhasil mengisi template ke: {file_path}")