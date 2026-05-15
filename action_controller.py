import pyautogui

def control_action(gesture):
    if gesture=="ONE":
        pyautogui.press("volumeup")
    elif gesture=="TWO":
        pyautogui.press("volumedown")
    elif gesture=="THREE":
        pyautogui.scroll(-50)
    elif gesture=="FOUR":
        pyautogui.scroll(50)
    elif gesture=="FIST":
        pyautogui.press("esc")
    
