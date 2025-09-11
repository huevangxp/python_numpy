import pandas as pd

data = pd.read_excel("./file/user_account_payment.xlsx", sheet_name="Sheet1")

# print(data.head())

# find top 5 money
userTopMoney = data.nlargest(5, 'amount')
print(userTopMoney)

# find bottom 5 money
userBottomMoney = data.nsmallest(5, 'amount')
print(userBottomMoney)
 

print(df.count().nsmallest(5, 'amount'))

# find top 5 money by accName and std
print(df.std().nlargest(5, 'amount'))
print(df.std().nsmallest(5, 'amount'))

# find top 5 money by accName and var
print(df.var().nlargest(5, 'amount'))
print(df.var().nsmallest(5, 'amount'))

# find top 5 money by accName and median
print(df.median().nlargest(5, 'amount'))
print(df.median().nsmallest(5, 'amount'))

# find top 5 money by accName and corr
print(df.corr().nlargest(5, 'amount'))
print(df.corr().nsmallest(5, 'amount'))

# find top 5 money by accName and cov
print(df.cov().nlargest(5, 'amount'))
print(df.cov().nsmallest(5, 'amount'))

# find top 5 money by accName and describe
print(df.describe().nlargest(5, 'amount'))
print(df.describe().nsmallest(5, 'amount'))

# find top 5 money by accName and apply
print(df.apply(lambda x: x['amount'].sum()).nlargest(5, 'amount'))
print(df.apply(lambda x: x['amount'].sum()).nsmallest(5, 'amount'))

# find top 5 money by accName and pipe
print(df.pipe(lambda x: x['amount'].sum()).nlargest(5, 'amount'))
print(df.pipe(lambda x: x['amount'].sum()).nsmallest(5, 'amount'))

# find top 5 money by accName and sort_values
print(df.sort_values(by='amount', ascending=False).nlargest(5, 'amount'))
print(df.sort_values(by='amount', ascending=True).nsmallest(5, 'amount'))
