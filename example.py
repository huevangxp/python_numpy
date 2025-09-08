import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('./file/user_account_payment.xlsx', sheet_name='Sheet1')
data.head()

df = pd.DataFrame(data)
print(df)

print(df.columns)
print(df['accNo'])
print(df['accName'])
money = df[['accName','amount']]
print("sum money: ", "{:,.2f}".format(money['amount'].sum()))
print("top 5 money: ", money.nlargest(5, 'amount'))
money.nlargest(5, 'amount').plot(kind='bar', x='accName', y='amount', color='blue')
# check df money large 5 000 000
money_large_5_000_000 = money[money['amount'] > 5000000]
print("money large 5 000 000: ", money_large_5_000_000)
money_large_5_000_000.to_csv("output.csv", index=False)
plt.show()

