# Day 35 – YOLO Vehicle Detection & Tracking 🚗🚛

## 📌 Overview
On Day 35, I worked on **real-time object detection and tracking using YOLO**.
The main objective was to process a video and detect vehicles such as:
- 🚗 Cars
- 🚛 Trucks
- 🚌 Buses
The system processes the video frame by frame, detects objects using YOLO, and tracks objects across multiple frames to identify unique objects and count their entries and exits.

## 🎯 Objectives

The objectives of this task were:
1. Understand YOLO-based object detection.
2. Detect vehicles from a video.
3. Process video frame by frame.
4. Track detected objects across frames.
5. Assign unique IDs to tracked objects.
6. Count objects entering a defined region.
7. Count objects leaving a defined region.
8. Find the maximum number of objects present simultaneously.
9. Generate final statistics after processing the complete video.

## 🛠️ Technologies Used

- **Python**
- **YOLO**
- **Ultralytics**
- **OpenCV**
- **Object Detection**
- **Object Tracking**
- **Video Processing**

## 📂 Project Structure

```text

├── Source Code
│   ├── video_processing.py
│   ├── detection.py
│ 
│   └── app.py
│
├── Sample Input Videos
│   ├── video1.mp4
├── Processed Output Videos
│   ├── processed_video1.mp4
├── performance_comparison.csv
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
├── Streamlit App URL.txt
 

## Performance Comparison:

The YOLO-based vehicle detection and tracking system was evaluated using video frames during inference.

### Performance Metrics

| Metric | Observation |
|---|---|
| Input resolution | 384 × 640 |
| Detection model | YOLO |
| Detected classes | Car, Truck, Bus |
| Unique objects tracked | 99 |
| Total entries | 23 |
| Total exits | 9 |
| Maximum simultaneous objects | 23 |
| Preprocessing time | Generally 2–10 ms/frame |
| Postprocessing time | Generally below 5 ms/frame |
| Inference time | Approximately 40–300+ ms/frame |

### FPS

FPS was estimated from inference latency using:
`FPS = 1000 / inference_time_ms`
For example, an inference time of 48.5 ms corresponds to approximately 20.6 FPS.
However, inference latency varied between frames, so the system's actual FPS is not constant.

### Detection Performance

The model consistently detected multiple vehicles in each frame. Most frames contained approximately 5–8 cars and 1–2 trucks, while buses were detected occasionally.
The tracking system identified 99 unique objects across the processed video segment, with 23 entries and 9 exits recorded.

### Performance Analysis

The results show that the system is capable of performing real-time or near-real-time vehicle detection depending on system conditions and inference latency. Lower inference times resulted in higher FPS, while frames with higher inference latency reduced the overall processing speed.
The variation in inference time can be affected by hardware resources, video processing, frame resolution, model configuration, and system load.

🔍 How YOLO Works:

Instead of analyzing an image separately for every possible object, YOLO processes the complete image and predicts the objects present in it.
For each frame of the video, YOLO identifies:
Object class
Object location
Bounding box
Confidence score

For example:
7 cars, 1 truck
means that YOLO detected 7 cars and 1 truck in that frame.

🎥 Video Processing:

The input video is processed frame by frame.
The program displays information such as:
Processing frame: 786
This means the program is currently processing frame number 786.
For every frame, YOLO performs:

Video Frame
     ↓
YOLO Detection
     ↓
Detect Vehicles
     ↓
Assign/Update Object IDs
     ↓
Track Objects
     ↓
Count Entries/Exits

🚗 Vehicle Detection:

During processing, the model successfully detected vehicles.
Example output:
0: 384x640 7 cars, 1 truck
This means:
Cars   = 7
Trucks = 1
Total  = 8 objects

The number of detected vehicles changes from frame to frame because vehicles enter, leave, or move through the camera's view.

🔄 Object Tracking:

Object tracking is different from simple object detection.
Detection answers:
"What objects are present in this frame?"
Tracking answers:
"Is this the same object that I detected in the previous frame?"

Tracking allows the system to assign unique IDs to objects and follow them throughout the video.
This is important for calculating:
Unique objects
Entries
Exits
Maximum simultaneous objects

📊 Final Results:

After processing the complete video, the program generated the following results:

Metric	Result
Unique Objects	99
Total Entries	23
Total Exits	9
Maximum Objects	23
Final Output
Unique Objects: 99
Total Entries: 23
Total Exits: 9
Maximum Objects: 23

📈 Detection Examples:

During the video, different frames produced different detections.
Some examples:
Frame 786 → 7 cars, 1 truck
Frame 813 → 5 cars, 2 trucks
Frame 827 → 8 cars, 2 trucks
Frame 844 → 4 cars, 1 truck
Frame 893 → 5 cars, 1 bus, 1 truck
Frame 920 → 6 cars, 1 truck
Frame 942 → 5 cars, 1 truck

This demonstrates that the system was continuously detecting changing vehicle conditions throughout the video.

⚙️ Important YOLO Output Information

The YOLO output also displays processing speed:
Speed:
Preprocess
Inference
Postprocess

For example:
Speed: 5.5ms preprocess,
       165.7ms inference,
       3.0ms postprocess
These values represent the time taken for different stages of processing one frame.

Preprocess:
The input frame is prepared before being given to the model.
Inference
The YOLO model performs object detection.
Postprocess
The detected results are processed and converted into final detections.

🧠 What I Learned

Through this task, I learned:

Basics of YOLO object detection.
How YOLO detects multiple objects in a single frame.
How video frames can be processed using Python.
Difference between object detection and object tracking.
How tracking IDs can be used to identify unique objects.
How vehicle entry and exit counting works.
How to calculate the maximum number of objects present at one time.
How to interpret YOLO inference speed.
How object detection results change between video frames.
💡 Key Concepts:
Object Detection
Object detection identifies what objects are present and where they are located in an image or video.
Object Tracking
Object tracking follows detected objects across consecutive frames.
Unique Object
A unique object represents one tracked entity throughout the video rather than counting the same vehicle repeatedly in every frame.
Entry Count
The number of tracked objects that crossed the defined entry region.
Exit Count
The number of tracked objects that crossed the defined exit region.
Maximum Objects
The highest number of objects detected/tracked simultaneously during the video.

📌 Sample Detection Output
Processing frame: 900
0: 384x640 5 cars, 1 bus, 1 truck
Speed: 6.6ms preprocess,
       223.2ms inference,
       3.2ms postprocess

The program continues this process until all video frames have been processed.
