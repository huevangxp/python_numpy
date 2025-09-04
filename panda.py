import pandas as pd

# Create a DataFrame
data = pd.read_excel('./file/user_account_payment.xlsx')
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
