import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="YOLO Object Detection",
    page_icon="🤖",
    layout="centered"
)

# -------------------- TITLE --------------------
st.title("🤖 YOLO Object Detection App")
st.caption("Upload an image and get accurate object detection results")

# -------------------- LOAD MODEL --------------------
@st.cache_resource
def load_model():
    return YOLO("yolo11n.pt")

model = load_model()

# -------------------- SIDEBAR --------------------
st.sidebar.header("⚙️ Detection Settings")
conf_threshold = st.sidebar.slider(
    "Confidence Threshold",
    min_value=0.1,
    max_value=1.0,
    value=0.5,
    step=0.05
)

# -------------------- IMAGE UPLOAD --------------------
uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_file is not None:
    # Read image correctly
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    # Show original image
    st.subheader("🖼️ Original Image")
    st.image(image, use_container_width=True)

    # Run detection
    if st.button("🚀 Run Detection"):
        with st.spinner("Detecting objects..."):
            results = model(image_np, conf=conf_threshold)

            # Plot result (BGR → RGB conv
