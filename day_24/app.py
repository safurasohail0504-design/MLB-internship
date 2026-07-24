import os
import gc
import torch
import cv2
import numpy as np
import streamlit as st
import easyocr
torch.set_num_threads(1)
st.set_page_config(page_title="Simple OCR Reader", layout="centered")
st.title("📄 Simple OCR Document Reader")
@st.cache_resource(show_spinner=False)
def load_ocr():
    return easyocr.Reader(['en'], gpu=False)
with st.spinner("Initializing OCR engine..."):
    reader = load_ocr()
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
file_name = st.text_input("Enter File Name", "extracted_text")
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    if image is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Image")
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            st.image(image_rgb)
        with col2:
            st.subheader("Extracted Text")
            with st.spinner("Reading text..."):
                results = reader.readtext(image)
                text = "\n".join([item[1] for item in results])
                st.text_area("", text, height=250)
                st.download_button(
                    label="Download Text File",
                    data=text.encode("utf-8"),
                    file_name=f"{file_name}.txt",
                    mime="text/plain"
                )
        del image, file_bytes
        gc.collect()