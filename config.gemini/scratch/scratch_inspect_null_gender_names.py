import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import pandas as pd
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor = conn_old.cursor(dictionary=True)

print("=== Names with null/empty jk in old DB pelamar ===")
cursor.execute("SELECT idpelamar, nama, jk, email FROM pelamar WHERE jk IS NULL OR jk = ''")
for r in cursor.fetchall():
    print(r)

# Check unmatched users names as well
cursor.execute("SELECT idusers, email, nama FROM users")
df_users = pd.DataFrame(cursor.fetchall())
cursor.execute("SELECT idpelamar, email, nama FROM pelamar")
df_pel = pd.DataFrame(cursor.fetchall())
cursor.execute("SELECT idpelamar, idusers FROM pelamar_users")
df_pu = pd.DataFrame(cursor.fetchall())

cursor.execute("SELECT DISTINCT idusers FROM pekerjaan")
df_pekerjaan_users = pd.DataFrame(cursor.fetchall())
cursor.execute("SELECT DISTINCT idusers FROM pendidikan")
df_pendidikan_users = pd.DataFrame(cursor.fetchall())
cursor.execute("SELECT DISTINCT idusers FROM kursus")
df_kursus_users = pd.DataFrame(cursor.fetchall())

child_users = set(df_pekerjaan_users['idusers']).union(
    set(df_pendidikan_users['idusers'])
).union(
    set(df_kursus_users['idusers'])
)

def clean_str(s):
    if pd.isna(s): return ""
    return str(s).strip().lower()

def clean_name_without_titles(s):
    import re
    if pd.isna(s): return ""
    s = str(s).strip().lower()
    if ',' in s: s = s.split(',')[0]
    titles = [
        r'\bs\.?\s*pd\b', r'\bm\.?\s*pd\b', r'\bs\.?\s*s\b', r'\bs\.?\s*t\b', 
        r'\bs\.?\s*hum\b', r'\bs\.?\s*kom\b', r'\ba\.?\s*md\b', r'\bs\.?\s*e\b', 
        r'\bm\.?\s*m\b', r'\bdr\b', r'\bdra\b', r'\bdrs\b', r'\bprof\b',
        r'\bpsi\b', r'\bs\.?\s*psi\b'
    ]
    for title in titles:
        s = re.sub(title, '', s, flags=re.IGNORECASE)
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

df_users['email_clean'] = df_users['email'].apply(clean_str)
df_users['name_clean'] = df_users['nama'].apply(clean_name_without_titles)

df_pel['email_clean'] = df_pel['email'].apply(clean_str)
df_pel['name_clean'] = df_pel['nama'].apply(clean_name_without_titles)

pu_map = dict(zip(df_pu['idusers'], df_pu['idpelamar']))
email_to_pelamar = {row['email_clean']: row['idpelamar'] for _, row in df_pel.iterrows() if row['email_clean']}
name_to_pelamar = {row['name_clean']: row['idpelamar'] for _, row in df_pel.iterrows() if row['name_clean']}

unmatched_names = []
for u_id in child_users:
    u_rows = df_users[df_users['idusers'] == u_id]
    if u_rows.empty: continue
    u_row = u_rows.iloc[0]
    u_email = u_row['email_clean']
    u_name = u_row['name_clean']
    
    p_id = pu_map.get(u_id) or email_to_pelamar.get(u_email) or name_to_pelamar.get(u_name)
    if not p_id:
        unmatched_names.append((u_id, u_row['nama'], u_row['email']))

print("\n=== Unmatched Users (placeholders) names ===")
for u_id, name, email in unmatched_names:
    print(f"idusers: {u_id}, name: {name}, email: {email}")

cursor.close()
conn_old.close()
