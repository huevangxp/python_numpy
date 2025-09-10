import pandas as pd

data = pd.read_excel("./file/user_account_payment.xlsx", sheet_name="Sheet1")

# print(data.head())

# find top 5 money
print(data.nlargest(5, 'amount'))

# find bottom 5 money
print(data.nsmallest(5, 'amount'))
