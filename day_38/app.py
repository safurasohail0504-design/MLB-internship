import os
import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="Shoe Detection", page_icon="👟", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATHS = [
    os.path.join(BASE_DIR, "models", "best.pt"),
    os.path.join(BASE_DIR, "runs", "shoe_detection_v1", "weights", "best.pt")
]
TEST_DIR = os.path.join(BASE_DIR, "test_images")
PREDICTION_DIR = os.path.join(BASE_DIR, "predictions", "shoe_predictions")

MODEL_PATH = next((p for p in MODEL_PATHS if os.path.exists(p)), None)

@st.cache_resource
def load_model(path):
    return YOLO(path)

def detect_image(model, image, confidence, size):
    results = model.predict(image, conf=confidence, imgsz=size, verbose=False)
    return results[0]

def detection_data(result):
    data = []
    if result.boxes is None or len(result.boxes) == 0:
        return data
    for box in result.boxes:
        data.append({
            "Class": "Shoe",
            "Confidence": round(float(box.conf[0]), 3)
        })
    return data

def show_prediction(result):
    annotated = result.plot()
    return Image.fromarray(annotated[:, :, ::-1])

if MODEL_PATH is None:
    st.error("Model file not found. Place best.pt inside models/best.pt.")
    st.stop()

model = load_model(MODEL_PATH)

st.title("👟 Shoe Detection")
st.caption("Custom YOLO object detection model trained on a self-created shoe dataset.")

st.sidebar.header("Detection Settings")
confidence = st.sidebar.slider("Confidence Threshold", 0.10, 0.90, 0.25, 0.05)
image_size = st.sidebar.selectbox("Image Size", [512, 640], index=0)

st.sidebar.divider()
st.sidebar.write("**Model:** Custom Shoe Detector")
st.sidebar.write("**Class:** shoe")

tab1, tab2, tab3 = st.tabs([
    "🔍 Detect Image",
    "🧪 Unseen Test Images",
    "📊 Model Results"
])

with tab1:
    st.subheader("Test Your Image")
    uploaded = st.file_uploader(
        "Upload a shoe image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:
        image = Image.open(uploaded).convert("RGB")

        if st.button("Run Detection", type="primary"):
            with st.spinner("Detecting shoes..."):
                result = detect_image(
                    model,
                    image,
                    confidence,
                    image_size
                )

            prediction = show_prediction(result)
            detections = detection_data(result)

            col1, col2 = st.columns(2)

            with col1:
                st.image(
                    image,
                    caption="Original Image",
                    use_container_width=True
                )

            with col2:
                st.image(
                    prediction,
                    caption="Detection Result",
                    use_container_width=True
                )

            st.divider()

            if detections:
                st.subheader("Detection Results")

                c1, c2 = st.columns(2)

                with c1:
                    st.metric("Shoes Detected", len(detections))

                with c2:
                    average_conf = sum(
                        x["Confidence"] for x in detections
                    ) / len(detections)
                    st.metric(
                        "Average Confidence",
                        f"{average_conf:.2f}"
                    )

                st.dataframe(
                    detections,
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.warning("No shoes detected.")

with tab2:
    st.subheader("Unseen Image Testing")
    st.write(
        "These images were collected separately from the training, "
        "validation, and test datasets."
    )

    if os.path.exists(TEST_DIR):
        test_images = [
            f for f in os.listdir(TEST_DIR)
            if f.lower().endswith(
                (".jpg", ".jpeg", ".png")
            )
        ]
    else:
        test_images = []

    if not test_images:
        st.info("No unseen test images found.")
    else:
        selected = st.selectbox(
            "Select an unseen image",
            sorted(test_images)
        )

        image_path = os.path.join(TEST_DIR, selected)
        image = Image.open(image_path).convert("RGB")

        if st.button("Test Selected Image", type="primary"):
            with st.spinner("Running detection..."):
                result = detect_image(
                    model,
                    image,
                    confidence,
                    image_size
                )

            prediction = show_prediction(result)
            detections = detection_data(result)

            col1, col2 = st.columns(2)

            with col1:
                st.image(
                    image,
                    caption="Unseen Image",
                    use_container_width=True
                )

            with col2:
                st.image(
                    prediction,
                    caption="Model Prediction",
                    use_container_width=True
                )

            if detections:
                st.success(
                    f"{len(detections)} shoe(s) detected."
                )
            else:
                st.warning("No shoes detected.")

    st.divider()

    if os.path.exists(PREDICTION_DIR):
        saved_predictions = [
            f for f in os.listdir(PREDICTION_DIR)
            if f.lower().endswith(
                (".jpg", ".jpeg", ".png")
            )
        ]

        if saved_predictions:
            st.subheader("Saved Prediction Results")

            selected_predictions = st.multiselect(
                "Choose prediction images",
                sorted(saved_predictions),
                default=sorted(saved_predictions)[:3]
            )

            if selected_predictions:
                cols = st.columns(3)

                for i, filename in enumerate(
                    selected_predictions
                ):
                    with cols[i % 3]:
                        st.image(
                            os.path.join(
                                PREDICTION_DIR,
                                filename
                            ),
                            caption=filename,
                            use_container_width=True
                        )

with tab3:
    st.subheader("Model Performance")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Precision", "0.869")
    c2.metric("Recall", "0.752")
    c3.metric("mAP@50", "0.830")
    c4.metric("mAP@50-95", "0.580")

    st.divider()

    st.subheader("Validation vs Independent Test")

    results = {
        "Metric": [
            "Precision",
            "Recall",
            "mAP@50",
            "mAP@50-95"
        ],
        "Validation": [
            0.650,
            0.574,
            0.598,
            0.391
        ],
        "Test": [
            0.869,
            0.752,
            0.830,
            0.580
        ]
    }

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Dataset Overview")

    d1, d2, d3, d4 = st.columns(4)

    d1.metric("Original Images", "206")
    d2.metric("Training Images", "435")
    d3.metric("Validation Images", "41")
    d4.metric("Test Images", "20")

    st.caption(
        "The training set includes augmented images generated "
        "from the original training data."
    )

    st.divider()

    st.subheader("Class")

    st.write("👟 **Shoe**")

    st.info(
        "The model was trained as a single-class object detector "
        "to locate shoes in images."
    )