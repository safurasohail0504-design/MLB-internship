import cv2
import os
print("IMAGE SELECTION:")
print("1. Landscape")
print("2. Person")
print("3. Vehicle")
print("4. Document")
print("5. Object")
image_choice = input("Choose an image: ")
image_path = ""
if image_choice == "1":
    image_path = "C:/Users/User/Documents/git/day_18/sample images/landscape.jpg"
elif image_choice == "2":
    image_path = "C:/Users/User/Documents/git/day_18/sample images/person.jpeg"
elif image_choice == "3":
    image_path = "C:/Users/User/Documents/git/day_18/sample images/vehicle.jpeg"
elif image_choice == "4":
    image_path = "C:/Users/User/Documents/git/day_18/sample images/document.jpeg"
elif image_choice == "5":
    image_path = "C:/Users/User/Documents/git/day_18/sample images/object.jpg"
else:
    print("Invalid choice")
    image_path = "C:/Users/User/Documents/git/day_18/sample images/landscape.jpg"
original_img = cv2.imread(image_path)
if original_img is None:
    print("Error: Could not load the image. Please verify the file path.")
    exit()
output_dir = "C:/Users/User/Documents/git/day_18/processed output images"
running = True
while running:
    print("1. Original Image")
    print("2. Grayscale")
    print("3. Resize")
    print("4. Rotate")
    print("5. Flip")
    print("6. Crop")
    print("7. Draw Shapes")
    print("8. Add Text")
    print("9. Save Original Image")
    print("10. Exit")
    op_choice = input("Choose an operation (1-10): ")
    if op_choice == "1":
        cv2.imshow("Original Image", original_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif op_choice == "2":
        gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale Image", gray_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_dir, "grayscale.jpg")
        cv2.imwrite(save_path, gray_img)
        print("Saved to:", save_path)   
    elif op_choice == "3":
        width = int(input("Enter new width in pixels: "))
        height = int(input("Enter new height in pixels: "))
        resized_img = cv2.resize(original_img, (width, height))
        cv2.imshow("Resized Image", resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_dir, "resized.jpg")
        cv2.imwrite(save_path, resized_img)
        print("Saved to:", save_path)
    elif op_choice == "4":
        print("1. 90 Degrees")
        print("2. 180 Degrees")
        print("3. 270 Degrees")
        rot_choice = input("Choose rotation: ")       
        if rot_choice == "1":
            rotated_img = cv2.rotate(original_img, cv2.ROTATE_90_CLOCKWISE)
            filename = "rotate90.jpg"
        elif rot_choice == "2":
            rotated_img = cv2.rotate(original_img, cv2.ROTATE_180)
            filename = "rotate180.jpg"
        elif rot_choice == "3":
            rotated_img = cv2.rotate(original_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            filename = "rotate270.jpg"
        else:
            rotated_img = original_img.copy()
            filename = "rotate_default.jpg"
            print("Invalid rotation selected.") 
        cv2.imshow("Rotated Image", rotated_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_dir, filename)
        cv2.imwrite(save_path, rotated_img)
        print("Saved to:", save_path)      
    elif op_choice == "5":
        print("1. Horizontal")
        print("2. Vertical")
        flip_choice = input("Choose flip direction: ")     
        if flip_choice == "1":
            flipped_img = cv2.flip(original_img, 1)
            filename = "flip_horizontal.jpg"
        elif flip_choice == "2":
            flipped_img = cv2.flip(original_img, 0)
            filename = "flip_vertical.jpg"
        else:
            flipped_img = original_img.copy()
            filename = "flip_default.jpg"
            print("Invalid flip option selected.")       
        cv2.imshow("Flipped Image", flipped_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_dir, filename)
        cv2.imwrite(save_path, flipped_img)
        print("Saved to:", save_path)   
    elif op_choice == "6":
        img_height, img_width = original_img.shape[:2]
        print("Image dimensions: Width =", img_width, "Height =", img_height)
        start_row = int(input("Enter Start Row (Y start): "))
        end_row = int(input("Enter End Row (Y end): "))
        start_col = int(input("Enter Start Column (X start): "))
        end_col = int(input("Enter End Column (X end): "))     
        cropped_img = original_img[start_row:end_row, start_col:end_col]
        cv2.imshow("Cropped Image", cropped_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_dir, "cropped.jpg")
        cv2.imwrite(save_path, cropped_img)
        print("Saved to:", save_path)  
    elif op_choice == "7":
        shapes_img = original_img.copy()
        cv2.rectangle(shapes_img, (50, 50), (200, 200), (0, 0, 255), 3)
        cv2.circle(shapes_img, (150, 150), 40, (0, 255, 0), -1)
        cv2.line(shapes_img, (10, 10), (300, 10), (255, 0, 0), 4)
        import numpy as np
        pts = np.array([[10, 50], [50, 10], [120, 20], [120, 80]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(shapes_img, [pts], True, (255, 255, 0), 2)
        cv2.imshow("Draw Shapes", shapes_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_dir, "shapes.jpg")
        cv2.imwrite(save_path, shapes_img)
        print("Saved to:", save_path)
    elif op_choice == "8":
        user_name = input("Enter your name: ")
        text_img = original_img.copy()
        cv2.putText(text_img, user_name, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3, cv2.LINE_AA)
        cv2.imshow("Add Text", text_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_path = os.path.join(output_dir, "text.jpg")
        cv2.imwrite(save_path, text_img)
        print("Saved to:", save_path)
    elif op_choice == "9":
        save_path = os.path.join(output_dir, "original_saved.jpg")
        cv2.imwrite(save_path, original_img)
        print("Saved Original Image to:", save_path)      
    elif op_choice == "10":
        print("Exiting Toolkit.")
        running = False      
    else:
        print("Invalid choice. Try again.")