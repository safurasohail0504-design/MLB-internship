import os
import csv
import time
import cv2
import tempfile
import pandas as pd
import streamlit as st
from ultralytics import YOLO

st.set_page_config(page_title="Smart Video Analytics", page_icon="🎥", layout="wide")

OUTPUT_DIR = "Processed Output Videos"
EVENT_DIR = "Events"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(EVENT_DIR, exist_ok=True)

@st.cache_resource
def load_model(): return YOLO("yolov8n.pt")

def get_video_info(path): cap = cv2.VideoCapture(path); fps = cap.get(cv2.CAP_PROP_FPS) or 30; frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)); cap.release(); return fps, frames, w, h

def make_roi(w, h, mode, x, y, rw, rh): return (0, 0, w, h) if mode == "Full Frame" else ((int((w-rw)/2), int((h-rh)/2), rw, rh) if mode == "Center" else (x, y, rw, rh))

def inside_roi(cx, cy, roi): x, y, w, h = roi; return x <= cx <= x+w and y <= cy <= y+h

def event_direction(previous, current): return "entry" if not previous and current else ("exit" if previous and not current else "")

def write_events(path, events): pd.DataFrame(events, columns=["frame","track_id","event","timestamp"]).to_csv(path, index=False)

def safe_writer(path, fps, w, h): return cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

def process_video(input_path, output_path, events_path, model, imgsz, frame_skip, roi_mode, roi_values, progress=None):
    cap = cv2.VideoCapture(input_path)
    source_fps = cap.get(cv2.CAP_PROP_FPS) or 30
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 1
    src_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    src_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    roi = make_roi(src_w, src_h, roi_mode, *roi_values)
    writer = safe_writer(output_path, source_fps, src_w, src_h)
    if not writer.isOpened(): raise RuntimeError("Could not create processed video.")
    active = set()
    previous_states = {}
    unique_ids = set()
    events = []
    max_objects = 0
    frame_count = 0
    processed_count = 0
    inference_total = 0.0
    start = time.perf_counter()
    last_result = None
    while True:
        ok, frame = cap.read()
        if not ok: break
        frame_count += 1
        if frame_skip > 0 and frame_count % (frame_skip + 1) != 1:
            if last_result is not None:
                annotated = last_result.plot()
                cv2.rectangle(annotated, (roi[0], roi[1]), (roi[0]+roi[2], roi[1]+roi[3]), (0,255,255), 2)
                writer.write(annotated)
            else:
                cv2.rectangle(frame, (roi[0], roi[1]), (roi[0]+roi[2], roi[1]+roi[3]), (0,255,255), 2)
                writer.write(frame)
            continue
        t0 = time.perf_counter()
        results = model.track(frame, persist=True, imgsz=imgsz, classes=[0,2,5,7], verbose=False, tracker="bytetrack.yaml")
        inference_total += time.perf_counter() - t0
        last_result = results[0]
        current = set()
        if last_result.boxes is not None and len(last_result.boxes) > 0:
            boxes = last_result.boxes
            ids = boxes.id.int().cpu().tolist() if boxes.id is not None else list(range(len(boxes)))
            xyxy = boxes.xyxy.int().cpu().tolist()
            names = last_result.names
            for track_id, box, cls in zip(ids, xyxy, boxes.cls.int().cpu().tolist()):
                x1,y1,x2,y2 = box
                cx, cy = int((x1+x2)/2), int((y1+y2)/2)
                if inside_roi(cx, cy, roi): current.add(track_id)
                unique_ids.add(track_id)
                previous = previous_states.get(track_id, False)
                now_inside = inside_roi(cx, cy, roi)
                direction = event_direction(previous, now_inside)
                if direction:
                    timestamp = frame_count / source_fps
                    events.append([frame_count, track_id, direction, round(timestamp,2)])
                previous_states[track_id] = now_inside
        active = current
        max_objects = max(max_objects, len(active))
        annotated = last_result.plot()
        cv2.rectangle(annotated, (roi[0], roi[1]), (roi[0]+roi[2], roi[1]+roi[3]), (0,255,255), 2)
        cv2.putText(annotated, f"Current Objects: {len(active)}", (20,35), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        cv2.putText(annotated, f"Unique Objects: {len(unique_ids)}", (20,70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        cv2.putText(annotated, f"FPS: {processed_count/(time.perf_counter()-start):.1f}", (20,105), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        writer.write(annotated)
        processed_count += 1
        if progress: progress(min(frame_count/total_frames,1.0))
    cap.release()
    writer.release()
    elapsed = time.perf_counter() - start
    avg_fps = frame_count / elapsed if elapsed else 0
    write_events(events_path, events)
    return {"total_objects":len(unique_ids),"entries":sum(1 for e in events if e[2]=="entry"),"exits":sum(1 for e in events if e[2]=="exit"),"max_objects":max_objects,"avg_fps":avg_fps,"processing_time":elapsed,"inference_time":inference_total,"frames":frame_count,"roi":roi}

def show_summary(summary): 
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.metric("Total Objects", summary["total_objects"])
    c2.metric("Total Entries", summary["entries"])
    c3.metric("Total Exits", summary["exits"])
    c4.metric("Maximum Objects in ROI", summary["max_objects"])
    c5.metric("Average FPS", f'{summary["avg_fps"]:.2f}')

def save_uploaded(uploaded): suffix = os.path.splitext(uploaded.name)[1] or ".mp4"; fd,path=tempfile.mkstemp(suffix=suffix); os.close(fd); open(path,"wb").write(uploaded.getbuffer()); return path

def run_configuration(input_path, label, imgsz, skip, roi_mode, roi_values, model):
    out = os.path.join(OUTPUT_DIR, f"processed_{label}.mp4")
    ev = os.path.join(EVENT_DIR, f"events_{label}.csv")
    bar = st.progress(0)
    result = process_video(input_path,out,ev,model,imgsz,skip,roi_mode,roi_values,bar.progress)
    bar.empty()
    result["configuration"] = label
    result["image_size"] = imgsz
    result["frame_skip"] = skip
    result["output"] = out
    result["events"] = ev
    return result

def show_downloads(summary):
    out = summary["output"]
    ev = summary["events"]
    if os.path.exists(out):
        with open(out,"rb") as f: st.download_button("⬇️ Download Processed Video",f,file_name=os.path.basename(out),mime="video/mp4")
    if os.path.exists(ev):
        with open(ev,"rb") as f: st.download_button("⬇️ Download events.csv",f,file_name="events.csv",mime="text/csv")

def performance_table(results):
    rows = [{"Configuration":r["configuration"],"Image Size":r["image_size"],"Frame Skip":r["frame_skip"],"FPS":round(r["avg_fps"],2),"Processing Time (s)":round(r["processing_time"],2),"Inference Time (s)":round(r["inference_time"],2),"Objects":r["total_objects"]} for r in results]
    df = pd.DataFrame(rows)
    st.dataframe(df,use_container_width=True)
    if not df.empty:
        best = df.loc[df["FPS"].idxmax()]
        st.success(f'Best configuration: {best["Configuration"]} with {best["FPS"]} FPS.')

st.title("🎥 Smart Video Analytics System")
st.caption("YOLO object detection + ByteTrack tracking + ROI analytics + entry/exit events + performance testing")

with st.sidebar:
    st.header("⚙️ Processing Settings")
    imgsz = st.selectbox("Image Size", [640,480], index=0)
    frame_skip = st.selectbox("Frame Skipping", [0,1,2], index=0)
    roi_mode = st.selectbox("ROI", ["Full Frame","Center","Custom"])
    st.subheader("ROI Adjustment")
    rx = st.slider("ROI X",0,100,10)
    ry = st.slider("ROI Y",0,100,10)
    rw = st.slider("ROI Width",10,100,80)
    rh = st.slider("ROI Height",10,100,80)
    performance_mode = st.checkbox("Run Performance Comparison",False)
    compare_videos = st.checkbox("Use uploaded video for comparison",True)

uploaded = st.file_uploader("Upload a recorded video",type=["mp4","avi","mov","mkv"])
if uploaded:
    input_path = save_uploaded(uploaded)
    fps,frames,w,h = get_video_info(input_path)
    st.video(input_path)
    st.write(f"Video: {uploaded.name} | Resolution: {w}×{h} | Source FPS: {fps:.2f} | Frames: {frames}")
    roi_values = (int(w*rx/100),int(h*ry/100),max(10,int(w*rw/100)),max(10,int(h*rh/100)))
    if st.button("🚀 Start Processing",type="primary"):
        model = load_model()
        if performance_mode:
            configs = [("640px",640,0),("480px",480,0),("640px_FrameSkip",640,frame_skip if frame_skip>0 else 1)]
            results = []
            for label,size,skip in configs:
                st.subheader(f"Processing {label}")
                results.append(run_configuration(input_path,label,size,skip,roi_mode,roi_values,model))
            st.session_state["performance_results"] = results
            st.session_state["summary"] = results[-1]
        else:
            result = run_configuration(input_path,"final",imgsz,frame_skip,roi_mode,roi_values,model)
            st.session_state["summary"] = result
            st.session_state["performance_results"] = []
        st.success("Processing completed successfully.")

if "summary" in st.session_state:
    summary = st.session_state["summary"]
    st.subheader("📊 Analytics Summary")
    show_summary(summary)
    st.write(f'Processing Time: {summary["processing_time"]:.2f} seconds')
    st.write(f'Inference Time: {summary["inference_time"]:.2f} seconds')
    st.write(f'ROI: {summary["roi"]}')
    st.subheader("🎥 Processed Video")
    if os.path.exists(summary["output"]):
        with open(summary["output"],"rb") as video_file: video_bytes = video_file.read()
        st.video(video_bytes,format="video/mp4")
    else:
        st.error("Processed video file was not created.")
    st.subheader("📄 Events")
    if os.path.exists(summary["events"]):
        events_df = pd.read_csv(summary["events"])
        st.dataframe(events_df,use_container_width=True)
    show_downloads(summary)

if "performance_results" in st.session_state and st.session_state["performance_results"]:
    st.subheader("⚡ Performance Comparison")
    performance_table(st.session_state["performance_results"])
    st.info("Compare FPS and processing time. Higher FPS and lower processing time indicate better performance.")
