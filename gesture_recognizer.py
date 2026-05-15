import cv2
import mediapipe as mp

def detect_gesture(results):
    index_open = results.multi_hand_landmarks[0].landmark[8].y < results.multi_hand_landmarks[0].landmark[6].y
    middle_open = results.multi_hand_landmarks[0].landmark[12].y < results.multi_hand_landmarks[0].landmark[10].y
    ring_open =  results.multi_hand_landmarks[0].landmark[16].y < results.multi_hand_landmarks[0].landmark[14].y
    pinky_open = results.multi_hand_landmarks[0].landmark[20].y < results.multi_hand_landmarks[0].landmark[18].y

    gesture = "UNKNOWN"
    if index_open and not middle_open and not ring_open and not pinky_open:
        gesture = "ONE"
    elif index_open and middle_open and not ring_open and not pinky_open:
        gesture = "TWO"
    elif index_open and middle_open and ring_open and not pinky_open:
        gesture = "THREE"
    elif index_open and middle_open and ring_open and pinky_open:
        gesture = "FOUR"
    elif not index_open and not middle_open and not ring_open and not pinky_open:
        gesture = "FIST"
    
    return gesture