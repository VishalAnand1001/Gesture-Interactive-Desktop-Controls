import cv2
webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if ret==True:
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)
        if key==27:
            break

webcam.release()
cv2.destroyAllWindows()