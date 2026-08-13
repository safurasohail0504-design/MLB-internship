import os
from collections import Counter

BASE = "yolo_dataset"

splits = {
    "train": "train",
    "validation": "valid",
    "test": "test"
}

for name, folder in splits.items():
    image_dir = os.path.join(BASE, folder, "images")
    label_dir = os.path.join(BASE, folder, "labels")

    images = [f for f in os.listdir(image_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    labels = [f for f in os.listdir(label_dir) if f.endswith(".txt")]

    print(f"\n{name}")
    print("Images:", len(images))
    print("Label files:", len(labels))

    counts = Counter()

    for file in labels:
        with open(os.path.join(label_dir, file), "r") as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    counts[parts[0]] += 1

    print("Class distribution:", dict(counts))

    missing = []

    for image in images:
        label = os.path.splitext(image)[0] + ".txt"
        if label not in labels:
            missing.append(image)

    print("Images without annotations:", len(missing))