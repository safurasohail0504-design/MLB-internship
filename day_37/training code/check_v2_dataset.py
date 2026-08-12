from pathlib import Path

ROOT = Path(r"C:\Users\User\Documents\GitHub\day_37")
IMAGE_DIR = ROOT / "improved_dataset" / "train" / "images"
LABEL_DIR = ROOT / "improved_dataset" / "train" / "labels"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
VALID_CLASSES = {"0", "1"}

images = {p.stem: p for p in IMAGE_DIR.iterdir()
          if p.suffix.lower() in IMAGE_EXTENSIONS}

labels = {p.stem: p for p in LABEL_DIR.glob("*.txt")}

missing_labels = sorted(set(images) - set(labels))
orphan_labels = sorted(set(labels) - set(images))

invalid_lines = []
invalid_classes = []
empty_labels = []

for name, label_path in labels.items():
    lines = [line.strip() for line in label_path.read_text().splitlines() if line.strip()]

    if not lines:
        empty_labels.append(name)
        continue

    for line_no, line in enumerate(lines, 1):
        parts = line.split()

        if len(parts) != 5:
            invalid_lines.append((name, line_no, line))
            continue

        class_id, x, y, w, h = parts

        if class_id not in VALID_CLASSES:
            invalid_classes.append((name, line_no, class_id))

        try:
            values = [float(x), float(y), float(w), float(h)]

            if not all(0 <= value <= 1 for value in values):
                invalid_lines.append((name, line_no, line))

        except ValueError:
            invalid_lines.append((name, line_no, line))


print("\n========== V2 DATASET CHECK ==========\n")

print(f"Images found: {len(images)}")
print(f"Labels found: {len(labels)}")

print("\n----- IMAGE/LABEL MATCHING -----")
print(f"Images without labels: {len(missing_labels)}")
print(f"Labels without images: {len(orphan_labels)}")

if missing_labels:
    print("\nMissing labels:")
    for name in missing_labels:
        print(f"  {name}.txt")

if orphan_labels:
    print("\nLabels without images:")
    for name in orphan_labels:
        print(f"  {name}")

print("\n----- LABEL FORMAT -----")
print(f"Empty label files: {len(empty_labels)}")
print(f"Invalid label lines: {len(invalid_lines)}")
print(f"Invalid class IDs: {len(invalid_classes)}")

if empty_labels:
    print("\nEmpty labels:")
    for name in empty_labels:
        print(f"  {name}.txt")

if invalid_classes:
    print("\nInvalid class IDs:")
    for name, line_no, class_id in invalid_classes:
        print(f"  {name}.txt | line {line_no} | class={class_id}")

if invalid_lines:
    print("\nInvalid YOLO lines:")
    for name, line_no, line in invalid_lines:
        print(f"  {name}.txt | line {line_no} | {line}")

print("\n======================================")

if not missing_labels and not orphan_labels and not empty_labels and not invalid_lines and not invalid_classes:
    print("✅ V2 DATASET IS READY FOR TRAINING!")
else:
    print("❌ V2 DATASET HAS PROBLEMS — FIX THEM BEFORE TRAINING.")