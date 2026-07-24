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
        text_bytes = text.encode("utf-8")
        st.download_button(label="Download Text File",data=text_bytes,file_name=file_name + ".txt",mime="text/plain")