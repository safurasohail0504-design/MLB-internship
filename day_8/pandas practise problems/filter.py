import pandas as pd
df=pd.read_csv("sales_data.csv")
print(df[df["total_amount"] > 1500])
print(df[df["region"] == "Lahore"])