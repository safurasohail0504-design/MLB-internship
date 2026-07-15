import cv2
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
day_18_dir = os.path.dirname(script_dir)

img_path = os.path.join(day_18_dir, "sample images", "img2.jpg")
output_folder = os.path.join(day_18_dir, "processed output images")

img = cv2.imread(img_path)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("1. Show Original Image")
print("2. Convert to Grayscale")
print("3. Resize Image")
print("4. Rotate Image")
print("5. Flip Image")
print("6. Crop Image")
print("7. Draw Shapes")
print("8. Add Text")
print("9. Save Image")
print("10. Exit")

choice = input("Enter your choice: ")
if choice=="1":
    if img is None:
        print("Error: Could not load the image. Please verify img2.jpg exists in 'day_18/sample images'")
    else:
        cv2.imshow("Original",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
elif choice=="2":
    if img is None:
        print("Error: Could not load the image.")
    else:
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_folder, "grayscale.jpg")
        cv2.imwrite(save_path, gray)
        print("Grayscale image saved successfully to:", save_path)
        img = gray
elif choice == "3":
    if img is None:
        print("Error: Could not load the image.")
    else:
        width = int(input("Enter Width: "))
        height = int(input("Enter Height: "))
        img = cv2.resize(img, (width, height))
        cv2.imshow("Resized", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_folder, "resized.jpg")
        cv2.imwrite(save_path, img)
        print("Resized image saved successfully to:", save_path)
elif choice == "4":
    if img is None:
        print("Error: Could not load the image.")
    else:
        print("1. 90 Degree")
        print("2. 180 Degree")
        print("3. 270 Degree")
        r = input("Choose Rotation: ")
        if r == "1":
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            filename = "rotate90.jpg"
        elif r == "2":
            img = cv2.rotate(img, cv2.ROTATE_180)
            filename = "rotate180.jpg"
        elif r == "3":
            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            filename = "rotate270.jpg"
        cv2.imshow("Rotated",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_folder, filename)
        cv2.imwrite(save_path, img)
        print("Rotated image saved successfully to:", save_path)
elif choice=="5":
    if img is None:
        print("Error: Could not load the image.")
    else:
        print("1. Horizontal")
        print("2. Vertical")
        f = input("Choose Flip: ")
        if f == "1":
            img = cv2.flip(img, 1)
            filename = "flip_horizontal.jpg"
        elif f == "2":
            img = cv2.flip(img, 0)
            filename = "flip_vertical.jpg"
        cv2.imshow("Flipped", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_folder, filename)
        cv2.imwrite(save_path, img)
        print("Flipped image saved successfully to:", save_path)
elif choice=="6":
    if img is None:
        print("Error: Could not load the image.")
    else:
        y1 = int(input("Start Row: "))
        y2 = int(input("End Row: "))
        x1 = int(input("Start Column: "))
        x2 = int(input("End Column: "))
        img = img[y1:y2,x1:x2]
        cv2.imshow("cropped",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_folder, "cropped.jpg")
        cv2.imwrite(save_path, img)
        print("Cropped image saved successfully to:", save_path)
elif choice == "7":
    if img is None:
        print("Error: Could not load the image.")
    else:
        cv2.rectangle(img, (30,30), (200,180), (255,0,0), 3)
        cv2.circle(img, (300,150), 50, (0,255,0), 3)
        cv2.line(img, (20,250), (300,250), (0,0,255), 3)
        points=np.array([[350,50],[450,100],[400,200],[300,150]], np.int32)
        cv2.polylines(img,[points],True,(255,255,0),3)
        cv2.imshow("Shapes",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_folder, "shapes.jpg")
        cv2.imwrite(save_path, img)
        print("Shapes image saved successfully to:", save_path)
elif choice == "8":
    if img is None:
        print("Error: Could not load the image.")
    else:
        name = input("Enter Your Name: ")
        cv2.putText(img,name,(30,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.imshow("Text Added", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_folder, "text.jpg")
        cv2.imwrite(save_path, img)
        print("Text image saved successfully to:", save_path)
elif choice == "9":
    if img is None:
        print("Error: Could not load the image.")
    else:
        save_path = os.path.join(output_folder, "project-output.jpg")
        cv2.imwrite(save_path, img)
        print("Image Saved Successfully to:", save_path)
elif choice == "10":
    print("Program Closed")
    exit()
else:
    print("Invalid Choice")