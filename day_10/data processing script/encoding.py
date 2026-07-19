import pandas as pd
df=pd.read_csv("data processing script/new_student_performance.csv")
test=df.dtypes
print(test)
df=pd.get_dummies(df,columns=["Program"])
print(df.head())
df.to_csv("data processing script/new_student_performance.csv",index=False)