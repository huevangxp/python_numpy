import pandas as pd

data = pd.read_excel('./file/user_account_payment.xlsx', sheet_name='Sheet1')
data.head()

df = pd.DataFrame(data)
print(df)
