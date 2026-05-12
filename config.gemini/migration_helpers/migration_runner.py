# config.gemini/migration_helpers/migration_runner.py
import pandas as pd
from sqlalchemy.engine import Engine
from sqlalchemy import text
from typing import Dict, List, Any
import logging
import time
import os

from .fk_remapper import apply_region_fk_remapping, detect_region_fk_columns
from .migration_utils import migration_summary_report, log_failed_mappings_to_file

logger = logging.getLogger(__name__)

def get_primary_key_columns(engine: Engine, table_name: str) -> List[str]:
    """
    Fetches primary key columns for a given table.
    This is a simplified implementation. A real-world scenario might need more
    robust SQL for different database dialects (e.g., querying INFORMATION_SCHEMA).
    """
    try:
        with engine.connect() as conn:
            if 'mysql' in engine.dialect.name:
                query = text(f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY'")
                result = conn.execute(query).fetchall()
                pk_cols = [row[4] for row in result] # Column_name is the 5th column (index 4)
            elif 'sqlite' in engine.dialect.name:
                query = text(f"PRAGMA table_info({table_name})")
                result = conn.execute(query).fetchall()
                pk_cols = [row[1] for row in result if row[5] == 1]
            else:
                pk_cols = ['id'] # Fallback to 'id'
            
            if not pk_cols:
                logger.warning(f"Could not determine primary key for table '{table_name}'. Defaulting to ['id']. Duplicate checking might be inaccurate.")
                return ['id']
            return pk_cols
    except Exception as e:
        logger.error(f"Could not fetch primary key for table '{table_name}': {e}. Defaulting to ['id'].")
        return ['id']

def check_for_existing_records(new_engine: Engine, table_name: str, df: pd.DataFrame, primary_key_cols: List[str]) -> pd.DataFrame:
    """
    Checks for existing records in the new database based on primary key columns.
    Returns DataFrame with an 'is_duplicate' flag.
    """
    if not primary_key_cols or df.empty:
        df['is_duplicate'] = False
        return df

    pk_col = primary_key_cols[0] # Simplified to single-column PK for this implementation
    
    try:
        with new_engine.connect() as conn:
            existing_ids_df = pd.read_sql(text(f"SELECT {pk_col} FROM {table_name}"), conn)
        
        if existing_ids_df.empty:
            df['is_duplicate'] = False
            return df
            
        existing_pks = set(existing_ids_df[pk_col])
        df['is_duplicate'] = df[pk_col].isin(existing_pks)
        logger.info(f"Identified {df['is_duplicate'].sum()} potential duplicate records for {table_name} based on PK: {pk_col}.")
    except Exception as e:
        logger.error(f"Error checking for existing records in {table_name} using PK {pk_col}: {e}")
        df['is_duplicate'] = False
    return df

def migrate_table(
    table_name: str,
    old_engine: Engine,
    new_engine: Engine,
    all_region_mappings: Dict[str, pd.DataFrame],
) -> Dict[str, Any]:
    """
    Orchestrates the migration of a single table, including FK remapping and validation.
    """
    logger.info(f"========== Starting migration for table: {table_name} ==========")
    start_time = time.time()
    
    source_row_count = 0
    processed_row_count = 0
    failed_row_count = 0
    successful_inserts = 0
    duplicate_skips = 0

    try:
        primary_key_cols = get_primary_key_columns(new_engine, table_name)

        with old_engine.connect() as conn:
            old_df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        source_row_count = len(old_df)

        if source_row_count == 0:
            logger.warning(f"Source table '{table_name}' is empty. Skipping.")
            return {"status": "skipped_empty", "duration": time.time() - start_time, **locals()}

        remapped_df = apply_region_fk_remapping(old_df, all_region_mappings)
        processed_row_count = len(remapped_df)
        
        invalid_fk_rows_indices = pd.Index([])
        detected_fks = detect_region_fk_columns(remapped_df)
        for col_name in detected_fks.values():
            invalid_fk_rows_indices = invalid_fk_rows_indices.union(remapped_df[remapped_df[col_name] == -1].index)
        
        failed_df = remapped_df.loc[invalid_fk_rows_indices].copy()
        failed_df['error_type'] = 'Unmapped Region FK'
        failed_row_count = len(failed_df)

        clean_df = remapped_df.drop(invalid_fk_rows_indices)

        if failed_row_count > 0:
            log_failed_mappings_to_file(failed_df, filename_prefix=f"failed_fk_{table_name}")

        if clean_df.empty:
            logger.warning(f"All rows for '{table_name}' failed validation. No data to insert.")
            return {"status": "all_failed_validation", "duration": time.time() - start_time, **locals()}

        clean_df = check_for_existing_records(new_engine, table_name, clean_df, primary_key_cols)
        to_insert_df = clean_df[~clean_df['is_duplicate']].drop(columns=['is_duplicate'])
        duplicate_skips = clean_df['is_duplicate'].sum()

        if to_insert_df.empty:
            logger.info(f"No new records to insert for '{table_name}' after duplicate check.")
            return {"status": "no_new_records", "duration": time.time() - start_time, **locals()}

        with new_engine.connect() as conn:
            transaction = conn.begin()
            try:
                # Ensure columns match target table before insert
                with new_engine.connect() as conn_check:
                    target_cols_df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 0", conn_check)
                
                cols_to_insert = [col for col in to_insert_df.columns if col in target_cols_df.columns]
                to_insert_df[cols_to_insert].to_sql(table_name, conn, if_exists='append', index=False)
                
                successful_inserts = len(to_insert_df)
                transaction.commit()
                logger.info(f"Successfully inserted {successful_inserts} new rows into '{table_name}'.")
            except Exception as e:
                transaction.rollback()
                logger.error(f"Error inserting data into '{table_name}': {e}", exc_info=True)
                log_failed_mappings_to_file(to_insert_df.assign(error_type='Insert Failed'), filename_prefix=f"failed_insert_{table_name}")
                failed_row_count += len(to_insert_df)
                successful_inserts = 0
                raise

    except Exception as e:
        logger.critical(f"Critical error during migration of table '{table_name}': {e}", exc_info=True)
        status = "failed_critical"
    else:
        status = "completed_successfully" if failed_row_count == 0 else "completed_with_errors"
    
    finally:
        duration = time.time() - start_time
        migration_summary_report(table_name, source_row_count, processed_row_count, failed_row_count, successful_inserts, duplicate_skips)
        result_summary = {
            "table_name": table_name,
            "source_row_count": source_row_count,
            "processed_row_count": processed_row_count,
            "failed_row_count": failed_row_count,
            "successful_inserts": successful_inserts,
            "duplicate_skips": duplicate_skips,
            "status": status,
            "duration": round(duration, 2)
        }

    return result_summary
