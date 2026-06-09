import sys
import os
import pandas as pd
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor_old = conn_old.cursor(dictionary=True)

cursor_old.execute("SELECT idsiswa, lulus FROM siswa")
df_siswa = pd.DataFrame(cursor_old.fetchall())

print("Value counts for db_old.siswa.lulus:")
print(df_siswa['lulus'].value_counts(dropna=False))

cursor_old.close()
conn_old.close()
