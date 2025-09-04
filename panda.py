import pandas as pd

# Create a DataFrame
data = pd.read_excel('./file/user_account_payment.xlsx', sheet_name='Sheet1')

print(data.head(10))