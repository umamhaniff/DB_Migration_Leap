# config.gemini/migration_helpers/test_region_mapper.py
import pytest
import pandas as pd
from sqlalchemy import create_engine, text
from .region_mapper import generate_province_mapping, generate_kabupaten_mapping, generate_kecamatan_mapping

# This file now contains tests for province, kabupaten, and kecamatan.

@pytest.fixture
def mock_db_engines_with_kecamatans():
    old_engine = create_engine('sqlite:///:memory:')
    new_engine = create_engine('sqlite:///:memory:')

    # Create mock old tables
    with old_engine.connect() as conn:
        conn.execute(text("CREATE TABLE provinces (id INTEGER PRIMARY KEY, name VARCHAR(255));"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (1, 'PROVINSI JAWA BARAT'), (2, 'PROVINSI DKI JAKARTA'), (3, 'UNKNOWN PROVINCE');"))
        
        conn.execute(text("CREATE TABLE kabupatens (id INTEGER PRIMARY KEY, name VARCHAR(255), province_id INTEGER);"))
        conn.execute(text("""
            INSERT INTO kabupatens (id, name, province_id) VALUES 
            (10, 'KAB. BANDUNG', 1), (11, 'KOTA BEKASI', 1), (12, 'KAB. BOGOR', 1),
            (13, 'UNKNOWN KABUPATEN', 1), (14, 'KAB. DUMMY', 3);
        """))
        
        conn.execute(text("CREATE TABLE kecamatans (id INTEGER PRIMARY KEY, name VARCHAR(255), kabupaten_id INTEGER);"))
        conn.execute(text("""
            INSERT INTO kecamatans (id, name, kabupaten_id) VALUES 
            (100, 'Cileunyi', 10), (101, 'Bojongsoang', 10), (102, 'Bekasi Timur', 11),
            (103, 'Ciampea', 12), (104, 'UNKNOWN KECAMATAN', 10),
            (105, 'KEC. DUMMY', 13), (106, 'Cileunyi', 11);
        """))
        conn.commit()

    # Create mock new tables
    with new_engine.connect() as conn:
        conn.execute(text("CREATE TABLE provinces (id INTEGER PRIMARY KEY, name VARCHAR(255));"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (1001, 'Jawa Barat'), (1002, 'DKI Jakarta');"))

        conn.execute(text("CREATE TABLE kabupatens (id INTEGER PRIMARY KEY, name VARCHAR(255), province_id INTEGER);"))
        conn.execute(text("""
            INSERT INTO kabupatens (id, name, province_id) VALUES 
            (2001, 'Bandung', 1001), (2002, 'Bekasi', 1001), (2003, 'Bogor', 1001);
        """))

        conn.execute(text("CREATE TABLE kecamatans (id INTEGER PRIMARY KEY, name VARCHAR(255), kabupaten_id INTEGER);"))
        conn.execute(text("""
            INSERT INTO kecamatans (id, name, kabupaten_id) VALUES 
            (3001, 'Cileunyi', 2001), (3002, 'Bojongsoang', 2001), (3003, 'Bekasi Timur', 2002),
            (3004, 'Ciampea', 2003), (3005, 'Cileunyi', 2002);
        """))
        conn.commit()

    yield old_engine, new_engine
    old_engine.dispose()
    new_engine.dispose()

def test_generate_kecamatan_mapping(mock_db_engines_with_kecamatans):
    old_engine, new_engine = mock_db_engines_with_kecamatans
    province_map_df = generate_province_mapping(old_engine, new_engine)
    kabupaten_map_df = generate_kabupaten_mapping(old_engine, new_engine, province_map_df)
    
    # Prerequisite checks
    assert kabupaten_map_df[kabupaten_map_df['old_id'] == 10]['new_id'].iloc[0] == 2001 # Bandung
    assert kabupaten_map_df[kabupaten_map_df['old_id'] == 13]['status_mapping'].iloc[0] == 'not_found' # UNKNOWN KABUPATEN

    kecamatan_map_df = generate_kecamatan_mapping(old_engine, new_engine, kabupaten_map_df)
    
    assert not kecamatan_map_df.empty
    # Old kecamatans with mapped parents: 100, 101, 102, 103, 104, 106. (ID 105 parent is unmapped). Total 6.
    # 'Cileunyi' is duplicated in old data for different parents (10 and 11). Both should be handled.
    assert len(kecamatan_map_df) == 6
    
    # Test mapped kecamatan (Cileunyi in Kab. Bandung)
    cileunyi_bandung = kecamatan_map_df[kecamatan_map_df['old_id'] == 100].iloc[0]
    assert cileunyi_bandung['normalized_name'] == 'cileunyi'
    assert cileunyi_bandung['new_id'] == 3001
    assert cileunyi_bandung['status_mapping'] == 'mapped'

    # Test mapped kecamatan (Cileunyi in Kota Bekasi)
    cileunyi_bekasi = kecamatan_map_df[kecamatan_map_df['old_id'] == 106].iloc[0]
    assert cileunyi_bekasi['normalized_name'] == 'cileunyi'
    assert cileunyi_bekasi['new_id'] == 3005
    assert cileunyi_bekasi['status_mapping'] == 'mapped'

    # Test unmapped by name
    unknown_kec_map = kecamatan_map_df[kecamatan_map_df['old_id'] == 104].iloc[0]
    assert unknown_kec_map['new_id'] == -1
    assert unknown_kec_map['status_mapping'] == 'not_found'

    # Test that kecamatan with unmapped parent is filtered out
    assert 105 not in kecamatan_map_df['old_id'].values
