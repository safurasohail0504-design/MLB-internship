import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data
y = iris.target

# scaling first
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# pca
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# kmeans on original data
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
cluster_labels = kmeans.labels_

# side by side comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
colors = ['red', 'blue', 'green']

# left plot - kmeans clusters on pca axes
for cluster in range(3):
    mask = cluster_labels == cluster
    axes[0].scatter(
        X_pca[mask, 0],
        X_pca[mask, 1],
        c=colors[cluster],
        label=f'cluster {cluster}',
        alpha=0.7
    )
axes[0].set_title('kmeans clusters (on pca axes)')
axes[0].set_xlabel('PC1')
axes[0].set_ylabel('PC2')
axes[0].legend()

# right plot - actual labels on pca axes
for i, species in enumerate(iris.target_names):
    mask = y == i
    axes[1].scatter(
        X_pca[mask, 0],
        X_pca[mask, 1],
        c=colors[i],
        label=species,
        alpha=0.7
    )
axes[1].set_title('actual species (on pca axes)')
axes[1].set_xlabel('PC1')
axes[1].set_ylabel('PC2')
axes[1].legend()

plt.suptitle('pca vs clustering comparison', fontsize=13)
plt.tight_layout()
plt.savefig('pca_vs_clustering.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("comparison plot saved as pca_vs_clustering.png")

# i added this observation at the end
print("\nobservation:")
print("kmeans clusters and actual species boundaries look similar")
print("this means kmeans found meaningful groups without using labels")
print("small mismatches expected since kmeans doesnt know true labels")