#Surya Pranav's Dino Jump Controller
import cv2
import mediapipe as mp
import pyautogui
import time

# --- Config ---
JUMP_THRESHOLD = 0.02   # How much shoulders must rise (relative to frame height)
COOLDOWN_SEC   = 0.2    # Seconds before another jump can trigger
# --------------

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

cap = cv2.VideoCapture(0)

prev_shoulder_y  = None
last_jump_time   = 0
jump_triggered   = False

print("Press Q to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror the screen for it to look natural
    h, w = frame.shape[:2]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    status_text = "No pose detected"
    color       = (0, 0, 255)

    if results.pose_landmarks:
        lm = results.pose_landmarks.landmark

        # Average of left + right shoulder Y (normalized 0-1, so UP = smaller value)
        left_y  = lm[mp_pose.PoseLandmark.LEFT_SHOULDER].y
        right_y = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
        shoulder_y = (left_y + right_y) / 2

        if prev_shoulder_y is not None:
            delta = prev_shoulder_y - shoulder_y  # Positive = moved UP

            now = time.time()
            cooldown_ok = (now - last_jump_time) > COOLDOWN_SEC

            if delta > JUMP_THRESHOLD and cooldown_ok:
                pyautogui.press("space")
                last_jump_time  = now
                jump_triggered  = True
                print(f"JUMP! delta={delta:.3f}")

        prev_shoulder_y = shoulder_y

        # Draw pose skeleton
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Visual feedback
        if jump_triggered and (time.time() - last_jump_time) < 0.3:
            status_text = "JUMP!"
            color       = (0, 255, 0)
        else:
            jump_triggered = False
            status_text    = "Ready"
            color          = (255, 200, 0)

    # HUD
    cv2.putText(frame, status_text, (20, 50),
                cv2.FONT_HERSHEY_DUPLEX, 1.4, color, 2)
    cv2.putText(frame, "Q = quit", (20, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 1)

    cv2.imshow("Jump Dino Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()