import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Salary": [5000, 4000, 5500, 6000, 4200, 6100]
}

df = pd.DataFrame(data)

# Average salary by department
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

# Apply a custom function (e.g., max - min salary per department)
# salary_range = df.groupby("Department")["Salary"].apply(lambda x: x.max() - x.min())
# print(salary_range)

# Group by multiple columns
df_grouped = df.groupby(["Department", "Employee"])["Salary"].sum()
print(df_grouped)

# Group by with aggregation functions
df_grouped = df.groupby("Department")["Salary"].agg([
    ("mean_salary", "mean"),
    ("max_salary", "max"),
    ("min_salary", "min")
])

# Group by with pivot table
df_pivot = df.pivot_table(values="Salary", index="Department", columns="Employee", aggfunc="sum")
print(df_pivot)

print(df_grouped)

# Group by with pipe
df_grouped = df.groupby("Department").pipe(lambda x: x["Salary"].mean())
print(df_grouped)

# SUM salary by department
df_grouped = df.groupby("Department")["Salary"].sum()
print(df_grouped)

# SUM salary by employee
df_grouped = df.groupby("Employee")["Salary"].sum()
print(df_grouped)

# SUM salary by department and employee
df_grouped = df.groupby(["Department", "Employee"])["Salary"].sum()
print(df_grouped)
