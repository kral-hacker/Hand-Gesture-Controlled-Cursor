# 🖐️ Hand Gesture Controlled Cursor

A fun side project that turns your hand gestures into system-level commands like controlling the mouse cursor, switching tabs, and adjusting volume — all without touching your keyboard or mouse!

## 📽️ Demo

Check out the full demo video here:  
[![Demo Video](https://img.shields.io/badge/Watch%20Demo-YouTube-red?logo=youtube)](https://your-demo-video-link.com)

---

## ✨ Features

- Real-time hand gesture tracking using **MediaPipe**
- Control cursor movement and clicks with your fingers
- Switch browser tabs with a three-finger gesture
- Control system volume using hand gestures
- Works with just a webcam — no special hardware required

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV** – for real-time video capture and frame processing
- **MediaPipe** – for accurate hand tracking and gesture detection
- **PyAutoGUI** – to simulate mouse movement, clicks, tab switches, and volume control

---

## 🎮 How to Use

| Gesture | Action |
|--------|--------|
| ☝️ Thumb + Index Finger Up | Move the cursor |
| 🤏 Pinch Thumb & Index | Mouse Click |
| ✌️ + ☝️ Ring Finger Up | Switch Tabs |
| 🤘 + ☝️ Little Finger Up | Volume Up |
| ✊ Fist | Volume Down |
| ✋ All Fingers Up | Pause (No movement) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hand-gesture-cursor-control.git
cd hand-gesture-cursor-control

### 2. Run the changes.py file 
