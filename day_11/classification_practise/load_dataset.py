from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
X = iris.data
y = iris.target
print("dataset loaded")
print("features:", iris.feature_names)
print("target classes:", iris.target_names)
print("shape:", X.shape)