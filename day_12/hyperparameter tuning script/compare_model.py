import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

cancer=load_breast_cancer()
X_train,X_test,y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42)

# baseline
baseline=LogisticRegression(max_iter=5000)
baseline.fit(X_train, y_train)
base_pred=baseline.predict(X_test)
base_acc=accuracy_score(y_test, base_pred)
base_f1=f1_score(y_test, base_pred)

# tuned
param_grid = {
    'C':[0.01, 0.1, 1, 10, 100],
    'solver':['lbfgs', 'liblinear'],
    'max_iter':[100, 500, 1000, 5000]
}
grid_search = GridSearchCV(
    LogisticRegression(), param_grid,
    cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
tuned_pred = best_model.predict(X_test)
tuned_acc  = accuracy_score(y_test, tuned_pred)
tuned_f1   = f1_score(y_test, tuned_pred)

print(" model comparison")
print(f"baseline accuracy: {base_acc:.4f}")
print(f"tuned accuracy: {tuned_acc:.4f}")
print(f"baseline f1 score : {base_f1:.4f}")
print(f"tuned f1 score: {tuned_f1:.4f}")

diff = tuned_acc - base_acc
if diff > 0:
    print(f"\nimprovement after tuning: +{diff:.4f}")
elif diff < 0:
    print(f"\ntuned model did worse: {diff:.4f}")
else:
    print("\nno change,baseline was already good enough")

# i added this to understand what changed
print("\nbaseline parameters: max_iter=5000, C=1 (default)")
print("best tuned parameters:", grid_search.best_params_)