import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

cursor.execute("SELECT idmitra, nama FROM mitra WHERE idmitra = 'M' OR idmitra NOT REGEXP '[0-9]'")
rows = cursor.fetchall()
print("Partners with 'M' or no digits in idmitra:", rows)

cursor.close()
conn_old.close()
