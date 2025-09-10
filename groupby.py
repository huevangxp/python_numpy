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

# find top 5 money by accName and mean
print(groupByAccName.mean().nlargest(5, 'amount'))
print(groupByAccName.mean().nsmallest(5, 'amount'))

# find top 5 money by accName and max
print(groupByAccName.max().nlargest(5, 'amount'))
print(groupByAccName.max().nsmallest(5, 'amount'))

# find top 5 money by accName and min
print(groupByAccName.min().nlargest(5, 'amount'))
print(groupByAccName.min().nsmallest(5, 'amount'))

# find top 5 money by accName and count
print(groupByAccName.count().nlargest(5, 'amount'))
print(groupByAccName.count().nsmallest(5, 'amount'))

# find top 5 money by accName and std
print(groupByAccName.std().nlargest(5, 'amount'))
print(groupByAccName.std().nsmallest(5, 'amount'))

# find top 5 money by accName and var
print(groupByAccName.var().nlargest(5, 'amount'))
print(groupByAccName.var().nsmallest(5, 'amount'))

# find top 5 money by accName and median
print(groupByAccName.median().nlargest(5, 'amount'))
print(groupByAccName.median().nsmallest(5, 'amount'))

# find top 5 money by accName and corr
print(groupByAccName.corr().nlargest(5, 'amount'))
print(groupByAccName.corr().nsmallest(5, 'amount'))

# find top 5 money by accName and cov
print(groupByAccName.cov().nlargest(5, 'amount'))
print(groupByAccName.cov().nsmallest(5, 'amount'))

# find top 5 money by accName and describe
print(groupByAccName.describe().nlargest(5, 'amount'))
print(groupByAccName.describe().nsmallest(5, 'amount'))

# find top 5 money by accName and apply
print(groupByAccName.apply(lambda x: x['amount'].sum()).nlargest(5, 'amount'))
print(groupByAccName.apply(lambda x: x['amount'].sum()).nsmallest(5, 'amount'))

# find top 5 money by accName and pipe
print(groupByAccName.pipe(lambda x: x['amount'].sum()).nlargest(5, 'amount'))
print(groupByAccName.pipe(lambda x: x['amount'].sum()).nsmallest(5, 'amount'))

