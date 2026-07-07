import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score, confusion_matrix)

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# i think these are the right metrics
acc = accuracy_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1  = f1_score(y_test, y_pred)
cm  = confusion_matrix(y_test, y_pred)

print("baseline model evaluation")
print(f"accuracy : {acc:.4f}")
print(f"precision: {pre:.4f}")
print(f"recall   : {rec:.4f}")
print(f"f1 score : {f1:.4f}")
print(f"misclassified: {int((1-acc)*len(y_test))}/{len(y_test)}")
print("\nconfusion matrix:")
print(cm)