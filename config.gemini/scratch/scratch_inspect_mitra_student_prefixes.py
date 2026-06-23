import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
import re
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

# Fetch all partners
cursor.execute("SELECT idmitra, nama FROM mitra")
mitras = cursor.fetchall()

print("=== Partner, associated students prefix, and proposal ===")
for m in mitras:
    idmitra = m['idmitra']
    # Get all students for this partner
    cursor.execute("SELECT no_induk FROM siswa WHERE idmitra = %s AND no_induk IS NOT NULL AND no_induk != ''", (idmitra,))
    students = cursor.fetchall()
    
    # Extract letter prefixes from students
    prefixes = []
    for s in students:
        no_induk = s['no_induk']
        # Remove digits and common signs
        prefix = re.sub(r'[0-9#-/\s]', '', no_induk)
        if prefix:
            prefixes.append(prefix)
            
    unique_prefixes = set(prefixes)
    print(f"idmitra: {idmitra:<7} | Name: {m['nama'][:30]:<30} | Unique Prefixes: {list(unique_prefixes)}")

cursor.close()
conn_old.close()
