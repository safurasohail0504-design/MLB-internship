from ultralytics import YOLO
import cv2
import csv

model=YOLO("yolov8n.pt")

cap=cv2.VideoCapture("Sample Input Videos/video1.mp4")

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=int(cap.get(cv2.CAP_PROP_FPS))

writer=cv2.VideoWriter(
"Processed Output Videos/roi_video.mp4",
cv2.VideoWriter_fourcc(*"mp4v"),
fps,
(width,height)
)

line_x=380

old_position={}

csv_file=open("events.csv","w",newline="")
csv_writer=csv.writer(csv_file)

csv_writer.writerow(["Track ID","Event","Frame"])

frame_no=0

while True:

    success,frame=cap.read()

    if not success:
        break

    frame_no+=1

    results=model.track(
        frame,
        tracker="bytetrack.yaml",
        persist=True
    )

    frame=results[0].plot()

    cv2.line(frame,(line_x,0),(line_x,height),(0,255,255),3)

    if results[0].boxes.id is not None:

        for box in results[0].boxes:

            if int(box.cls[0])!=0:
                continue

            track_id=int(box.id[0])

            x1,y1,x2,y2=map(int,box.xyxy[0])

            center_x=(x1+x2)//2

            if track_id not in old_position:

                old_position[track_id]=center_x

            else:

                old=old_position[track_id]

                if old<line_x and center_x>=line_x:

                    csv_writer.writerow([track_id,"Entry",frame_no])

                elif old>line_x and center_x<=line_x:

                    csv_writer.writerow([track_id,"Exit",frame_no])

                old_position[track_id]=center_x

    writer.write(frame)

cap.release()
writer.release()
csv_file.close()

print("Event log saved.")