# Day 39 – Model Testing & Error Analysis

## Project Introduction

This project focuses on testing the custom shoe-detection YOLO model created during Day 38 and turning it into a complete Computer Vision application.
The complete workflow followed in this task was:
**Dataset → Model → Inference → Error Analysis → Evaluation → Application**
The selected object remained **shoes**, using the custom YOLO model trained on the Day 38 dataset.

## Technologies Used

* Python
* Ultralytics YOLOv8
* PyTorch
* OpenCV
* NumPy
* Pillow
* Streamlit
* GitHub
* Hugging Face Spaces

## Folder Structure

```text
Day_39
│
├── app.py
├── README.md
├── requirements.txt
│
├── models
│   └── best.pt
│
├── unseen_images
│   └── 20 completely unseen images
│
├── predictions
│   └── shoe_predictions
│
├── error_analysis
│   ├── unseen_evaluation_report.txt
│   ├── unseen_predictions.csv
│   └── difficult_examples.txt
│
└── training_script
    └── prediction.py
```

## Model Used

The custom YOLOv8 shoe-detection model from Day 38 was used for Day 39 testing.

The model detects one class:

```text
Class 0 = shoe
```
The trained model was loaded from:

```text
models/best.pt
```
No additional training was performed for Day 39 because the focus of this task was model testing, error analysis, inference, and application development.

## Unseen Image Testing

The model was tested on **20 completely unseen images**.

These images were stored separately in:

```text
unseen_images/
```

The images were not part of the original training, validation, or test dataset.

The purpose of using unseen images was to check how the trained model behaves on new real-world examples.

## Prediction Process

A Python prediction script was created to run the custom YOLO model on all 20 unseen images.

The script:

* Loads `best.pt`.
* Reads the 20 unseen images.
* Runs YOLO inference.
* Uses a confidence threshold of 0.25.
* Generates bounding boxes.
* Displays detected class and confidence.
* Saves prediction images.
* Calculates the number of detections per image.
* Calculates average confidence.
* Generates a CSV summary.
* Generates an evaluation report.

Prediction results were saved in:

```text
predictions/shoe_predictions/
```

The generated CSV report was saved as:

```text
error_analysis/unseen_predictions.csv
```

## Unseen Image Results

The final unseen-image testing produced:

```text
Unseen Images Tested: 20
Images With Detections: 20
Images Without Detections: 0
Total Predicted Objects: 162
Average Detection Confidence: 0.6429
```

All 20 unseen images produced at least one shoe detection.

However, the number of predicted objects was not always equal to the actual number of shoes because some images contained missed detections, duplicate detections, and false positives.

## Model Metrics

The official numerical evaluation metrics were obtained separately using the labeled test dataset.

```text
Precision: 0.8693
Recall: 0.7520
mAP@50: 0.8305
mAP@50-95: 0.5800
```

These values **do not represent metrics calculated from the 20 unseen images**.

The 20 unseen images did not contain ground-truth annotation files, so Precision, Recall, mAP@50, and mAP@50-95 could not be calculated directly for that batch.

Instead, the unseen images were evaluated through manual visual inspection of the prediction outputs.

## Manual Error Analysis

The prediction images were reviewed for:

* Duplicate bounding boxes
* False-positive detections
* Missed objects
* Severe over-detection
* Low-confidence detections
* Difficult object orientations
* Partially visible shoes
* Crowded scenes

Several important model limitations were identified.

### Duplicate / Overlapping Boxes

The model sometimes produced multiple bounding boxes around the same shoe instead of one clean bounding box.

Examples included:

```text
catkin-childrens-shoe-1728294
e_stamm-shoes-4655404
usa-reiseblogger-running-5370071
```

This indicates that the model can confuse different visual features of the same shoe as separate objects.

### False Positives

Some non-shoe regions were incorrectly classified as shoes.

Examples included:

```text
e_stamm-shoes-4655404
planet_fox-ball-8048205
```

In one case, text on a shoe box was detected as a shoe-like object. In another case, part of a soccer ball was incorrectly detected.

These errors suggest that high-contrast patterns, textures, and shapes can sometimes confuse the model.

### Missed Detections

The model also missed some shoes when multiple objects were present.

Examples included:

```text
spiralni-shoe-4814211
ddcreativohn-shoes-3967944
```

In the hiking-boot example, two boots were treated as one object. In another image, two hanging shoes were present but only one was detected.

### Severe Over-Detection

The most significant error occurred in:

```text
ivabalk-bowling-shoes-2779989
```

The model produced **105 detections** in a single image.

The image contained many visually similar bowling shoes arranged closely together. The model generated numerous overlapping and duplicate detections.

This demonstrates that the model struggles with dense scenes containing many repetitive objects.

### Low-Confidence Detections

Lower confidence was observed when shoes were:

* Partially visible
* Hanging
* Rotated unusually
* Small within the image
* Heavily textured
* Worn or dirty

Examples included:

```text
ddcreativohn-shoes-3967944
spiralni-shoe-4814211
un-perfekt-sports-shoes-3994967
```

## Five Difficult Examples

Five difficult examples were selected from the unseen-image prediction results.

```text
1. ivabalk-bowling-shoes-2779989
   Severe over-detection in a crowded scene.

2. spiralni-shoe-4814211
   Two boots were treated as one object.

3. e_stamm-shoes-4655404
   False detections occurred on text/letters.

4. ddcreativohn-shoes-3967944
   One of two hanging shoes was missed.

5. catkin-childrens-shoe-1728294
   Multiple overlapping boxes were produced for one shoe.
```

These examples were selected through manual inspection of the prediction outputs.

## Where the Model Performs Well

The model performs better when shoes are clearly visible and have relatively simple backgrounds.

Examples include:

```text
homar-converse-1935026
rojesh55-sport-7047874
```

The model also successfully detected multiple shoes in several street and real-world scenes.
This indicates that the model has learned useful visual features for identifying shoes.

## Error Analysis Conclusion

The unseen-image testing showed that the model is capable of detecting shoes across different real-world conditions, but it still has several limitations.

The main errors identified were:

1. Duplicate bounding boxes
2. False positives
3. Missed objects
4. Severe over-detection in crowded scenes
5. Lower confidence on unusual viewpoints and partial objects

The unseen-image results should therefore be considered a **qualitative/manual evaluation**, while the Precision, Recall, mAP@50, and mAP@50-95 values come from the separately labeled test evaluation.

## Application

A user-friendly Streamlit application was created around the custom YOLO model.

The application supports:

* Image upload
* Short video upload
* Custom YOLO inference
* Bounding-box visualization
* Shoe class labels
* Confidence scores
* Adjustable confidence threshold
* Detection statistics
* Downloadable prediction results

The confidence threshold allows the user to control how confident the model must be before displaying a detection.

For example:

```text
0.25 → more detections, including weaker predictions
0.50 → fewer, more confident detections
0.75 → only high-confidence detections
```

This makes it possible to observe the effect of the confidence threshold on false and missed detections.

## Problems Found

The main problems identified during testing were:

* Duplicate detections on individual shoes
* False positives on visually similar regions
* Missed shoes in multi-object images
* Poor performance in highly crowded scenes
* Difficulty with unusual shoe orientations
* Lower confidence on partially visible shoes
* Difficulty separating closely touching objects

## Future Improvements

With additional time, the model could be improved by:

1. Adding more crowded shoe images.
2. Adding more examples containing touching or overlapping shoes.
3. Adding negative images containing objects that visually resemble shoes.
4. Adding more unusual orientations.
5. Adding more partially visible shoes.
6. Improving bounding-box annotation quality.
7. Increasing dataset diversity.
8. Testing different confidence and IoU thresholds.
9. Training with a GPU for faster experimentation.
10. Comparing different YOLO model sizes.

## Conclusion

Day 39 provided practical experience in **model testing, inference, error analysis, and application development**.
The custom YOLO model was tested on 20 completely unseen images, prediction outputs were generated, difficult examples were identified, and the model's strengths and weaknesses were analyzed manually.
The project was then extended into an end-to-end Computer Vision application capable of accepting images and short videos, running the custom YOLO model, displaying detections and confidence scores, adjusting the confidence threshold, showing detection statistics, and saving prediction results.
The main learning outcome was that **a trained model is only one part of a Computer Vision system**. Testing on unseen data, identifying errors, understanding failure cases, and building a usable inference application are equally important parts of the complete AI pipeline.
