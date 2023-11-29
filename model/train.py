from ultralytics import YOLO

EPOCHS = 5
IMGSZ=640

model = YOLO("yolov8n.pt")
training_results = model.train(
    data="./dataset/data.yaml",
    epochs=EPOCHS,
    imgsz=IMGSZ
)
