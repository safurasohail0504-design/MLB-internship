Day 13: Clustering and Dimensionality Reduction

What is Clustering

Clustering is an unsupervised machine learning technique where the goal is to group similar data points together without using any labels. Unlike supervised learning where the model learns from labeled examples, clustering finds hidden patterns and natural groupings in the data on its own. For example in this project the model was given 150 flower measurements with no information about which species they belong to, and it had to figure out the groups by itself based on how similar the measurements were to each other. Clustering is widely used in real world applications like customer segmentation, anomaly detection, recommendation systems, and image compression.

What is PCA

PCA stands for Principal Component Analysis. It is a dimensionality reduction technique that takes high dimensional data and compresses it into fewer dimensions while keeping as much useful information as possible. In this project the Iris dataset had 4 features which makes it impossible to visualize directly on a 2D plot. PCA reduced those 4 features into 2 principal components so the data could be plotted and understood visually. Each principal component is a new axis that captures the direction of maximum variance in the data. The first component captures the most variance, the second captures the next most, and so on. Scaling the data before applying PCA is important because PCA is sensitive to the scale of features.

How I Determined the Best Value of K

I used the Elbow Method to find the optimal number of clusters. This works by running KMeans for different values of K from 1 to 10 and recording the inertia for each. Inertia measures how tightly packed the clusters are — lower inertia means the data points are closer to their cluster centers. When plotted, the inertia drops sharply at first and then starts to flatten out. The point where the curve bends like an elbow is the best value of K because adding more clusters after that point does not significantly improve the tightness of clusters. For the Iris dataset the elbow appeared at K equals 3, which also makes sense because the dataset actually contains 3 flower species. This confirmed that K equals 3 was the right choice.

Insights Gained from the Visualizations

The original data plot using petal length and petal width showed that setosa is very clearly separated from the other two species. Versicolor and virginica are closer to each other and overlap slightly which makes them harder to distinguish.

The KMeans clustering plot showed that the model successfully found 3 distinct groups without knowing the actual species labels. Cluster 0 matched setosa almost perfectly. Clusters 1 and 2 matched versicolor and virginica reasonably well but had some overlap at the boundary between them. This matches what we saw in the original data plot — those two species are naturally similar in measurements.

The PCA visualization reduced the 4 features into 2 principal components that together retained more than 95 percent of the total variance in the data. This means very little information was lost during the reduction. The 2D PCA plot made it much easier to see the separation between species and clusters visually. Setosa was completely separated from the other two while versicolor and virginica showed some overlap in the middle region.

The side by side comparison of KMeans clusters and actual species on the PCA axes showed that the cluster boundaries found by KMeans were very close to the real species boundaries. The main source of confusion was between versicolor and virginica which have overlapping feature ranges. Overall this project showed that KMeans can discover meaningful structure in data even without any labels, and PCA is a powerful tool for making high dimensional data understandable through visualization.
