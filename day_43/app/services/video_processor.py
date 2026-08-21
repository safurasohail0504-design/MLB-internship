from ultralytics import YOLO
from pathlib import Path
import cv2
import time


# Load custom YOLO model
MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "best.pt"

model = YOLO(str(MODEL_PATH))


def process_video(input_path, output_path, job_id, jobs):

    start_time = time.time()

    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        raise ValueError("Could not open video.")

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 25

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames <= 0:
        cap.release()
        raise ValueError("Video contains no frames.")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    if not out.isOpened():
        cap.release()
        raise ValueError("Could not create output video.")

    processed_frames = 0
    total_detections = 0

    try:

        while True:

            success, frame = cap.read()

            if not success:
                break

            # YOLO inference
            results = model(
                frame,
                conf=0.25,
                verbose=False
            )

            frame_detections = 0

            for result in results:

                for box in result.boxes:

                    class_id = int(box.cls[0])

                    class_name = result.names[class_id]

                    confidence = float(box.conf[0])

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0].tolist()
                    )

                    # Bounding box
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    # Label
                    label = f"{class_name} {confidence:.2f}"

                    cv2.putText(
                        frame,
                        label,
                        (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

                    frame_detections += 1

            processed_frames += 1
            total_detections += frame_detections

            # Frame information
            cv2.putText(
                frame,
                f"Frame: {processed_frames}/{total_frames}",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

            # Save frame
            out.write(frame)

            # Update progress
            jobs[job_id]["progress"] = int(
                (processed_frames / total_frames) * 100
            )

    finally:

        cap.release()
        out.release()

    processing_time = time.time() - start_time

    average_fps = (
        processed_frames / processing_time
        if processing_time > 0
        else 0
    )

    return {
        "total_frames": total_frames,
        "processed_frames": processed_frames,
        "total_detections": total_detections,
        "average_fps": round(average_fps, 2),
        "processing_time_seconds": round(processing_time, 2)
    }