import streamlit as st
import cv2
import numpy as np

def compare_images(img1, img2):

    gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

    orb = cv2.ORB_create()

    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # Create Brute Force Matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(descriptors1, descriptors2)

    # Sort matches
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw first 30 matches
    result = cv2.drawMatches(
        img1,
        keypoints1,
        img2,
        keypoints2,
        matches[:30],
        None,
        flags=2
    )

    return result, len(keypoints1), len(keypoints2), len(matches)


# ---------------- Streamlit App ---------------- #

st.title("Image Feature Matching System")

st.write(
    "Upload two similar images to detect ORB keypoints and compare their features."
)

image1 = st.file_uploader(
    "Upload Image 1",
    type=["jpg", "jpeg", "png"]
)

image2 = st.file_uploader(
    "Upload Image 2",
    type=["jpg", "jpeg", "png"]
)

if image1 is not None and image2 is not None:

    # Read Image 1
    file1 = np.asarray(bytearray(image1.read()), dtype=np.uint8)
    img1 = cv2.imdecode(file1, cv2.IMREAD_COLOR)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    # Read Image 2
    file2 = np.asarray(bytearray(image2.read()), dtype=np.uint8)
    img2 = cv2.imdecode(file2, cv2.IMREAD_COLOR)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    st.subheader("Original Images")

    col1, col2 = st.columns(2)

    with col1:
        st.image(img1)

    with col2:
        st.image(img2)

    if st.button("Compare Images"):

        output, kp1, kp2, total_matches = compare_images(img1, img2)

        st.subheader("Matched Features")

        st.image(output)

        st.success(f"Image 1 Keypoints : {kp1}")
        st.success(f"Image 2 Keypoints : {kp2}")
        st.success(f"Good Matches : {total_matches}")

        # Convert image into PNG bytes
        output_bgr = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)

        success, buffer = cv2.imencode(".png", output_bgr)

        st.download_button(
            label="Download Matched Image",
            data=buffer.tobytes(),
            file_name="feature_matching.png",
            mime="image/png"
        )