import sys
import os
import re
import pandas as pd
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import get_db_config

cfg = get_db_config()
conn_old = mysql.connector.connect(**cfg['db_old'])
cursor_old = conn_old.cursor(dictionary=True)

# Fetch all tables
cursor_old.execute("SELECT idusers, email, nama FROM users")
df_users = pd.DataFrame(cursor_old.fetchall())

cursor_old.execute("SELECT idpelamar, idpengajuan, email, nama FROM pelamar")
df_pelamar = pd.DataFrame(cursor_old.fetchall())

cursor_old.execute("SELECT idpelamar, idusers FROM pelamar_users")
df_pu = pd.DataFrame(cursor_old.fetchall())

cursor_old.execute("SELECT DISTINCT idusers FROM pekerjaan")
df_pekerjaan_users = pd.DataFrame(cursor_old.fetchall())

cursor_old.execute("SELECT DISTINCT idusers FROM pendidikan")
df_pendidikan_users = pd.DataFrame(cursor_old.fetchall())

cursor_old.execute("SELECT DISTINCT idusers FROM kursus")
df_kursus_users = pd.DataFrame(cursor_old.fetchall())

# Collect all idusers that exist in child tables
child_users = set(df_pekerjaan_users['idusers']).union(
    set(df_pendidikan_users['idusers'])
).union(
    set(df_kursus_users['idusers'])
)

print(f"Total users in old DB: {len(df_users)}")
print(f"Total pelamar in old DB: {len(df_pelamar)}")
print(f"Total distinct idusers in child tables (pekerjaan, pendidikan, kursus): {len(child_users)}")

# Matching functions
def clean_str(s):
    if pd.isna(s): return ""
    return str(s).strip().lower()

def clean_name_without_titles(s):
    if pd.isna(s): return ""
    s = str(s).strip().lower()
    if ',' in s: 
        s = s.split(',')[0]
    # Remove common academic/professional titles
    titles = [
        r'\bs\.?\s*pd\b', r'\bm\.?\s*pd\b', r'\bs\.?\s*s\b', r'\bs\.?\s*t\b', 
        r'\bs\.?\s*hum\b', r'\bs\.?\s*kom\b', r'\ba\.?\s*md\b', r'\bs\.?\s*e\b', 
        r'\bm\.?\s*m\b', r'\bdr\b', r'\bdra\b', r'\bdrs\b', r'\bprof\b',
        r'\bpsi\b', r'\bs\.?\s*psi\b'
    ]
    for title in titles:
        s = re.sub(title, '', s, flags=re.IGNORECASE)
    # Remove non-alphanumeric characters
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

# Clean dataframes
df_users['email_clean'] = df_users['email'].apply(clean_str)
df_users['name_clean'] = df_users['nama'].apply(clean_name_without_titles)

df_pelamar['email_clean'] = df_pelamar['email'].apply(clean_str)
df_pelamar['name_clean'] = df_pelamar['nama'].apply(clean_name_without_titles)

# 1. pelamar_users mapping
pu_map = dict(zip(df_pu['idusers'], df_pu['idpelamar']))

# 2. Email mapping (from pelamar)
email_to_pelamar = {}
for _, row in df_pelamar.iterrows():
    email = row['email_clean']
    if email and email not in email_to_pelamar:
        email_to_pelamar[email] = row['idpelamar']

# 3. Name mapping (from pelamar)
name_to_pelamar = {}
for _, row in df_pelamar.iterrows():
    name = row['name_clean']
    if name and name not in name_to_pelamar:
        name_to_pelamar[name] = row['idpelamar']

# Now map child users
matched = 0
unmatched_users = []
user_to_pelamar_id = {}

# 1. pelamar_users mapping
pu_map = dict(zip(df_pu['idusers'], df_pu['idpelamar']))

# 2. Email mapping (from pelamar)
email_to_pelamar = {}
for _, row in df_pelamar.iterrows():
    email = row['email_clean']
    if email and email not in email_to_pelamar:
        email_to_pelamar[email] = row['idpelamar']

# 3. Name mapping (from pelamar)
name_to_pelamar = {}
for _, row in df_pelamar.iterrows():
    name = row['name_clean']
    if name and name not in name_to_pelamar:
        name_to_pelamar[name] = row['idpelamar']

# Step A: Attempt to map all child_users to an existing idpelamar
for u_id in child_users:
    # Get user details
    u_rows = df_users[df_users['idusers'] == u_id]
    if u_rows.empty:
        # Not found in users table, we'll treat u_id as its own old idpelamar
        unmatched_users.append((u_id, "User not in users table", ""))
        continue
    
    u_row = u_rows.iloc[0]
    u_email = u_row['email_clean']
    u_name = u_row['name_clean']
    
    # Priority 1: pelamar_users table
    p_id = pu_map.get(u_id)
    if p_id:
        user_to_pelamar_id[u_id] = p_id
        matched += 1
        continue
        
    # Priority 2: Email matching
    p_id = email_to_pelamar.get(u_email)
    if p_id:
        user_to_pelamar_id[u_id] = p_id
        matched += 1
        continue
        
    # Priority 3: Name matching
    p_id = name_to_pelamar.get(u_name)
    if p_id:
        user_to_pelamar_id[u_id] = p_id
        matched += 1
        continue
        
    # Unmatched
    unmatched_users.append((u_id, u_row['nama'], u_row['email']))

print(f"\nMatched to existing pelamar: {matched} / {len(child_users)}")
print(f"Unmatched (needs placeholder): {len(unmatched_users)}")

# Step B: Create placeholder pelamar records for unmatched users
df_pelamar_extended = df_pelamar.copy()
placeholders_added = 0

for u_id, name, email in unmatched_users:
    # Append placeholder record to df_pelamar_extended
    new_row = {
        'idpelamar': u_id,  # Use idusers as the old idpelamar for key mapping
        'nama': name,
        'email': email,
        'idpengajuan': None,
        # other fields can be NaN/None
    }
    df_pelamar_extended = pd.concat([df_pelamar_extended, pd.DataFrame([new_row])], ignore_index=True)
    placeholders_added += 1

# Step C: Assign new auto-increment ID to all pelamar (including placeholders)
df_pelamar_extended['id_pelamar_new'] = df_pelamar_extended.index + 1
pelamar_id_map = dict(zip(df_pelamar_extended['idpelamar'], df_pelamar_extended['id_pelamar_new']))

# Step D: Construct the final user_to_pelamar_id_new mapping
final_user_to_pelamar_id = {}
for u_id in child_users:
    # Check if we mapped it to a real pelamar
    old_p_id = user_to_pelamar_id.get(u_id)
    if old_p_id:
        final_user_to_pelamar_id[u_id] = pelamar_id_map.get(old_p_id)
    else:
        # It was unmatched, so its placeholder idpelamar is u_id
        final_user_to_pelamar_id[u_id] = pelamar_id_map.get(u_id)

print(f"Total pelamar records (including placeholders): {len(df_pelamar_extended)}")
print(f"Null new IDs in child mapping: {sum(pd.isna(list(final_user_to_pelamar_id.values())))}")
print(f"Total mapped: {len(final_user_to_pelamar_id)} / {len(child_users)}")

cursor_old.close()
conn_old.close()
