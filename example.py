import pandas as pd

# 1. assign() → Create new columns dynamically

df = pd.DataFrame({"A": [1, 2, 3], "B": [10, 20, 30]})

# Add a new column without modifying original
df2 = df.assign(C=lambda x: x["A"] + x["B"])
print(df2)

# 🔹 2. query() → Filter with SQL-like syntax
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["NY", "London", "Paris", "NY"]
})

# Instead of df[df["Age"] > 30]
print(df.query("Age > 30 and City == 'NY'"))

# 🔹 3. merge() → Join DataFrames
df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": [0,1, 2, 3]})
df2 = pd.DataFrame({"key": ["B", "C", "D", "E"], "value": [1,4, 5, 6]})

# Instead of pd.merge(df1, df2, on="key")
print(df1.merge(df2, on="key"))
