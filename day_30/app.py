import streamlit as st
from ultralytics import YOLO
from pathlib import Path
import tempfile
import cv2
import os
st.set_page_config(
    page_title="Smart Object Tracking",
    page_icon="🎥",
    layout="centered"
)
st.title("🎥 Smart Object Tracking")
st.write("Upload a video to detect and track objects.")
MODEL_PATH = Path(__file__).parent / "best.pt"
@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))
try:
    model = load_model()
except Exception as e:
    st.error("Unable to load YOLO model.")
    st.exception(e)
    st.stop()
uploaded_video = st.file_uploader(
    "Upload Video",
    type=["mp4", "avi", "mov"]
)
if uploaded_video is not None:
    st.subheader("Original Video")
    st.video(uploaded_video)
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_input.write(uploaded_video.read())
    temp_input.close()
    cap = cv2.VideoCapture(temp_input.name)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 25
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    writer = cv2.VideoWriter(
        temp_output.name,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )
    unique_ids = set()
    progress = st.progress(0)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame = 0
    while True:
        ret, image = cap.read()
        if not ret:
            break
        results = model.track(
            image,
            persist=True,
            verbose=False
        )
        result = results[0]
        if result.boxes.id is not None:
            ids = result.boxes.id.cpu().numpy().astype(int)
            for obj_id in ids:
                unique_ids.add(obj_id)
        tracked = result.plot()
        writer.write(tracked)
        frame += 1
        if total_frames > 0:
            progress.progress(frame / total_frames)
    cap.release()
    writer.release()
    progress.empty()
    st.success("Tracking Completed!")
    st.subheader("Processed Video")
    st.video(temp_output.name)
    st.write(f"### Total Unique Objects: {len(unique_ids)}")
    if len(unique_ids) > 0:
        st.write("Tracked IDs:")
        st.write(sorted(list(unique_ids)))
    with open(temp_output.name, "rb") as file:
        st.download_button(
            "⬇ Download Processed Video",
            data=file,
            file_name="tracked_video.mp4",
            mime="video/mp4"
        )
    os.remove(temp_input.name)
st.markdown("---")
st.caption("Developed using Streamlit + Ultralytics YOLO Tracking")