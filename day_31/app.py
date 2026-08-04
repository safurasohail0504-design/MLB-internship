import streamlit as st
from ultralytics import YOLO
import cv2
import os

st.set_page_config(page_title="Vehicle Counting", page_icon="🚗")

st.title("🚗 Smart Vehicle Counting System")
st.write("Upload a traffic video to detect, track and count vehicles.")

model = YOLO("yolov8n.pt")

uploaded_video = st.file_uploader(
    "Upload Traffic Video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video is not None:

    input_video = "input_video.mp4"

    with open(input_video, "wb") as f:
        f.write(uploaded_video.read())

    cap = cv2.VideoCapture(input_video)

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = int(cap.get(5))

    output_video = "vehicle_count_output.mp4"

    out = cv2.VideoWriter(
        output_video,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    line_y = 300

    ids = []

    car = 0
    truck = 0
    bus = 0
    motorcycle = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model.track(frame, persist=True)

        boxes = results[0].boxes

        frame = results[0].plot()

        cv2.line(frame, (0, line_y), (width, line_y), (0,255,0), 3)

        if boxes.id is not None:

            for box, track_id in zip(boxes, boxes.id):

                track_id = int(track_id)

                x1, y1, x2, y2 = box.xyxy[0]

                center_y = int((y1 + y2) / 2)

                class_id = int(box.cls[0])

                class_name = model.names[class_id]

                if center_y > line_y:

                    if track_id not in ids:

                        ids.append(track_id)

                        if class_name == "car":
                            car += 1

                        elif class_name == "truck":
                            truck += 1

                        elif class_name == "bus":
                            bus += 1

                        elif class_name == "motorcycle":
                            motorcycle += 1

        total = car + truck + bus + motorcycle

        cv2.putText(frame, f"Cars : {car}", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        cv2.putText(frame, f"Trucks : {truck}", (20,80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

        cv2.putText(frame, f"Buses : {bus}", (20,120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

        cv2.putText(frame, f"Motorcycles : {motorcycle}", (20,160),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

        cv2.putText(frame, f"Total : {total}", (20,200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 3)

        out.write(frame)

    cap.release()
    out.release()

    st.success("Vehicle Counting Completed!")

    st.video(output_video)

    with open(output_video, "rb") as file:

        st.download_button(
            "⬇ Download Processed Video",
            file,
            file_name="vehicle_count_output.mp4"
        )

    os.remove(input_video)