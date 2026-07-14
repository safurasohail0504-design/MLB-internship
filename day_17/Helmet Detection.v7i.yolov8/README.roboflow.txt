
Helmet Detection - v7 2024-05-22 1:08pm
==============================

This dataset was exported via roboflow.com on May 22, 2024 at 7:41 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2571 images.
Helmet are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random brigthness adjustment of between -15 and +15 percent
* Random exposure adjustment of between -10 and +10 percent

The following transformations were applied to the bounding boxes of each image:
* Random shear of between -10° to +10° horizontally and -10° to +10° vertically


