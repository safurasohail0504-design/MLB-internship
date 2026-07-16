# Day 9 – Data Cleaning and Data Visualization

## Overview
In this task, I learned how to clean a dataset using Pandas and visualize data using Matplotlib. I cleaned the student performance dataset, created different charts, and built a Student Performance Dashboard to analyze students' results.

## Technologies Used
- Python
- Pandas
- Matplotlib

## Project Structure
day_9
│
├── data cleaning script
├── data visualization script
├── mini project
├── cleaned student performance
│   └── cleaned_student_performance.csv
├── generated charts
├── README.md
└── screen_recording.mp4

## Data Cleaning Steps Performed
- Loaded the dataset using Pandas.
- Checked for missing values.
- Checked and removed duplicate records.
- Renamed the Machine_Learning column to ML.
- Created a new Average_Score column by calculating the average marks of all subjects.
- Created a Performance column with categories:
  - Excellent
  - Good
  - Average
  - Needs Improvement
- Saved the cleaned dataset as cleaned_student_performance.csv.

## Data Visualizations Created
### Bar Chart
- Displayed the average marks of students.
- Used to compare student performance.
### Histogram
- Displayed the distribution of Average_Score.
- Helped understand how marks are spread across students.
### Scatter Plot
- Compared Python and Machine Learning marks.
- Helped observe the relationship between both subjects.
### Pie Chart
- Displayed the distribution of Performance categories.
- Helped visualize how many students belong to each performance level.
### Box Plot
- Displayed the spread of marks for all subjects.
- Helped identify variation and possible outliers.

## Mini Project
Student Performance Dashboard
The dashboard answers the following questions:
- Total number of students
- Average marks of each subject
- Top 5 performing students
- Students who need improvement
- Subject with the highest class average
The results were displayed using tables and charts.

## Three Key Insights
- Machine Learning had the highest class average among all subjects.
- Only a few students were in the Needs Improvement category, while most students performed well.
- Students with high Python marks generally also achieved high Machine Learning marks.

## Challenges Faced
- Faced file path errors while loading the CSV file.
- Initially plotted all students instead of only the Top 5 students.
- Learned how to create new columns, rename columns, and generate different chart types using Matplotlib.

## Learning Outcome
After completing this task, I can:
- Clean datasets using Pandas.
- Handle missing values and duplicate records.
- Create new columns and modify datasets.
- Generate different types of charts using Matplotlib.
- Analyze data and present meaningful insights through a dashboard.