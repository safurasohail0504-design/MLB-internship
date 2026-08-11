import os
import tempfile
import pandas as pd
import streamlit as st
from pathlib import Path
from ultralytics import YOLO
st.set_page_config(page_title="YOLO Performance Audit", page_icon="🎯", layout="wide")
MODEL_PATH = "best.pt"
DATA_PATH = "data.yaml"
RESULT_DIR = Path("results")
MATRIX_DIR = Path("confusion matrix")
CHALLENGE_DIR = Path("challenge_predictions")
RESULT_DIR.mkdir(exist_ok=True)
MATRIX_DIR.mkdir(exist_ok=True)
CHALLENGE_DIR.mkdir(exist_ok=True)
@st.cache_resource
def load_model(): return YOLO(MODEL_PATH)
def run_validation(model): return model.val(data=DATA_PATH, imgsz=640, split="val", plots=True, project=str(RESULT_DIR), name="validation", exist_ok=True)
def save_metrics(results):
    metrics = {"Precision": float(results.box.mp), "Recall": float(results.box.mr), "mAP@50": float(results.box.map50), "mAP@50-95": float(results.box.map)}
    pd.DataFrame([metrics]).to_csv(RESULT_DIR / "evaluation_metrics.csv", index=False)
    with open(RESULT_DIR / "evaluation_results.txt", "w") as f:
        for key, value in metrics.items(): f.write(f"{key}: {value:.4f}\n")
    return metrics
def show_metrics(metrics):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Precision", f'{metrics["Precision"]:.3f}')
    c2.metric("Recall", f'{metrics["Recall"]:.3f}')
    c3.metric("mAP@50", f'{metrics["mAP@50"]:.3f}')
    c4.metric("mAP@50-95", f'{metrics["mAP@50-95"]:.3f}')
def find_confusion_matrix():
    files = list(RESULT_DIR.rglob("confusion_matrix.png"))
    files += list(RESULT_DIR.rglob("confusion_matrix_normalized.png"))
    return files
def show_confusion_matrix():
    files = find_confusion_matrix()
    if files:
        for file in files:
            st.image(str(file), caption=file.name, use_container_width=True)
    else:
        st.warning("Confusion matrix was not generated yet.")
def prediction_review(model, image_paths, output_dir, limit=30):
    output_dir.mkdir(parents=True, exist_ok=True)
    selected = image_paths[:limit]
    results = model.predict(source=[str(x) for x in selected], imgsz=640, conf=0.25, save=True, project=str(output_dir.parent), name=output_dir.name, exist_ok=True, verbose=False)
    rows = []
    for index, result in enumerate(results, 1):
        detected = len(result.boxes)
        names = result.names
        classes = result.boxes.cls.int().cpu().tolist() if detected else []
        confidences = result.boxes.conf.cpu().tolist() if detected else []
        labels = [names[c] for c in classes]
        rows.append({"Image": f"image_{index:03d}", "Detections": detected, "Classes": ", ".join(labels), "Max Confidence": round(max(confidences), 3) if confidences else 0})
    df = pd.DataFrame(rows)
    df.to_csv(output_dir / "prediction_review.csv", index=False)
    return df
def get_validation_images():
    candidates = [
        Path("valid/images"),
        Path("../day_29/Helmet_Dataset/valid/images"),
        Path("../Helmet_Dataset/valid/images")
    ]
    for folder in candidates:
        if folder.exists():
            return sorted(list(folder.glob("*.jpg")) + list(folder.glob("*.jpeg")) + list(folder.glob("*.png")))
    return []
def classify_error(row):
    if row["Detections"] == 0: return "Missed Object"
    if row["Detections"] > 1: return "Multiple/False Detection"
    if row["Max Confidence"] < 0.50: return "Low Confidence"
    return "Review Required"
def create_error_analysis(df):
    if df.empty: return pd.DataFrame()
    df["Error Category"] = df.apply(classify_error, axis=1)
    df.to_csv(RESULT_DIR / "error_analysis.csv", index=False)
    return df
def show_error_analysis(df):
    if df.empty:
        st.info("Run prediction review first.")
        return
    counts = df["Error Category"].value_counts().reset_index()
    counts.columns = ["Error Category", "Count"]
    st.dataframe(counts, use_container_width=True)
    st.dataframe(df, use_container_width=True)
def challenge_prediction(model, uploaded_image):
    suffix = Path(uploaded_image.name).suffix or ".jpg"
    fd, path = tempfile.mkstemp(suffix=suffix)
    os.close(fd)
    with open(path, "wb") as f: f.write(uploaded_image.getbuffer())
    results = model.predict(source=path, imgsz=640, conf=0.25, save=True, project=str(CHALLENGE_DIR), name="examples", exist_ok=True, verbose=False)
    result = results[0]
    annotated = result.plot()
    st.image(annotated, caption="Model Prediction", channels="BGR", use_container_width=True)
    if len(result.boxes):
        rows = []
        for cls, conf in zip(result.boxes.cls.int().cpu().tolist(), result.boxes.conf.cpu().tolist()):
            rows.append({"Class": result.names[cls], "Confidence": round(float(conf), 3)})
        st.dataframe(pd.DataFrame(rows), use_container_width=True)
    else:
        st.warning("No object detected.")
def save_summary(metrics, error_df):
    with open(RESULT_DIR / "error_analysis_report.txt", "w") as f:
        f.write("YOLO MODEL PERFORMANCE AUDIT\n\n")
        for key, value in metrics.items(): f.write(f"{key}: {value:.4f}\n")
        f.write("\nERROR ANALYSIS\n")
        if not error_df.empty:
            for key, value in error_df["Error Category"].value_counts().items(): f.write(f"{key}: {value}\n")
st.title("🎯 YOLO Model Performance Audit")
st.caption("Model evaluation, confusion matrix, prediction review and error analysis")
if not Path(MODEL_PATH).exists():
    st.error("best.pt was not found in the Day 36 folder.")
    st.stop()
if not Path(DATA_PATH).exists():
    st.error("data.yaml was not found in the Day 36 folder.")
    st.stop()
model = load_model()
st.sidebar.header("Evaluation Controls")
run_eval = st.sidebar.button("Run Model Evaluation")
run_review = st.sidebar.button("Review 30 Predictions")
st.sidebar.markdown("### Model")
st.sidebar.write("YOLO trained helmet detection model")
st.sidebar.write("Input size: 640px")
st.sidebar.write("Validation split: val")
if run_eval:
    with st.spinner("Running validation..."):
        validation_results = run_validation(model)
        metrics = save_metrics(validation_results)
        st.session_state["metrics"] = metrics
        st.session_state["validation_done"] = True
    st.success("Model evaluation completed.")
if "metrics" in st.session_state:
    st.subheader("📊 Model Performance")
    show_metrics(st.session_state["metrics"])
st.divider()
st.subheader("📈 Confusion Matrix")
if st.session_state.get("validation_done"):
    show_confusion_matrix()
else:
    st.info("Run model evaluation to generate the confusion matrix.")
st.divider()
st.subheader("🔍 Prediction Review")
validation_images = get_validation_images()
if not validation_images:
    st.warning("Validation images were not found. Check the validation dataset path.")
else:
    st.write(f"Validation images available: {len(validation_images)}")
    st.write("The task requires manual review of at least 30 predictions.")
    if run_review:
        with st.spinner("Generating prediction review..."):
            review_df = prediction_review(model, validation_images, RESULT_DIR / "prediction_review", 30)
            error_df = create_error_analysis(review_df)
            st.session_state["review_df"] = review_df
            st.session_state["error_df"] = error_df
            if "metrics" in st.session_state: save_summary(st.session_state["metrics"], error_df)
        st.success("30 prediction examples generated.")
if "review_df" in st.session_state:
    st.dataframe(st.session_state["review_df"], use_container_width=True)
st.divider()
st.subheader("⚠️ Error Analysis")
if "error_df" in st.session_state:
    show_error_analysis(st.session_state["error_df"])
else:
    st.info("Generate the prediction review first.")
st.divider()
st.subheader("🧪 Difficult Example Testing")
st.write("Upload difficult images such as small objects, occluded objects, people without helmets, hats or caps.")
challenge_image = st.file_uploader("Upload a challenging image", type=["jpg", "jpeg", "png"])
if challenge_image:
    challenge_prediction(model, challenge_image)
st.divider()
st.subheader("📹 Video Testing")
video = st.file_uploader("Upload a video for qualitative model testing", type=["mp4", "avi", "mov", "mkv"])
if video:
    suffix = Path(video.name).suffix or ".mp4"
    fd, video_path = tempfile.mkstemp(suffix=suffix)
    os.close(fd)
    with open(video_path, "wb") as f: f.write(video.getbuffer())
    st.video(video)
    if st.button("Run YOLO on Video"):
        with st.spinner("Processing video..."):
            video_results = model.predict(source=video_path, imgsz=640, save=True, project="video_results", name="prediction", exist_ok=True, verbose=False)
        st.success("Video prediction completed.")
        st.info("Video testing is qualitative. Precision, Recall and mAP require labeled validation/test data.")
st.divider()
st.subheader("📥 Download Results")
result_files = [
    RESULT_DIR / "evaluation_results.txt",
    RESULT_DIR / "evaluation_metrics.csv",
    RESULT_DIR / "error_analysis.csv",
    RESULT_DIR / "error_analysis_report.txt"
]
for file in result_files:
    if file.exists():
        with open(file, "rb") as f:
            st.download_button(f"Download {file.name}", f, file_name=file.name)
st.divider()
st.subheader("🎯 Day 36 Audit Checklist")
checklist = {
    "Validation completed": st.session_state.get("validation_done", False),
    "Precision recorded": "metrics" in st.session_state,
    "Recall recorded": "metrics" in st.session_state,
    "mAP@50 recorded": "metrics" in st.session_state,
    "mAP@50-95 recorded": "metrics" in st.session_state,
    "Confusion matrix generated": bool(find_confusion_matrix()),
    "30 predictions reviewed": "review_df" in st.session_state and len(st.session_state["review_df"]) >= 30,
    "Error analysis created": "error_df" in st.session_state,
}
for item, status in checklist.items():
    st.write(("✅" if status else "⬜") + " " + item)