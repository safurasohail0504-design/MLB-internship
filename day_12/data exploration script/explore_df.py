import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# converting to dataframe - easier to work with
df = pd.DataFrame(X, columns=cancer.feature_names)
df['target'] = y

print("dataframe created")
print("shape:", df.shape)

# head
print("\nfirst 5 rows:")
print(df.head())

# info - not sure what all this shows but it looks useful
print("\ninfo:")
print(df.info())

# describe - i think this gives statistics
print("\nstatistical summary:")
print(df.describe())

# missing values
print("\nmissing values:", df.isnull().sum().sum())