import pandas as pd

# 1. assign() → Create new columns dynamically

df = pd.DataFrame({"A": [1, 2, 3], "B": [10, 20, 30]})

# Add a new column without modifying original
df2 = df.assign(C=lambda x: x["A"] + x["B"])
print(df2)
