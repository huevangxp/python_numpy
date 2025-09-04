import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'James', 'Linda'],
    'Age': [28, 22, 35, 32],
    'City': ['New York', 'Paris', 'London', 'Berlin']
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
