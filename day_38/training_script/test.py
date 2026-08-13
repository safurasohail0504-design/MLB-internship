import os

base = "yolo_dataset"

print(os.path.exists(os.path.join(base, "train", "images")))
print(os.path.exists(os.path.join(base, "valid", "images")))
print(os.path.exists(os.path.join(base, "test", "images")))