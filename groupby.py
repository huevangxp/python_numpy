import pandas as pd

data = pd.read_excel("./file/user_account_payment.xlsx", sheet_name="Sheet1")

print(data.head())

# add bonus to money large than 5000000
bonus = data[data['amount'] >= 5000000]['amount'] = data['amount'] * 1.1

print(bonus)