Day 37 – YOLO Model Improvement & V1 vs V2 Comparison

Project Introduction

This project focuses on improving the previously trained YOLOv8 helmet-detection model and comparing the improved V2 model with the existing V1 model.

The purpose of this task was to train a new model using an improved helmet dataset, evaluate both versions using the same validation dataset, compare their performance, and create a practical interface for testing both models on the same images.

The task also included reviewing prediction examples to understand whether the new training approach actually improved the model. The comparison was kept based on the actual evaluation results without artificially favoring V2.

Technologies Used

Python

Ultralytics YOLOv8

PyTorch

Streamlit

OpenCV

Pandas

NumPy

Matplotlib

CSV

Roboflow Dataset


Folder Structure

Day_37
│
├── models
│   ├── V1_best.pt
│   └── V2_best.pt
│
├── improved_dataset
│   ├── train
│   ├── valid
│   ├── test
│   └── data.yaml
│
├── training code
│   └── train_v2.py
│
├── evaluation
│   └── compare_models.py
│
├── V1 vs V2
│   ├── Original
│   ├── V1
│   └── V2
│
├── results
│   └── v2_training_correct
│       ├── weights
│       │   ├── best.pt
│       │   └── last.pt
│       ├── results.csv
│       ├── results.png
│       └── training plots
│
├── app.py
└── README.md

Model and Dataset

V1 Model

The original trained YOLOv8 model used as the baseline was:

models/V1_best.pt

V1 was used as the baseline model so that the performance of the newly trained V2 model could be measured against an already trained version.

V2 Model

The improved model was trained using:

models/V1_best.pt

as the starting pretrained/custom weights and the improved helmet-detection dataset.

The final V2 model was saved as:

models/V2_best.pt

The V2 training was performed for:

5 epochs

The training was performed on CPU, which resulted in a significantly longer training time.

Dataset Used

The V2 model was trained using the improved helmet-detection dataset.

Training dataset:

2311 images

Validation dataset:

126 images
274 ground-truth objects

The validation dataset was kept consistent with the evaluation setup so that V1 and V2 could be compared fairly.

The dataset contains two classes:

Class 0 → Cap / Hat
Class 1 → Helmet

Purpose of V2 Training

The purpose of creating V2 was to investigate whether training the existing model on an improved dataset could produce better detection performance.

The comparison focuses on:

Precision

Recall

mAP@50

mAP@50-95

Detection examples

Confidence scores

Prediction differences


The goal was not simply to create another model, but to determine whether the new training process actually improved the existing model.

V2 Training

The V2 model was trained using the improved dataset with:

Epochs: 5
Batch Size: 8
Image Size: 640
Optimizer: AdamW

The training completed successfully.

The final training output produced:

best.pt
last.pt
results.csv
results.png

The best model was selected for the V1 vs V2 comparison.

V1 Performance

The baseline V1 model achieved:

Metric	V1

Precision	0.9127
Recall	0.8168
mAP@50	0.8697
mAP@50-95	0.6795


These results provided the baseline against which V2 was evaluated.

V2 Performance

The final V2 model achieved:

Metric	V2

Precision	0.8330
Recall	0.7400
mAP@50	0.7800
mAP@50-95	0.5170


V1 vs V2 Comparison

The actual validation results were:

Metric	V1	V2

Precision	0.9127	0.8330
Recall	0.8168	0.7400
mAP@50	0.8697	0.7800
mAP@50-95	0.6795	0.5170


Based on the current validation results, V1 performs better than V2.

V2 training was successfully completed, but the improved dataset and current training configuration did not produce better overall validation performance than V1.

The results were kept as the actual measured results rather than modifying the comparison to artificially make V2 appear better.

Performance Analysis

Precision

V1 achieved:

0.9127

while V2 achieved:

0.8330

This means V1 currently produces more accurate detections overall.

The lower V2 precision indicates that V2 still produces more incorrect detections compared with V1.

Recall

V1 achieved:

0.8168

while V2 achieved:

0.7400

V1 therefore detects a larger proportion of the actual objects in the validation dataset.

The lower V2 recall indicates that some objects are still being missed.

mAP@50

V1:

0.8697

V2:

0.7800

V1 currently provides stronger detection performance at the IoU 0.50 threshold.

mAP@50-95

V1:

0.6795

V2:

0.5170

The lower V2 mAP@50-95 indicates that V2 currently has weaker overall localization quality across stricter IoU thresholds.

This metric is particularly useful because it evaluates not only whether an object was detected, but also how accurately its bounding box is positioned.

V2 Training Progress

During V2 training, the validation performance changed across epochs.

The results showed improvement during training, with the strongest final recorded V2 result reaching:

Precision: 0.833
Recall: 0.740
mAP@50: 0.780
mAP@50-95: 0.517

Although V2 improved during its own training process, it still did not surpass the V1 baseline.

V1 vs V2 Prediction Review

A comparison structure was created:

V1 vs V2
│
├── Original
├── V1
└── V2

The purpose of these folders is to visually compare:

Original image

V1 prediction

V2 prediction


The same images can therefore be inspected across both model versions.

The comparison helps identify differences that cannot always be understood from numerical metrics alone.

Streamlit Application

A Streamlit application was developed to provide a practical V1 vs V2 model comparison interface.

The application allows the user to:

Upload an image

Run V1 detection

Run V2 detection

Adjust the confidence threshold

Adjust image size

View V1 predictions

View V2 predictions

Compare detection counts

Inspect prediction confidence


The application uses:

models/V1_best.pt
models/V2_best.pt

for model comparison.

Model Comparison

The application compares both models using the same uploaded image.

For each model, the application displays:

Detection Count
Predicted Classes
Confidence Scores
Bounding Boxes

This allows direct visual comparison between the two model versions.

Current Findings

The current results show that:

V1 > V2

for the main validation metrics.

V1 currently has:

Higher Precision

Higher Recall

Higher mAP@50

Higher mAP@50-95


Therefore, V2 cannot currently be considered an improvement over V1 based on the validation results.

V2 Limitations

The current V2 model still has several areas that require improvement:

Lower precision than V1

Lower recall than V1

Lower mAP@50

Lower mAP@50-95

Possible false detections

Missed objects

Localization errors

Difficulty with visually similar objects

Sensitivity to difficult image conditions


Possible Improvements

Based on the current comparison, future V2 improvements could include:

1. Dataset Quality

Review training annotations and ensure bounding boxes accurately cover the target objects.

2. Hard Negative Examples

Add images containing people without helmets or caps and visually similar background objects.

This can help reduce false detections.

3. Dataset Diversity

Increase variation in:

Lighting

Camera angles

Object sizes

Backgrounds

Person poses

Helmet types

Crowded scenes


4. Small Object Examples

Include more examples containing small and distant helmets or caps to improve recall.

5. Occlusion Examples

Add examples where helmets or caps are partially hidden or where multiple people overlap.

6. Training Configuration

Experiment with:

More training epochs

Learning rate

Batch size

Augmentation

Image size

Confidence threshold

NMS/IoU settings


Any change should be validated against the same validation dataset.

Blockers

The main blocker during this task was the training time.

The V2 model was trained on CPU, making each epoch relatively time-consuming. The 5-epoch training run took approximately:

3.68 hours

Another challenge was that an earlier V2 training checkpoint was not a complete resumable Ultralytics checkpoint, which prevented direct continuation from the previous epoch.

Additional time was spent configuring the V1 vs V2 prediction folders and ensuring that the Streamlit application could correctly access the comparison images.

Final Evaluation

The final measured results were:

Metric	V1	V2

Precision	0.9127	0.8330
Recall	0.8168	0.7400
mAP@50	0.8697	0.7800
mAP@50-95	0.6795	0.5170

The V2 training pipeline, evaluation process, comparison structure, and Streamlit application were completed successfully.
However, the current results show that V2 has not yet surpassed V1. The comparison provides a measurable baseline for further experimentation and model improvement rather than assuming that the newer model is automatically better.
