import streamlit as st
import cv2
import tempfile
import time
from ultralytics import YOLO
model=YOLO("yolov8n.pt")
st.set_page_config(page_title="Smart Video Analytics",layout="wide")
st.title("🎥 Smart Video Analytics System")
uploaded_file=st.file_uploader("Upload Video",type=["mp4","avi","mov"])
if uploaded_file:
    temp=tempfile.NamedTemporaryFile(delete=False,suffix=".mp4")
    temp.write(uploaded_file.read())
    video_path=temp.name
    start=st.button("🚀 Start Processing")
    if start:
        st.info("Processing video...")
        cap=cv2.VideoCapture(video_path)
        fps=cap.get(cv2.CAP_PROP_FPS)
        width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if fps==0:
            fps=30
        writer=cv2.VideoWriter("Processed Output Videos/processed_video.mp4",cv2.VideoWriter_fourcc(*"mp4v"),fps,(width,height))
        unique_ids=set()
        old_position={}
        inside_line=set()
        total_entry=0
        total_exit=0
        max_objects=0
        frame_no=0
        line_y=height//2
        progress=st.progress(0)
        frame_placeholder=st.empty()
        while True:
            success,frame=cap.read()
            if not success:
                break
            frame_no+=1
            start_time=time.time()
            results=model.track(frame,persist=True,tracker="bytetrack.yaml",verbose=False)
            end_time=time.time()
            processing_fps=1/(end_time-start_time)
            annotated_frame=results[0].plot()
            current_count=0
            if results[0].boxes.id is not None:
                ids=results[0].boxes.id.int().cpu().tolist()
                current_count=len(ids)
                unique_ids.update(ids)
                for box in results[0].boxes:
                    if int(box.cls[0])!=0:
                        continue
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
            if current_count>max_objects:
                max_objects=current_count
            cv2.line(annotated_frame,(0,line_y),(width,line_y),(0,255,255),3)
            cv2.putText(annotated_frame,f"Current Objects: {current_count}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
            cv2.putText(annotated_frame,f"Unique Objects: {len(unique_ids)}",(20,70),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)
            cv2.putText(annotated_frame,f"Entries: {total_entry}",(20,100),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
            cv2.putText(annotated_frame,f"Exits: {total_exit}",(20,130),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
            cv2.putText(annotated_frame,f"FPS: {processing_fps:.1f}",(20,160),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)
            writer.write(annotated_frame)
            progress.progress(min(frame_no/total_frames,1.0))
            frame_placeholder.image(cv2.cvtColor(annotated_frame,cv2.COLOR_BGR2RGB),channels="RGB",use_container_width=True)
        cap.release()
        writer.release()
        st.success("✅ Processing Completed!")
        st.markdown("---")
        col1,col2=st.columns(2)
        with col1:
            st.metric("Current Objects",current_count)
            st.metric("Unique Objects",len(unique_ids))
            st.metric("Total Entries",total_entry)
        with col2:
            st.metric("Total Exits",total_exit)
            st.metric("Maximum Objects",max_objects)
            st.metric("Average FPS",f"{processing_fps:.1f}")
        st.markdown("---")
        st.subheader("🎥 Processed Video")
        st.video("Processed Output Videos/processed_video.mp4")