import cv2
image1=cv2.imread("Sample Image Pairs/pair1/book1.jpg")
image2=cv2.imread("Sample Image Pairs/pair1/book2.jpg")
gray1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
orb=cv2.ORB_create()
keypoints1,descriptors1=orb.detectAndCompute(gray1,None)
keypoints2,descriptors2=orb.detectAndCompute(gray2,None)
bf=cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.knnMatch(descriptors1, descriptors2, k=2)
good_matches = []
for first, second in matches:
    if first.distance < 0.75 * second.distance:
        good_matches.append(first)
output = cv2.drawMatches(image1,keypoints1,image2,keypoints2,good_matches,None)
cv2.imwrite("Output Images/pair1_knn.jpg",output)
print("Image 1 Keypoints:",len(keypoints1))
print("Image 2 Keypoints:",len(keypoints2))
print("Good Matches:",len(good_matches))