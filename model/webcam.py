import cv2
from ultralytics import YOLO
import math
import time

# YOLO set up
path_to_weights = "./runs/detect/train10/weights/best.pt"
model = YOLO(path_to_weights)

# 0 indicates it's a webcam
capture = cv2.VideoCapture(0)

# sets resolution
capture.set(3, 640)
capture.set(4, 480)

classNames = ["walk"]

while True:
    success, img= capture.read()
    results = model(img, stream=True)

    # draw box
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            # print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            # print("Class name -->", classNames[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 0, 255)
            thickness = 2

            cv2.putText(img, f"{classNames[cls]}: {confidence}", org, font, fontScale, color, thickness)

    # names the window
    cv2.imshow('Webcam', img)

    # press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
