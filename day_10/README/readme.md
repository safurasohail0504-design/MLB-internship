# Day 10 – Data Preprocessing and Machine Learning

## Overview
In this task, I learned how to prepare data for Machine Learning using Pandas and Scikit-learn. I performed data preprocessing, trained my first Linear Regression model, evaluated its performance, and built a Student Score Prediction System to predict students' average scores.

## Technologies Used
* Python
* Pandas
* Scikit-learn
* Matplotlib

## Project Structure
day_10
│
├── data processing script
├── linear regression script
├── student score prediction project
├── generated graphs
│   └── actual_vs_predicted.png
├── new_student_performance.csv
├── README.md
└── screen_recording.mp4

## Data Preprocessing Steps Performed
* Loaded the student performance dataset using Pandas.
* Checked dataset information and data types.
* Encoded the Program categorical column using One-Hot Encoding.
* Created a new Average_Score column by calculating the average marks of all subjects.
* Selected feature columns and target variable.
* Split the dataset into Training and Testing sets using an 80:20 ratio.
* Applied StandardScaler for feature scaling.

## Machine Learning Implementation

### Linear Regression
* Built a Linear Regression model using Scikit-learn.
* Trained the model using the training dataset.
* Predicted Average_Score for the testing dataset.
* Compared Actual and Predicted values using a comparison table.

### Model Evaluation
The following evaluation metrics were used:
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### Visualization
* Created a Scatter Plot showing Actual vs Predicted Average Scores.
* Used the graph to visualize the prediction accuracy of the model.

## Mini Project
Student Score Prediction System
The project performs the following tasks:
* Loads the dataset.
* Preprocesses the data.
* Trains a Linear Regression model.
* Predicts student average scores.
* Displays model evaluation metrics.
* Prints a comparison table of Actual vs Predicted scores.
* Visualizes prediction results using a scatter plot.

## Model Performance and Observations
* The Linear Regression model successfully predicted students' Average_Score.
* The model achieved MAE = 0.0, MSE = 0.0, and R² Score = 1.0.
* Since Average_Score was calculated directly from the subject marks used as input features, the model produced perfect predictions.

## Challenges Faced
* Understood the difference between original and encoded datasets.
* Learned when One-Hot Encoding is required and when it should not be repeated.
* Faced feature selection and train-test split confusion, which was resolved through practice.
* Learned the complete Machine Learning workflow from preprocessing to model evaluation.

## Learning Outcome
After completing this task, I can:
* Prepare datasets for Machine Learning.
* Perform One-Hot Encoding and Feature Scaling.
* Select feature and target variables correctly.
* Split datasets into training and testing sets.
* Train a Linear Regression model using Scikit-learn.
* Evaluate model performance using MAE, MSE, and R² Score.
* Visualize prediction results using a scatter plot.
* Build a complete Machine Learning prediction pipeline.