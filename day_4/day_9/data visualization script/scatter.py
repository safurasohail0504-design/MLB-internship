import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("cleaned student performance/cleaned_student_performance.csv")
#plt.figure(figsize=(12,6))
plt.scatter(df["Python"],df["Machine_Learning"])
plt.ylabel("python marks")
plt.xlabel("ML marks")
plt.title("python vs ML")
#plt.xticks(rotation=90)
#plt.xticks(fontsize=8)
#plt.tight_layout()
plt.savefig("scatter.png")
plt.show()