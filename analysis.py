import pandas as pd

df = pd.read_json("review-Massachusetts.json", lines=True)

print(df.shape)
print(df.columns.tolist())
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
