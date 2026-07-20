import cv2
import numpy as np
images = [
    "document1.jpg",
    "document2.jpeg",
    "document3.jpg",
    "document4.jpg",
    "document5.jpg",
    "document6.jpg",
    "document7.jpg",
    "document8.png",
    "document9.jpg",
    "document10.jpg"
]
for image in images:
    path = "input images/" + image
    img = cv2.imread(path)
    if img is None:
        print(image, "not found!")
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    canny = cv2.Canny(blur, 50, 150)
    kernel = np.ones((7, 7), np.uint8)
    closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
    closing = cv2.dilate(closing, kernel, iterations=1)
    closing = cv2.erode(closing, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(
        closing,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    document = None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 5000:
            continue
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
        if len(approx) == 4:
            document = approx
            break
    if document is not None:
        cv2.drawContours(img, [document], -1, (0, 255, 0), 3)
        print(image, "Document Found")
    else:
        print(image, "Document Not Found")
    output = "output images/boundary_" + image
    cv2.imwrite(output, img)
    cv2.imshow(image, img)
cv2.waitKey(0)
cv2.destroyAllWindows()