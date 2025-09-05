 
import matplotlib.pyplot as plt
import pandas as pd

# Cell 2 - Load Excel file
data = pd.read_excel('./file/user_account_payment.xlsx', sheet_name='Sheet1')
data.head()

# Cell 3 - Data analysis
print(data.columns)
print(data['accNo'])
print(data['accName'])
money = data[['accName','amount']]
print("sum money: ", "{:,.2f}".format(money['amount'].sum()))
print("top 5 money: ", money.nlargest(5, 'amount'))
money.nlargest(5, 'amount').plot(kind='bar', x='accName', y='amount', color='blue')
plt.show()
