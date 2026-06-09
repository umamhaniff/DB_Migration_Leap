import mysql.connector
from config import get_db_config

try:
    config = get_db_config()
    db_new = mysql.connector.connect(**config['db_new'])
    cursor = db_new.cursor()
    
    # 1. Inspect pelamar columns
    cursor.execute("DESCRIBE pelamar")
    print("=== Schema of db_new.pelamar ===")
    for row in cursor.fetchall():
        if row[0] in ['id_pelamar', 'id_pengajuan']:
            print(row)
            
    # 2. Inspect siswa columns
    cursor.execute("DESCRIBE siswa")
    print("\n=== Schema of db_new.siswa ===")
    for row in cursor.fetchall():
        if row[0] in ['id_siswa', 'id_provinsi', 'id_kabupaten', 'id_kecamatan', 'id_kelurahan', 'id_mitra']:
            print(row)

    # 3. Inspect mitra_progres
    cursor.execute("DESCRIBE mitra_progres")
    print("\n=== Schema of db_new.mitra_progres ===")
    for row in cursor.fetchall():
        if row[0] in ['id_mitra', 'id_progres_mitra']:
            print(row)
            
    cursor.close()
    db_new.close()
except Exception as e:
    print("Error:", e)
