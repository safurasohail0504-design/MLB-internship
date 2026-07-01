import pandas as pd
df=pd.read_csv("sales_data.csv")
print(df.isnull())
print("no of missing values:")
print(df.isnull().sum())