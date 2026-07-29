import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="Image Segmentation Tool")
st.title("Document & Object Segmentation Tool")
st.write("Upload an image and select a segmentation method.")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

method = st.selectbox(
    "Segmentation Method",
    [
        "Binary Threshold",
        "Adaptive Threshold",
        
        "Otsu Threshold",
        "Foreground Segmentation"
    ]
)

def segment(image, method):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if method == "Binary Threshold":
        _, result = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    elif method == "Adaptive Threshold":
        result = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

    elif method == "Otsu Threshold":
        _, result = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

    else:
        _, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        result = cv2.bitwise_and(image, image, mask=mask)

    return result

if uploaded_file:
    file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    output = segment(image, method)

    with col2:
        st.subheader("Segmented Image")
        st.image(output, use_container_width=True)

    if len(output.shape) == 2:
        success, buffer = cv2.imencode(".png", output)
    else:
        save_img = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
        success, buffer = cv2.imencode(".png", save_img)

    st.download_button(
        "Download Segmented Image",
        data=buffer.tobytes(),
        file_name="segmented_image.png",
        mime="image/png"
    )