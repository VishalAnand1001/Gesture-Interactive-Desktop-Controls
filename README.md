# Gesture Controlled Desktop System

A real-time AI-powered desktop automation system that uses hand gestures to control system actions through a webcam.

Built using Python, OpenCV, MediaPipe, and PyAutoGUI.

---

# Features

* Real-time webcam feed processing
* AI-based hand tracking using MediaPipe
* Finger-state gesture recognition
* Desktop automation using PyAutoGUI
* Cooldown system to prevent repeated actions
* Modular project structure

---

# Tech Stack

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

---

# Project Workflow

```text
Webcam Feed
     ↓
Hand Detection
     ↓
Landmark Extraction
     ↓
Gesture Recognition
     ↓
Desktop Action Mapping
     ↓
Cooldown System
     ↓
Real-Time Desktop Control
```

---

# Gestures and Actions

| Gesture       | Action          |
| ------------- | --------------- |
| ONE Finger    | Increase Volume |
| TWO Fingers   | Decrease Volume |
| THREE Fingers | Scroll Down     |
| FOUR Fingers  | Scroll Up       |
| FIST          | Press ESC       |

---

# Project Structure

```text
GESTURE-INTERACTIVE-DESKTOP-CONTROLS/
│
├── main.py
├── hand_detector.py
├── gesture_recognizer.py
├── action_controller.py
├── requirements.txt
└── README.md
```

---

# File Responsibilities

## main.py

Controls the overall application pipeline:

* Captures webcam frames
* Calls hand detection
* Calls gesture recognition
* Executes desktop actions
* Displays webcam output

## hand_detector.py

Responsible for:

* Hand tracking using MediaPipe
* Landmark extraction
* Drawing hand landmarks

## gesture_recognizer.py

Responsible for:

* Finger-state analysis
* Gesture detection logic
* Mapping open fingers to gestures

## action_controller.py

Responsible for:

* Desktop automation
* Volume control
* Scrolling
* Cooldown/debounce system

---

# How Gesture Recognition Works

The system detects whether each finger is open or closed by comparing landmark coordinates from MediaPipe.

Example:

```python
index_open = landmark[8].y < landmark[6].y
```

If the fingertip is above the finger joint, the finger is considered open.

The combination of open and closed fingers is then mapped to a specific gesture.

---

# Cooldown System

A cooldown system was implemented to prevent repeated actions from triggering every frame.

Example:

```python
if current_time - last_action_time < cooldown:
    return
```

This ensures stable and controlled desktop interactions.

---

# Installation

## 1. Clone the repository

```bash
git clone <your-repository-link>
cd GESTURE-INTERACTIVE-DESKTOP-CONTROLS
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

## 3. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

```bash
python main.py
```

Press `ESC` to close the application.

---

# Future Improvements

* Real-time mouse cursor control
* Gesture-based clicking
* Brightness control
* Multi-hand support
* AI-based custom gesture training
* Smoother cursor movement
* Gesture confidence filtering

---

# Challenges Faced

* MediaPipe installation and environment setup
* Understanding landmark coordinate systems
* Mapping gestures reliably
* Preventing action spamming
* Integrating multiple modules together

---

# Learning Outcomes

This project helped in learning:

* Computer Vision fundamentals
* Real-time webcam processing
* MediaPipe hand tracking
* Gesture recognition logic
* Desktop automation
* Modular software architecture
* Cooldown/debounce systems
* Debugging and environment management

---

# Author

Vishal Anand

Computer Science Student | AI Enthusiast