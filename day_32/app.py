import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
model=YOLO("yolov8n.pt")
st.title("Smart People Counting System")
uploaded_file=st.file_uploader("Upload Image or Video",type=["jpg","jpeg","png","mp4"])
if uploaded_file:
    temp=tempfile.NamedTemporaryFile(delete=False)
    temp.write(uploaded_file.read())
    path=temp.name
    if uploaded_file.type.startswith("image"):
        image=cv2.imread(path)
        results=model(image)
        frame=results[0].plot()
        people=0
        for box in results[0].boxes:
            if int(box.cls[0])==0:
                people+=1
        cv2.putText(frame,"People : "+str(people),(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        st.image(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    else:
        cap=cv2.VideoCapture(path)
        width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps=int(cap.get(cv2.CAP_PROP_FPS))
        writer=cv2.VideoWriter("output.mp4",cv2.VideoWriter_fourcc(*"mp4v"),fps,(width,height))
        max_people=0
        entry=0
        exit=0
        line=height//2
        ids={}
        while True:
            success,frame=cap.read()
            if not success:
                break
            results=model.track(frame,persist=True,tracker="bytetrack.yaml")
            frame=results[0].plot()
            people=0
            if results[0].boxes.id is not None:
                for box in results[0].boxes:
                    if int(box.cls[0])!=0:
                        continue
                    people+=1
                    track_id=int(box.id[0])
                    x1,y1,x2,y2=map(int,box.xyxy[0])
                    center=(y1+y2)//2
                    if track_id not in ids:
                        ids[track_id]=center
                    else:
                        old=ids[track_id]
                        if old<line and center>=line:
                            entry+=1
                        elif old>line and center<=line:
                            exit+=1
                        ids[track_id]=center
            if people>max_people:
                max_people=people
            cv2.line(frame,(0,line),(width,line),(0,0,255),2)
            cv2.putText(frame,"People : "+str(people),(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            cv2.putText(frame,"Entry : "+str(entry),(20,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
            cv2.putText(frame,"Exit : "+str(exit),(20,120),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            cv2.putText(frame,"Max : "+str(max_people),(20,160),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
            writer.write(frame)
        cap.release()
        writer.release()
        st.video("output.mp4")
        with open("output.mp4","rb") as file:
          st.download_button(
        label="Download Output Video",
        data=file,
        file_name="people_count.mp4",
        mime="video/mp4"
    )