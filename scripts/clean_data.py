import pandas as pd
from pathlib import Path

# read raw data
df = pd.read_csv("data/raw/data.csv", encoding="ISO-8859-1")

# basic cleaning
df = df.copy()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df = df[df["CustomerID"].notna()]
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# create revenue column
df["revenue"] = df["Quantity"] * df["UnitPrice"]

# cast customer id to nullable integer
df["CustomerID"] = df["CustomerID"].astype("Int64")

# create output folder
Path("data/processed").mkdir(parents=True, exist_ok=True)

# save cleaned data
df.to_csv("data/processed/cleaned_retail_data.csv", index=False)

# quick checks
print(df.head())
print(df.shape)
print(df.dtypes)
print(df["revenue"].describe())
print("Saved to data/processed/cleaned_retail_data.csv")
