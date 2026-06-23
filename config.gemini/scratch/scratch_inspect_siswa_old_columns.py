import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor()

cursor.execute("DESCRIBE siswa")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn_old.close()
