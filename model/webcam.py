import cv2
from ultralytics import YOLO
import math
import time
import sys

sys.path.insert(0, '../middleware')

from basic import *
# YOLO set up
import sys
TRAIN_NUM = 10
# if len(sys.argv) == 2:
#     if sys.argv[1] == "-h":
#         print("Usage: webcam.py [train number]")
#         exit()
#     else:
#         try:
#             TRAIN_NUM = int(sys.argv[1])
#         except ValueError:
#             print("Train number")
#             exit()
path_to_weights = f"./runs/detect/train{TRAIN_NUM}/weights/best.pt"
model = YOLO(path_to_weights)

# 0 indicates it's a webcam
capture = cv2.VideoCapture(0)

# sets resolution
capture.set(3, 640)
capture.set(4, 480)

classes = [
    # ('stand', (0, 0, 255)),
    # ('walk', (0, 255, 0))
    ('head_up', (255, 0, 0)),
    ('right_click', (255, 0, 0)),
    ('shift', (255, 0, 0)),
    ('walk', (255, 0, 0))
]

# Middleware setup
ctrl = Movement()
hands = Hands()
head = Head()

while True:
    success, img= capture.read()
    results = model(img, stream=True, verbose=False)

    # draw box
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # get class index and confidence
            (className, classColor) = classes[int(box.cls[0])]
            confidence = math.ceil((box.conf[0] * 100)) / 100

            if (confidence < 0.70):
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
            print(f"Detected {className}: {confidence}")

            if className == 'head_up':
                ctrl.stop()
                head.rotateUp()
            elif className == 'right_click':
                ctrl.stop()
                hands.placeBlock()
            elif className == 'shift':
                ctrl.sneak()
            elif className == 'walk':
                ctrl.moveForward()
            else:
                ctrl.stop()


    # names the window
    cv2.imshow('Webcam', img)

    # press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
