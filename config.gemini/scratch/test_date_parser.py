import sys
import os
import re
import pandas as pd

unique_dates = [
    "02 Maret 2023",
    "February 2022",
    "20 OKTOBER 2020",
    "29 September - 6 Oktober 2021",
    "14 Mei",
    "27 - 29 Mei 2023",
    "14-21 Mei",
    "13-14 Mei 2023",
    "26 November 2022",
    "3 Agustus 2019",
    "24 Februari 2018",
    "27 Agustus 2021",
    "-",
    "11 Desember 2021",
    "8 September 2023",
    "2 Oktober 2023",
    "14 Mei 2024 ",
    "16-Juli-2023",
    "12-Juli-2022",
    "12/12/2020",
    "03/07/2019",
    "27 Agustus 2015",
    "13 Januari 2018",
    "11 September 2016",
    "24 Feb 2022",
    "25 September 2023",
    "24 Desember 2021",
    " 23 Februari 2018",
    "22 juni 2021",
    "4-8 januari 2021",
    "20 juli 2020",
    "28 september 2020",
    "21 september 2020",
    "13-14 februari 2021",
    "23 april - 18 juni 2022",
    "12 september - 15 oktober 2022",
    "12 -15 Desember 2017",
    "January 2025",
    "May 2024",
    "May 2023",
    "20 Mei 2024",
    "27 Juni 2024",
    "21 Januari 2021 - 23 Maret 2021",
    "21 September 2022",
    "7 Maret 2023",
    "15 November 2023",
    "26 Juni 2024",
    "11 Oktober 2025",
    "13 Februari 2026",
    "31 Maret 2026",
    None,
    ""
]

def parse_date(date_str):
    if pd.isna(date_str): return None
    s = str(date_str).strip()
    if s in ('', '-', '0', 'nan', 'NaN'): return None
    
    # First normalize day-of-month ranges: "27 - 29 Mei 2023" -> "27 Mei 2023"
    s = re.sub(r'\b(\d{1,2})\s*-\s*\d{1,2}\b', r'\1', s)
    
    # Try to see if it's a month-level range: e.g. "29 September - 6 Oktober 2021"
    # We split on hyphens with spaces around them, or 'sd', 's/d', 'dan'
    parts = re.split(r'\s+-\s+|\s+(?:sd|s/d|dan|s\.d\.)\s+', s, flags=re.IGNORECASE)
    if len(parts) > 1:
        part1 = parts[0].strip()
        part2 = parts[1].strip()
        # Check if part1 has a year (4 digits)
        if not re.search(r'\b\d{4}\b', part1):
            # Find year in part2
            year_match = re.search(r'\b\d{4}\b', part2)
            if year_match:
                part1 = part1 + " " + year_match.group(0)
        s = part1
        
    # Map Indonesian months to English
    months_id_to_en = {
        'januari': 'January', 'februari': 'February', 'maret': 'March', 'april': 'April',
        'mei': 'May', 'juni': 'June', 'juli': 'July', 'agustus': 'August',
        'september': 'September', 'oktober': 'October', 'november': 'November', 'desember': 'December',
        'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April', 'jun': 'June',
        'jul': 'July', 'agu': 'August', 'agst': 'August', 'sep': 'September', 'okt': 'October', 'nov': 'November', 'des': 'December'
    }
    
    # Normalize spaces and punctuation (but keep spaces between tokens)
    s = s.replace('-', ' ').replace('/', ' ').replace('.', '').strip()
    s = re.sub(r'\s+', ' ', s)
    
    # Clean month name translation
    for id_m, en_m in months_id_to_en.items():
        s = re.sub(rf'\b{id_m}\b', en_m, s, flags=re.IGNORECASE)
        
    # Check if it has a year
    year_match = re.search(r'\b\d{4}\b', s)
    if not year_match:
        # Default to year 2023 if no year is found
        s = s + " 2023"
        
    # Try parsing with various formats
    formats = [
        '%d %B %Y', '%d %b %Y', '%B %Y', '%b %Y',
        '%d %m %Y', '%m %d %Y', '%Y %m %d',
        '%d %m %y', '%m %d %y', '%y %m %d'
    ]
    for fmt in formats:
        try:
            return pd.to_datetime(s, format=fmt).date()
        except:
            continue
            
    # Fallback to general pandas parsing
    try:
        res = pd.to_datetime(s, errors='coerce')
        if pd.notna(res):
            return res.date()
    except:
        pass
        
    return None

print(f"{'Original':<35} | {'Parsed':<12}")
print("-" * 50)
for d in unique_dates:
    res = parse_date(d)
    print(f"{str(d):<35} | {str(res):<12}")
