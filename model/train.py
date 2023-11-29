# parse program arguments
import sys
EPOCHS = 20
IMGSZ=640

if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print("Usage: train.py [num epochs, default is 20]")
        exit()
    else:
        EPOCHS = sys.argv[1]

# train with YOLOv8
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
training_results = model.train(
    data="./dataset/data.yaml",
    epochs=EPOCHS,
    imgsz=IMGSZ
)
