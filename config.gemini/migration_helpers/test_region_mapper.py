# config.gemini/migration_helpers/test_region_mapper.py
import pytest
import pandas as pd
from sqlalchemy import create_engine, text
from .region_mapper import generate_province_mapping, generate_kabupaten_mapping

@pytest.fixture
def mock_db_engines():
    # Setup in-memory SQLite databases for testing
    old_engine = create_engine('sqlite:///:memory:')
    new_engine = create_engine('sqlite:///:memory:')

    # Create mock old_provinces table
    with old_engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE provinces (
                id INTEGER PRIMARY KEY,
                name VARCHAR(255)
            );
        """))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (1, 'PROVINSI JAWA BARAT');"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (2, 'KAB. BANTEN');")) # Will be normalized to 'banten'
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (3, 'PROVINSI ACEH');"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (4, 'UNKNOWN PROVINCE');"))
        conn.commit()

    # Create mock new_provinces table
    with new_engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE provinces (
                id INTEGER PRIMARY KEY,
                name VARCHAR(255)
            );
        """))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (101, 'Jawa Barat');"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (102, 'Banten');"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (103, 'Aceh');"))
        conn.commit()

    yield old_engine, new_engine

    # Teardown (not strictly necessary for in-memory, but good practice)
    old_engine.dispose()
    new_engine.dispose()

def test_generate_province_mapping(mock_db_engines):
    old_engine, new_engine = mock_db_engines
    province_map_df = generate_province_mapping(old_engine, new_engine)

    assert not province_map_df.empty
    assert len(province_map_df) == 4 # Should match the number of old provinces

    # Test mapped province
    jabar_map = province_map_df[province_map_df['old_id'] == 1].iloc[0]
    assert jabar_map['normalized_name'] == 'jawa barat'
    assert jabar_map['new_id'] == 101

    # Test another mapped province
    banten_map = province_map_df[province_map_df['old_id'] == 2].iloc[0]
    assert banten_map['normalized_name'] == 'banten'
    assert banten_map['new_id'] == 102

    # Test unmapped province
    unknown_map = province_map_df[province_map_df['old_id'] == 4].iloc[0]
    assert unknown_map['new_id'] == -1
    assert unknown_map['status_mapping'] == 'not_found'

@pytest.fixture
def mock_db_engines_with_kabupatens():
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
            (13, 'KOTA BOGOR', 1), (14, 'KOTA BANDUNG', 1), (15, 'KOTA JAKARTA PUSAT', 2),
            (16, 'UNKNOWN KABUPATEN', 1), (17, 'KAB. DUMMY', 3);
        """))
        conn.commit()

    # Create mock new tables
    with new_engine.connect() as conn:
        conn.execute(text("CREATE TABLE provinces (id INTEGER PRIMARY KEY, name VARCHAR(255));"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (1001, 'Jawa Barat'), (1002, 'DKI Jakarta');"))

        conn.execute(text("CREATE TABLE kabupatens (id INTEGER PRIMARY KEY, name VARCHAR(255), province_id INTEGER);"))
        conn.execute(text("""
            INSERT INTO kabupatens (id, name, province_id) VALUES 
            (2001, 'Bandung', 1001), (2002, 'Bekasi', 1001), (2003, 'Bogor', 1001),
            (2004, 'Kota Bogor', 1001), (2005, 'Kota Bandung', 1001), (2006, 'Kota Jakarta Pusat', 1002);
        """))
        conn.commit()

    yield old_engine, new_engine
    old_engine.dispose()
    new_engine.dispose()

def test_generate_kabupaten_mapping(mock_db_engines_with_kabupatens):
    old_engine, new_engine = mock_db_engines_with_kabupatens
    province_map_df = generate_province_mapping(old_engine, new_engine)
    
    # Prerequisite check
    assert province_map_df[province_map_df['old_id'] == 1]['new_id'].iloc[0] == 1001
    assert province_map_df[province_map_df['old_id'] == 3]['new_id'].iloc[0] == -1

    kabupaten_map_df = generate_kabupaten_mapping(old_engine, new_engine, province_map_df)

    assert not kabupaten_map_df.empty
    assert len(kabupaten_map_df) == 5 # After de-duplication, 5 unique old entries should remain to be mapped.
    
    # Test mapped kabupaten
    bandung_map = kabupaten_map_df[kabupaten_map_df['old_id'] == 10].iloc[0]
    assert bandung_map['normalized_name'] == 'bandung'
    assert bandung_map['new_id'] == 2001
    assert bandung_map['status_mapping'] == 'mapped'

    # Test mapped "KOTA"
    bekasi_map = kabupaten_map_df[kabupaten_map_df['old_id'] == 11].iloc[0]
    assert bekasi_map['normalized_name'] == 'bekasi'
    assert bekasi_map['new_id'] == 2002
    assert bekasi_map['status_mapping'] == 'mapped'

    # Test unmapped by name
    unknown_kab_map = kabupaten_map_df[kabupaten_map_df['old_id'] == 16].iloc[0]
    assert unknown_kab_map['new_id'] == -1
    assert unknown_kab_map['status_mapping'] == 'not_found'

    # Test that kabupaten with unmapped parent province is filtered out
    assert 17 not in kabupaten_map_df['old_id'].values
