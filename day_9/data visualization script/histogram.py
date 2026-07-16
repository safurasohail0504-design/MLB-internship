import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("cleaned student performance/cleaned_student_performance.csv")
#plt.figure(figsize=(12,6))
plt.hist(df["Average_Score"])
plt.ylabel("No of students")
plt.xlabel("average score")
plt.title("distribution of average scores")
#plt.xticks(rotation=90)
#plt.xticks(fontsize=8)
#plt.tight_layout()
plt.savefig("histogram.png")
plt.show()