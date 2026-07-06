from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3)
model = LogisticRegression(max_iter=50)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Predictions:", y_pred)
print("Actual :", y_test)
print("\nSample Predictions (first 10):")
print(f"{'Actual':<20} {'Predicted':<20} {'Correct?'}")
print("-" * 50)
for i in range(10):
    actual = iris.target_names[y_test[i]]
    predicted = iris.target_names[y_pred[i]]
    correct = "Yes" if y_test[i] == y_pred[i] else "No"
    print(f"{actual:<20} {predicted:<20} {correct}")