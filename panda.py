import pandas as pd

# Create a DataFrame
data = pd.read_excel('./file/user_account_payment.xlsx', sheet_name='Sheet1')

print(data.columns)

print(data['accNo'])

print(data['accName'])

money = data[['accName','amount']]

# sum money add format currency

print("sum money: ", "{:,.2f}".format(money['amount'].sum()))

# show me top 5 money format currency
print("top 5 money: ", money.nlargest(5, 'amount'))

#show me to chart top 5 money with matplotlib

money.nlargest(5, 'amount').plot(kind='bar')
plt.show()






