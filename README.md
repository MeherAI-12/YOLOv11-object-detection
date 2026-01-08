
# 🎯 YOLO Object Detection Web App using Streamlit

## 📌 Project Overview

This project is a **real-time object detection web application** built using **Streamlit** and the **Ultralytics YOLO (You Only Look Once)** model.
The application allows users to **upload an image**, run object detection, and visually see **bounding boxes, class labels, and confidence-based detections** directly in the browser.

The app is lightweight, fast, and **deployment-ready**, making it suitable for **demo purposes, academic projects, and AI/ML portfolios**.

---

## 🚀 Key Features

* 📤 Image upload support (`.jpg`, `.png`, `.jpeg`, `.webp`)
* 🤖 YOLOv8 pre-trained model for object detection
* 🎯 Adjustable confidence threshold
* 🖼️ Displays both original and detected images
* 📦 Shows total detected object count
* 🏷️ Lists detected object classes
* ⚡ Optimized model loading using Streamlit caching
* ☁️ Easily deployable on Streamlit Cloud

---

## 🧠 Technologies Used

* **Python**
* **Streamlit** – Web application framework
* **Ultralytics YOLOv8** – Object detection model
* **OpenCV** – Image processing
* **NumPy** – Array operations
* **Pillow (PIL)** – Image handling

---

## 🛠️ How the Code Works (Step-by-Step)

### 1️⃣ Import Required Libraries

The application imports essential libraries for:

* UI rendering (`streamlit`)
* Object detection (`ultralytics YOLO`)
* Image handling (`PIL`, `OpenCV`)
* Numerical processing (`NumPy`)

---

### 2️⃣ Page Configuration

```python
st.set_page_config(
    page_title="YOLO Object Detection",
    page_icon="🎯",
    layout="centered"
)
```

Sets the web page title, icon, and layout for a clean UI.

---

### 3️⃣ Load YOLO Model (Cached)

```python
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")
```

* Loads the YOLOv8 model only once
* Prevents reloading on every Streamlit rerun
* Improves performance significantly

---

### 4️⃣ Sidebar Controls

A confidence threshold slider allows users to control detection sensitivity:

```python
conf = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.5, 0.05)
```

---

### 5️⃣ Image Upload

```python
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg", "webp"])
```

Users upload an image that will be processed by the YOLO model.

---

### 6️⃣ Object Detection Pipeline

* Uploaded image is converted to RGB format
* YOLO performs inference using `model.predict()`
* Bounding boxes are drawn using YOLO’s built-in `plot()` function
* OpenCV converts image from **BGR → RGB** for proper display in Streamlit

---

### 7️⃣ Display Results

* Annotated detection image is displayed
* Total number of detected objects is shown
* Detected object class names are listed for clarity

---

## 📂 Project Structure

```
├── app.py
├── requirements.txt
├── README.md
```

---

## 📦 Installation & Usage

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Run the Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This application can be deployed easily using:

* **Streamlit Cloud**
* **Localhost**
* **Docker (optional)**

---

## 🎓 Learning Outcomes

* Hands-on experience with YOLO object detection
* Practical Streamlit deployment skills
* Image processing using OpenCV
* Efficient ML model handling in web apps

---

## 🔮 Future Enhancements

* 🎥 Video and webcam detection
* 🐟 Custom-trained YOLO models (e.g., underwater fish detection)
* 📊 Detection confidence tables
* 🧠 GPU acceleration support

---

## 👨‍💻 Author

**Meher Vitthal Rao Kamdi**
AI/ML Research Intern | Python Developer
...
