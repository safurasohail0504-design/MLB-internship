import cv2
import time

from app.services.detector import model


def process_video(input_path, output_path, job_id, jobs):

    start_time = time.time()

    # Open input video
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        raise ValueError("Could not open video.")

    # Get video information
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 25

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if width <= 0 or height <= 0:
        cap.release()
        raise ValueError("Invalid video dimensions.")

    if total_frames <= 0:
        cap.release()
        raise ValueError("Video contains no frames.")

    # Create output video
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

            # Run YOLO on current frame
            results = model(
                frame,
                conf=0.25,
                verbose=False
            )

            frame_detections = 0

            # Process YOLO results
            for result in results:

                for box in result.boxes:

                    class_id = int(box.cls[0])

                    class_name = result.names[class_id]

                    confidence = float(box.conf[0])

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0].tolist()
                    )

                    # Draw bounding box
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    # Detection label
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

            # Update counters
            processed_frames += 1
            total_detections += frame_detections

            # Display frame progress
            cv2.putText(
                frame,
                f"Frame: {processed_frames}/{total_frames}",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

            # Save processed frame
            out.write(frame)

            # Update job progress
            jobs[job_id]["progress"] = int(
                (processed_frames / total_frames) * 100
            )

    finally:

        cap.release()
        out.release()

    # Calculate processing statistics
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
