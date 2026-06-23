import os
import pickle
import datetime
import pandas as pd

def format_val(val):
    if pd.isna(val) or val is None:
        return None
    s_val = str(val).strip()
    if s_val in ('NaT', 'NaN', 'None', '<NaT>', ''):
        return None
    if isinstance(val, (pd.Timestamp, datetime.datetime)):
        return val.strftime('%Y-%m-%d %H:%M:%S')
    if isinstance(val, datetime.date):
        return val.strftime('%Y-%m-%d')
    if isinstance(val, datetime.time):
        return val.strftime('%H:%M:%S')
    # Fallback check for type name strings (like Pandas Timestamp)
    t_name = type(val).__name__
    if t_name in ('Timestamp', 'date', 'datetime', 'time'):
        return str(val)
    return val

def fix_pickle(path):
    if not os.path.exists(path):
        return False
    
    print(f"Processing pickle: {path}")
    with open(path, "rb") as f:
        try:
            data = pickle.load(f)
        except Exception as e:
            print(f"Error loading {path}: {e}")
            return False
            
    if not isinstance(data, dict):
        print(f"Skipping {path}: not a dict of DataFrames")
        return False
        
    modified = False
    for tbl, df in data.items():
        if not isinstance(df, pd.DataFrame):
            continue
            
        # Detect datetime columns or object columns with datetime/timestamp values
        cols_to_convert = []
        for col in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                cols_to_convert.append(col)
            elif df[col].dtype == object:
                # Check first few non-null elements
                non_nulls = df[col].dropna()
                if not non_nulls.empty:
                    first_val = non_nulls.iloc[0]
                    if isinstance(first_val, (datetime.date, datetime.datetime, datetime.time, pd.Timestamp)) or \
                       type(first_val).__name__ in ('Timestamp', 'date', 'datetime', 'time'):
                        cols_to_convert.append(col)
                        
        if cols_to_convert:
            print(f"  Table '{tbl}': converting columns {cols_to_convert}")
            for col in cols_to_convert:
                df[col] = df[col].apply(format_val)
            modified = True
            
    if modified:
        with open(path, "wb") as f:
            pickle.dump(data, f)
        print(f"  Successfully updated and saved {path}")
    else:
        print(f"  No datetime conversions needed for {path}")
    return True

def main():
    phases = ['fase_1', 'fase_2', 'fase_3', 'fase_4', 'fase_5']
    for phase in phases:
        if not os.path.exists(phase):
            continue
        for file in os.listdir(phase):
            if file.endswith(".pkl") and not file.startswith("mapping_"):
                path = os.path.join(phase, file)
                fix_pickle(path)

if __name__ == '__main__':
    main()
