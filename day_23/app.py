import streamlit as st
import cv2
import numpy as np
st.title("Computer Vision Image Processing Studio")
uploaded_file=st.file_uploader("Upload Image",type=["jpg","jpeg","png"])
operation=st.selectbox(
    "Select Operation",
    [
        "Grayscale",
        "Blur",
        "Edge Detection",
        "Rotation",
        "Brightness",
        "Contour Detection",
        "Image Flip",
        "Thresholding"
    ]
)
file_name=st.text_input("Enter File Name","processed_image")
if uploaded_file is not None:
    file_bytes=np.asarray(bytearray(uploaded_file.read()),dtype=np.uint8)
    image=cv2.imdecode(file_bytes,1)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    st.write("Original Image")
    st.image(image)
    if operation=="Grayscale":
        output=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    elif operation=="Blur":
        output=cv2.GaussianBlur(image,(9,9),0)
    elif operation=="Edge Detection":
        gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        blur=cv2.GaussianBlur(gray,(9,9),0)
        output=cv2.Canny(blur,100,200)
    elif operation=="Rotation":
        height,width,channel=image.shape
        matrix=cv2.getRotationMatrix2D((width/2,height/2),45,1)
        output=cv2.warpAffine(image,matrix,(width,height))
    elif operation=="Brightness":
        output=cv2.convertScaleAbs(image,beta=50)
    elif operation=="Contour Detection":
        gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        ret,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
        contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        output=image.copy()
        for contour in contours:
            area=cv2.contourArea(contour)
            if area<500:
                continue
            cv2.drawContours(output,[contour],-1,(0,255,0),2)
    elif operation=="Image Flip":
        output=cv2.flip(image,1)
    elif operation=="Thresholding":
        gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        ret,output=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    st.write("Processed Image")
    if len(output.shape)==2:
        st.image(output)
    else:
        st.image(output)
    if st.button("Save Image"):
        if len(output.shape)==2:
            save_image=output
        else:
            save_image=cv2.cvtColor(output,cv2.COLOR_RGB2BGR)
        path="Sample Output Images/"+file_name+".png"
        cv2.imwrite(path,save_image)
        with open(path,"rb") as file:
            st.download_button("Download Image",file,file_name=file_name+".png")