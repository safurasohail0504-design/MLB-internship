import pandas as pd
df=pd.read_csv("data processing script/student_performance.csv")
df["Average_Score"]=(df["Python"]+df["Mathematics"]+df["Statistics"]+df["Machine_Learning"])/4
print(df)
df.to_csv("data processing script/new_student_performance.csv",index=False)