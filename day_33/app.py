import streamlit as st
import cv2
import tempfile
import csv
import os
from ultralytics import YOLO
model=YOLO("yolov8n.pt")
st.set_page_config(page_title="Smart Security Monitoring",layout="wide")
st.title("👮 AI Smart Security Monitoring System")
st.markdown("""
### Supported Videos
Upload a landscape CCTV or surveillance style video.
Recommended:
- Static camera
- People entering/leaving an area
- MP4 format
""")
uploaded_file=st.file_uploader("Upload Video",type=["mp4","avi","mov"])
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
        results=model.track(frame,tracker="bytetrack.yaml",persist=True)
        frame=results[0].plot()
        cv2.line(frame,(line_x,0),(line_x,height),(0,255,255),3)
        if results[0].boxes.id is not None:
            for box in results[0].boxes:
                if int(box.cls[0])!=0:
                    continue
                if box.id is None:
                    continue
                track_id=int(box.id[0])
                x1,y1,x2,y2=map(int,box.xyxy[0])
                center_x=(x1+x2)//2
                if track_id not in old_position:
                    old_position[track_id]=center_x
                else:
                    old=old_position[track_id]
                    if old<line_x and center_x>=line_x:
                        total_entry+=1
                        if track_id not in inside:
                            inside.append(track_id)
                        entry_time[track_id]=current_time
                        csv_writer.writerow([track_id,"Entry",current_time,"-"])
                        person=frame[y1:y2,x1:x2]
                        if person.size!=0:
                            cv2.imwrite("snapshots/person_"+str(track_id)+".jpg",person)
                    elif old>line_x and center_x<=line_x:
                        total_exit+=1
                        stay=0
                        if track_id in entry_time:
                            stay=round(current_time-entry_time[track_id],2)
                            stay_times.append(stay)
                        csv_writer.writerow([track_id,"Exit",current_time,stay])
                        if track_id in inside:
                            inside.remove(track_id)
                    old_position[track_id]=center_x
        if len(inside)>max_people:
            max_people=len(inside)
        cv2.putText(frame,"Inside : "+str(len(inside)),(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.putText(frame,"Entry : "+str(total_entry),(20,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv2.putText(frame,"Exit : "+str(total_exit),(20,120),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.putText(frame,"Maximum : "+str(max_people),(20,160),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
        writer.write(frame)
    cap.release()
    writer.release()
    csv_file.close()
    average_time=0
    if len(stay_times)>0:
        average_time=round(sum(stay_times)/len(stay_times),2)
    st.success("Processing Completed")
    st.subheader("Summary")
    st.write("Current Maximum Occupancy :",max_people)
    st.write("Total Entries :",total_entry)
    st.write("Total Exits :",total_exit)
    st.write("Average Stay Time :",average_time,"seconds")
    st.video("output.mp4")
    with open("output.mp4","rb") as file:
        st.download_button(label=" Download Processed Video",
        data=file,file_name="security_output.mp4",mime="video/mp4")
    with open("events.csv","rb") as file:
        st.download_button(label=" Download Event Log (CSV)",
        data=file,file_name="events.csv",mime="text/csv")