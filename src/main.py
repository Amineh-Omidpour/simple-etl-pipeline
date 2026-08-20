import pandas as pd


# Extract
df = pd.read_csv("data/orders.csv")

print("Original data:")
print(df)


# Transform
df["total_amount"] = df["quantity"] * df["unit_price"]

# Data quality checks
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nTransformed data:")
print(df)


print("\nNumber of rows:", len(df))