import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data
y = iris.target

# scaling before pca - i think this is important
# pca is affected by scale so need to standardize first
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# reducing to 2 components so we can visualize on 2d plot
# original data had 4 features, now reducing to 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("original shape:", X.shape)
print("pca shape     :", X_pca.shape)

# how much variance each component explains
print("\nvariance explained by each component:")
print(pca.explained_variance_ratio_)

# i added this to see total variance retained
total_variance = sum(pca.explained_variance_ratio_)
print(f"\ntotal variance retained: {total_variance*100:.2f}%")
print("not sure if this is good enough or if i need more components")

# converting to dataframe
df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df_pca['target'] = y

print("\nfirst 5 rows after pca:")
print(df_pca.head())

# plotting pca result with actual labels
plt.figure(figsize=(8, 6))
colors = ['red', 'blue', 'green']
for i, species in enumerate(iris.target_names):
    mask = y == i
    plt.scatter(
        X_pca[mask, 0],
        X_pca[mask, 1],
        c=colors[i],
        label=species,
        alpha=0.7
    )

plt.title('pca visualization - iris dataset')
plt.xlabel('principal component 1')
plt.ylabel('principal component 2')
plt.legend()
plt.tight_layout()
plt.savefig('pca_visualization.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("\npca visualization saved as pca_visualization.png")