from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# splitting - using 0.2 for test size
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

print("data splited")
print("total samples :", len(X))
print("training samples:", X_train.shape[0])
print("testing samples :", X_test.shape[0])

# i added this to check split ratio
print(f"\ntrain ratio: {X_train.shape[0]/len(X)*100:.1f}%")
print(f"test ratio : {X_test.shape[0]/len(X)*100:.1f}%")