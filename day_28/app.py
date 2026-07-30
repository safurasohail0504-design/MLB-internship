import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile

st.set_page_config(
    page_title="Smart Object Detection",
    page_icon="📷",
    layout="centered"
)

st.title("📷 Smart Object Detection")
st.write("Upload an image and detect objects using YOLOv8.")

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

uploaded_image = st.file_uploader(
    "Choose an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:

    image = Image.open(uploaded_image).convert("RGB")

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    image_array = np.array(image)

    with st.spinner("Detecting objects..."):
        results = model(image_array)

    result = results[0]

    detected_image = result.plot()
    detected_image = cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB)

    st.subheader("Detected Image")
    st.image(detected_image, use_container_width=True)

    st.subheader("Detected Objects")

    if len(result.boxes) == 0:
        st.info("No objects detected.")

    else:
        for box in result.boxes:

            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])

            st.write(
                f"**{class_name}** | Confidence: **{confidence:.2f}**"
            )

    output_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    cv2.imwrite(
        output_file.name,
        cv2.cvtColor(detected_image, cv2.COLOR_RGB2BGR)
    )

    with open(output_file.name, "rb") as file:

        st.download_button(
            label="⬇ Download Processed Image",
            data=file,
            file_name="processed_image.jpg",
            mime="image/jpeg"
        )