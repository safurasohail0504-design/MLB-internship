from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score, confusion_matrix)
import warnings
warnings.filterwarnings('ignore')
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3)
model = LogisticRegression(max_iter=50)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall    = recall_score(y_test, y_pred, average='weighted')
f1        = f1_score(y_test, y_pred, average='weighted')
cm        = confusion_matrix(y_test, y_pred)
print("Model Evaluation ")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print("\nConfusion Matrix:")
print(cm)
print("\nInterpretation:")
misclassified = int((1 - accuracy) * len(y_test))
print(f"Misclassified: {misclassified}/{len(y_test)} samples")
if accuracy >= 0.90:
    print("Performance:good,not perfect")
elif accuracy >= 0.75:
    print("Performance: decent,room for improvement")
else:
    print("Performance: poor,needs tuning")
if misclassified == 0:
    print("No errors,likely overfitting, check with new data")
else:
    print(f"Small errors present,model generalizing reasonably well")