# config.gemini/migration_helpers/test_fk_remapper.py
import pytest
import pandas as pd
from .fk_remapper import detect_region_fk_columns, apply_region_fk_remapping

@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['Item A', 'Item B', 'Item C', 'Item D'],
        'idprovinsi': [1, 2, 99, 1],
        'id_kabupaten': [10, 11, 10, 999],
        'other_data': ['xyz', 'abc', 'def', 'ghi']
    })

@pytest.fixture
def mock_all_region_mappings():
    # Province mapping
    province_map = pd.DataFrame({
        'old_id': [1, 2, 3],
        'new_id': [101, 102, -1],
        'status_mapping': ['mapped', 'mapped', 'not_found']
    })
    # Kabupaten mapping
    kabupaten_map = pd.DataFrame({
        'old_id': [10, 11, 12],
        'new_id': [201, 202, -1],
        'status_mapping': ['mapped', 'mapped', 'not_found']
    })
    return {
        'province': province_map,
        'kabupaten': kabupaten_map
    }

def test_detect_region_fk_columns(sample_dataframe):
    detected = detect_region_fk_columns(sample_dataframe)
    assert detected == {
        'province': 'idprovinsi',
        'kabupaten': 'id_kabupaten'
    }

    df_upper_case = pd.DataFrame({
        'IDPROVINSI': [1,2],
        'IDKABUPATEN': [10,11]
    })
    detected_upper = detect_region_fk_columns(df_upper_case)
    assert detected_upper == {
        'province': 'IDPROVINSI',
        'kabupaten': 'IDKABUPATEN'
    }

def test_apply_region_fk_remapping(sample_dataframe, mock_all_region_mappings):
    remapped_df = apply_region_fk_remapping(sample_dataframe, mock_all_region_mappings)

    # Check if original columns are preserved and new IDs are applied
    assert 'id' in remapped_df.columns
    assert 'name' in remapped_df.columns
    assert 'other_data' in remapped_df.columns

    # Check remapped province IDs
    assert list(remapped_df['idprovinsi']) == [101, 102, -1, 101] # 99 was unmapped, now -1

    # Check remapped kabupaten IDs
    assert list(remapped_df['id_kabupaten']) == [201, 202, 201, -1] # 999 was unmapped, now -1

    # Ensure no temporary columns remain
    assert 'old_id_mapping' not in remapped_df.columns
    assert 'new_id_mapping' not in remapped_df.columns
    assert 'status_mapping' not in remapped_df.columns

    # Check original dataframe is not modified
    assert list(sample_dataframe['idprovinsi']) == [1, 2, 99, 1]
