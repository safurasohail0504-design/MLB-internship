import gradio as gr
import cv2
import numpy as np
def process_image(image,operation):
    if operation=="Grayscale":
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        return gray
    elif operation=="Blur":
        blur=cv2.GaussianBlur(image,(9,9),0)
        return blur
    elif operation=="Edge Detection":
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(9,9),0)
        canny=cv2.Canny(blur,100,200)
        return canny
    elif operation=="Rotation":
        height,width,chanel=image.shape
        matrix=cv2.getRotationMatrix2D((width/2,height/2),45,1)
        rotate=cv2.warpAffine(image,matrix,(width,height))
        return rotate
    elif operation=="Brightness":
        bright=cv2.convertScaleAbs(image,beta=50)
        return bright
    elif operation=="Contour Detection":
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
        contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        contour_image=image.copy()
        for contour in contours:
            area=cv2.contourArea(contour)
            if area<500:
                continue
            cv2.drawContours(contour_image,[contour],-1,(0,255,0),2)
        return contour_image
    elif operation=="Image Flip":
        flip=cv2.flip(image,1)
        return flip
    elif operation=="Thresholding":
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        return thresh

    return image
with gr.Blocks() as demo:
    gr.Markdown("""# Computer Vision Image Processing Studio
Upload an image, choose an image processing operation, and view the processed result instantly.""")
    with gr.Row():
        input_image=gr.Image(type="numpy",label="Upload Image")
        output_image=gr.Image(type="numpy",label="Processed Image")
    operation=gr.Dropdown(["Grayscale","Blur","Edge Detection","Rotation","Brightness","Contour Detection","Image Flip","Thresholding"],label="Select Operation")
    process_button=gr.Button(" Process Image")
    process_button.click(fn=process_image,inputs=[input_image,operation],outputs=output_image)
demo.launch()