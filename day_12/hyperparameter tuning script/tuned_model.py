import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score, confusion_matrix)

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42)

param_grid = {
    'C'       : [0.01, 0.1, 1, 10, 100],
    'solver'  : ['lbfgs', 'liblinear'],
    'max_iter': [100, 500, 1000, 5000]
}

grid_search = GridSearchCV(
    LogisticRegression(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
tuned_pred = best_model.predict(X_test)
tuned_acc  = accuracy_score(y_test, tuned_pred)

print("tuned model evaluation")
print(f"accuracy : {tuned_acc:.4f}")
print(f"precision: {precision_score(y_test, tuned_pred):.4f}")
print(f"recall   : {recall_score(y_test, tuned_pred):.4f}")
print(f"f1 score : {f1_score(y_test, tuned_pred):.4f}")
print(f"misclassified: {int((1-tuned_acc)*len(y_test))}/{len(y_test)}")
print("\nconfusion matrix:")
print(confusion_matrix(y_test, tuned_pred))