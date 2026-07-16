import pandas as pd
df=pd.read_csv("data cleaning script/student_performance.csv")
print(df)
print("no of missing values in each col:")
print(df.isnull().sum())