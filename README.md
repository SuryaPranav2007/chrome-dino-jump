# Chrome Dino Jump — Body Controlled!

Control the Chrome Dino game by physically jumping in front of your webcam!
Built using Python, OpenCV, MediaPipe, and PyAutoGUI.

---
## How It Works

Your webcam detects your shoulder position in real time using MediaPipe Pose.
When you jump, your shoulders rise — the script detects that movement and
automatically presses the spacebar, making the dino jump.

---
## Requirements

- Python 3.11
- Google Chrome
---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/suryapranav2007/chrome-dino-jump.git
cd chrome-dino-jump
```

**2. Install dependencies**
```bash
py -3.11 -m pip install opencv-python mediapipe==0.10.9 pyautogui
```
---

## How To Run

1. Open Chrome and go to `chrome://dino`
2. Press **Space once** to start the game
3. **Alt+Tab** back to your terminal
4. Run the script:
```bash
py -3.11 jump_dino.py
```
5. Click on Chrome to bring it into focus
6. Jump in front of your webcam — the dino jumps with you!

---
## Controls

| Action | Result |
|---|---|
| Jump | Dino jumps |
| Press Q on webcam window | Quit the program |

---

## Tuning Sensitivity

Open `jump_dino.py` and adjust these values at the top:

```python
JUMP_THRESHOLD = 0.02   # Lower = more sensitive
COOLDOWN_SEC   = 0.3    # Lower = faster response
```

---

## Libraries Used

| Library | Purpose |
|---|---|
| OpenCV | Webcam access and display |
| MediaPipe | Human pose detection |
| PyAutoGUI | Keyboard automation |

---

## 👤 Author

Surya Pranav — [GitHub](https://github.com/suryapranav2007)
