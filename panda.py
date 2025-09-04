import pandas as pd

# Create a DataFrame
data = pd.read_excel('./file/user_account_payment.xlsx')
data = data.head(10)

print(data)