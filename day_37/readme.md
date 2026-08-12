# Day 36 – YOLO Model Performance Audit

## Project Introduction

This project focuses on evaluating a trained YOLOv8 computer vision model instead of building a new detection system.
The purpose of this task is to understand how well the trained model performs, identify its mistakes, analyze difficult predictions, and determine what can be improved in the next version of the model.
The model was evaluated on a validation dataset containing helmet-related images. The evaluation includes Precision, Recall, mAP@50, mAP@50-95, confusion matrix analysis, prediction review, ground-truth comparison, and manual error analysis.

# Technologies Used

- Python
- Ultralytics YOLOv8
- PyTorch
- OpenCV
- Pandas
- NumPy
- Matplotlib
- CSV
- Roboflow Dataset

# Folder Structure

```text
Day_36
│
├── best.pt
├── data.yaml
├── README.md
|
├── evaluation script
│   ├── evaluate.py
│   ├── prediction_review.py
│   ├── ground_truth_review.py
│   └── error_analysis.py
│
├── predictions
│   ├── ground_truth
│   └── review
│
├── results
│   └── evaluation_results.txt
│
├── confusion matrix
│   ├── confusion_matrix.png
│   └── confusion_matrix_normalized.png
│
└── error_analysis
    ├── error_analysis.csv
    └── error_analysis_report.txt


Model and Dataset
Model Used:
The trained YOLOv8 model used for evaluation was:
best.pt

The model was trained during the previous helmet detection tasks and was selected for evaluation because it represents the custom-trained model rather than the general YOLOv8 pre-trained model.

Dataset Used:
The evaluation was performed using the Helmet Detection dataset.
The validation dataset contained:
Validation Images: 126
Ground-Truth Objects: 274

The dataset contains two classes.
The original dataset configuration contains:
nc: 2
names: ['0', '1']
The class labels were inspected manually to understand what each class represents.
Based on the dataset inspection:
Class 0 → Cap / Hat
Class 1 → Helmet
Purpose of Model Evaluation
A trained model should not be judged only by whether it produces predictions.
A professional computer vision workflow also asks:

How many predictions are correct?
How many objects are missed?
How many false detections occur?
How confident is the model?
Which classes perform well?
Which classes perform poorly?
Does the model confuse similar objects?
Does the model detect objects in difficult situations?
What should be improved in the next training version?

This project was created to answer these questions.
Evaluation Metrics
The model was evaluated using the following metrics:
Precision
Recall
mAP@50
mAP@50-95
Confusion Matrix

Precision

Precision measures how many of the objects predicted by the model were actually correct.
In simple words:
When the model says an object is a helmet or cap, how often is it correct?
A high Precision value means the model produces fewer false detections.
The evaluated Precision was:
Precision: 0.9127
This means that the model's detections were generally accurate, although some false detections were still observed during manual review.

Recall

Recall measures how many of the actual objects in the dataset were successfully detected by the model.
In simple words:
Out of all the real objects present in the image, how many did the model find?
The evaluated Recall was:
Recall: 0.8168
The recall is lower than precision, which indicates that the model still misses some objects.
This is particularly important in images containing multiple people or objects where some helmets or caps may not be detected.

F1 Score:

F1 Score combines Precision and Recall into a single metric.
It is useful when both false detections and missed objects are important.
The formula is:
F1 = 2 × Precision × Recall / (Precision + Recall)
Using the evaluated Precision and Recall:
Precision = 0.9127
Recall = 0.8168
The approximate F1 Score is:
F1 ≈ 0.862
This indicates that the model has a good overall balance between precision and recall.

IoU

IoU stands for Intersection over Union.
It measures how much the predicted bounding box overlaps with the correct ground-truth bounding box.
IoU = Area of Intersection / Area of Union
A higher IoU means the predicted bounding box is closer to the correct location.
IoU is important because a detection can have the correct class but still have a poorly positioned bounding box.

mAP@50

mAP@50 means mean Average Precision at IoU threshold 0.50.
The prediction is considered correct when the predicted bounding box has sufficient overlap with the ground-truth box at an IoU threshold of 0.50.
The evaluated result was:
mAP@50: 0.8697
This indicates strong detection performance at the IoU 0.50 threshold.

mAP@50-95

mAP@50-95 is a stricter evaluation metric.
Instead of using only IoU 0.50, it evaluates multiple IoU thresholds from:
0.50
0.55
0.60
...
0.95
The evaluated result was:
mAP@50-95: 0.6795

The lower mAP@50-95 compared with mAP@50 indicates that some bounding boxes are not extremely precise even when the model successfully detects the correct object.

This metric is therefore useful for identifying localization problems.

Overall Model Performance

The final evaluation results were:

Precision: 0.9127
Recall: 0.8168
mAP@50: 0.8697
mAP@50-95: 0.6795

The validation dataset contained:

Images: 126
Objects: 274

The model produced strong overall detection results, especially in Precision and mAP@50.

However, manual inspection showed several difficult cases that are not fully represented by the overall metrics.

Class Performance

The validation results were:

Class 0:
Precision: 0.886
Recall: 0.789
mAP@50: 0.840
mAP@50-95: 0.554

Class 1:
Precision: 0.939
Recall: 0.845
mAP@50: 0.899
mAP@50-95: 0.805

Based on the dataset inspection:

Class 0 → Cap / Hat
Class 1 → Helmet

Therefore, the helmet class performed better than the cap/hat class.

Best-Performing Class

The best-performing class was:

Class 1 – Helmet

Its results were:

Precision: 0.939
Recall: 0.845
mAP@50: 0.899
mAP@50-95: 0.805

The helmet class achieved strong precision, recall, and localization performance.

Worst-Performing Class

The weaker class was:

Class 0 – Cap / Hat

Its results were:

Precision: 0.886
Recall: 0.789
mAP@50: 0.840
mAP@50-95: 0.554

The particularly lower mAP@50-95 suggests that some cap/hat bounding boxes are not localized very precisely.

Confusion Matrix

The project generated two confusion matrix files:

confusion_matrix/confusion_matrix.png
confusion_matrix/confusion_matrix_normalized.png

The confusion matrix helps identify:

Correct classifications
Incorrect classifications
Background false positives
Class confusion
Which classes are easier or harder for the model

The normalized confusion matrix is useful for comparing class performance using proportions rather than raw counts.

Prediction Review

A manual prediction review was performed on the validation dataset.

The model processed:

126 validation images

Prediction images were saved inside:

predictions/review/

The images were renamed into a simpler format:

image_001.jpg
image_002.jpg
image_003.jpg
...
image_126.jpg

This made manual error analysis easier.

Ground Truth Review

Ground-truth visualizations were saved inside:

predictions/ground_truth/

These images were compared with the prediction results to determine whether the model:

Detected the correct object
Missed an object
Detected an incorrect object
Used the wrong class
Produced duplicate detections
Produced an incorrectly sized bounding box
Error Analysis

Manual inspection was performed to identify incorrect and difficult predictions.

The main error categories were:

Missed Object
Wrong Class
False Detection
Low Confidence
Small Object
Occlusion
Duplicate Detection
Poor Localization

The error analysis was stored in:

error_analysis/error_analysis.csv

A written explanation was also created:

error_analysis/error_analysis_report.txt
Major Errors Observed
1. False Detection

In some images, the model detected objects as caps or helmets even though no helmet or cap was present.

For example, some people without helmets were detected with predictions such as:

Class 1 – 0.85 confidence

This indicates that the model sometimes interprets the shape of a person's head or another object as a helmet.

2. Duplicate Detection

Some images contained two or more bounding boxes around the same cap or helmet.

This creates duplicate detections for one real object.

Possible causes include:

Similar visual features
Detection confidence threshold
Object overlap
NMS behavior
Difficult object boundaries
3. Large False Bounding Box

In some images, the model produced a bounding box that covered almost the entire image instead of only the cap or helmet.

This is a serious localization error.

Possible causes include:

Incorrect learned features
Difficult image composition
Training examples with inconsistent bounding boxes
Similar background patterns
Poor localization during training
4. Hair Detected as Cap

In some images, the model detected a person's hair as another cap.

This indicates that the model may have learned visual patterns that are not specific enough to identify the actual cap.

The model may associate:

head shape + dark region + hair

with the cap class.

5. Background Objects Detected

Some objects such as shirts, chairs, or other regions were incorrectly detected as caps or helmets.

This represents a false positive.

The model may be relying on visual shapes instead of learning the complete features of the target object.

6. Missed Objects

Some images contained multiple people wearing caps or helmets, but the model detected only some of them.

This is a recall problem.

Possible reasons include:

Small objects
Objects far from the camera
Occlusion
Overlapping people
Low image quality
Similar background colors
7. Small and Distant Objects

Small caps or helmets in the background were harder to detect.

When the object occupies only a small number of pixels, the model receives less visual information.

This can reduce both classification and localization accuracy.

8. Occlusion

When one person's head or helmet overlaps with another person, the model may:

Miss one object
Detect only one object
Produce duplicate boxes
Produce incorrect bounding boxes

Occlusion is therefore an important difficult case for this model.

Difficult Examples

Five difficult examples were selected for detailed analysis.

Difficult Example 1 – Duplicate Detection
Observation

One cap received multiple bounding boxes.

Expected Result

Only one bounding box should cover the cap.

Model Behavior

The model detected the same cap more than once.

Possible Reason

The visual features of the cap may have produced multiple overlapping candidate detections.

Possible Improvement

Improve training examples containing similar caps and tune the confidence and IoU/NMS thresholds.

Difficult Example 2 – Hair Detected as Cap
Observation

The model detected both the birthday cap and a person's hair.

Expected Result

Only the actual cap should be detected.

Model Behavior

Two detections were generated.

Possible Reason

The model may have learned that certain head or hair shapes resemble the cap class.

Possible Improvement

Add hard-negative training images containing people with similar hairstyles but no caps.

Difficult Example 3 – Person Without Helmet Detected
Observation

A person without a helmet received a helmet prediction with high confidence.

Expected Result

No helmet detection should be produced.

Model Behavior

The model classified a person's head as a helmet.

Possible Reason

The model has learned features that are too general and may associate head shapes with helmets.

Possible Improvement

Add more negative examples containing people without helmets and improve class diversity.

Difficult Example 4 – Multiple People Wearing Caps
Observation

Several people were visible in the background wearing caps, but some were not detected.

Expected Result

Each visible cap should be detected.

Model Behavior

Only some caps were detected.

Possible Reason

The objects were small, distant, or partially occluded.

Possible Improvement

Add more small-object and crowded-scene training examples and increase the effective training image size if computationally possible.

Difficult Example 5 – Incorrect Large Bounding Box
Observation

The model produced a bounding box much larger than the actual target.

Expected Result

The bounding box should tightly cover only the cap or helmet.

Model Behavior

The predicted bounding box covered a large part of the image.

Possible Reason

The model had difficulty localizing the target and may have learned incorrect visual patterns from the training data.

Possible Improvement

Review and correct training annotations and add more examples with accurately labeled bounding boxes.

Error Analysis Summary

The major observed problems were:

Error Type	Observation
False Detection	Non-helmet/head/background regions detected
Duplicate Detection	Multiple boxes around one object
Poor Localization	Bounding boxes larger than target
Missed Object	Some visible objects not detected
Small Object	Distant objects frequently missed
Occlusion	Overlapping objects difficult to detect
Wrong Detection	Hair, shirt, chair or other regions detected
Low Confidence	Some difficult objects received low confidence
Why Overall Metrics Are Not Enough

The model has strong numerical evaluation results, but the manual review shows that the model still has important weaknesses.

For example:

Precision = 0.9127

looks strong.

However, manual inspection can reveal specific false detections that are hidden inside the overall metric.

Therefore, professional model evaluation should combine:

Metrics
+
Confusion Matrix
+
Prediction Visualization
+
Manual Error Analysis
Model Strengths

The model performs well when:

The target object is clearly visible
The helmet is large enough
The object is not heavily occluded
The image has good quality
The target has a clear shape
The object is separated from the background

The helmet class showed particularly strong performance.

Model Weaknesses

The main weaknesses include:

False helmet detections
Hair being detected as a helmet
Background objects being detected
Duplicate detections
Large bounding boxes
Missed small objects
Difficulty with crowded scenes
Difficulty with occlusion
Confusion caused by visually similar objects
Proposed Improvements

Based on the error analysis, the following improvements are recommended.

1. Improve Dataset Quality

Review the existing annotations and ensure every bounding box tightly covers the correct object.

Incorrect labels can teach the model incorrect visual patterns.

2. Add Hard Negative Examples

Add images containing:

People without helmets
People with normal hair
People wearing hats
Chairs
Bags
Shirts
Background objects

These examples can help reduce false positives.

3. Increase Dataset Diversity

Include different:

Lighting conditions
Camera angles
Helmet types
Cap styles
Backgrounds
Person poses
Distances
Crowded scenes
4. Add Small Objects

More examples of small and distant helmets/caps should be included.

This can improve recall for difficult scenes.

5. Add Occlusion Examples

Training should include images where:

People overlap
Helmets are partially hidden
Multiple people are close together
6. Tune Confidence Threshold

The confidence threshold can be adjusted to reduce false detections.

A higher threshold may reduce false positives but can also reduce recall.

Therefore, threshold tuning should be evaluated carefully.

7. Tune NMS / IoU Settings

Duplicate detections can sometimes be reduced by adjusting IoU/NMS-related settings.

However, this should be tested using validation results rather than changed blindly.

8. Retrain the Model

After correcting annotations and adding difficult examples, the model should be retrained and evaluated again.

The goal should be to improve:

Recall
mAP@50-95
False Positive Rate
Localization Quality
Final Evaluation

The final model evaluation was:

Precision: 0.9127
Recall: 0.8168
mAP@50: 0.8697
mAP@50-95: 0.6795

Overall, the model demonstrates good detection performance, particularly for the helmet class.
However, manual prediction analysis identified several areas for improvement, including false detections, duplicate detections, poor localization, missed small objects, and incorrect detections of visually similar background regions.
