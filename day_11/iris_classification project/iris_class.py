import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score, confusion_matrix)
import matplotlib.pyplot as plt
import seaborn as sns
iris = load_iris()
X = iris.data
y = iris.target
print("Dataset loaded")
print("Samples:", X.shape[0])
print("Features:", X.shape[1])
print("Classes:", iris.target_names)
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
print("\nDataset Overview ")
print(df.head())
print("\nClass Distribution:")
print(df['target'].value_counts())
print("\nMissing Values:", df.isnull().sum().sum())
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25)
print("\nData Split")
print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])
lr_model = LogisticRegression(max_iter=80)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
print("\nLogistic Regression trained")
dt_model = DecisionTreeClassifier(max_depth=3)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
print("decision tree trained")
print("\nsample predictions: logistic regression")
print(f"{'actual':<20} {'predicted':<20} {'correct?'}")
for i in range(12):
    actual    = iris.target_names[y_test[i]]
    predicted = iris.target_names[lr_pred[i]]
    correct   = "Yes" if y_test[i] == lr_pred[i] else "No"
    print(f"{actual:<20} {predicted:<20} {correct}")
lr_acc=accuracy_score(y_test, lr_pred)
lr_pre=precision_score(y_test, lr_pred, average='weighted')
lr_rec=recall_score(y_test, lr_pred, average='weighted')
lr_f1=f1_score(y_test, lr_pred, average='weighted')
lr_cm=confusion_matrix(y_test, lr_pred)
print("\nlogistic regression evaluation")
print(f"accuracy : {lr_acc:.4f}")
print(f"precision: {lr_pre:.4f}")
print(f"recall   : {lr_rec:.4f}")
print(f"F1 Score : {lr_f1:.4f}")
print(f"misclassified: {int((1 - lr_acc) * len(y_test))}/{len(y_test)}")
print("\nConfusion Matrix:")
print(lr_cm)
dt_acc=accuracy_score(y_test, dt_pred)
dt_pre=precision_score(y_test, dt_pred,average='weighted')
dt_rec=recall_score(y_test, dt_pred,average='weighted')
dt_f1=f1_score(y_test, dt_pred,average='weighted')
dt_cm=confusion_matrix(y_test, dt_pred)
print("\ndecision tree evaluation")
print(f"accuracy : {dt_acc:.4f}")
print(f"precision: {dt_pre:.4f}")
print(f"recall   : {dt_rec:.4f}")
print(f"F1 Score : {dt_f1:.4f}")
print(f"misclassified: {int((1 - dt_acc) * len(y_test))}/{len(y_test)}")
print("\nconfusion matrix:")
print(dt_cm)
print("\nmodel comparison")
print(f"logistic regression -> Accuracy: {lr_acc:.4f} | F1: {lr_f1:.4f}")
print(f"decision tree       -> Accuracy: {dt_acc:.4f} | F1: {dt_f1:.4f}")
if lr_acc > dt_acc:
    print("logistic regression performed better on this split")
elif dt_acc > lr_acc:
    print("decision tree performed better on this split")
else:
    print("both models performed equally on this split")
fig, axes = plt.subplots(1,2,figsize=(12,5))
sns.heatmap(lr_cm,annot=True,fmt='d',cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names,
            ax=axes[0])
axes[0].set_title('logistic regression')
axes[0].set_xlabel('predicted')
axes[0].set_ylabel('actual')
sns.heatmap(dt_cm,annot=True,fmt='d',cmap='Greens',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names,
            ax=axes[1])
axes[1].set_title('Decision Tree')
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')
plt.suptitle('confusion matrix comparison',fontsize=14)
plt.tight_layout()
plt.savefig('confusion_matrix.png')
plt.show()
print("\nConfusion matrix saved as confusion_matrix.png")