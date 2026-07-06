from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3)
model = LogisticRegression(max_iter=50)
model.fit(X_train, y_train)
print("Model trained")
print("solver :", model.solver)
print("max_iter :", model.max_iter)
print("C (regularization):", model.C)