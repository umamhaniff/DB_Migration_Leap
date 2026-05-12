# config.gemini/migration_helpers/fk_remapper.py
import pandas as pd
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

def detect_region_fk_columns(df: pd.DataFrame) -> Dict[str, str]:
    """
    Detects region foreign key columns (idprovinsi, idkabupaten, idkecamatan, idkelurahan)
    in a DataFrame and returns a dictionary of detected columns with their region type.
    """
    detected_fks = {}
    column_mapping_patterns = {
        'province': ['idprovinsi', 'id_provinsi', 'province_id'],
        'kabupaten': ['idkabupaten', 'id_kabupaten', 'regency_id'],
        'kecamatan': ['idkecamatan', 'id_kecamatan', 'district_id'],
        'kelurahan': ['idkelurahan', 'id_kelurahan', 'village_id']
    }

    df_columns = [col.lower() for col in df.columns]

    for region_type, patterns in column_mapping_patterns.items():
        for pattern in patterns:
            if pattern in df_columns:
                # Find the original case of the column name
                original_column_name = next(col for col in df.columns if col.lower() == pattern)
                detected_fks[region_type] = original_column_name
                logger.info(f"Detected {region_type} FK column: {original_column_name}")
                break
    return detected_fks

def apply_region_fk_remapping(df: pd.DataFrame, all_region_mappings: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Applies region foreign key remapping to a DataFrame.
    It detects FK columns and replaces old IDs with new mapped IDs.
    Returns the DataFrame with remapped FKs.
    """
    df_copy = df.copy()
    detected_fks = detect_region_fk_columns(df_copy)

    for region_type, col_name in detected_fks.items():
        if region_type not in all_region_mappings:
            logger.warning(f"No mapping found for region type '{region_type}'. Skipping FK remapping for column '{col_name}'.")
            continue

        mapping_df = all_region_mappings[region_type]
        
        # Ensure the column to merge on is of the same type
        df_copy[col_name] = pd.to_numeric(df_copy[col_name], errors='coerce').fillna(-1).astype(int)
        mapping_df['old_id'] = pd.to_numeric(mapping_df['old_id'], errors='coerce').fillna(-1).astype(int)

        # Prepare the mapping dataframe for merging with unique column names
        mapping_df_for_merge = mapping_df[['old_id', 'new_id', 'status_mapping']].rename(columns={
            'new_id': 'new_id_mapping',
            'status_mapping': 'status_mapping_temp'
        })

        # Perform the merge to get new IDs
        df_copy = pd.merge(
            df_copy,
            mapping_df_for_merge,
            left_on=col_name,
            right_on='old_id',
            how='left'
        )
        
        # Replace the old FK column with the new_id, handle unmapped cases
        df_copy[col_name] = df_copy['new_id_mapping'].fillna(-1).astype(int)
        
        # Log unmapped records specific to this FK column
        unmapped_count = df_copy['status_mapping_temp'].eq('not_found').sum()
        if unmapped_count > 0:
            logger.warning(f"{unmapped_count} records in column '{col_name}' could not be mapped (region '{region_type}'). Their IDs are set to -1.")
            
        # Drop temporary mapping columns
        df_copy = df_copy.drop(columns=['old_id', 'new_id_mapping', 'status_mapping_temp'])

    logger.info(f"Applied FK remapping for columns: {list(detected_fks.values())}")
    return df_copy
