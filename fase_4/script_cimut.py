# fase_4/script_cimut.py
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
