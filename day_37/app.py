import os
import pandas as pd
import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="Helmet Detection Model Comparison", page_icon="🎯", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
V1_PATH = os.path.join(BASE_DIR, "models", "V1_best.pt")
V2_PATH = os.path.join(BASE_DIR, "models", "V2_best.pt")
EXAMPLE_DIR = os.path.join(BASE_DIR, "v1 vs v2")
ORIGINAL_DIR = os.path.join(EXAMPLE_DIR, "original")
V1_DIR = os.path.join(EXAMPLE_DIR, "V1")
V2_DIR = os.path.join(EXAMPLE_DIR, "V2")

V1_METRICS = {"Precision": 0.9127, "Recall": 0.8168, "mAP50": 0.8697, "mAP50-95": 0.6795}
V2_METRICS = {"Precision": 0.8330, "Recall": 0.7400, "mAP50": 0.7800, "mAP50-95": 0.5170}

os.makedirs(EXAMPLE_DIR, exist_ok=True)
os.makedirs(ORIGINAL_DIR, exist_ok=True)
os.makedirs(V1_DIR, exist_ok=True)
os.makedirs(V2_DIR, exist_ok=True)

@st.cache_resource
def load_model(path): return YOLO(path)

def metric_delta(v1, v2): return v2 - v1

def get_names(model):
    names = model.names
    return names if isinstance(names, dict) else dict(enumerate(names))

def detect(model, image, conf, imgsz):
    return model.predict(image, conf=conf, imgsz=imgsz, verbose=False)[0]

def detection_table(result, names):
    rows = []
    if result.boxes is None: return pd.DataFrame()
    for box in result.boxes:
        cid = int(box.cls[0])
        rows.append({"Class": names.get(cid, str(cid)), "Confidence": round(float(box.conf[0]), 3)})
    return pd.DataFrame(rows)

def save_result(result, path):
    Image.fromarray(result.plot()[:, :, ::-1]).save(path, quality=95)

def image_files(folder):
    if not os.path.exists(folder): return []
    return sorted([x for x in os.listdir(folder) if x.lower().endswith((".jpg", ".jpeg", ".png"))])

def metric_table():
    rows = []
    for metric in V1_METRICS:
        rows.append({
            "Metric": metric.replace("mAP50-95", "mAP50-95").replace("mAP50", "mAP50"),
            "V1": V1_METRICS[metric],
            "V2": V2_METRICS[metric],
            "Change": round(metric_delta(V1_METRICS[metric], V2_METRICS[metric]), 4)
        })
    return pd.DataFrame(rows)

def show_metrics():
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("V1 Precision", f"{V1_METRICS['Precision']:.4f}")
    c2.metric("V1 Recall", f"{V1_METRICS['Recall']:.4f}")
    c3.metric("V1 mAP50", f"{V1_METRICS['mAP50']:.4f}")
    c4.metric("V1 mAP50-95", f"{V1_METRICS['mAP50-95']:.4f}")
    st.dataframe(metric_table(), use_container_width=True, hide_index=True)

def show_model_status():
    missing = []
    if not os.path.exists(V1_PATH): missing.append("models/V1_best.pt")
    if not os.path.exists(V2_PATH): missing.append("models/V2_best.pt")
    if missing:
        st.error("Missing model file(s): " + ", ".join(missing))
        st.stop()

def show_comparison():
    df = metric_table()
    better = df["Change"].sum()
    if better < 0:
        st.warning("Current validation results show V1 performing better than V2. The comparison below reflects the actual results without artificially favoring either model.")
    elif better > 0:
        st.success("Current validation results show improvement from V1 to V2.")
    else:
        st.info("Current validation results show no overall change between the models.")

def show_examples():
    originals = image_files(ORIGINAL_DIR)
    v1_images = image_files(V1_DIR)
    v2_images = image_files(V2_DIR)

    if not originals:
        st.info("No comparison examples were found in the v1 vs v2/original folder.")
        return

    st.subheader("Saved Comparison Examples")
    count = min(len(originals), len(v1_images), len(v2_images))

    if count == 0:
        st.info("Original, V1 and V2 example images are required for comparison.")
        return

    selected = st.selectbox("Select example", range(count), format_func=lambda x: f"Example {x + 1}")

    original = os.path.join(ORIGINAL_DIR, originals[selected])
    v1 = os.path.join(V1_DIR, v1_images[selected])
    v2 = os.path.join(V2_DIR, v2_images[selected])

    c1, c2, c3 = st.columns(3)
    with c1:
        st.image(original, caption="Original", use_container_width=True)
    with c2:
        st.image(v1, caption="V1 Prediction", use_container_width=True)
    with c3:
        st.image(v2, caption="V2 Prediction", use_container_width=True)

def show_upload(v1_model, v2_model, names_v1, names_v2):
    st.subheader("Live Model Comparison")
    uploaded = st.file_uploader("Upload an image for V1 and V2 comparison", type=["jpg", "jpeg", "png"])

    if not uploaded:
        st.info("Upload an image to compare both models on the same input.")
        return

    image = Image.open(uploaded).convert("RGB")

    conf = st.slider("Confidence Threshold", 0.10, 0.90, 0.25, 0.05)
    imgsz = st.selectbox("Image Size", [640, 480], index=0)

    if st.button("Run V1 and V2", type="primary"):
        with st.spinner("Running both detection models..."):
            result_v1 = detect(v1_model, image, conf, imgsz)
            result_v2 = detect(v2_model, image, conf, imgsz)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.image(image, caption="Original Image", use_container_width=True)

        with c2:
            st.image(result_v1.plot(), caption="V1 Prediction", use_container_width=True)

        with c3:
            st.image(result_v2.plot(), caption="V2 Prediction", use_container_width=True)

        df_v1 = detection_table(result_v1, names_v1)
        df_v2 = detection_table(result_v2, names_v2)

        st.subheader("Detection Details")

        d1, d2 = st.columns(2)

        with d1:
            st.markdown("### V1")
            if df_v1.empty:
                st.warning("No detections.")
            else:
                st.dataframe(df_v1, use_container_width=True, hide_index=True)
                st.write(f"Detections: **{len(df_v1)}**")

        with d2:
            st.markdown("### V2")
            if df_v2.empty:
                st.warning("No detections.")
            else:
                st.dataframe(df_v2, use_container_width=True, hide_index=True)
                st.write(f"Detections: **{len(df_v2)}**")

def show_class_performance():
    st.subheader("Validation Performance")
    st.dataframe(
        pd.DataFrame({
            "Metric": ["Precision", "Recall", "mAP50", "mAP50-95"],
            "V1": [
                V1_METRICS["Precision"],
                V1_METRICS["Recall"],
                V1_METRICS["mAP50"],
                V1_METRICS["mAP50-95"]
            ],
            "V2": [
                V2_METRICS["Precision"],
                V2_METRICS["Recall"],
                V2_METRICS["mAP50"],
                V2_METRICS["mAP50-95"]
            ]
        }),
        use_container_width=True,
        hide_index=True
    )

def show_example_summary():
    originals = image_files(ORIGINAL_DIR)
    v1_images = image_files(V1_DIR)
    v2_images = image_files(V2_DIR)

    data = {
        "Folder": ["Original", "V1", "V2"],
        "Images": [len(originals), len(v1_images), len(v2_images)]
    }

    st.subheader("Comparison Dataset")
    st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

show_model_status()

v1_model = load_model(V1_PATH)
v2_model = load_model(V2_PATH)

names_v1 = get_names(v1_model)
names_v2 = get_names(v2_model)

st.title("Helmet Detection Model Comparison")
st.caption("Comparative evaluation of V1 and V2 YOLO detection models.")

show_comparison()

st.divider()
show_metrics()

st.divider()
show_upload(v1_model, v2_model, names_v1, names_v2)

st.divider()
show_examples()

st.divider()
show_example_summary()

st.divider()
st.subheader("Current Evaluation")
st.write(
    "The application compares both trained models using the same images and "
    "reports their actual validation performance. V2 is evaluated independently "
    "rather than being assumed to outperform V1."
)