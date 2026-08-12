from pathlib import Path
from collections import Counter
label_folder = Path(r"C:\Users\User\Documents\GitHub\day_29\Helmet_Dataset\train\labels")
image_count = Counter()
object_count = Counter()
for label_file in label_folder.glob("*.txt"):
    classes_in_image = set()
    with open(label_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            class_id = int(parts[0])
            classes_in_image.add(class_id)
            object_count[class_id] += 1
    for class_id in classes_in_image:
        image_count[class_id] += 1
print("IMAGE DISTRIBUTION")
for class_id, count in sorted(image_count.items()):
    print(f"Class {class_id}: {count} images")
print("\nOBJECT DISTRIBUTION")
for class_id, count in sorted(object_count.items()):
    print(f"Class {class_id}: {count} objects")