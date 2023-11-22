# Notes
These are my notes about what I did as I followed this tutorial:
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
