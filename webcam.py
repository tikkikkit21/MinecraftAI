import cv2

# 0 indicates it's a webcam
capture = cv2.VideoCapture(0)

# sets resolution
capture.set(3, 640)
capture.set(4, 480)

while True:
    ret, img= capture.read()

    # names the window
    cv2.imshow('Webcam', img)

    # press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
