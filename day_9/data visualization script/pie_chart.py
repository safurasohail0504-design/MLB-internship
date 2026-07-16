import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("cleaned student performance/cleaned_student_performance.csv")
performance=df["performance"].value_counts()
plt.pie(performance,labels=performance.index,autopct="%1.1f%%")
plt.title("student performance distribution")
#plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()