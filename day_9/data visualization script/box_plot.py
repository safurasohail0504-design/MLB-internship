import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("cleaned student performance/cleaned_student_performance.csv")
subj=df[["Python","Mathematics","Statistics","Machine_Learning"]]
plt.boxplot(subj)
plt.xticks([1,2,3,4],["Python","Math","Statistics","ML"])
plt.ylabel("marks")
plt.title("marks distribution")
plt.savefig("box_plot.png")
plt.show()