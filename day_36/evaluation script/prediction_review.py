from ultralytics import YOLO
from pathlib import Path
from PIL import Image
model = YOLO("best.pt")
input_folder = Path(r"C:\Users\User\Documents\GitHub\day_29\Helmet_Dataset\valid\images")
output_folder = Path(r"C:\Users\User\Documents\GitHub\day_36\predictions\review")
output_folder.mkdir(parents=True, exist_ok=True)
images = list(input_folder.glob("*.jpg")) + list(input_folder.glob("*.jpeg")) + list(input_folder.glob("*.png"))
results = model.predict(
    source=str(input_folder),imgsz=640,conf=0.25,save=True,
    save_txt=False,project=str(output_folder.parent),name=output_folder.name,exist_ok=True,verbose=True)
saved_images = list(output_folder.glob("*.jpg")) + list(output_folder.glob("*.jpeg")) + list(output_folder.glob("*.png"))
for index, image_path in enumerate(saved_images, start=1):
    new_name = f"image_{index:03d}.jpg"
    new_path = output_folder / new_name
    image = Image.open(image_path).convert("RGB")
    image.save(new_path, quality=95)
    if image_path != new_path:
        image_path.unlink()
print("\nPREDICTION REVIEW:")
print(f"Total validation images processed: {len(images)}")
print(f"Predictions saved to: {output_folder.resolve()}")