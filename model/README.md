# Model
YOLOv8 for image recognition

## Dataset
Use `dataset.py` to download the Roboflow dataset. Note that the API key,
project, and workspace code are stored in a separate .env file, which is not
included in the repository for security reasons. Teammates will need to obtain
the values and store in their own local .env file.

Pip packages used:
- `roboflow`
- `python-dotenv`

## Training
Use `train.py` to train the model after downloading the dataset. You can provide
the number of training epochs like so: `train.py [num epochs]`. If none are
provided, the default is 20. You can also use `-h` for a help message.

Pip packages used:
- `ultranalytics`

## Webcam Detection
Use `webcam.py` to open the webcam and start detecting motions. It'll draw a
box around a detected class and output the class name and confidence level.
Currently, there's some YOLO output in the console for every frame detected. I
want to disable it, but haven't figured it out yet.

Pip packages used:
- `opencv-python`
