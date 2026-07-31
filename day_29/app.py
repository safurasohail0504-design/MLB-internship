import io
from pathlib import Path
import cv2
import numpy as np
import streamlit as st
from PIL import Image
from ultralytics import YOLO
st.set_page_config(
    page_title="Custom Helmet Detection",
    page_icon="⛑️",
    layout="centered",
)
st.title("⛑️ Custom Helmet Detection System")
st.write("Upload an image to detect helmets using your trained YOLOv8 model.")
MODEL_PATH = Path(__file__).parent / "best.pt"
@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))
try:
    with st.spinner("Loading YOLO model..."):
        model = load_model()
except Exception as e:
    st.error("Unable to load YOLO model.")
    st.exception(e)
    st.stop()
uploaded_image = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"],
)
if uploaded_image is not None:
    image = Image.open(uploaded_image).convert("RGB")
    st.subheader("Original Image")
    st.image(image, use_container_width=True)
    image_array = np.array(image)
    with st.spinner("Running Detection..."):
        results = model.predict(image_array, verbose=False)
    result = results[0]
    detected_image = result.plot()
    detected_image = cv2.cvtColor(
        detected_image,
        cv2.COLOR_BGR2RGB,
    )
    st.subheader("Detected Image")
    st.image(detected_image, use_container_width=True)
    total = len(result.boxes)
    st.success(f"Total Objects Detected: {total}")
    if total == 0:
        st.warning("No helmets detected.")
    else:
        st.subheader("Detection Details")
        for i, box in enumerate(result.boxes, start=1):
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = model.names.get(class_id, str(class_id))
            st.write(
                f"**{i}. {class_name}** — Confidence: **{confidence:.2%}**"
            )
    output_image = Image.fromarray(detected_image)
    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")
    st.download_button(
        label="📥 Download Detected Image",
        data=buffer.getvalue(),
        file_name="helmet_detection_result.png",
        mime="image/png",
        use_container_width=True,
    )
st.markdown("---")
st.caption("Developed using Streamlit + Ultralytics YOLOv8")