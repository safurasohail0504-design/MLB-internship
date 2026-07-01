import pandas as pd
df=pd.read_csv("sales_data.csv")
print(df[["quantity", "unit_price", "total_amount"]].describe())