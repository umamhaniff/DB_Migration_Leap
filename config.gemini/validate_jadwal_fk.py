import sys
import os
import mysql.connector
sys.path.append(os.path.abspath('.'))
from config import get_db_config

config = get_db_config()
db_old = mysql.connector.connect(**config['db_old'])
db_new = mysql.connector.connect(**config['db_new'])

c_old = db_old.cursor()
c_new = db_new.cursor()

# Get all unique idpendkursus (kursus), idperiode (periode), idlevel (level), idsesi (sesi) in old jadwal
c_old.execute("SELECT DISTINCT idpendkursus, idperiode, idlevel, idsesi FROM jadwal")
old_refs = c_old.fetchall()

# Get all existing keys in new DB
c_new.execute("SELECT id_kursus FROM kursus")
new_kursus = set(r[0] for r in c_new.fetchall())

c_new.execute("SELECT id_periode FROM periode")
new_periode = set(r[0] for r in c_new.fetchall())

c_new.execute("SELECT id_level FROM level")
new_level = set(r[0] for r in c_new.fetchall())

c_new.execute("SELECT id_sesi FROM sesi")
new_sesi = set(r[0] for r in c_new.fetchall())

print(f"Total unique schedules ref combinations: {len(old_refs)}")
print(f"New DB keys count: kursus={len(new_kursus)}, periode={len(new_periode)}, level={len(new_level)}, sesi={len(new_sesi)}")

invalid_kursus = set()
invalid_periode = set()
invalid_level = set()
invalid_sesi = set()

for r in old_refs:
    k, p, l, s = r
    if k not in new_kursus:
        invalid_kursus.add(k)
    if p not in new_periode:
        invalid_periode.add(p)
    if l not in new_level:
        invalid_level.add(l)
    if s not in new_sesi:
        invalid_sesi.add(s)

print("Validation Results:")
print(f"  Invalid kursus refs in old jadwal: {invalid_kursus or 'None'}")
print(f"  Invalid periode refs in old jadwal: {invalid_periode or 'None'}")
print(f"  Invalid level refs in old jadwal: {invalid_level or 'None'}")
print(f"  Invalid sesi refs in old jadwal: {invalid_sesi or 'None'}")

db_old.close()
db_new.close()
