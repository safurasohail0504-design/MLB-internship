import pandas as pd
df=pd.read_csv("data cleaning script/student_performance.csv")
print("new col:average score:")
df["Average_Score"]=(df["Python"]+df["Mathematics"]+df["Statistics"]+df["Machine_Learning"])/4
print(df)
df.to_csv("data cleaning script/cleaned_student_performance.csv", index=False)