# Day 38 – Custom Dataset Creation

## Project Introduction

This project focuses on creating a custom Computer Vision dataset from scratch and using it to train a YOLO object detection model.
The complete workflow followed in this task was:
**Collect → Clean → Annotate → Split → Augment → Analyze → Train → Evaluate → Test**
The selected object for this dataset was **shoes** because shoes are easy to collect while still providing variation in shape, angle, size, background, and object arrangement.

## Technologies Used

* Python
* Ultralytics YOLOv8
* PyTorch
* OpenCV
* Pandas
* NumPy
* Matplotlib
* Roboflow
* Pexels
* Streamlit
* YOLO annotation format

## Folder Structure

```text
Day_38
│
├── app.py
├── README.md
├── requirements.txt
│
├── models
│   └── best.pt
│
├── original
│   └── shoes
│
├── yolo_dataset
│   ├── train
│   │   ├── images
│   │   └── labels
│   ├── valid
│   │   ├── images
│   │   └── labels
│   ├── test
│   │   ├── images
│   │   └── labels
│   └── data.yaml
│
├── training_script
│   ├── dataset_analysis.py
│   ├── train.py
│   ├── evaluate.py
│   ├── prediction.py
│   └── test.py
│
├── test_images
│   └── unseen images
│
├── predictions
│   └── shoe_predictions
│
└── runs
    └── shoe_detection_v1
```

## Object Selected

The selected object was:

**Class 0 → Shoe**

A single class was used because the objective was to learn the complete custom object-detection dataset workflow rather than create a multi-class detection problem.

## Image Collection

The original images were collected from **Pexels**.

Initially, 215 shoe images were collected and stored locally in:

```text
original/shoes
```

During the upload process, some incomplete `.crdownload` files were rejected by Roboflow and removed.

Final usable images uploaded to Roboflow:

**206 images**

The images contained different shoe types, viewpoints, backgrounds, object sizes, and scenes.

## Dataset Annotation

The dataset was created using **Roboflow**.

Roboflow project:

```text
Shoe Detection
```

Project slug:

```text
shoe-detection-f8tsr
```

Workspace:

```text
safura-sohail
```

The object-detection class was:

```text
shoe
```

Each shoe was annotated using a bounding box around the complete visible shoe.

The annotations were manually checked and corrected, particularly in images containing multiple shoes.

The dataset was exported in **YOLOv8 format**.

## YOLO Annotation Format

Each image has a corresponding `.txt` annotation file.

The YOLO annotation format contains:

```text
class_id center_x center_y width height
```

All bounding-box coordinates are normalized between 0 and 1.

Since this project contains one class:

```text
0 = shoe
```

## Dataset Split

The dataset was divided before augmentation into approximately:

| Split      | Percentage |
| ---------- | ---------: |
| Training   |        70% |
| Validation |        20% |
| Testing    |        10% |

The exported dataset contained:

```text
Training Images: 435
Validation Images: 41
Testing Images: 20
```

The training set contains additional augmented training examples.

Validation and testing images were kept separate from training augmentation.

## Dataset Analysis

A Python dataset-analysis script was created to inspect the dataset.

The script checks:

* Number of images
* Number of label files
* Class distribution
* Images without annotations
* Annotation availability

The final analysis showed:

```text
Training:
Images: 435
Label files: 435
Class distribution: {'0': 4117}
Images without annotations: 0

Validation:
Images: 41
Label files: 41
Class distribution: {'0': 163}
Images without annotations: 0

Testing:
Images: 20
Label files: 20
Class distribution: {'0': 162}
Images without annotations: 0
```

No images were found without corresponding annotations.

## Data Augmentation

Augmentation was applied to the training dataset using Roboflow.

The applied techniques included:

* Horizontal flipping
* Rotation
* Brightness/contrast changes
* Cropping
* Resizing to 512 × 512

The purpose of augmentation was to increase variation in the training data while keeping the validation and testing data untouched.

Augmented images are additional training examples generated from the original images and are not considered completely new real-world data.

## Problems Found During Dataset Creation

Several issues were identified during the dataset creation process.

### Corrupted Downloads

Some downloaded files were incomplete `.crdownload` files and could not be uploaded to Roboflow.

The usable dataset therefore decreased from:

```text
215 → 206 images
```

### Auto-Labeling Problems

The first batch Auto Label attempt in Roboflow produced poor results.

It detected shoes in only a small number of images and frequently missed additional shoes in images containing multiple objects.

Per-image AI-assisted detection followed by manual correction produced much better annotation results.

### Multiple Objects

Images containing multiple shoes required additional checking because automated detection sometimes detected only one shoe.

These images were manually corrected before approval.

### Temporary Roboflow Errors

Some Roboflow operations such as Approve and AI-assisted detection occasionally produced temporary errors. Refreshing and retrying resolved these issues.

## Model Training

A YOLOv8 model was trained using the custom shoe dataset.

Training configuration:

```text
Model: YOLOv8
Image Size: 512
Epochs: 10
Classes: 1
Class: shoe
Device: CPU
```

Training was performed on CPU, so training required approximately:

```text
0.318 hours
```

The trained weights were generated as:

```text
best.pt
last.pt
```

The final best model was saved for evaluation and deployment.

## Training Results

The best validation results obtained during training were:

```text
Precision: 0.650
Recall: 0.574
mAP@50: 0.598
mAP@50-95: 0.391
```

The validation dataset contained:

```text
Images: 41
Instances: 162
```

The results demonstrate that the model learned to detect shoes, although there is still room for improvement.

## Test Evaluation

After training, the model was evaluated separately on the test split.

Test results:

```text
Precision: 0.8693
Recall: 0.7520
mAP@50: 0.8305
mAP@50-95: 0.5800
```

The test dataset contained:

```text
Images: 20
Instances: 161
```

The test evaluation was performed separately from training so that the model could be evaluated on data that was not used for learning.

## New Unseen Images

At least 10 completely new shoe images were collected separately from the original dataset.

These images were stored in:

```text
test_images/
```

They were not included in the original training, validation, or test dataset.

The trained model was then used to generate predictions on these unseen images.

Prediction results were saved in:

```text
predictions/shoe_predictions/
```

The model successfully generated shoe detections across all 10 unseen test images.

Examples included images with:

* 2 shoes
* 3 shoes
* 4 shoes
* 5 shoes
* 6 shoes
* 7 shoes

This provided a practical test of the model on new images containing different numbers and arrangements of shoes.

## Dataset Quality Considerations

The dataset was checked for several important quality issues.

### Missing Annotations

No images without annotation files were found in the final dataset.

### Class Imbalance

Only one class was used:

```text
shoe
```

Therefore, there was no class-to-class imbalance problem.

However, the number of shoe instances varied significantly between images.

### Duplicate Images

Duplicate or highly similar images should be avoided because they can reduce dataset diversity and may cause data leakage if similar images appear in different splits.

### Data Leakage

Validation and test images were kept separate from training augmentation.

The 10 completely new images used for final prediction testing were also kept outside the original dataset.

## Final Evaluation

The custom YOLOv8 shoe detector achieved:

| Metric    | Result |
| --------- | -----: |
| Precision | 0.8693 |
| Recall    | 0.7520 |
| mAP@50    | 0.8305 |
| mAP@50-95 | 0.5800 |

The model showed good detection performance on the test dataset, while the lower mAP@50-95 indicates that bounding-box localization can still be improved.

## Future Improvements

The dataset could be improved by:
1. Collecting more real-world shoe images.
2. Adding more difficult backgrounds.
3. Adding more partially occluded shoes.
4. Including more small and distant shoes.
5. Adding different lighting conditions.
6. Reviewing annotations for tighter bounding boxes.
7. Removing highly similar or duplicate images.
8. Training for more epochs if sufficient computing time is available.
9. Using a GPU to reduce training time.
10. Adding more diverse shoe types and orientations.

## Conclusion

This task provided practical experience in creating a Computer Vision dataset from scratch.
The complete process included collecting original images, cleaning the data, annotating objects, exporting YOLO labels, splitting the dataset, applying training augmentation, analyzing dataset quality, training YOLOv8, evaluating the trained model, and testing it on completely new images.
The main learning outcome was understanding that **dataset quality and annotation quality are fundamental to successful object detection**, and that model performance should be evaluated using both numerical metrics and predictions on unseen images.