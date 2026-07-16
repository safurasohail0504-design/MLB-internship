import pandas as pd
df=pd.read_csv("data cleaning script/student_performance.csv")
print(df)
print("duplicated col:")
print(df.duplicated())
print("remove duplicate col:")
df=df.drop_duplicates()
print(df)