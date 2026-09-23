# 😊 Face Emotion Detection

A real-time facial emotion detection system built using **Python, OpenCV, and FER (Facial Emotion Recognition)**. The application uses a webcam to detect faces and identify the dominant emotion expressed by each detected face.

## 🚀 Features

* Real-time webcam-based face detection
* Facial emotion recognition
* Detection of multiple faces in a frame
* Bounding box around detected faces
* Displays the dominant emotion above each detected face
* Real-time video processing using OpenCV
* Simple and beginner-friendly implementation

## 🧠 Emotions Detected

The FER library provides emotion probabilities for detected faces. The project identifies the emotion with the highest probability as the dominant emotion.

Common emotions include:

* 😄 Happy
* 😢 Sad
* 😠 Angry
* 😨 Fear
* 😲 Surprise
* 🤢 Disgust
* 😐 Neutral

## 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **FER (Facial Emotion Recognition)**
* **MTCNN**
* Computer Vision
* Deep Learning

## 📁 Project Structure

```text
face-emotion-detection/
│
├── emotion.py
├── camera_test.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ How It Works

The system follows these steps:

```text
Webcam
   ↓
Capture Video Frame
   ↓
Detect Faces
   ↓
Analyze Facial Expressions
   ↓
Calculate Emotion Probabilities
   ↓
Find Dominant Emotion
   ↓
Display Emotion + Face Bounding Box
```

## 🔍 Implementation

The project initializes the webcam using OpenCV and processes the video stream frame by frame.

```python
cap = cv2.VideoCapture(1)
```

The FER detector is initialized with MTCNN:

```python
detector = FER(mtcnn=True)
```

Each frame is then passed to the emotion detector:

```python
result = detector.detect_emotions(frame)
```

For every detected face, the project obtains the emotion probabilities and selects the emotion with the highest probability:

```python
dominant_emotion = max(
    emotions,
    key=emotions.get
)
```

The detected emotion is then displayed on the live video feed.

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/face-emotion-detection.git
```

### 2. Navigate to the project

```bash
cd face-emotion-detection
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Run the main emotion detection program:

```bash
python emotion.py
```

A webcam window should open and display detected faces along with their dominant emotions.

Press:

```text
Q
```

to stop the application.

## 📷 Camera Configuration

The project currently uses:

```python
cv2.VideoCapture(1)
```

If your webcam does not open, try changing the camera index:

```python
cv2.VideoCapture(0)
```

For example:

```python
cap = cv2.VideoCapture(0)
```

`0` usually refers to the default webcam, while `1` may refer to another connected camera.

## 🧪 Testing the Camera

The repository also contains `camera_test.py`, which can be used to verify whether the selected webcam is working correctly before running emotion detection.

```bash
python camera_test.py
```

The camera test captures frames and displays them in an OpenCV window.

## 📊 Output

The application displays:

* Detected face location
* Bounding box around each face
* Dominant detected emotion
* Live webcam feed

Example:

```text
┌─────────────────────────────┐
│                             │
│       ┌───────────┐         │
│       │   FACE    │         │
│       │           │ Happy   │
│       └───────────┘         │
│                             │
└─────────────────────────────┘
```

## 🎯 Applications

Facial emotion recognition can be explored for applications such as:

* Human-computer interaction
* Educational interfaces
* User experience research
* Interactive AI systems
* Customer experience analysis
* Social robotics
* Accessibility applications

## 🔮 Future Improvements

Possible improvements include:

* Add emotion confidence scores
* Improve face detection accuracy
* Add emotion history and analytics
* Save detected emotion statistics
* Add graphical dashboards
* Support image and video files
* Add age and gender estimation
* Improve performance for low-light conditions
* Build a web interface using Streamlit or Flask
* Add database storage for emotion statistics
* Deploy the application as a web application

## ⚠️ Limitations

Emotion recognition is an estimation based on facial appearance and should not be treated as a definitive measurement of a person's actual emotional state.

Performance can also vary depending on:

* Lighting conditions
* Camera quality
* Face angle
* Occlusion
* Distance from the camera
* Multiple faces
* Facial expressions

## 📚 Learning Outcomes

Through this project, the following concepts were explored:

* Computer vision
* Real-time video processing
* Face detection
* Facial emotion recognition
* Python programming
* OpenCV
* Deep learning-based emotion analysis
* Webcam integration

## 👨‍💻 Author

**Ayushmaan**

GitHub: `https://github.com/YOUR_USERNAME`

LinkedIn: `https://www.linkedin.com/in/YOUR_USERNAME/`

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub!
