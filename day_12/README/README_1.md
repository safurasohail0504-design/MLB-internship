Day 12: Model Evaluation and Hyperparameter Tuning

What I Learned About Model Evaluation

Model evaluation is how you measure whether a machine learning model is actually working well or just appearing to work well. I learned that accuracy alone is not always enough, especially when dealing with medical data like cancer diagnosis where missing a real case is far more dangerous than a false alarm. This is why we use multiple metrics together.

Accuracy tells you the overall percentage of correct predictions. Precision tells you out of all the times the model predicted a positive case, how many were actually positive. Recall tells you out of all the actual positive cases, how many the model correctly identified. F1 Score balances precision and recall and is more useful when both types of errors matter. The Confusion Matrix shows exactly which classes the model confused with each other, making it easier to spot where the model is going wrong.

I also learned about the difference between training accuracy and testing accuracy. When training accuracy is much higher than testing accuracy, the model has likely memorized the training data instead of learning general patterns, which is called overfitting. When both are low, the model is too simple and is called underfitting.

What Hyperparameter Tuning Is and Why It Matters

Hyperparameters are settings that you choose before training a model. They are not learned by the model itself, they are configured by the developer. Examples in Logistic Regression include C which controls how strictly the model is regularized, solver which determines the internal algorithm used, and max_iter which sets how many iterations the model gets to find the best fit.

Hyperparameter tuning means trying different combinations of these settings to find which ones give the best performance. I used GridSearchCV which systematically tries every combination from a given grid of values and runs 5 fold cross validation for each combination. Cross validation means the training data is split into 5 parts and the model is trained and tested 5 times on different portions, giving a more reliable performance estimate than a single train test split. The combination with the highest average score across all 5 folds is selected as the best.

This matters because the default settings of a model are not always the best for every dataset. Small changes in hyperparameters can sometimes meaningfully improve performance, especially on datasets where classes are imbalanced or features have very different scales.

Best Parameters Found by GridSearchCV

GridSearchCV tested combinations across C values of 0.01, 0.1, 1, and 10, solvers lbfgs and liblinear, and max_iter values of 100, 200, and 500. The best parameters selected were the combination that produced the highest cross validation accuracy across all 5 folds. The cross validation score showed how well the model was expected to generalize to unseen data under those settings.

Comparison Between Baseline and Tuned Models

The baseline model was trained using default Logistic Regression settings with max_iter set to 100, which was intentionally kept low so the model would not fully converge. This resulted in slightly lower accuracy and some misclassifications. After applying GridSearchCV and training with the best found parameters, the tuned model showed improvement in accuracy and F1 score compared to the baseline. The confusion matrix for the tuned model had fewer misclassified samples, meaning the model became better at distinguishing malignant from benign cases after tuning.

Key Observations

The dataset was reasonably balanced with 212 malignant and 357 benign samples, which meant accuracy was a reliable metric here and not misleading. Scaling the features using StandardScaler before training made a noticeable difference since the 30 features in this dataset have very different numerical ranges and Logistic Regression performs better when all features are on a similar scale. The training accuracy and testing accuracy were close to each other in both models, which suggests the model was not overfitting badly. Most misclassifications were on the boundary between malignant and benign cases, which makes sense because those cases are inherently harder to distinguish from measurements alone.
