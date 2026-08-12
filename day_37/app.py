import os
import pandas as pd
import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="Helmet Detection Model Comparison", page_icon="🎯", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
COMPARISON_DIR = os.path.join(BASE_DIR, "V1 vs V2")

V1_MODEL_PATH = os.path.join(MODELS_DIR, "V1_best.pt")
V2_MODEL_PATH = os.path.join(MODELS_DIR, "V2_best.pt")

def resolve_folder(parent, target):
    if not os.path.exists(parent):
        return None
    target_clean = target.lower().replace(" ", "").replace("_", "")
    for name in os.listdir(parent):
        path = os.path.join(parent, name)
        name_clean = name.lower().replace(" ", "").replace("_", "")
        if os.path.isdir(path) and name_clean == target_clean:
            return path
    return None

def find_comparison_folder():
    if not os.path.exists(COMPARISON_DIR):
        return resolve_folder(BASE_DIR, "V1 vs V2")
    return COMPARISON_DIR

def get_images(folder):
    if not folder or not os.path.exists(folder):
        return []
    files = []
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path) and name.lower().endswith((".jpg", ".jpeg", ".png")):
            files.append(path)
    return sorted(files)

def get_folder_images():
    root = find_comparison_folder()
    original = resolve_folder(root, "Original") if root else None
    v1 = resolve_folder(root, "V1") if root else None
    v2 = resolve_folder(root, "V2") if root else None
    return root, original, v1, v2

@st.cache_resource
def load_models():
    v1 = YOLO(V1_MODEL_PATH)
    v2 = YOLO(V2_MODEL_PATH)
    return v1, v2

def get_names(model):
    names = model.names
    if isinstance(names, dict):
        return names
    return {i: name for i, name in enumerate(names)}

def predict(model, image, confidence, image_size):
    results = model.predict(image, conf=confidence, imgsz=image_size, verbose=False)
    return results[0]

def prediction_table(result, names):
    rows = []
    if result.boxes is None or len(result.boxes) == 0:
        return pd.DataFrame(columns=["Class", "Confidence"])
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = names.get(class_id, str(class_id))
        rows.append({"Class": class_name, "Confidence": round(confidence, 3)})
    return pd.DataFrame(rows)

def model_metrics():
    return {
        "Precision": {"V1": 0.9127, "V2": 0.8330},
        "Recall": {"V1": 0.8168, "V2": 0.7400},
        "mAP50": {"V1": 0.8697, "V2": 0.7800},
        "mAP50-95": {"V1": 0.6795, "V2": 0.5170}
    }

def comparison_dataframe():
    metrics = model_metrics()
    rows = []
    for metric in metrics:
        v1 = metrics[metric]["V1"]
        v2 = metrics[metric]["V2"]
        rows.append({
            "Metric": metric,
            "V1": v1,
            "V2": v2,
            "Change": round(v2 - v1, 4)
        })
    return pd.DataFrame(rows)

def display_metric_cards():
    metrics = model_metrics()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("V1 Precision", f'{metrics["Precision"]["V1"]:.4f}')
    c2.metric("V1 Recall", f'{metrics["Recall"]["V1"]:.4f}')
    c3.metric("V1 mAP50", f'{metrics["mAP50"]["V1"]:.4f}')
    c4.metric("V1 mAP50-95", f'{metrics["mAP50-95"]["V1"]:.4f}')

def show_saved_comparisons(original, v1, v2):
    original_images = get_images(original)
    v1_images = get_images(v1)
    v2_images = get_images(v2)

    counts = pd.DataFrame({
        "Folder": ["Original", "V1", "V2"],
        "Images": [len(original_images), len(v1_images), len(v2_images)]
    })
    st.dataframe(counts, use_container_width=True, hide_index=True)

    if not original_images:
        st.warning("No comparison images were detected in the Original folder.")
        return

    st.subheader("Saved Comparison Examples")
    available = min(len(original_images), len(v1_images), len(v2_images))
    if available == 0:
        st.warning("Complete Original, V1 and V2 image sets are required for saved comparisons.")
        return

    options = [os.path.basename(x) for x in original_images[:available]]
    selected = st.multiselect(
        "Select examples",
        options,
        default=options[:min(5, len(options))]
    )

    for name in selected:
        original_path = os.path.join(original, name)
        v1_path = os.path.join(v1, name)
        v2_path = os.path.join(v2, name)

        if not os.path.exists(v1_path):
            v1_match = [x for x in v1_images if os.path.basename(x) == name]
            v1_path = v1_match[0] if v1_match else None

        if not os.path.exists(v2_path):
            v2_match = [x for x in v2_images if os.path.basename(x) == name]
            v2_path = v2_match[0] if v2_match else None

        cols = st.columns(3)

        with cols[0]:
            st.image(original_path, caption="Original", use_container_width=True)

        with cols[1]:
            if v1_path:
                st.image(v1_path, caption="V1 Prediction", use_container_width=True)
            else:
                st.info("V1 prediction unavailable.")

        with cols[2]:
            if v2_path:
                st.image(v2_path, caption="V2 Prediction", use_container_width=True)
            else:
                st.info("V2 prediction unavailable.")

def show_live_comparison(v1_model, v2_model, v1_names, v2_names, confidence, image_size):
    st.subheader("Live Model Comparison")
    uploaded = st.file_uploader(
        "Upload an image for V1 and V2 comparison",
        type=["jpg", "jpeg", "png"]
    )

    if not uploaded:
        st.info("Upload an image to compare both models.")
        return

    image = Image.open(uploaded).convert("RGB")

    if st.button("Run V1 and V2", type="primary"):
        with st.spinner("Running both models..."):
            v1_result = predict(v1_model, image, confidence, image_size)
            v2_result = predict(v2_model, image, confidence, image_size)

        v1_plot = v1_result.plot()
        v2_plot = v2_result.plot()

        cols = st.columns(3)

        with cols[0]:
            st.image(image, caption="Original Image", use_container_width=True)

        with cols[1]:
            st.image(v1_plot, caption="V1 Prediction", use_container_width=True)

        with cols[2]:
            st.image(v2_plot, caption="V2 Prediction", use_container_width=True)

        st.subheader("Detection Details")

        v1_df = prediction_table(v1_result, v1_names)
        v2_df = prediction_table(v2_result, v2_names)

        c1, c2 = st.columns(2)

        with c1:
            st.write("### V1")
            if v1_df.empty:
                st.warning("No detections.")
            else:
                st.dataframe(v1_df, use_container_width=True, hide_index=True)
                st.write(f"Detections: **{len(v1_df)}**")

        with c2:
            st.write("### V2")
            if v2_df.empty:
                st.warning("No detections.")
            else:
                st.dataframe(v2_df, use_container_width=True, hide_index=True)
                st.write(f"Detections: **{len(v2_df)}**")

def show_evaluation():
    st.subheader("Model Evaluation")
    df = comparison_dataframe()
    display_df = df.copy()
    for column in ["V1", "V2", "Change"]:
        display_df[column] = display_df[column].map(lambda x: f"{x:.4f}")
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    metrics = model_metrics()
    if all(metrics[x]["V2"] < metrics[x]["V1"] for x in metrics):
        st.info("The current validation results show that V1 performs better than V2 on all reported metrics.")
    else:
        st.success("V2 improves at least one reported validation metric over V1.")

def show_dataset_status():
    root, original, v1, v2 = get_folder_images()
    st.subheader("Comparison Dataset")

    if not root:
        st.warning("The V1 vs V2 comparison folder was not found in the deployed repository.")
        return

    st.write(f"Comparison directory: `{os.path.relpath(root, BASE_DIR)}`")

    show_saved_comparisons(original, v1, v2)

st.title("Helmet Detection Model Comparison")
st.caption("Comparative evaluation of two YOLO helmet-detection models using identical images and validation metrics.")

if not os.path.exists(V1_MODEL_PATH):
    st.error("V1_best.pt was not found in the models folder.")
    st.stop()

if not os.path.exists(V2_MODEL_PATH):
    st.error("V2_best.pt was not found in the models folder.")
    st.stop()

try:
    v1_model, v2_model = load_models()
except Exception as error:
    st.error("The YOLO models could not be loaded.")
    st.exception(error)
    st.stop()

v1_names = get_names(v1_model)
v2_names = get_names(v2_model)

with st.sidebar:
    st.header("Prediction Settings")
    image_size = st.selectbox("Image Size", [640, 480], index=0)
    confidence = st.slider("Confidence Threshold", 0.10, 0.90, 0.25, 0.05)
    st.divider()
    st.write("### Model Classes")
    for class_id, class_name in v1_names.items():
        st.write(f"**{class_id}:** {class_name}")

display_metric_cards()

st.divider()
show_live_comparison(v1_model, v2_model, v1_names, v2_names, confidence, image_size)

st.divider()
show_dataset_status()

st.divider()
show_evaluation()

st.divider()
st.subheader("Model Interpretation")
st.write(
    "V2 was trained using the improved dataset and initialized from V1. "
    "The final comparison reports the actual validation results rather than "
    "assuming that the newer model must outperform the previous model."
)

metrics = model_metrics()
interpretation = pd.DataFrame({
    "Metric": ["Precision", "Recall", "mAP50", "mAP50-95"],
    "Interpretation": [
        "Correctness of predicted detections.",
        "Ability to detect the actual objects.",
        "Detection performance at IoU 0.50.",
        "Detection performance across IoU 0.50–0.95."
    ],
    "V1": [
        metrics["Precision"]["V1"],
        metrics["Recall"]["V1"],
        metrics["mAP50"]["V1"],
        metrics["mAP50-95"]["V1"]
    ],
    "V2": [
        metrics["Precision"]["V2"],
        metrics["Recall"]["V2"],
        metrics["mAP50"]["V2"],
        metrics["mAP50-95"]["V2"]
    ]
})

interpretation["V1"] = interpretation["V1"].map(lambda x: f"{x:.4f}")
interpretation["V2"] = interpretation["V2"].map(lambda x: f"{x:.4f}")

st.dataframe(interpretation, use_container_width=True, hide_index=True)

st.divider()
st.subheader("Model Files")
st.write(f"V1: `{os.path.relpath(V1_MODEL_PATH, BASE_DIR)}`")
st.write(f"V2: `{os.path.relpath(V2_MODEL_PATH, BASE_DIR)}`")

st.success("Model comparison application is ready.")
