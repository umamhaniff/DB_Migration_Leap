import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

# Check nulls in old DB table
print("--- Check old DB pelamar table nulls ---")
cursor.execute("SELECT COUNT(*) as count FROM pelamar WHERE nama IS NULL OR nama = ''")
print("Null/empty nama in old DB:", cursor.fetchone()['count'])

cursor.execute("SELECT COUNT(*) as count FROM pelamar WHERE panggilan IS NULL OR panggilan = ''")
print("Null/empty panggilan in old DB:", cursor.fetchone()['count'])

cursor.execute("SELECT COUNT(*) as count FROM pelamar WHERE jk IS NULL OR jk = ''")
print("Null/empty jk in old DB:", cursor.fetchone()['count'])

cursor.close()
conn_old.close()
