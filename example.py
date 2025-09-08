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
df2 = pd.DataFrame({"key": ["A", "C", "D", "E"], "value": [1,4, 5, 6]})

# Instead of pd.merge(df1, df2, on="key")
print(df1.merge(df2, on="key"))

# 🔹 4. groupby() → Group and aggregate
df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Salary": [5000, 4000, 5500, 6000, 4200, 6100]
})

# Instead of df.groupby("Department")["Salary"].mean()
print(df.groupby("Employee")["Salary"].sum())

# 🔹 5. pivot_table() → Aggregate and summarize
df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Salary": [5000, 4000, 5500, 6000, 4200, 6100]
})

# Instead of df.pivot_table(values="Salary", index="Department", columns="Employee", aggfunc="sum")
print(df.pivot_table(values="Salary", index="Department", columns="Department", aggfunc="sum"))

# 🔹 6. pipe() → Chain operations

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["NY", "London", "Paris", "NY"]
})

# Instead of df[df["Age"] > 30].query("City == 'NY'")
print(df[(df["Age"] > 30) & (df["City"] == "NY")])

# 🔹 7. apply() → Custom functions
# Instead of df["Salary"].apply(lambda x: x * 1.1)
df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Salary": [5000, 4000, 5500, 6000, 4200, 6100]
})
print(df["Salary"].apply(lambda x: x * 1.1))
