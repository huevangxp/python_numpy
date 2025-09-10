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
