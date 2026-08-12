from ultralytics import YOLO
from pathlib import Path
import shutil
BASE_DIR = Path(__file__).resolve().parent.parent

V1_MODEL = BASE_DIR / "models" / "V1_best.pt"
V2_MODEL = BASE_DIR / "models" / "V2_best.pt"

ORIGINAL_DIR = BASE_DIR / "V1 vs V2" / "original"
V1_OUTPUT = BASE_DIR / "V1 vs V2" / "V1"
V2_OUTPUT = BASE_DIR / "V1 vs V2" / "V2"

V1_OUTPUT.mkdir(parents=True, exist_ok=True)
V2_OUTPUT.mkdir(parents=True, exist_ok=True)

print("Loading V1 model...")
v1 = YOLO(str(V1_MODEL))
print("V1 loaded successfully.")

print("Loading V2 model...")
v2 = YOLO(str(V2_MODEL))
print("V2 loaded successfully.")

images = []

for file in ORIGINAL_DIR.iterdir():
    if file.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp"]:
        images.append(file)

images.sort()

print(f"\nImages found: {len(images)}")

if len(images) == 0:
    print("❌ No images found in V1 vs V2/original/")
    exit()

if len(images) > 5:
    images = images[:5]

print("\nImages being tested:")

for image in images:
    print(" -", image.name)

print("\n V1 PREDICTIONS ")

v1.predict(
    source=[str(img) for img in images],
    conf=0.25,
    save=True,
    project=str(V1_OUTPUT),
    name="predictions",
    exist_ok=True
)

# Move generated images one level up
v1_prediction_folder = V1_OUTPUT / "predictions"

if v1_prediction_folder.exists():

    for file in v1_prediction_folder.iterdir():

        destination = V1_OUTPUT / file.name

        if destination.exists():
            destination.unlink()

        shutil.move(str(file), str(destination))

    v1_prediction_folder.rmdir()




print("\n V2 PREDICTIONS")

v2.predict(
    source=[str(img) for img in images],
    conf=0.25,
    save=True,
    project=str(V2_OUTPUT),
    name="predictions",
    exist_ok=True
)

# Move generated images one level up
v2_prediction_folder = V2_OUTPUT / "predictions"

if v2_prediction_folder.exists():

    for file in v2_prediction_folder.iterdir():

        destination = V2_OUTPUT / file.name

        if destination.exists():
            destination.unlink()

        shutil.move(str(file), str(destination))

    v2_prediction_folder.rmdir()

print("V1 vs V2 COMPARISON COMPLETED")

print("\nV1 predictions:")
print(V1_OUTPUT)

print("\nV2 predictions:")
print(V2_OUTPUT)

print("\nOpen these folders and compare the same image:")
print("Original → V1 → V2")