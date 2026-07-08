import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# loading data
iris = load_iris()
X = iris.data

# i know iris has 3 species so using k=3
# but normally we wouldnt know this in real unsupervised problems
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# getting cluster labels
labels = kmeans.labels_
print("cluster labels:", labels)

# adding labels to dataframe
df = pd.DataFrame(X, columns=iris.feature_names)
df['cluster'] = labels

print("\ncluster distribution:")
print(df['cluster'].value_counts())

# i added this to see cluster centers
print("\ncluster centers:")
print(kmeans.cluster_centers_)

# inertia tells how tight the clusters are
# lower inertia means tighter clusters i think
print("\ninertia:", kmeans.inertia_)

print("\nfirst 10 rows with cluster labels:")
print(df.head(10))