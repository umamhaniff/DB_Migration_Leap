import mysql.connector
import pandas as pd
from config import get_db_config

try:
    config = get_db_config()
    # Connect to the old database
    db_old = mysql.connector.connect(**config['db_old'])
    cursor_old = db_old.cursor(dictionary=True)

    # 1. Inspect pelamar.idpengajuan
    cursor_old.execute("SELECT idpelamar, idpengajuan, nama, email FROM pelamar LIMIT 5")
    pelamar_samples = cursor_old.fetchall()
    print("=== SAMPLE FROM db_old.pelamar ===")
    for row in pelamar_samples:
        print(row)

    # 2. Inspect pengajuan.idpengajuan
    cursor_old.execute("SELECT idpengajuan, keterangan, jumlah FROM pengajuan LIMIT 5")
    pengajuan_samples = cursor_old.fetchall()
    print("\n=== SAMPLE FROM db_old.pengajuan ===")
    for row in pengajuan_samples:
        print(row)

    cursor_old.close()
    db_old.close()
except Exception as e:
    print("Error:", e)
