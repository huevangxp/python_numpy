import pandas as pd

# Create a DataFrame
data = pd.read_excel('./file/user_account_payment.xlsx', sheet_name='Sheet1')

print(data.columns)

print(data['accNo'])

print(data['accName'])

money = data['accName','amount']

# sum money add format currency

print("sum money: ", "{:,.2f}".format(money.sum()))

# show me top 5 money 
print("top 5 money: ", money.nlargest(5))



