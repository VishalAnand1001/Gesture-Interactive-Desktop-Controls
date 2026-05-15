import pyautogui
import time

last_action_time = 0
cooldown = 1

def control_action(gesture):
    global last_action_time
    current_time = time.time()
    if current_time - last_action_time < cooldown:
        return
    
    if gesture == "ONE":
        pyautogui.press("volumeup")
    elif gesture == "TWO":
        pyautogui.press("volumedown")
    elif gesture == "THREE":
        pyautogui.scroll(-50)
    elif gesture == "FOUR":
        pyautogui.scroll(50)
    elif gesture == "FIST":
        pyautogui.press("esc")
    else:
        return
    
    last_action_time = current_time