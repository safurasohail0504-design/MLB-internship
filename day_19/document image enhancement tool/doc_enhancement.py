import os
import cv2
import numpy as np
input_dir = "C:/Users/User/Documents/GitHub/day_19/Input Images/"
output_dir = "C:/Users/User/Documents/GitHub/day_19/Enhanced Output Images/"
images = [
    "document1.jpg",
    "document2.jpg",
    "document3.png",
    "document4.jpeg",
    "document5.jpg",
    "document6.jpeg",
    "document7.jpg",
    "document8.jpg",
    "document9.jpg",
    "document10.jpg"
]
def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect
def correct_perspective(img):
    h, w, c = img.shape
    gray_temp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_temp = cv2.GaussianBlur(gray_temp, (5, 5), 0)
    edged = cv2.Canny(blur_temp, 75, 200)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
    doc_contour = None
    img_area = h * w
    for c_item in contours:
        peri = cv2.arcLength(c_item, True)
        approx = cv2.approxPolyDP(c_item, 0.02 * peri, True)
        if len(approx) == 4:
            if cv2.contourArea(approx) > (img_area * 0.15):
                doc_contour = approx
                break
    if doc_contour is not None:
        pts = doc_contour.reshape(4, 2)
        rect = order_points(pts)
        center = np.mean(rect, axis=0)
        rect = center + (rect - center) * 1.05
        (tl, tr, br, bl) = rect
        width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        max_width = max(int(width_a), int(width_b))
        height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        max_height = max(int(height_a), int(height_b))
        dst = np.array([
            [0, 0],
            [max_width - 1, 0],
            [max_width - 1, max_height - 1],
            [0, max_height - 1]
        ], dtype="float32")
        matrix = cv2.getPerspectiveTransform(rect, dst)
        return cv2.warpPerspective(img, matrix, (max_width, max_height))
    return img.copy()
def process_document(img):
    warp = correct_perspective(img)
    gray = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    bright = cv2.convertScaleAbs(blur, alpha=1.0, beta=35)
    contrast = cv2.convertScaleAbs(bright, alpha=1.3, beta=0)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharp = cv2.filter2D(contrast, -1, kernel)
    return warp, gray, blur, bright, contrast, sharp
print("Choose Document")
for i in range(len(images)):
    print(f"{i + 1}. {images[i].split('.')[0]}")
choice = int(input("\nEnter document number (1-10): "))
selected_image = images[choice - 1]
img_path = os.path.join(input_dir, selected_image)
img = cv2.imread(img_path)
warp, gray, blur, bright, contrast, sharp = process_document(img)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_filename = "enhanced_" + selected_image
output_path = os.path.join(output_dir, output_filename)
cv2.imwrite(output_path, sharp)
cv2.imshow("Original", img)
cv2.imshow("Perspective Corrected", warp)
cv2.imshow("Grayscale", gray)
cv2.imshow("Noise Removed", blur)
cv2.imshow("Brightness Enhanced", bright)
cv2.imshow("Contrast Enhanced", contrast)
cv2.imshow("Sharpened", sharp)
print(f"\nSaved successfully to: {output_path}")
print("Press any key on an image window to exit...")
cv2.waitKey(0)
cv2.destroyAllWindows()