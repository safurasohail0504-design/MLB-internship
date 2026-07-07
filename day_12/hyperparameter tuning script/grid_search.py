import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42)

# these are the parameters i want to try
# not sure if i should add more values
param_grid = {
    'C'       : [0.01, 0.1, 1, 10, 100],
    'solver'  : ['lbfgs', 'liblinear'],
    'max_iter': [100, 500, 1000, 5000]
}

# cv=5 means 5 fold cross validation i think
grid_search = GridSearchCV(
    LogisticRegression(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

print("running grid search")
grid_search.fit(X_train, y_train)

print("\nbest parameters found:")
print(grid_search.best_params_)
print(f"\nbest cross validation score: {grid_search.best_score_:.4f}")

# i added this to see how many combinations were tried
print(f"\ntotal combinations tried: {len(grid_search.cv_results_['params'])}")