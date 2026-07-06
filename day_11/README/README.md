Day 11: Model Evaluation and Classification

What is Classification

Classification is a type of supervised machine learning task where the goal is to predict which category or class a given input belongs to. The model learns from labeled training data and then assigns a class label to new, unseen inputs. For example, looking at the measurements of a flower and predicting whether it is a setosa, versicolor, or virginica is a classification problem. The output is always one of a fixed set of categories, not a continuous number.

Difference Between Regression and Classification

Regression and classification are both supervised learning tasks, but they differ in what they predict. Regression predicts a continuous numerical value, such as predicting the price of a house based on its size and location. The output can be any number within a range. Classification on the other hand predicts a discrete label or category, such as predicting whether an email is spam or not spam, or which species a flower belongs to. The key difference is that regression answers "how much" while classification answers "which one."

Evaluation Metrics Used

Accuracy measures the percentage of total predictions that were correct. It is the simplest metric but can be misleading when classes are imbalanced.

Precision measures out of all the times the model predicted a certain class, how many of those predictions were actually correct. High precision means fewer false alarms.

Recall measures out of all the actual instances of a class, how many did the model correctly identify. High recall means fewer missed cases.

F1 Score is the balance between precision and recall. It is useful when both false positives and false negatives matter and you cannot afford to optimize one at the expense of the other.

Confusion Matrix is a table that shows exactly how many samples were correctly and incorrectly classified for each class. It helps identify which specific classes the model is confusing with each other.

Model Performance and Observations

Two models were trained and evaluated on the Iris dataset: Logistic Regression and Decision Tree.

Logistic Regression achieved an accuracy of 0.9737, meaning it correctly classified 37 out of 38 test samples. It misclassified one virginica flower as versicolor. Precision was slightly higher at 0.9757, recall and F1 score were both 0.9737. This model performed well because the Iris dataset is mostly linearly separable and Logistic Regression handles linear boundaries effectively.

Decision Tree achieved an accuracy of 0.8947, misclassifying 4 out of 38 samples. All 4 errors were between the versicolor and virginica classes, which are naturally harder to distinguish from each other. The model was constrained with a maximum depth of 3, which limited its ability to perfectly separate those two classes. Precision, recall, and F1 score were all equal at 0.8947 for this split.

Overall, Logistic Regression outperformed Decision Tree on this dataset and this particular train-test split. The versicolor and virginica classes were the main source of confusion for both models, which makes sense since these two species have overlapping feature ranges. Increasing the Decision Tree depth or using more data could potentially close the performance gap between the two models.
