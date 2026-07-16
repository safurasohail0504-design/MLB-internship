import pandas as pd
df=pd.read_csv("data cleaning script/student_performance.csv")
print(df)
print(df.columns)
print("rename col name:Machine_Learning to ML:")
df=df.rename(columns={"Machine_Learning":"ML"})
print(df)
df.to_csv("data cleaning script/cleaned_student_performance.csv", index=False)