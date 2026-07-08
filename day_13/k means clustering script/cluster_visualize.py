import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_

# using petal length and petal width for visualization
# i picked these two because they seem most useful for separating species
plt.figure(figsize=(8, 6))
colors = ['red', 'blue', 'green']

for cluster in range(3):
    # getting points belonging to this cluster
    mask = labels == cluster
    plt.scatter(
        X[mask, 2],      # petal length
        X[mask, 3],      # petal width
        c=colors[cluster],
        label=f'cluster {cluster}',
        alpha=0.7
    )

# plotting cluster centers
centers = kmeans.cluster_centers_
plt.scatter(
    centers[:, 2],
    centers[:, 3],
    c='black',
    marker='x',
    s=200,
    linewidths=3,
    label='centroids'
)

plt.title('kmeans clustering - iris dataset')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.legend()
plt.tight_layout()
plt.savefig('cluster_visualization.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("cluster visualization saved as cluster_visualization.png")