from pathlib import Path
import cv2

input_images = Path(r"C:\Users\User\Documents\GitHub\day_29\Helmet_Dataset\valid\images")
input_labels = Path(r"C:\Users\User\Documents\GitHub\day_29\Helmet_Dataset\valid\labels")
output_folder = Path(r"C:\Users\User\Documents\GitHub\day_36\predictions\ground_truth")

output_folder.mkdir(parents=True, exist_ok=True)

images = list(input_images.glob("*.jpg")) + list(input_images.glob("*.jpeg")) + list(input_images.glob("*.png"))

class_counts = {"0": 0, "1": 0}
saved = 0

for image_path in images:
    label_path = input_labels / f"{image_path.stem}.txt"

    if not label_path.exists():
        continue

    image = cv2.imread(str(image_path))

    if image is None:
        continue

    height, width = image.shape[:2]

    with open(label_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split()

        if len(parts) != 5:
            continue

        class_id = parts[0]

        x_center = float(parts[1]) * width
        y_center = float(parts[2]) * height
        box_width = float(parts[3]) * width
        box_height = float(parts[4]) * height

        x1 = int(x_center - box_width / 2)
        y1 = int(y_center - box_height / 2)
        x2 = int(x_center + box_width / 2)
        y2 = int(y_center + box_height / 2)

        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(width - 1, x2)
        y2 = min(height - 1, y2)

        class_counts[class_id] = class_counts.get(class_id, 0) + 1

        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(image, f"GT Class {class_id}", (x1, max(20, y1 - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    output_path = output_folder / f"gt_{saved + 1:03d}.jpg"

    cv2.imwrite(str(output_path), image)

    saved += 1

print("\nGROUND TRUTH REVIEW:")
print(f"Images processed: {saved}")
print(f"Class 0 objects: {class_counts.get('0', 0)}")
print(f"Class 1 objects: {class_counts.get('1', 0)}")
print(f"Saved to: {output_folder.resolve()}")