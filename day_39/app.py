import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os
import cv2

st.set_page_config(page_title="Shoe Detection AI", page_icon="👟", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pt")

model = YOLO(MODEL_PATH)

st.title("👟 Shoe Detection AI")
st.write("Custom YOLO model trained to detect shoes in images and videos.")

confidence = st.slider("Confidence Threshold", 0.10, 0.90, 0.25, 0.05)

input_type = st.radio("Choose Input", ["Image", "Video"], horizontal=True)

if input_type == "Image":

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")

        results = model.predict(
            image,
            conf=confidence,
            imgsz=512,
            verbose=False
        )

        result = results[0]
        output_image = result.plot()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)

        with col2:
            st.subheader("Detection Result")
            st.image(output_image, channels="BGR", use_container_width=True)

        detections = len(result.boxes)

        st.subheader("Detection Statistics")

        c1, c2, c3 = st.columns(3)

        c1.metric("Shoes Detected", detections)

        if detections > 0:
            confidences = result.boxes.conf.cpu().numpy()
            average_confidence = float(confidences.mean())
            highest_confidence = float(confidences.max())
        else:
            average_confidence = 0
            highest_confidence = 0

        c2.metric("Average Confidence", f"{average_confidence:.2f}")
        c3.metric("Highest Confidence", f"{highest_confidence:.2f}")

        if detections > 0:
            st.success(f"{detections} shoe(s) detected.")
        else:
            st.warning("No shoes detected at the selected confidence threshold.")

        success, buffer = cv2.imencode(".jpg", output_image)

        if success:
            st.download_button(
                "Download Prediction",
                data=buffer.tobytes(),
                file_name="shoe_prediction.jpg",
                mime="image/jpeg"
            )

else:

    uploaded_video = st.file_uploader(
        "Upload a short video",
        type=["mp4", "avi", "mov", "mkv"]
    )

    if uploaded_video is not None:

        temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp_input.write(uploaded_video.read())
        temp_input.close()

        output_path = os.path.join(
            tempfile.gettempdir(),
            "shoe_detection_output.mp4"
        )

        cap = cv2.VideoCapture(temp_input.name)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        if fps <= 0:
            fps = 25

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(
            output_path,
            fourcc,
            fps,
            (width, height)
        )

        total_frames = 0
        frames_with_detections = 0
        total_detections = 0

        progress = st.progress(0)

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            results = model.predict(
                frame,
                conf=confidence,
                imgsz=512,
                verbose=False
            )

            result = results[0]

            detections = len(result.boxes)

            total_frames += 1
            total_detections += detections

            if detections > 0:
                frames_with_detections += 1

            output_frame = result.plot()

            writer.write(output_frame)

            if total_frames % 5 == 0:
                progress.progress(min((total_frames % 100) / 100, 1.0))

        cap.release()
        writer.release()

        progress.progress(1.0)

        st.success("Video processing completed.")

        col1, col2, col3 = st.columns(3)

        col1.metric("Frames Processed", total_frames)
        col2.metric("Total Detections", total_detections)
        col3.metric("Frames With Shoes", frames_with_detections)

        with open(output_path, "rb") as video_file:
            st.download_button(
                "Download Processed Video",
                data=video_file.read(),
                file_name="shoe_detection_output.mp4",
                mime="video/mp4"
            )
        os.unlink(temp_input.name)
