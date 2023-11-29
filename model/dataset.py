# get Roboflow tokens from .env file
from dotenv import load_dotenv
load_dotenv()

import os
api = os.environ.get("ROBOFLOW_API")
workspace = os.environ.get("ROBOFLOW_WORKSPACE")
project = os.environ.get("ROBOFLOW_PROJECT")

# download dataset
from roboflow import Roboflow
rf = Roboflow(api)
project = rf.workspace(workspace).project(project)
dataset = project.version(1).download(model_format="yolov8", location="./dataset")
