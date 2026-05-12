# config.gemini/migration_helpers/region_mapper.py
import pandas as pd
from sqlalchemy.engine import Engine
from sqlalchemy import text 
from .region_normalizer import normalize_region_name
import logging

logger = logging.getLogger(__name__)

def generate_province_mapping(old_engine: Engine, new_engine: Engine) -> pd.DataFrame:
    """
    Generates a mapping DataFrame for provinces.
    Includes old_id, old_name, normalized_name, new_id, and status_mapping.
    """
    logger.info("Generating province mapping...")
    # Fetch old provinces
    with old_engine.connect() as conn:
        old_provinces_df = pd.read_sql(text("SELECT id as old_id, name as old_name FROM provinces"), conn)

    # Fetch new provinces
    with new_engine.connect() as conn:
        new_provinces_df = pd.read_sql(text("SELECT id as new_id, name as new_name FROM provinces"), conn)

    # Normalize names for old provinces
    old_provinces_df['normalized_name'] = old_provinces_df['old_name'].apply(normalize_region_name)
    new_provinces_df['normalized_name'] = new_provinces_df['new_name'].apply(normalize_region_name)

    # Merge to find matches
    mapping_df = pd.merge(
        old_provinces_df,
        new_provinces_df[['normalized_name', 'new_id']],
        on='normalized_name',
        how='left'
    )

    # Determine mapping status
    mapping_df['status_mapping'] = mapping_df['new_id'].apply(
        lambda x: 'mapped' if pd.notna(x) else 'not_found'
    )
    mapping_df['new_id'] = mapping_df['new_id'].fillna(-1).astype(int) # Use -1 for not found

    # Select and reorder columns
    mapping_df = mapping_df[['old_id', 'old_name', 'normalized_name', 'new_id', 'status_mapping']]

    logger.info(f"Province mapping generated. Total old provinces: {len(old_provinces_df)}, Mapped: {mapping_df['status_mapping'].eq('mapped').sum()}")
    return mapping_df

if __name__ == '__main__':
    # This block will be executed if the script is run directly, useful for testing
    import sys
    import os
    # Add parent directory to path to import db_connections
    # This path needs to be relative to the file's location
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    from config.gemini.migration_helpers.db_connections import get_db_engine

    logging.basicConfig(level=logging.INFO)

    try:
        # Placeholder for actual DB engines (you need to set up your .env)
        old_db_engine = get_db_engine('old')
        new_db_engine = get_db_engine('new')

        province_map = generate_province_mapping(old_db_engine, new_db_engine)
        print("\nProvince Mapping Sample:")
        print(province_map.head().to_markdown(index=False))
        print(f"\nUnmapped Provinces:\n{province_map[province_map['status_mapping'] == 'not_found'].to_markdown(index=False)}")
    except Exception as e:
        print(f"Error during test run: {e}")
        print("Please ensure your .env file is configured correctly for both OLD and NEW databases.")
