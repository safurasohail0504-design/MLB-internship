import pandas as pd
df=pd.read_csv("data processing script/student_performance.csv")
rows=df.head(5)
print(rows)
inform=df.info()
print(inform)
col=df.columns
print(col)