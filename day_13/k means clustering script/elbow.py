import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data

# trying different values of k to find the best one
# not sure how many to try - going with 1 to 10
inertia_values = []
k_range = range(1, 11)

for k in k_range:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertia_values.append(model.inertia_)
    print(f"k={k} -> inertia: {model.inertia_:.2f}")

# plotting elbow curve
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia_values, marker='o', color='blue')
plt.title('elbow method - finding best k')
plt.xlabel('number of clusters (k)')
plt.ylabel('inertia')
plt.xticks(k_range)
plt.grid(True)
plt.tight_layout()
plt.savefig('elbow_curve.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("\nelbow curve saved as elbow_curve.png")

# i think the elbow point is where the curve bends
# for iris it should be around k=3
print("looking at the plot, elbow appears to be around k=3")