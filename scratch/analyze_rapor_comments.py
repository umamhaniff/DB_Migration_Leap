import sys
import os
import pandas as pd
import mysql.connector
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    # Fetch all 'nilai' values from old rapor table
    cursor_old.execute("SELECT idrapor, nilai FROM rapor WHERE nilai IS NOT NULL AND nilai != ''")
    rows = cursor_old.fetchall()
    print(f"Total non-empty 'nilai' rows to analyze: {len(rows)}")
    
    df = pd.DataFrame(rows)
    df['len'] = df['nilai'].apply(lambda x: len(str(x)))
    
    # 1. Analyze length distribution
    print("\n=== 1. Length Distribution ===")
    print(df['len'].describe())
    
    # 2. Find values containing special character ''
    spec_char_rows = df[df['nilai'].str.contains('', na=False)]
    print(f"\n=== 2. Rows with special character '': {len(spec_char_rows)} ===")
    for idx, row in spec_char_rows.head(5).iterrows():
        print(f"  ID: {row['idrapor']} | {repr(row['nilai'])}")
        
    # 3. Find most common exact strings
    print("\n=== 3. Most Common Exact Values (Top 10) ===")
    value_counts = df['nilai'].value_counts()
    for val, count in value_counts.head(10).items():
        if len(str(val)) > 30:
            print(f"  [{count} times] (len={len(str(val))}): {repr(val[:80])}...")
        else:
            print(f"  [{count} times]: {repr(val)}")

    # 4. Analyze repetitive boilerplate phrases
    # Let's see if there are standard template phrases and count them
    print("\n=== 4. Analysis of Common Templates ===")
    templates = [
        ("Good job", r"(?i)Good job"),
        ("Great job", r"(?i)Great job"),
        ("Excellent", r"(?i)Excellent"),
        ("Well done", r"(?i)Well done"),
        ("progress in strengthening the fundamentals of coding through a creative approach", r"(?i)progress in strengthening the fundamentals of coding"),
        ("telah menunjukkan kemajuan yang signifikan", r"telah menunjukkan kemajuan yang signifikan")
    ]
    for label, pattern in templates:
        matches = df['nilai'].str.contains(pattern, na=False, regex=True).sum()
        print(f"  Pattern '{label}': {matches} matches ({matches/len(df)*100:.1f}%)")
        
    # Let's print some examples of the long repetitive coding comments
    coding_progress_df = df[df['nilai'].str.contains("progress in strengthening|kemajuan yang signifikan", na=False)]
    print(f"\n=== 5. Examples of Repetitive Coding Progress Comments ({len(coding_progress_df)} rows) ===")
    for idx, row in coding_progress_df.head(5).iterrows():
        print(f"  ID: {row['idrapor']} (len={row['len']}): {repr(row['nilai'])}")

    conn_old.close()

if __name__ == '__main__':
    main()
