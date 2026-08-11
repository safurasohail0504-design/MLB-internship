import os
import io
import csv
import pandas as pd
import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="YOLO Model Performance Audit", page_icon="🎯", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best.pt")
DATA_PATH = os.path.join(BASE_DIR, "data.yaml")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
CM_DIR = os.path.join(BASE_DIR, "confusion matrix")
ERROR_DIR = os.path.join(BASE_DIR, "error_analysis")
PREDICTION_DIR = os.path.join(BASE_DIR, "predictions", "review")

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(CM_DIR, exist_ok=True)
os.makedirs(ERROR_DIR, exist_ok=True)
os.makedirs(PREDICTION_DIR, exist_ok=True)

@st.cache_resource
def load_model(): return YOLO(MODEL_PATH)

def get_metrics(): return {"Precision": 0.9127, "Recall": 0.8168, "mAP@50": 0.8697, "mAP@50-95": 0.6795}

def get_class_names(model):
    return model.names if hasattr(model, "names") else {0: "Cap", 1: "Helmet"}
def read_error_report():
    path = os.path.join(ERROR_DIR, "error_analysis.csv")
    if not os.path.exists(path): return pd.DataFrame()
    return pd.read_csv(path)

def read_evaluation_results():
    path = os.path.join(RESULTS_DIR, "evaluation_results.txt")
    if not os.path.exists(path): return ""
    with open(path, "r", encoding="utf-8") as file: return file.read()

def save_prediction_image(result, image_name):
    output_path = os.path.join(PREDICTION_DIR, image_name)
    annotated = result.plot()
    Image.fromarray(annotated[:, :, ::-1]).save(output_path, quality=95)
    return output_path

def display_metrics(metrics):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Precision", f'{metrics["Precision"]:.4f}')
    c2.metric("Recall", f'{metrics["Recall"]:.4f}')
    c3.metric("mAP@50", f'{metrics["mAP@50"]:.4f}')
    c4.metric("mAP@50-95", f'{metrics["mAP@50-95"]:.4f}')

def prediction_details(result, names):
    rows = []
    if result.boxes is None or len(result.boxes) == 0: return pd.DataFrame()
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = names.get(class_id, str(class_id)) if isinstance(names, dict) else names[class_id]
        rows.append({"Class ID": class_id, "Class": class_name, "Confidence": round(confidence, 4)})
    return pd.DataFrame(rows)

def run_prediction(uploaded_file, model, confidence, image_size):
    image = Image.open(uploaded_file).convert("RGB")
    results = model.predict(image, imgsz=image_size, conf=confidence, verbose=False)
    return image, results[0]

def show_confusion_matrix():
    normalized = os.path.join(CM_DIR, "confusion_matrix_normalized.png")
    regular = os.path.join(CM_DIR, "confusion_matrix.png")
    available = False
    if os.path.exists(normalized):
        st.image(normalized, caption="Normalized Confusion Matrix", use_container_width=True)
        available = True
    if os.path.exists(regular):
        st.image(regular, caption="Confusion Matrix", use_container_width=True)
        available = True
    if not available: st.info("Confusion matrix files are not available.")

def show_error_analysis():
    df = read_error_report()
    if df.empty:
        st.info("Error-analysis CSV is not available.")
        return
    if "Category" in df.columns:
        counts = df["Category"].value_counts().reset_index()
        counts.columns = ["Error Category", "Count"]
        st.dataframe(counts, use_container_width=True)
        st.bar_chart(counts.set_index("Error Category"))
    st.dataframe(df, use_container_width=True)

def download_file(path, label, mime):
    if os.path.exists(path):
        with open(path, "rb") as file:
            st.download_button(label, file.read(), os.path.basename(path), mime=mime)

st.title("🎯 YOLO Model Performance Audit")
st.caption("Evaluate model performance, test new images, inspect errors and understand model failures.")

if not os.path.exists(MODEL_PATH):
    st.error("best.pt was not found in the Day 36 folder.")
    st.stop()

model = load_model()
names = get_class_names(model)

if names == {0: "0", 1: "1"}:
    names = {0: "Cap", 1: "Helmet"}

with st.sidebar:
    st.header("⚙️ Prediction Settings")
    image_size = st.selectbox("Image Size", [640, 480], index=0)
    confidence = st.slider("Confidence Threshold", 0.10, 0.90, 0.25, 0.05)
    st.divider()
    st.write("### Model Classes")
    for class_id, class_name in names.items():
        st.write(f"**{class_id}:** {class_name}")

st.subheader("📷 Test Your Model")
st.write("Upload an image and run the trained YOLO model to inspect its prediction.")

uploaded = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Original Image", use_container_width=True)

    if st.button("🔍 Run Detection", type="primary"):
        with st.spinner("Running YOLO detection..."):
            image, result = run_prediction(uploaded, model, confidence, image_size)

        annotated = result.plot()

        with col2:
            st.image(annotated, caption="YOLO Prediction", use_container_width=True)

        prediction_df = prediction_details(result, names)

        st.subheader("📊 Detection Results")

        if prediction_df.empty:
            st.warning("No objects were detected.")
        else:
            st.dataframe(prediction_df, use_container_width=True)

            total = len(prediction_df)
            st.success(f"Detected Objects: {total}")

            for _, row in prediction_df.iterrows():
                st.write(f'**{row["Class"]}** — Confidence: **{row["Confidence"]:.2f}**')

            output_name = f"uploaded_{uploaded.name.rsplit('.', 1)[0]}.jpg"
            output_path = save_prediction_image(result, output_name)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Prediction",
                    file.read(),
                    output_name,
                    "image/jpeg"
                )

st.divider()

st.subheader("📈 Model Performance")

metrics = get_metrics()
display_metrics(metrics)

st.caption("Metrics obtained from the Day 36 validation run on the helmet dataset.")

st.subheader("📋 Metric Interpretation")

interpretation = pd.DataFrame({
    "Metric": ["Precision", "Recall", "mAP@50", "mAP@50-95"],
    "Value": [metrics["Precision"], metrics["Recall"], metrics["mAP@50"], metrics["mAP@50-95"]],
    "Meaning": [
        "How many detected objects were correct",
        "How many actual objects were successfully detected",
        "Detection accuracy using IoU threshold 0.50",
        "Detection accuracy across IoU thresholds 0.50–0.95"
    ]
})
st.dataframe(interpretation, use_container_width=True)
st.divider()
st.subheader("🧩 Confusion Matrix")
show_confusion_matrix()
st.divider()
st.subheader("🔎 Error Analysis")
st.write("Reviewing model mistakes helps identify where the next training version should improve.")
show_error_analysis()
report_path = os.path.join(ERROR_DIR, "error_analysis_report.txt")
if os.path.exists(report_path):
    with open(report_path, "r", encoding="utf-8") as file:
        report = file.read()

    with st.expander("📄 View Error Analysis Report"):
        st.text(report)

st.divider()

st.subheader("🖼️ Prediction Review")

review_images = sorted(
    [
        file for file in os.listdir(PREDICTION_DIR)
        if file.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
)
if review_images:
    selected_images = st.multiselect(
        "Select prediction examples to inspect",
        review_images,
        default=review_images[:5]
    )

    if selected_images:
        cols = st.columns(3)
        for index, image_name in enumerate(selected_images):
            with cols[index % 3]:
                st.image(
                    os.path.join(PREDICTION_DIR, image_name),
                    caption=image_name,
                    use_container_width=True
                )
else:
    st.info("No saved prediction-review images are available.")
st.divider()
st.subheader("🎯 Day 36 Challenge")
st.write("""
The model should not only be judged by its metrics. Difficult predictions
should be investigated to understand why the model failed.
""")
challenge_categories = [
    "False Detection",
    "Duplicate Detection",
    "Missed Object",
    "Low Confidence",
    "Small Object",
    "Occlusion",
    "Wrong Class",
    "Localization Error"
]
st.write("### Error Categories")
for category in challenge_categories:
    st.write(f"• {category}")
st.info(
    "Five difficult examples should be selected from the prediction review "
    "and explained according to the Day 36 challenge requirements."
)
st.divider()
st.subheader("📥 Downloads")
download_file(
    os.path.join(RESULTS_DIR, "evaluation_results.txt"),
    "⬇️ Download Evaluation Results",
    "text/plain"
)
download_file(
    os.path.join(ERROR_DIR, "error_analysis.csv"),
    "⬇️ Download Error Analysis CSV",
    "text/csv"
)
download_file(
    os.path.join(ERROR_DIR, "error_analysis_report.txt"),
    "⬇️ Download Error Analysis Report",
    "text/plain"
)
download_file(
    os.path.join(CM_DIR, "confusion_matrix.png"),
    "⬇️ Download Confusion Matrix",
    "image/png"
)
download_file(
    os.path.join(CM_DIR, "confusion_matrix_normalized.png"),
    "⬇️ Download Normalized Confusion Matrix",
    "image/png"
)
st.success("🎯 Day 36 Model Performance Audit is ready.")