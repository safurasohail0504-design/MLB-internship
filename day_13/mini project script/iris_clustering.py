import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
iris = load_iris()
X = iris.data
y = iris.target
print("dataset loaded")
print("samples :", X.shape[0])
print("features:", X.shape[1])
print("classes :", iris.target_names)
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
print("\nfirst 5 rows:")
print(df.head())
print("\nclass distribution:")
print(df['target'].value_counts())
print("\nmissing values:", df.isnull().sum().sum())
print("\nbasic statistics:")
print(df.describe())
print("\nnote: target column not used in clustering")
print("\nrunning elbow method")
inertia_values=[]
k_range=range(1,11)
for k in k_range:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertia_values.append(model.inertia_)
    print(f"k={k} -> inertia:{model.inertia_:.2f}")
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia_values, marker='o', color='blue')
plt.title('elbow method,finding best k')
plt.xlabel('number of clusters (k)')
plt.ylabel('inertia')
plt.xticks(k_range)
plt.grid(True)
plt.tight_layout()
plt.savefig('elbow_curve.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("\nelbow curve saved")
print("looking at the plot, elbow bends around k=3")
print("this makes sense since iris has 3 species")
print("\napplying kmeans with k=3")
kmeans=KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels=kmeans.labels_
df['cluster']=labels
print("cluster distribution:")
print(df['cluster'].value_counts())
print("\ncluster centers:")
print(kmeans.cluster_centers_)
print(f"\ninertia:{kmeans.inertia_:.2f}")
plt.figure(figsize=(8, 6))
colors_actual = ['red','blue','green']
for i, species in enumerate(iris.target_names):
    mask=y==i
    plt.scatter(
        X[mask, 2],X[mask, 3],
        c=colors_actual[i],label=species,alpha=0.7
    )
plt.title('original data - actual species')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.legend()
plt.tight_layout()
plt.savefig('original_data.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("\noriginal data plot saved")
plt.figure(figsize=(8, 6))
colors_cluster = ['orange','purple','cyan']
for cluster in range(3):
    mask=labels==cluster
    plt.scatter(
        X[mask,2],X[mask,3],
        c=colors_cluster[cluster],label=f'cluster {cluster}',alpha=0.7
    )
centers=kmeans.cluster_centers_
plt.scatter(
    centers[:,2],centers[:,3],
    c='black',marker='x',s=200,
    linewidths=3,label='centroids'
)
plt.title('kmeans clusters,iris dataset')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.legend()
plt.tight_layout()
plt.savefig('kmeans_clusters.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("kmeans cluster plot saved")
print("\napplying pca")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print("original shape:", X.shape)
print("reduced shape :", X_pca.shape)
print("\nvariance explained:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"PC{i+1}:{var*100:.2f}%")
total_var = sum(pca.explained_variance_ratio_)
print(f"total variance retained:{total_var*100:.2f}%")
if total_var >= 0.90:
    print("good - more than 90% variance retained")
else:
    print("might need more components to retain more variance")
plt.figure(figsize=(8, 6))
for i, species in enumerate(iris.target_names):
    mask=y==i
    plt.scatter(
        X_pca[mask,0],X_pca[mask,1],
        c=colors_actual[i],label=species,alpha=0.7
    )
plt.title('pca visualization ,actual species')
plt.xlabel('principal component 1')
plt.ylabel('principal component 2')
plt.legend()
plt.tight_layout()
plt.savefig('pca_visualization.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("\npca visualization saved")
fig, axes=plt.subplots(1,2,figsize=(14,6))
for cluster in range(3):
    mask=labels==cluster
    axes[0].scatter(
        X_pca[mask, 0],X_pca[mask, 1],
        c=colors_cluster[cluster],label=f'cluster {cluster}',alpha=0.7
    )
axes[0].set_title('kmeans clusters (pca axes)')
axes[0].set_xlabel('PC1')
axes[0].set_ylabel('PC2')
axes[0].legend()
for i, species in enumerate(iris.target_names):
    mask=y==i
    axes[1].scatter(
        X_pca[mask, 0],X_pca[mask, 1],
        c=colors_actual[i],label=species,alpha=0.7
    )
axes[1].set_title('actual species (pca axes)')
axes[1].set_xlabel('PC1')
axes[1].set_ylabel('PC2')
axes[1].legend()
plt.suptitle('kmeans clusters vs actual species on pca axes', fontsize=13)
plt.tight_layout()
plt.savefig('pca_vs_clustering.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("comparison plot saved")
print("\nobservations: ")
print("clusters formed : 3")
print("elbow point : k=3")
print("total variance kept:{:.2f}%".format(total_var*100))
print("\ncluster 0 size:",(labels==0).sum())
print("cluster 1 size:",(labels==1).sum())
print("cluster 2 size:",(labels==2).sum())
print("\nkmeans found 3 natural groups without using species labels")
print("cluster boundaries match actual species fairly well")
print("main confusion between versicolor and virginica - similar features")
print("pca helped reduce 4 features to 2 while keeping most information")
print("2d pca plot makes it easier to see cluster separation visually")