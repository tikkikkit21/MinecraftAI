# Notes
The goal of this branch is to learn how to train custom data using YOLOv8. These
are my notes about what I did as I followed this tutorial:
https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/


1. First install packages: `pip install -r requirements.txt`
2. Use the [football player](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/2?ref=blog.roboflow.com)
sample dataset
    - In our actual project, we'll be uploading and annotating our own dataset
3. Export the dataset in Roboflow via the "Jupyter" option. The will result in some Python code:
    ```Python
    from roboflow import Roboflow
    rf = Roboflow(api_key="PZGlBTGGM8JFdz8FGC9r")
    project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
    dataset = project.version(2).download("yolov8")
    ```
    - Will need to `pip install roboflow` 
4. After running this script, we will have downloaded our dataset like so:

```
dataset-name
  ├─ data.yaml      <- YAML file with some config info about the dataset
  ├─ test/          <- images to test different models (step 2)
  ├─ train/         <- initial data to train the model (step 1)
  ├─ valid/         <- data to validate final selected model (step 3)
  
```
5. `yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=100 imgsz=640`
    - I did have to tweak `data.yaml` to match the file hierarchy by replacing `../` with `./` since the images were in the same location as the YAML
    - I also had to modify `C:\Users\Me\AppData\Roaming\Ultralytics\settings.yaml` to change the dataset directory to point to `yoloTest`
6. After like 16 hours (for 100 epochs), we have results in `runs/detect/train#`. There are weight files that we can use for later.
