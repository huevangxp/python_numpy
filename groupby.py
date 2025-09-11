import pandas as pd

data = pd.read_excel("./file/user_account_payment.xlsx", sheet_name="Sheet1")

# print(data.head())

# find top 5 money
userTopMoney = data.nlargest(5, 'amount')
print(userTopMoney)

# find bottom 5 money
userBottomMoney = data.nsmallest(5, 'amount')
print(userBottomMoney)
 

# find top 5 money by accName and sort_values
print(data.sort_values(by='amount', ascending=False).nlargest(5, 'amount'))
print(data.sort_values(by='amount', ascending=True).nsmallest(5, 'amount'))
