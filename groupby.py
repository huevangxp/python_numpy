import pandas as pd

data = pd.read_excel("./file/user_account_payment.xlsx", sheet_name="Sheet1")

# print(data.head())

# find top 5 money
userTopMoney = data.nlargest(5, 'amount')
print(userTopMoney)

# find bottom 5 money
userBottomMoney = data.nsmallest(5, 'amount')
print(userBottomMoney)

# group by accName
groupByAccName = data.groupby('accName')
print(groupByAccName)
print(groupByAccName.size())

# find top 5 money by accName
print(groupByAccName.nlargest(5, 'amount'))
print(groupByAccName.nsmallest(5, 'amount'))

# find top 5 money by accName and sum
print(groupByAccName.sum().nlargest(5, 'amount'))
print(groupByAccName.sum().nsmallest(5, 'amount'))

