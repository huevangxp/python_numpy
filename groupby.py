import pandas as pd

data = pd.read_excel("./file/user_account_payment.xlsx", sheet_name="Sheet1")

# print(data.head())

# find top 5 money
userTopMoney = data.nlargest(5, 'amount')
print(userTopMoney)

# find bottom 5 money
userBottomMoney = data.nsmallest(5, 'amount')
print(userBottomMoney)
 

df = data.groupby('accName').sum()
print(df) # find top 5 money by accName
print(df.nlargest(5, 'amount'))
print(df.nsmallest(5, 'amount'))

# find top 5 money by accName and mean
print(df.mean().nlargest(5, 'amount'))
print(df.mean().nsmallest(5, 'amount'))

# find top 5 money by accName and max
print(df.max().nlargest(5, 'amount'))
print(df.max().nsmallest(5, 'amount'))

# find top 5 money by accName and min
print(df.min().nlargest(5, 'amount'))
print(df.min().nsmallest(5, 'amount'))

# find top 5 money by accName and count
print(df.count().nlargest(5, 'amount'))
print(df.count().nsmallest(5, 'amount'))

# find top 5 money by accName and std
print(df.std().nlargest(5, 'amount'))
print(df.std().nsmallest(5, 'amount'))

# find top 5 money by accName and var
print(df.var().nlargest(5, 'amount'))
print(df.var().nsmallest(5, 'amount'))
