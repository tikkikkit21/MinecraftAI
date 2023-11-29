import cv2
from ultralytics import YOLO
import math
import time

# YOLO set up
import sys
TRAIN_NUM = ""
if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print("Usage: webcam.py [train number]")
        exit()
    else:
        try:
            TRAIN_NUM = int(sys.argv[1])
        except ValueError:
            print("Train number")
            exit()
path_to_weights = f"./runs/detect/train{TRAIN_NUM}/weights/best.pt"
model = YOLO(path_to_weights)

# 0 indicates it's a webcam
capture = cv2.VideoCapture(0)

# sets resolution
capture.set(3, 640)
capture.set(4, 480)

classes = [
    ('stand', (0, 0, 255)),
    ('walk', (0, 255, 0))
]

while True:
    success, img= capture.read()
    results = model(img, stream=True)

    # draw box
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # get class index and confidence
            (className, classColor) = classes[int(box.cls[0])]
            confidence = math.ceil((box.conf[0] * 100)) / 100

            if (confidence < 0.90):
                continue

            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), classColor, 2)

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            thickness = 2

            cv2.putText(img, f"{className}: {confidence}", org, font, fontScale, classColor, thickness)

    # names the window
    cv2.imshow('Webcam', img)

    # press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
