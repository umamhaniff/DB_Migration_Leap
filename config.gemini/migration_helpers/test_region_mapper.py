# config.gemini/migration_helpers/test_region_mapper.py
import pytest
import pandas as pd
from sqlalchemy import create_engine, text
from .region_mapper import generate_province_mapping, generate_kabupaten_mapping, generate_kecamatan_mapping, generate_kelurahan_mapping

@pytest.fixture
def mock_db_engines_with_kelurahans():
    old_engine = create_engine('sqlite:///:memory:')
    new_engine = create_engine('sqlite:///:memory:')

    # Create mock old tables
    with old_engine.connect() as conn:
        conn.execute(text("CREATE TABLE provinces (id INTEGER PRIMARY KEY, name VARCHAR(255));"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (1, 'PROVINSI JAWA BARAT');"))
        
        conn.execute(text("CREATE TABLE kabupatens (id INTEGER PRIMARY KEY, name VARCHAR(255), province_id INTEGER);"))
        conn.execute(text("INSERT INTO kabupatens (id, name, province_id) VALUES (10, 'KAB. BANDUNG', 1);"))
        
        conn.execute(text("CREATE TABLE kecamatans (id INTEGER PRIMARY KEY, name VARCHAR(255), kabupaten_id INTEGER);"))
        conn.execute(text("INSERT INTO kecamatans (id, name, kabupaten_id) VALUES (100, 'Cileunyi', 10), (101, 'UNKNOWN KECAMATAN', 10);"))
        
        conn.execute(text("CREATE TABLE kelurahans (id INTEGER PRIMARY KEY, name VARCHAR(255), kecamatan_id INTEGER);"))
        conn.execute(text("""
            INSERT INTO kelurahans (id, name, kecamatan_id) VALUES 
            (1000, 'Cibiru Wetan', 100), (1001, 'Cibiru Hilir', 100),
            (1002, 'UNKNOWN KELURAHAN', 100), (1003, 'KEL. DUMMY', 101),
            (1004, 'Cibiru Wetan', 101);
        """))
        conn.commit()

    # Create mock new tables
    with new_engine.connect() as conn:
        conn.execute(text("CREATE TABLE provinces (id INTEGER PRIMARY KEY, name VARCHAR(255));"))
        conn.execute(text("INSERT INTO provinces (id, name) VALUES (1001, 'Jawa Barat');"))

        conn.execute(text("CREATE TABLE kabupatens (id INTEGER PRIMARY KEY, name VARCHAR(255), province_id INTEGER);"))
        conn.execute(text("INSERT INTO kabupatens (id, name, province_id) VALUES (2001, 'Bandung', 1001);"))

        conn.execute(text("CREATE TABLE kecamatans (id INTEGER PRIMARY KEY, name VARCHAR(255), kabupaten_id INTEGER);"))
        conn.execute(text("INSERT INTO kecamatans (id, name, kabupaten_id) VALUES (3001, 'Cileunyi', 2001);"))

        conn.execute(text("CREATE TABLE kelurahans (id INTEGER PRIMARY KEY, name VARCHAR(255), kecamatan_id INTEGER);"))
        conn.execute(text("""
            INSERT INTO kelurahans (id, name, kecamatan_id) VALUES 
            (4001, 'Cibiru Wetan', 3001), (4002, 'Cibiru Hilir', 3001);
        """))
        conn.commit()

    yield old_engine, new_engine
    old_engine.dispose()
    new_engine.dispose()

def test_generate_kelurahan_mapping(mock_db_engines_with_kelurahans):
    old_engine, new_engine = mock_db_engines_with_kelurahans
    province_map_df = generate_province_mapping(old_engine, new_engine)
    kabupaten_map_df = generate_kabupaten_mapping(old_engine, new_engine, province_map_df)
    kecamatan_map_df = generate_kecamatan_mapping(old_engine, new_engine, kabupaten_map_df)
    
    # Prerequisite checks
    assert kecamatan_map_df[kecamatan_map_df['old_id'] == 100]['new_id'].iloc[0] == 3001 # Cileunyi
    assert kecamatan_map_df[kecamatan_map_df['old_id'] == 101]['status_mapping'].iloc[0] == 'not_found' # UNKNOWN KECAMATAN

    kelurahan_map_df = generate_kelurahan_mapping(old_engine, new_engine, kecamatan_map_df)
    
    assert not kelurahan_map_df.empty
    # Old kelurahans with mapped parents: 1000, 1001, 1002. (1003 and 1004 have unmapped parent). Total 3.
    assert len(kelurahan_map_df) == 3
    
    # Test mapped kelurahan
    cibiru_wetan = kelurahan_map_df[kelurahan_map_df['old_id'] == 1000].iloc[0]
    assert cibiru_wetan['normalized_name'] == 'cibiru wetan'
    assert cibiru_wetan['new_id'] == 4001
    assert cibiru_wetan['status_mapping'] == 'mapped'

    # Test unmapped by name
    unknown_kel_map = kelurahan_map_df[kelurahan_map_df['old_id'] == 1002].iloc[0]
    assert unknown_kel_map['new_id'] == -1
    assert unknown_kel_map['status_mapping'] == 'not_found'

    # Test that kelurahans with unmapped parent are filtered out
    assert 1003 not in kelurahan_map_df['old_id'].values
    assert 1004 not in kelurahan_map_df['old_id'].values
