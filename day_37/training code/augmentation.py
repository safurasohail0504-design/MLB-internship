import cv2
from pathlib import Path

input_folder = Path(r"C:\Users\User\Documents\GitHub\day_29\Helmet_Dataset\train\images")
output_folder = Path(r"C:\Users\User\Documents\GitHub\day_37\augmentation_examples")
output_folder.mkdir(parents=True, exist_ok=True)
images = list(input_folder.glob("*.jpg")) + list(input_folder.glob("*.jpeg")) + list(input_folder.glob("*.png"))
if not images:
    print("No images found.")
    exit()
image_path = images[0]
image = cv2.imread(str(image_path))
if image is None:
    print(f"Could not read image: {image_path}")
    exit()
flipped = cv2.flip(image, 1)
cv2.imwrite(str(output_folder / "flip.jpg"), flipped)
rotated_matrix = cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), 15, 1)
rotated = cv2.warpAffine(image, rotated_matrix, (image.shape[1], image.shape[0]))
cv2.imwrite(str(output_folder / "rotation.jpg"), rotated)
scaled = cv2.resize(image, None, fx=1.2, fy=1.2)
cv2.imwrite(str(output_folder / "scaling.jpg"), scaled)
bright = cv2.convertScaleAbs(image, alpha=1.0, beta=40)
cv2.imwrite(str(output_folder / "brightness.jpg"), bright)
contrast = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
cv2.imwrite(str(output_folder / "contrast.jpg"), contrast)
h, w = image.shape[:2]
cropped = image[int(h * 0.1):int(h * 0.9), int(w * 0.1):int(w * 0.9)]
cv2.imwrite(str(output_folder / "cropping.jpg"), cropped)
print("AUGMENTATION COMPLETE")
print(f"Original image: {image_path.name}")
print(f"Augmented examples saved to: {output_folder.resolve()}")