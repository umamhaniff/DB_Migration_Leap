# config.gemini/migration_helpers/migration_utils.py
import logging
import pandas as pd
from typing import Dict
import os

def setup_logging(log_file_path: str = "logs/migration.log", level=logging.INFO):
    """
    Sets up logging to a file and console.
    """
    log_dir = os.path.dirname(log_file_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    # To prevent duplicate handlers if run in a notebook cell multiple times
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
    logger = logging.getLogger(__name__)
    logger.info(f"Logging set up. Output to {log_file_path}")

def preview_mapping_results(mapping_df: pd.DataFrame, map_name: str, head_rows: int = 5):
    """
    Prints a preview of a mapping DataFrame and reports unmapped items.
    """
    logger = logging.getLogger(__name__)
    print(f"
--- Previewing {map_name.title()} Mapping ---")
    if mapping_df.empty:
        print(f"No data available for {map_name} mapping.")
        print("-" * 40)
        return
        
    print(f"Total old {map_name}: {len(mapping_df)}")
    print(f"Mapped {map_name}: {mapping_df['status_mapping'].eq('mapped').sum()}")
    print(f"Unmapped {map_name}: {mapping_df['status_mapping'].eq('not_found').sum()}")
    print(f"
Top {head_rows} rows of {map_name} mapping:")
    print(mapping_df.head(head_rows).to_markdown(index=False))

    unmapped_items = mapping_df[mapping_df['status_mapping'] == 'not_found']
    if not unmapped_items.empty:
        print(f"
Sample of unmapped {map_name}s (first {head_rows} records):")
        print(unmapped_items.head(head_rows).to_markdown(index=False))
        logger.warning(f"{len(unmapped_items)} {map_name}s were not mapped.")
    else:
        logger.info(f"All {map_name}s were successfully mapped.")
    print("-" * 40)

def migration_summary_report(
    table_name: str,
    source_row_count: int,
    processed_row_count: int,
    failed_row_count: int,
    successful_inserts: int,
    duplicate_skips: int
):
    """
    Generates a summary report for a table migration.
    """
    logger = logging.getLogger(__name__)
    print(f"
--- Migration Summary for Table: {table_name} ---")
    print(f"Source Row Count: {source_row_count}")
    print(f"Processed Rows (after remapping): {processed_row_count}")
    print(f"Failed Rows (validation errors): {failed_row_count}")
    print(f"Successfully Inserted Rows: {successful_inserts}")
    print(f"Duplicate Rows Skipped (on rerun): {duplicate_skips}")
    
    total_accounted_for = failed_row_count + successful_inserts + duplicate_skips
    if source_row_count == total_accounted_for:
        print("Status: ✅ Row counts match.")
    else:
        print(f"Status: ⚠️ Row count mismatch! Source: {source_row_count}, Accounted For: {total_accounted_for}")
        logger.error(f"Row count mismatch for {table_name}. Source: {source_row_count}, Accounted For: {total_accounted_for}")
    print("-" * 40)

def log_failed_mappings_to_file(
    failed_data: pd.DataFrame,
    log_dir: str = "logs",
    filename_prefix: str = "failed_mapping"
):
    """
    Logs a DataFrame of failed records to a CSV file in the logs directory.
    """
    logger = logging.getLogger(__name__)
    if failed_data.empty:
        logger.info(f"No failed data to log for {filename_prefix}.")
        return

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(log_dir, f"{filename_prefix}_{timestamp}.csv")
    
    try:
        failed_data.to_csv(file_path, index=False)
        logger.warning(f"Logged {len(failed_data)} failed records to {file_path}")
    except Exception as e:
        logger.error(f"Failed to log records to {file_path}: {e}")
