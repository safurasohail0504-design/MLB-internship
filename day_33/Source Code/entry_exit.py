from ultralytics import YOLO
import cv2

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

inside=[]

entry=0

exit=0

max_people=0

while True:

    success,frame=cap.read()

    if not success:
        break

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

                    entry+=1

                    if track_id not in inside:
                        inside.append(track_id)

                elif old>line_x and center_x<=line_x:

                    exit+=1

                    if track_id in inside:
                        inside.remove(track_id)

                old_position[track_id]=center_x

    if len(inside)>max_people:
        max_people=len(inside)

    cv2.putText(frame,"Inside : "+str(len(inside)),(20,40),
    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame,"Entry : "+str(entry),(20,80),
    cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.putText(frame,"Exit : "+str(exit),(20,120),
    cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.putText(frame,"Max : "+str(max_people),(20,160),
    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

    writer.write(frame)

cap.release()

writer.release()
