import streamlit as st
import cv2
import tempfile
import csv
import os
import time
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
st.set_page_config(page_title="AI Smart Security Monitoring",layout="wide")
st.title("👮 AI Smart Security Monitoring System")
st.markdown("""
## 📌 Instructions
1. Upload a CCTV or surveillance video.
2. Adjust the **Confidence Threshold**.
3. Adjust the **ROI (Region of Interest)**.
4. Click **Start Monitoring**.
### Recommended Video
- Static Camera
- MP4 Format
- Landscape Video
- Clear visibility
""")
st.sidebar.header("⚙ Detection Settings")
confidence = st.sidebar.slider("Confidence Threshold",0.10,1.00,0.40,0.05)
st.sidebar.markdown("---")
uploaded_file = st.file_uploader("📂 Upload CCTV Video",type=["mp4", "avi", "mov"])
if uploaded_file:
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(uploaded_file.read())
    video_path = temp.name
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    line_x = width //2
    old_position = {}
    inside = []
    entry_time = {}
    stay_times = []
    total_entry = 0
    total_exit = 0
    max_people = 0
    frame_no = 0
    if fps == 0:
        fps = 30
    st.sidebar.subheader("ROI Selection")
    roi_x1 = st.sidebar.slider("ROI Left",0,width,0)
    roi_x2 = st.sidebar.slider("ROI Right",0,width,width)
    roi_y1 = st.sidebar.slider("ROI Top",0,height,0)
    roi_y2 = st.sidebar.slider("ROI Bottom",0,height,height)
    start = st.button("🚀 Start Monitoring")
    if start:
        writer = cv2.VideoWriter("output.mp4",cv2.VideoWriter_fourcc(*"mp4v"),fps,(width, height))
        if not os.path.exists("snapshots"):
            os.makedirs("snapshots")
        csv_file = open("events.csv", "w", newline="")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Track ID","Event","Time(s)","Stay(s)"])
        progress = st.progress(0)
        frame_placeholder = st.empty()
if uploaded_file:
    temp=tempfile.NamedTemporaryFile(delete=False)
    temp.write(uploaded_file.read())
    video_path=temp.name
    cap=cv2.VideoCapture(video_path)
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps=int(cap.get(cv2.CAP_PROP_FPS))
    if fps==0:
        fps=30
    writer=cv2.VideoWriter("output.mp4",cv2.VideoWriter_fourcc(*"mp4v"),fps,(width,height))
    if not os.path.exists("snapshots"):
        os.makedirs("snapshots")
    csv_file=open("events.csv","w",newline="")
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(["Track ID","Event","Time(s)","Stay(s)"])
    line_x=width//2
    old_position={}
    inside=[]
    entry_time={}
    stay_times=[]
    total_entry=0
    total_exit=0
    max_people=0
    frame_no=0
    while True:
        success,frame=cap.read()
        if not success:
            break
        frame_no+=1
        current_time=round(frame_no/fps,2)
        results=model.track(frame,tracker="bytetrack.yaml",persist=True,conf=confidence,iou=iou_threshold)
        frame = results[0].plot()
        cv2.line(frame, (line_x, 0), (line_x, height), (0, 255, 255), 3)
        cv2.rectangle(frame,(roi_x1, roi_y1),(roi_x2, roi_y2),(255, 255, 0),2)
        if results[0].boxes.id is not None:
            for box in results[0].boxes:
                if int(box.cls[0]) != 0:
                    continue
                if box.id is None:
                    continue
                track_id = int(box.id[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                if not (roi_x1 <= center_x <= roi_x2 and roi_y1 <= center_y <= roi_y2):
                    continue
                if track_id not in entry_time:
                    entry_time[track_id] = current_time
                stay_now = round(current_time - entry_time[track_id], 2)
                cv2.putText(frame,f"{stay_now:.1f}s",(x1, y1 - 10),cv2.FONT_HERSHEY_SIMPLEX,0.55,(0,255,255),2)
                if track_id not in old_position:
                    old_position[track_id] = center_x
                else:
                    old = old_position[track_id]
                    if old < line_x and center_x >= line_x:
                        total_entry += 1
                        if track_id not in inside:
                            inside.append(track_id)
                            csv_writer.writerow([track_id,"Entry",current_time,"-"])
                            person = frame[y1:y2, x1:x2]
                            if person.size != 0:
                                cv2.imwrite(f"snapshots/person_{track_id}_{frame_no}.jpg",person)
                    elif old > line_x and center_x <= line_x:
                        total_exit += 1
                        stay = round(current_time - entry_time.get(track_id, current_time),2)
                        stay_times.append(stay)
                        csv_writer.writerow([track_id,"Exit",current_time,stay])
                        if track_id in inside:
                            inside.remove(track_id)
                    old_position[track_id] = center_x
        if len(inside) > max_people:
            max_people = len(inside)
        cv2.rectangle(frame, (10,10), (360,190), (0,0,0), -1)
        cv2.putText(frame,f"Inside : {len(inside)}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
        cv2.putText(frame,f"Entry : {total_entry}",(20,70),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
        cv2.putText(frame,f"Exit : {total_exit}",(20,100),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
        cv2.putText(frame,f"Maximum : {max_people}",(20,130),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)
        cv2.putText(frame,f"Time : {current_time:.1f}s",(20,160),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
        cv2.rectangle(frame,(width-340,10),(width-10,220),(0,0,0),-1)
        cv2.putText(frame,"Recent Events",(width-330,35),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)
        y = 60
        try:
            with open("events.csv", "r") as f:
                rows = list(csv.reader(f))[1:]
                rows = rows[-6:]
                for r in rows:
                    txt = f"ID {r[0]} {r[1]}"
                    cv2.putText(frame,txt,(width-330,y),cv2.FONT_HERSHEY_SIMPLEX,0.55,(255,255,255),1)
                    y += 25
        except:
            pass
        writer.write(frame)
    progress.progress(min(frame_no / total_frames, 1.0))
    frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),channels="RGB",use_container_width=True)
    cap.release()
    writer.release()
    csv_file.close()
    average_time = 0
    if len(stay_times) > 0:
        average_time = round(sum(stay_times) / len(stay_times),2)
    st.success("✅ Processing Completed Successfully!")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("👤 Maximum Occupancy",max_people)
        st.metric("➡ Total Entries",total_entry)
    with col2:
        st.metric("⬅ Total Exits",total_exit)
        st.metric("⏱ Average Stay Time",f"{average_time} sec")
    st.markdown("---")
    st.subheader("🎥 Processed Video")
    st.video("output.mp4")
    st.subheader("📄 Live Event Log")
    try:
        import pandas as pd
        df = pd.read_csv("events.csv")
        st.dataframe(df,use_container_width=True)
    except:
        st.info("No events recorded.")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        with open("output.mp4", "rb") as file:
            st.download_button(label="⬇ Download Processed Video",data=file,file_name="security_output.mp4",mime="video/mp4")
    with col2:
        with open("events.csv", "rb") as file:
            st.download_button(label="⬇ Download Event Log",data=file,file_name="events.csv",mime="text/csv")
    st.markdown("---")
    st.success("Snapshots are saved inside 📂 snapshots/")