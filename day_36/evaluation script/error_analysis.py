import csv
from pathlib import Path
output_folder = Path(r"C:\Users\User\Documents\GitHub\day_36\error_analysis")
output_folder.mkdir(parents=True, exist_ok=True)
csv_file = output_folder / "error_analysis.csv"
report_file = output_folder / "error_analysis_report.txt"
records = [
    ["image_005.jpg", "Localization Error", "Cap", "Bounding box covers almost the entire image", "Incorrect localization of the object"],
    ["image_007.jpg", "Duplicate Detection", "Cap", "Two boxes are placed on the same cap", "Multiple overlapping predictions"],
    ["image_010.jpg", "Duplicate Detection", "Cap", "Multiple boxes are placed around one cap", "Repeated predictions for the same object"],
    ["image_016.jpg", "False Positive", "Cap", "Hair is detected as another cap", "Visual similarity between hair and cap"],
    ["image_017.jpg", "False Positive", "Cap", "Hair or head region is detected as cap", "Model learned visual shortcuts"],
    ["image_019.jpg", "False Positive", "Cap", "Non-cap region is detected as cap", "Background or appearance confusion"],
    ["image_024.jpg", "False Positive", "Cap", "Extra box appears on the shirt", "Background confusion"],
    ["image_028.jpg", "Duplicate Detection", "Cap", "Two boxes appear on the same object", "Duplicate prediction"],
    ["image_039.jpg", "Duplicate Detection", "Cap", "Multiple boxes appear around one cap", "Duplicate prediction"],
    ["image_042.jpg", "Duplicate Detection", "Cap", "Multiple boxes appear around one cap", "Duplicate prediction"],
    ["image_047.jpg", "Duplicate Detection", "Cap", "Multiple boxes appear around one cap", "Duplicate prediction"],
    ["image_053.jpg", "False Positive", "Cap", "Chair is detected as cap", "Object/background confusion"],
    ["image_058.jpg", "Duplicate Detection", "Cap", "Two boxes appear around the same object", "Duplicate prediction"],
    ["image_060.jpg", "False Positive", "Cap", "Extra detection appears on another body region", "Visual similarity"],
    ["image_064.jpg", "False Positive", "Cap", "Shirt/body region is detected as cap", "Background confusion"],
    ["image_065.jpg", "Missed Object", "Cap", "Some background caps are not detected", "Small or distant objects"],
    ["image_069.jpg", "False Positive", "Cap", "Incorrect region is detected as cap", "Visual similarity"],
    ["image_072.jpg", "False Positive", "Cap", "Person without helmet or cap is detected", "False positive on head region"],
    ["image_084.jpg", "False Positive", "Cap", "Person without target object is detected", "Visual similarity/background confusion"],
    ["image_015.jpg", "Correct Behavior", "Cap", "Cap is detected correctly; bottle and bag are not target classes", "Model correctly ignores objects outside the dataset classes"],
    ["image_020.jpg", "Correct Behavior", "Cap", "Cap is detected correctly", "Good target localization"],
    ["image_022.jpg", "Correct Behavior", "Cap", "Target object is detected", "Good prediction"],
    ["image_029.jpg", "Correct Behavior", "Cap", "Target object is detected", "Good prediction"],
    ["image_033.jpg", "Correct Behavior", "Cap", "Target object is detected", "Good prediction"],
    ["image_034.jpg", "Correct Behavior", "Helmet", "Helmet is detected correctly", "Good helmet classification"],
    ["image_035.jpg", "Correct Behavior", "Helmet", "Helmet is detected correctly", "Good prediction"],
    ["image_050.jpg", "Correct Behavior", "Helmet", "Helmet is detected correctly", "Good prediction"],
    ["image_075.jpg", "Correct Behavior", "Helmet", "Helmet is detected correctly", "Good prediction"],
    ["image_100.jpg", "Correct Behavior", "Helmet", "Helmet is detected correctly", "Good prediction"],
]
headers = ["Image","Error Category","Class","Observation","Possible Reason"]
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(records)
categories = {}
for record in records:
    category = record[1]
    categories[category] = categories.get(category, 0) + 1
report_lines = [
    "YOLO MODEL PERFORMANCE AUDIT - ERROR ANALYSIS",
    "",
    "Total validation images reviewed: 126",
    "Representative cases recorded in this report: 30",
    "",
    "ERROR CATEGORY COUNTS",
    ""
]

for category, count in categories.items():
    report_lines.append(f"{category}: {count}")
report_lines.extend([
    "",
    "MAIN FINDINGS",
    "",
    "1. Helmet detection performed strongly on most reviewed images.",
    "2. Cap detection produced several duplicate detections.",
    "3. Some hair, shirts, chairs, heads and other regions were incorrectly classified as caps.",
    "4. Small or distant caps, especially in backgrounds, were sometimes missed.",
    "5. Some images contained multiple people or overlapping objects, making detection more difficult.",
    "6. The model sometimes produced large or poorly localized bounding boxes.",
    "",
    "POSSIBLE IMPROVEMENTS",
    "",
    "1. Add more diverse cap and non-cap training examples.",
    "2. Add hard-negative images containing hair, shirts, chairs and similar background patterns.",
    "3. Increase the number of small and distant cap examples.",
    "4. Review duplicate detections and tune confidence/NMS settings during inference.",
    "5. Improve bounding-box annotations for difficult training images.",
    "6. Collect more challenging images containing multiple people and overlapping objects.",
    "",
    "MODEL METRICS",
    "",
    "Precision: 0.9127",
    "Recall: 0.8168",
    "mAP@50: 0.8697",
    "mAP@50-95: 0.6795"
])
with open(report_file, "w", encoding="utf-8") as file:
    file.write("\n".join(report_lines))
print("ERROR ANALYSIS COMPLETED")
print(f"CSV saved to: {csv_file.resolve()}")
print(f"Report saved to: {report_file.resolve()}")
print(f"Representative cases: {len(records)}")