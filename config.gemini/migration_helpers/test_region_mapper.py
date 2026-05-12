# config.gemini/migration_helpers/test_region_mapper.py
import pytest
import pandas as pd
from sqlalchemy import create_engine, text
from .region_mapper import generate_province_mapping

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
    assert jabar_map['old_name'] == 'PROVINSI JAWA BARAT'
    assert jabar_map['normalized_name'] == 'jawa barat'
    assert jabar_map['new_id'] == 101
    assert jabar_map['status_mapping'] == 'mapped'

    # Test another mapped province (with KAB. prefix in old)
    banten_map = province_map_df[province_map_df['old_id'] == 2].iloc[0]
    assert banten_map['old_name'] == 'KAB. BANTEN'
    assert banten_map['normalized_name'] == 'banten'
    assert banten_map['new_id'] == 102
    assert banten_map['status_mapping'] == 'mapped'

    # Test unmapped province
    unknown_map = province_map_df[province_map_df['old_id'] == 4].iloc[0]
    assert unknown_map['old_name'] == 'UNKNOWN PROVINCE'
    assert unknown_map['normalized_name'] == 'unknown province'
    assert unknown_map['new_id'] == -1
    assert unknown_map['status_mapping'] == 'not_found'

    # Test column order and types
    expected_columns = ['old_id', 'old_name', 'normalized_name', 'new_id', 'status_mapping']
    assert list(province_map_df.columns) == expected_columns
    assert pd.api.types.is_integer_dtype(province_map_df['old_id'])
    assert pd.api.types.is_integer_dtype(province_map_df['new_id'])
    assert pd.api.types.is_string_dtype(province_map_df['old_name'])
    assert pd.api.types.is_string_dtype(province_map_df['normalized_name'])
    assert pd.api.types.is_string_dtype(province_map_df['status_mapping'])
