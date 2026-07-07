import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
y = cancer.target

# checking class distribution
df_target = pd.DataFrame(y, columns=['target'])

print("class distribution:")
print(df_target['target'].value_counts())

# i added this to understand what 0 and 1 mean
print("\ntarget meaning:")
print("0 =", cancer.target_names[0])
print("1 =", cancer.target_names[1])

# checking how balanced the classes are
total = len(y)
count_0 = (y == 0).sum()
count_1 = (y == 1).sum()

print(f"\nmalignant (0): {count_0} samples ({count_0/total*100:.1f}%)")
print(f"benign    (1): {count_1} samples ({count_1/total*100:.1f}%)")