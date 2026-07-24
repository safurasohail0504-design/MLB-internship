import streamlit as st
import easyocr
import cv2
import numpy as np
st.title("Simple OCR Document Reader")
reader = easyocr.Reader(["en"])
uploaded_file = st.file_uploader("Upload Image",type=["jpg", "jpeg", "png"])
file_name = st.text_input("Enter File Name", "output")
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    st.subheader("Original Image")
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    result = reader.readtext(image)
    text = ""
    for detection in result:
        text += detection[1] + "\n"
    st.subheader("Extracted Text")
    st.text_area("", text, height=250)
    if st.button("Save Text File"):
        path = "Extracted Text Files/" + file_name + ".txt"
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)
        st.success("Text File Saved Successfully")
        with open(path, "rb") as file:
            st.download_button("Download Text File",file,file_name=file_name + ".txt")