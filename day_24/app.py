import streamlit as st
import easyocr
import cv2
import numpy as np
st.set_page_config(page_title="Simple OCR Document Reader")
st.title("Simple OCR Document Reader")
@st.cache_resource
def load_reader():
    return easyocr.Reader(["en"], gpu=False)
try:
    with st.spinner("Loading OCR Model..."):
        reader = load_reader()
except Exception as e:
    st.error("Unable to load OCR model.")
    st.stop()
uploaded_file = st.file_uploader("Upload Image",type=["jpg", "jpeg", "png"])
file_name = st.text_input("Enter File Name", "output")
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    st.subheader("Original Image")
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), use_container_width=True)
    with st.spinner("Extracting Text..."):
        result = reader.readtext(image)
    text = ""
    for detection in result:
        text += detection[1] + "\n"
    st.subheader("Extracted Text")
    st.text_area("", text, height=250)
    st.download_button(
        label="Download Text File",
        data=text.encode("utf-8"),
        file_name=file_name + ".txt",
        mime="text/plain"
    )