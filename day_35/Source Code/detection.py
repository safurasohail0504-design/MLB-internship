from ultralytics import YOLO
import cv2
import time
model=YOLO("yolov8n.pt")
cap=cv2.VideoCapture("Sample Input Videos/video1.mp4")
fps=cap.get(cv2.CAP_PROP_FPS)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer=cv2.VideoWriter("Processed Output Videos/processed_video.mp4",cv2.VideoWriter_fourcc(*"mp4v"),fps,(width,height))
unique_ids=set()
old_position={}
inside_line=set()
total_entry=0
total_exit=0
max_objects=0
line_y=height//2
frame_no=0
while True:
    success,frame=cap.read()
    if not success:
        break
    frame_no+=1
    print("Processing frame:",frame_no)
    start_time=time.time()
    results=model.track(frame,persist=True,tracker="bytetrack.yaml")
    end_time=time.time()
    processing_fps=1/(end_time-start_time)
    annotated_frame=results[0].plot()
    current_count=0
    if results[0].boxes.id is not None:
        ids=results[0].boxes.id.int().cpu().tolist()
        current_count=len(ids)
        unique_ids.update(ids)
        for box in results[0].boxes:
            if box.id is None:
                continue
            track_id=int(box.id[0])
            x1,y1,x2,y2=map(int,box.xyxy[0])
            center_x=(x1+x2)//2
            center_y=(y1+y2)//2
            if track_id not in old_position:
                old_position[track_id]=center_y
            else:
                old=old_position[track_id]
                if old<line_y and center_y>=line_y:
                    total_entry+=1
                    inside_line.add(track_id)
                elif old>line_y and center_y<=line_y:
                    total_exit+=1
                    if track_id in inside_line:
                        inside_line.remove(track_id)
                old_position[track_id]=center_y
    if len(inside_line)>max_objects:
        max_objects=len(inside_line)
    cv2.line(annotated_frame,(0,line_y),(width,line_y),(0,255,255),3)
    cv2.putText(annotated_frame,f"FPS: {processing_fps:.1f}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    cv2.putText(annotated_frame,f"Current: {current_count}",(20,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
    cv2.putText(annotated_frame,f"Unique: {len(unique_ids)}",(20,110),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
    cv2.putText(annotated_frame,f"Entry: {total_entry}",(20,145),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    cv2.putText(annotated_frame,f"Exit: {total_exit}",(20,180),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.putText(annotated_frame,f"Maximum: {max_objects}",(20,215),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)
    writer.write(annotated_frame)
cap.release()
writer.release()
print("Unique Objects:",len(unique_ids))
print("Total Entries:",total_entry)
print("Total Exits:",total_exit)
print("Maximum Objects:",max_objects)