import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("cleaned student performance/cleaned_student_performance.csv")
plt.figure(figsize=(12,6))
plt.bar(df["Name"],df["Average_Score"])
plt.xlabel("students")
plt.ylabel("average score")
plt.title("average marks of students")
plt.xticks(rotation=90)
plt.xticks(fontsize=8)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()