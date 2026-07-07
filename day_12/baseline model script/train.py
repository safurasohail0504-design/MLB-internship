import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42)

# training model - not sure about max_iter value
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

print("model trained")
print("model type:", type(model).__name__)
print("max iterations:", model.max_iter)
print("solver used:", model.solver)

# i added this to see what classes model learned
print("classes:", model.classes_)