import pandas as pd
df=pd.read_csv("data cleaning script/student_performance_average.csv")
print("new col:performance:")
performance=[]
for average in df["Average_Score"]:
    if(average >= 90):
        performance.append("excellent")
    elif(average>=80):
        performance.append("good")
    elif(average>=70):
        performance.append("average")
    else:
        performance.append("improve")
df["performance"]=performance
print(df)

df.to_csv("data cleaning script/cleaned_student_performance.csv", index=False)
