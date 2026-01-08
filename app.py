import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="YOLO Object Detection",
    page_icon="🤖",
    layout="centered"
)

# -------------------- TITLE --------------------
st.markdown(
    "<h1 style='text-align: center;'>🤖 YOLO Object Detection App</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Upload an image and detect objects using YOLO</p>",
    unsafe_allow_html=True
)
st.divider()

# -------------------- LOAD MODEL --------------------
@st.cache_resource
def load_model():
    return YOLO("yolo11n.pt")

model = load_model()

# -------------------- SIDEBAR --------------------
st.sidebar.header("⚙️ Settings")
confidence = st.sidebar.slider(
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
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Show orig
