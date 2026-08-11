import os
import tempfile
from pathlib import Path

import pandas as pd
import streamlit as st
from ultralytics import YOLO

st.set_page_config(page_title="YOLO Model Performance Audit", page_icon="🎯", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "best.pt"
DATA_PATH = BASE_DIR / "data.yaml"
RESULTS_DIR = BASE_DIR / "results"
CONFUSION_DIR = BASE_DIR / "confusion matrix"
PREDICTIONS_DIR = BASE_DIR / "predictions" / "review"
ERROR_DIR = BASE_DIR / "error_analysis"

for folder in [RESULTS_DIR, CONFUSION_DIR, PREDICTIONS_DIR, ERROR_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

@st.cache_resource
def load_model(): return YOLO(str(MODEL_PATH))

def evaluate_model(model):
    return model.val(data=str(DATA_PATH), imgsz=640, split="val", plots=True, project=str(CONFUSION_DIR), name="validation", exist_ok=True)

def save_evaluation_results(results):
    box = results.box
    precision = float(box.mp if hasattr(box, "mp") else 0)
    recall = float(box.mr if hasattr(box, "mr") else 0)
    map50 = float(box.map50 if hasattr(box, "map50") else 0)
    map5095 = float(box.map if hasattr(box, "map") else 0)
    text = f"Precision: {precision:.4f}\nRecall: {recall:.4f}\nmAP@50: {map50:.4f}\nmAP@50-95: {map5095:.4f}\n"
    (RESULTS_DIR / "evaluation_results.txt").write_text(text, encoding="utf-8")
    return precision, recall, map50, map5095

def review_predictions(model, source):
    return model.predict(source=str(source), imgsz=640, conf=0.25, save=True, project=str(PREDICTIONS_DIR.parent), name="review", exist_ok=True, verbose=False)

def show_metrics(values):
    precision, recall, map50, map5095 = values
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Precision", f"{precision:.4f}")
    c2.metric("Recall", f"{recall:.4f}")
    c3.metric("mAP@50", f"{map50:.4f}")
    c4.metric("mAP@50-95", f"{map5095:.4f}")

def show_model_info():
    st.subheader("🤖 Model Information")
    st.write(f"Model: `best.pt`")
    st.write(f"Model path: `{MODEL_PATH}`")
    st.write(f"Dataset configuration: `{DATA_PATH}`")
    if MODEL_PATH.exists():
        st.success("best.pt found successfully.")
    else:
        st.error("best.pt was not found in the Day 36 folder.")

def show_error_report():
    report = ERROR_DIR / "error_analysis_report.txt"
    if report.exists():
        st.subheader("🔎 Error Analysis Report")
        st.text(report.read_text(encoding="utf-8"))

def show_results_files():
    st.subheader("📁 Generated Results")
    files = []
    for folder in [RESULTS_DIR, CONFUSION_DIR, PREDICTIONS_DIR, ERROR_DIR]:
        if folder.exists():
            files.extend(list(folder.rglob("*")))
    files = [f for f in files if f.is_file()]
    if files:
        for file in files[:100]:
            st.write(f"• {file.relative_to(BASE_DIR)}")
    else:
        st.info("No generated results found yet.")

def download_file(path, label, mime):
    if path.exists():
        with open(path, "rb") as file:
            st.download_button(label, file, file_name=path.name, mime=mime)

st.title("🎯 YOLO Model Performance Audit")
st.caption("Model evaluation, confusion matrix, prediction review and error analysis")

show_model_info()

if not MODEL_PATH.exists():
    st.stop()

if not DATA_PATH.exists():
    st.error("data.yaml was not found in the Day 36 folder.")
    st.stop()

model = load_model()

st.sidebar.header("⚙️ Evaluation Controls")
run_validation = st.sidebar.button("📊 Run Model Evaluation")
run_prediction = st.sidebar.button("🔍 Run Prediction Review")

st.sidebar.info("The application evaluates the trained helmet-detection model using the validation dataset.")

if run_validation:
    with st.spinner("Running YOLO validation..."):
        results = evaluate_model(model)
        values = save_evaluation_results(results)
        st.session_state["metrics"] = values
    st.success("Model evaluation completed.")

if "metrics" in st.session_state:
    st.header("📊 Model Performance")
    show_metrics(st.session_state["metrics"])

    precision, recall, map50, map5095 = st.session_state["metrics"]

    st.write("### Interpretation")
    st.write(f"**Precision:** {precision:.4f} — how many detected objects were actually correct.")
    st.write(f"**Recall:** {recall:.4f} — how many actual objects the model successfully detected.")
    st.write(f"**mAP@50:** {map50:.4f} — detection performance using IoU 0.50.")
    st.write(f"**mAP@50-95:** {map5095:.4f} — stricter average detection performance across multiple IoU thresholds.")

    st.success("Higher values generally indicate better detection performance.")

if run_prediction:
    source = BASE_DIR.parent / "day_29" / "Helmet_Dataset" / "valid" / "images"

    if not source.exists():
        uploaded = st.file_uploader("Upload validation images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
        if uploaded:
            temp_dir = Path(tempfile.mkdtemp())
            for image in uploaded:
                (temp_dir / image.name).write_bytes(image.getbuffer())
            source = temp_dir

    if source.exists():
        with st.spinner("Generating prediction review images..."):
            review_predictions(model, source)
        st.success("Prediction review completed.")
        st.info(f"Prediction images are saved in: `{PREDICTIONS_DIR}`")
    else:
        st.warning("Validation image folder is not available in the deployed app. Upload images to perform prediction review.")

st.header("🧩 Confusion Matrix")

matrix_files = list(CONFUSION_DIR.rglob("*confusion_matrix*.png"))

if matrix_files:
    for matrix in matrix_files:
        st.image(str(matrix), caption=matrix.name, use_container_width=True)
else:
    st.info("Run model evaluation to generate the confusion matrix.")

st.header("🔎 Error Analysis")

categories = {
    "Missed Object": 0,
    "Wrong Class": 0,
    "False Detection": 0,
    "Low Confidence": 0,
    "Small Object": 0,
    "Occlusion": 0
}

error_csv = ERROR_DIR / "error_analysis.csv"

if error_csv.exists():
    try:
        error_df = pd.read_csv(error_csv)
        st.dataframe(error_df, use_container_width=True)
    except Exception:
        st.warning("Could not read error_analysis.csv.")
else:
    st.info("Your manually reviewed error-analysis CSV will appear here after it is added to the repository.")

show_error_report()

st.header("📷 Prediction Examples")

prediction_images = sorted(PREDICTIONS_DIR.glob("*.jpg"))

if prediction_images:
    cols = st.columns(3)
    for index, image in enumerate(prediction_images[:30]):
        with cols[index % 3]:
            st.image(str(image), caption=image.stem, use_container_width=True)
else:
    st.info("No prediction review images are currently available.")

st.header("📥 Downloads")

download_file(RESULTS_DIR / "evaluation_results.txt", "⬇️ Download Evaluation Results", "text/plain")
download_file(ERROR_DIR / "error_analysis.csv", "⬇️ Download Error Analysis CSV", "text/csv")
download_file(ERROR_DIR / "error_analysis_report.txt", "⬇️ Download Error Analysis Report", "text/plain")

st.header("📁 Project Results")
show_results_files()

st.divider()

st.subheader("🎯 Day 36 Challenge")

st.write("""
The purpose of this audit is not only to report metrics. 
The model should be examined to understand where it fails and why.
""")

st.write("""
Recommended difficult cases to investigate:

- False detections on objects that look like helmets
- Multiple detections around one helmet
- Missed helmets
- Small helmets
- Occluded helmets
- People without helmets being detected as helmets
- Incorrect bounding-box locations
""")
st.success("Model Performance Audit interface is ready.")