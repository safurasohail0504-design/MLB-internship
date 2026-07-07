from sklearn.datasets import load_breast_cancer

# loading the dataset
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

print("dataset loaded")
print("total samples:", X.shape[0])
print("total features:", X.shape[1])
print("target names:", cancer.target_names)
print("feature names:", cancer.feature_names)