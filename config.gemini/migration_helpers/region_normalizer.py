# config.gemini/migration_helpers/region_normalizer.py
import re

def normalize_region_name(name: str) -> str:
    """
    Normalizes an Indonesian region name by:
    - Removing "KAB." prefix and converting to title case.
    - Converting "KOTA" prefix to "Kota <Nama>" and then title case.
    - Trimming whitespace.
    - Converting to lowercase for case-insensitive matching.
    """
    if not isinstance(name, str):
        return "" # Handle non-string inputs gracefully

    normalized = name.strip()

    # Rule 1: Remove "PROVINSI" prefix
    normalized = re.sub(r"^PROVINSI\s*\.?\s*", "", normalized, flags=re.IGNORECASE)

    # Rule 2: Remove "KAB." prefix
    normalized = re.sub(r"^KAB\.\s*", "", normalized, flags=re.IGNORECASE)

    # Rule 3: Convert "KOTA" prefix to "Kota <Nama>"
    if re.match(r"^KOTA\s", normalized, flags=re.IGNORECASE):
        normalized = "Kota " + re.sub(r"^KOTA\s*", "", normalized, flags=re.IGNORECASE)

    normalized = normalized.title()
    return normalized.lower() # All matching will be case-insensitive using lowercase
