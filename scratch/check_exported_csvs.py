import os
import pandas as pd

def main():
    csv_dir = 'extract/cek_csv'
    print(f"=== VERIFYING EXPORTED CSVS IN {csv_dir} ===")
    
    rapor_files = [
        'rapor_format.csv', 'rapor_format_sub.csv', 'rapor_format_formula.csv',
        'rapor_format_formula_sub.csv', 'rapor_level_config.csv', 'rapor_sub_level.csv',
        'rapor_siswa.csv', 'rapor_siswa_file.csv', 'rapor_lacak.csv'
    ]
    
    for filename in rapor_files:
        path = os.path.join(csv_dir, filename)
        if os.path.exists(path):
            try:
                # Read CSV keeping all as string to check raw output format
                df = pd.read_csv(path, keep_default_na=False)
                print(f"\nFile: {filename}")
                print(f"  Shape: {df.shape}")
                print(f"  Columns: {list(df.columns)}")
                
                # Check for decimal .0 in ID columns
                id_cols = [c for c in df.columns if 'id' in c or 'urutan' in c]
                for col in id_cols:
                    sample_vals = df[col].head(10).tolist()
                    has_decimal = any('.0' in str(v) for v in sample_vals if str(v).strip())
                    print(f"    Column '{col}': has decimal? {has_decimal} | Sample: {sample_vals[:5]}")
                
                # Specific checks
                if filename == 'rapor_format.csv':
                    # Check for duplicates on id_rapor_format
                    dups = df['id_rapor_format'].duplicated().sum()
                    print(f"    Duplicate Primary Keys (id_rapor_format): {dups}")
                    # Check for K00017
                    has_k00017 = 'K00017' in df['id_kursus'].values
                    print(f"    Contains deleted course 'K00017'? {has_k00017}")
                    
                if filename == 'rapor_format_sub.csv':
                    # Check for null urutan
                    has_empty_urutan = '' in df['urutan'].values or df['urutan'].isna().any()
                    print(f"    Has empty/null urutan? {has_empty_urutan}")
                    
                if filename == 'rapor_siswa.csv':
                    # Check for placeholder garbage
                    garbage_keywords = ['comment', 'coba', 'test', 'dummy']
                    garbage_rows = df[df['final_result'].str.lower().str.contains('|'.join(garbage_keywords), na=False)]
                    print(f"    Rows with placeholder keywords in final_result: {len(garbage_rows)}")
                    if len(garbage_rows) > 0:
                        print("    Sample garbage rows:", garbage_rows['final_result'].head(3).tolist())
                    
                    # Check max length of final_result
                    max_len = df['final_result'].apply(lambda x: len(str(x))).max()
                    print(f"    Maximum length in final_result: {max_len}")
                    
                if filename == 'rapor_lacak.csv':
                    # Check if id_jadwal has any string values like 'J000000023'
                    has_j_prefix = df['id_jadwal'].astype(str).str.contains('J').any()
                    print(f"    Contains old string schedule IDs (with 'J')? {has_j_prefix}")
                    # Check if id_siswa has any string values like 'S0000007'
                    has_s_prefix = df['id_siswa'].astype(str).str.contains('S').any()
                    print(f"    Contains old string student IDs (with 'S')? {has_s_prefix}")
                    
            except Exception as e:
                print(f"Error reading {filename}: {e}")
        else:
            print(f"File {filename}: NOT FOUND!")

if __name__ == '__main__':
    main()
