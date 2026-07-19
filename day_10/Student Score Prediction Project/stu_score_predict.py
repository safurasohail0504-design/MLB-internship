from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
df=pd.read_csv("data processing script/new_student_performance.csv")
df["Average_Score"]=(df["Python"]+df["Mathematics"]+df["Statistics"]+df["Machine_Learning"])/4
x=df[["Age","Python","Mathematics","Statistics","Machine_Learning","Attendance","Program_AI","Program_DS","Program_SE"]]
y=df["Average_Score"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
model=LinearRegression()
model.fit(x_train,y_train)
prediction=model.predict(x_test)
comparison=pd.DataFrame({"actual":y_test,"predicted":prediction})
print(comparison)
mae=mean_absolute_error(y_test,prediction)
mse=mean_squared_error(y_test,prediction)
r2=r2_score(y_test,prediction)
print("MAE:",mae)
print("MSE:",mse)
print("R2 Score:",r2)
plt.figure(figsize=(6,6))
plt.scatter(y_test,prediction)
plt.xlabel("Actual Average Score")
plt.ylabel("Predicted Average Score")
plt.title("Actual vs Predicted Scores")
plt.savefig("generated graphs/actual_vs_predicted.png")
plt.show()