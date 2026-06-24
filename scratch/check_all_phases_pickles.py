import os
import pandas as pd

phases = ['fase_3', 'fase_4', 'fase_5']
people = ['cimut', 'afrida', 'hanif']

print("--- ANALYZING ALL PICKLES IN ALL PHASES ---")

for phase in phases:
    print(f"\n==================== {phase.upper()} ====================")
    table_owners = {}
    for person in people:
        path = f"{phase}/{phase}_{person}.pkl"
        if os.path.exists(path):
            try:
                data = pd.read_pickle(path)
                if isinstance(data, dict):
                    print(f"\n* {person.upper()} ({path}):")
                    for k, df in data.items():
                        if isinstance(df, pd.DataFrame):
                            print(f"  - {k}: {df.shape[0]} rows")
                            if k not in table_owners:
                                table_owners[k] = []
                            table_owners[k].append(person)
                        else:
                            print(f"  - {k}: type={type(df)}")
                else:
                    print(f"\n* {person.upper()} ({path}): Not a dict (type={type(data)})")
            except Exception as e:
                print(f"\n* {person.upper()} ({path}): Error loading: {e}")
        else:
            print(f"\n* {person.upper()} ({path}): File does not exist")
            
    print(f"\n--- OVERLAPPING TABLES IN {phase.upper()} ---")
    overlaps = {k: v for k, v in table_owners.items() if len(v) > 1}
    if overlaps:
        for k, v in overlaps.items():
            print(f"  [WARN] Table '{k}' is exported by multiple people: {v}")
    else:
        print(f"  [OK] No overlapping tables in this phase.")
