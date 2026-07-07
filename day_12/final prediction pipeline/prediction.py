import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score,
 recall_score, f1_score, confusion_matrix)

cancer = load_breast_cancer()
X=cancer.data
y=cancer.target
print("dataset loaded")
print("samples:", X.shape[0])
print("features:", X.shape[1])
print("classes:", cancer.target_names)
df = pd.DataFrame(X, columns=cancer.feature_names)
df['target'] = y
print("\nfirst 5 rows:")
print(df.head())
print("\nclass distribution:")
print(df['target'].value_counts())
print("\nmalignant samples:",(y==0).sum())
print("benign samples   :",(y==1).sum())
print("\nmissing values:", df.isnull().sum().sum())
print("\nbasic statistics:")
print(df.describe())

X_train,X_test,y_train,y_test=train_test_split(
X, y, test_size=0.2)

print("\ntraining samples:",X_train.shape[0])
print("testing samples :",X_test.shape[0])
scaler = StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
print("scaling done")
baseline = LogisticRegression(max_iter=100)
baseline.fit(X_train_scaled, y_train)
base_pred = baseline.predict(X_test_scaled)
base_acc  = accuracy_score(y_test, base_pred)

print("\nbaseline model")
print(f"accuracy:{base_acc:.4f}")
print(f"precision:{precision_score(y_test, base_pred):.4f}")
print(f"recall:{recall_score(y_test, base_pred):.4f}")
print(f"f1 score :{f1_score(y_test, base_pred):.4f}")
print(f"misclassified: {int((1-base_acc)*len(y_test))}/{len(y_test)}")
print("\nconfusion matrix:")
print(confusion_matrix(y_test,base_pred))

train_pred_base=baseline.predict(X_train_scaled)
train_acc_base=accuracy_score(y_train, train_pred_base)
print(f"\ntraining accuracy:{train_acc_base:.4f}")
print(f"testing accuracy:{base_acc:.4f}")
if train_acc_base - base_acc > 0.05:
    print("note: possible overfitting as train acc much higher than test")
else:
    print("train and test accuracy close")
param_grid = {
    'C':[0.01, 0.1, 1, 10],
    'solver':['lbfgs', 'liblinear'],
    'max_iter':[100, 200, 500]
}
print("\nstarting gridsearch")
grid_search = GridSearchCV(
    LogisticRegression(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train_scaled, y_train)
print("gridsearch complete")
print("\nbest parameters:")
print(grid_search.best_params_)
print(f"\ncross validation score: {grid_search.best_score_:.4f}")
total_combos=len(grid_search.cv_results_['params'])
print(f"total combinations tried: {total_combos}")

best_model=grid_search.best_estimator_
tuned_pred=best_model.predict(X_test_scaled)
tuned_acc=accuracy_score(y_test, tuned_pred)

print("\ntuned model")
print(f"accuracy:{tuned_acc:.4f}")
print(f"precision:{precision_score(y_test, tuned_pred):.4f}")
print(f"recall:{recall_score(y_test, tuned_pred):.4f}")
print(f"f1 score:{f1_score(y_test, tuned_pred):.4f}")
print(f"misclassified:{int((1-tuned_acc)*len(y_test))}/{len(y_test)}")
print("\nconfusion matrix:")
print(confusion_matrix(y_test, tuned_pred))

train_pred_tuned=best_model.predict(X_train_scaled)
train_acc_tuned=accuracy_score(y_train, train_pred_tuned)
print(f"\ntraining accuracy:{train_acc_tuned:.4f}")
print(f"testing accuracy:{tuned_acc:.4f}")

print("\ncomparison ")
print(f"baseline accuracy:{base_acc:.4f}")
print(f"tuned accuracy:{tuned_acc:.4f}")
print(f"baseline f1:{f1_score(y_test, base_pred):.4f}")
print(f"tuned f1:{f1_score(y_test, tuned_pred):.4f}")

diff=tuned_acc - base_acc
if diff > 0:
    print(f"\nimprovement: +{diff:.4f}")
elif diff < 0:
    print(f"\ntuned did slightly worse: {diff:.4f}")
    print("maybe my param grid wasnt wide enough")
else:
    print("\nno change,baseline already performed well")
    print("gridsearch confirmed default params were good")
print("\nsample predictions")
print(f"{'actual':<20} {'predicted':<20} {'correct?'}")
for i in range(10):
    actual    = cancer.target_names[y_test[i]]
    predicted = cancer.target_names[tuned_pred[i]]
    correct   = "Yes" if y_test[i] == tuned_pred[i] else "No"
    print(f"{actual:<20} {predicted:<20} {correct}")
base_cm=confusion_matrix(y_test,base_pred)
tuned_cm=confusion_matrix(y_test,tuned_pred)
fig, axes=plt.subplots(1,2,figsize=(12,5))
sns.heatmap(base_cm, annot=True, fmt='d', cmap='Blues',
xticklabels=cancer.target_names,yticklabels=cancer.target_names,
ax=axes[0])
axes[0].set_title('baseline model')
axes[0].set_xlabel('predicted')
axes[0].set_ylabel('actual')
sns.heatmap(tuned_cm, annot=True, fmt='d', cmap='Greens',
xticklabels=cancer.target_names,yticklabels=cancer.target_names,
    ax=axes[1])
axes[1].set_title('tuned model')
axes[1].set_xlabel('predicted')
axes[1].set_ylabel('actual')
plt.suptitle('confusion matrix - baseline vs tuned', fontsize=13)
plt.tight_layout()
plt.savefig('confusion_matrix.png')
plt.show()
print("\nconfusion matrix saved")