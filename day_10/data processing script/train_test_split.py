from sklearn.model_selection import train_test_split
import pandas as pd
df=pd.read_csv("data processing script/new_student_performance.csv")
x=df[["Age","Python","Mathematics","Statistics","Machine_Learning","Attendance","Program_AI","Program_DS","Program_SE"]]
y=df["Average_Score"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("Training Samples:",len(x_train))
print("Testing Samples:",len(x_test))