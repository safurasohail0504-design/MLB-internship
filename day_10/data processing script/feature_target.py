import pandas as pd
df=pd.read_csv("data processing script/new_student_performance.csv")
x=df[["Age","Python","Mathematics","Statistics","Machine_Learning","Attendance","Program_AI","Program_DS","Program_SE"]]
y=df["Average_Score"]
print("features:")
print(x.head())
print("target:")
print(y.head())