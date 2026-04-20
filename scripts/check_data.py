import pandas as pd

df = pd.read_csv("data/raw/data.csv", encoding="ISO-8859-1")

print(df.head())
print(df.columns.tolist())
print(df.shape)
print(df.dtypes)
