import cv2
from hand_detector import detect_hands
from gesture_recognizer import detect_gesture

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if ret==True:
        frame, results = detect_hands(frame)
        gesture = "NO HAND"
        if results.multi_hand_landmarks:
            gesture = detect_gesture(results)
        cv2.putText(
            frame,
            gesture,
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)
        if key==27:
            break

webcam.release()
cv2.destroyAllWindows()