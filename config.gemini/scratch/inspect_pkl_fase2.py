import pickle
import pandas as pd

with open("fase_2/fase_2_afrida.pkl", "rb") as f:
    data = pickle.load(f)

print("Keys in pickle:")
print(data.keys())

df_param = data.get("parameter_nilai")
if df_param is not None:
    print("\nDataFrame parameter_nilai info:")
    print(df_param.info())
    print("\nDataFrame parameter_nilai columns:")
    print(df_param.columns)
    print("\nDataFrame parameter_nilai head:")
    print(df_param.head(10))
    
    # Check if there is an idp_nilai in data
    # (Since it was renamed in some steps, let's see)
else:
    print("\nparameter_nilai not found in pickle!")
