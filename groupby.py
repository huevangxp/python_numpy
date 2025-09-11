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