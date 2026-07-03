import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Database config
db_new_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3307)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NEW', 'dataleap_v5_migration'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

# Connect
conn_new = mysql.connector.connect(**db_new_config)
cursor_new = conn_new.cursor(dictionary=True)

# Count new siswa
cursor_new.execute("SELECT COUNT(*) as count FROM siswa")
print("New DB 'siswa' count:", cursor_new.fetchone()['count'])

# Count new siswa_keluar
cursor_new.execute("SELECT COUNT(*) as count FROM siswa_keluar")
print("New DB 'siswa_keluar' count:", cursor_new.fetchone()['count'])

# Check specific names
names_to_check = [
    "AHMAD YUDISTIRA RACHMAN", "ALIF AL MUJADDID", "ALIKA NAYYARA KAUTSAR"
]

print("\n--- Verifikasi Sampel Nama Siswa di DB Baru ---")
for name in names_to_check:
    cursor_new.execute("SELECT id_siswa, nama_lengkap, status_pendaftaran FROM siswa WHERE LOWER(nama_lengkap) = LOWER(%s)", (name,))
    siswa = cursor_new.fetchall()
    if siswa:
        for s in siswa:
            # Check in siswa_keluar
            cursor_new.execute("SELECT * FROM siswa_keluar WHERE id_siswa = %s", (s['id_siswa'],))
            sk = cursor_new.fetchone()
            sk_status = f"Ada (alasan: {sk['alasan_keluar']}, tanggal: {sk['tanggal_keluar']})" if sk else "Tidak Ada"
            print(f"Siswa: {s['nama_lengkap']} | ID Baru: {s['id_siswa']} | Status Pendaftaran: {s['status_pendaftaran']} | Di tabel siswa_keluar: {sk_status}")
    else:
        print(f"Siswa: {name} | Tidak Ditemukan!")

conn_new.close()
