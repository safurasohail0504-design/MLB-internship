from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)  
print("Data split")
print("Total samples :", len(X))
print("Training samples :", X_train.shape[0])
print("Testing samples :", X_test.shape[0])