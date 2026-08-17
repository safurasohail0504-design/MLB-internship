import os
import tempfile

import streamlit as st
from ultralytics import YOLO

st.set_page_config(
    page_title="Shoe Detection AI",
    page_icon="👟",
    layout="centered"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best.pt")

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None

    return YOLO(MODEL_PATH)

model = load_model()


if model is None:
    st.error("❌ YOLO model not found.")

    st.write("Streamlit is looking for:")

    st.code(MODEL_PATH)

    st.info(
        "Make sure best.pt is committed inside the day_39 folder."
    )

    st.stop()

st.title("👟 Shoe Detection AI")

st.write(
    "Upload an image and the custom YOLO model "
    "will detect shoes."
)

st.success("✅ YOLO model loaded successfully!")

uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    st.subheader("📷 Uploaded Image")

    st.image(
        uploaded_file,
        caption="Original Image",
        use_container_width=True
    )

    if st.button("🔍 Detect Shoes", type="primary"):

        with st.spinner("Detecting shoes..."):

            try:
                # Save uploaded image temporarily
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".jpg"
                ) as temp_file:

                    temp_file.write(uploaded_file.getbuffer())
                    temp_path = temp_file.name

                # Run YOLO
                results = model.predict(
                    source=temp_path,
                    conf=0.25,
                    verbose=False
                )

                # Get first result
                result = results[0]

                # Create annotated image
                annotated_image = result.plot()

                # Display result
                st.subheader("🎯 Detection Result")

                st.image(
                    annotated_image,
                    caption="Detected Shoes",
                    use_container_width=True
                )

                boxes = result.boxes

                if boxes is not None and len(boxes) > 0:

                    st.subheader("📊 Detection Details")

                    total_detections = len(boxes)

                    st.write(
                        f"**Total detections:** {total_detections}"
                    )

                    for i, box in enumerate(boxes):

                        class_id = int(
                            box.cls[0].item()
                        )

                        confidence = float(
                            box.conf[0].item()
                        )

                        class_name = model.names[class_id]

                        st.write(
                            f"**{i + 1}. {class_name}** "
                            f"— Confidence: "
                            f"{confidence:.2%}"
                        )

                else:

                    st.warning(
                        "⚠️ No shoes were detected "
                        "in this image."
                    )

                # Delete temporary file
                os.remove(temp_path)

            except Exception as e:

                st.error(
                    "❌ An error occurred during detection."
                )
                st.exception(e)
