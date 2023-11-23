from roboflow import Roboflow
rf = Roboflow(api_key="PZGlBTGGM8JFdz8FGC9r")
project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
dataset = project.version(2).download("yolov8")
