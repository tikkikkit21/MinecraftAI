# get Roboflow tokens from .env file
from dotenv import load_dotenv
load_dotenv()

import os
ROBOFLOW_API = os.environ.get("ROBOFLOW_API")
ROBOFLOW_WORKSPACE = os.environ.get("ROBOFLOW_WORKSPACE")
ROBOFLOW_PROJECT = os.environ.get("ROBOFLOW_PROJECT")

# download dataset
from roboflow import Roboflow
rf = Roboflow(ROBOFLOW_API)
project = rf.workspace(ROBOFLOW_WORKSPACE).project(ROBOFLOW_PROJECT)
dataset = project.version(1).download(model_format="yolov8", location="./dataset")
