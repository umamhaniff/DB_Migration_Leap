import sys
import os
import mysql.connector
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import get_db_config

def main():
    cfg = get_db_config()
    conn_old = mysql.connector.connect(**cfg['db_old'])
    cursor_old = conn_old.cursor(dictionary=True)
    
    cursor_old.execute("SELECT idrapor, idsiswa, idjadwal, nilai FROM rapor WHERE nilai IS NOT NULL")
    rows = cursor_old.fetchall()
    
    print("=== SEARCHING FOR WEIRD/PLACEHOLDER PATTERNS ===")
    
    # 1. Look for the word "comment" or "coment" or "comen"
    comment_pattern = re.compile(r'(comment|coment|comen|isi komentar|komentar)', re.IGNORECASE)
    matching_comments = []
    
    # 2. Look for "test" or "coba" or "dummy"
    test_pattern = re.compile(r'\b(test|coba|dummy|asdf|qwerty)\b', re.IGNORECASE)
    matching_tests = []
    
    # 3. Look for weird characters or symbols
    symbol_pattern = re.compile(r'[-_=+#*]{3,}')
    matching_symbols = []

    # 4. Longest remarks (> 150 chars)
    long_remarks = []

    for r in rows:
        val = str(r['nilai']).strip()
        
        if comment_pattern.search(val):
            matching_comments.append(r)
        if test_pattern.search(val):
            matching_tests.append(r)
        if symbol_pattern.search(val):
            matching_symbols.append(r)
        if len(val) > 150:
            long_remarks.append(r)

    print(f"\n1. Found {len(matching_comments)} rows containing 'comment' or similar words:")
    # Print unique values and their frequencies
    val_counts = {}
    for r in matching_comments:
        val_counts[r['nilai']] = val_counts.get(r['nilai'], 0) + 1
    for val, count in sorted(val_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"   [{count} times]: {repr(val)}")

    print(f"\n2. Found {len(matching_tests)} rows containing 'test', 'coba', etc.:")
    test_counts = {}
    for r in matching_tests:
        test_counts[r['nilai']] = test_counts.get(r['nilai'], 0) + 1
    for val, count in sorted(test_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"   [{count} times]: {repr(val)}")

    print(f"\n3. Found {len(matching_symbols)} rows with repetitive symbols (---, ===, etc.):")
    symbol_counts = {}
    for r in matching_symbols:
        symbol_counts[r['nilai']] = symbol_counts.get(r['nilai'], 0) + 1
    for val, count in sorted(symbol_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"   [{count} times]: {repr(val)}")

    print(f"\n4. Total rows > 150 characters: {len(long_remarks)}")
    print("   Showing some examples of these long remarks:")
    for r in long_remarks[:10]:
        print(f"   ID: {r['idrapor']} (len={len(r['nilai'])}): {repr(r['nilai'])}")

    conn_old.close()

if __name__ == '__main__':
    main()
