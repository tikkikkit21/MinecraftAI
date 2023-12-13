# check to make sure there's no existing 'dataset' folder
import os, shutil
if os.path.exists("./dataset"):
    okDelete = input("A folder named 'dataset' already exists, delete and replace it? (Y/n) ")
    
    if (okDelete.lower() in ['', 'y', 'yes']):
        print("Deleting 'dataset'...")
        shutil.rmtree("./dataset")
    else:
        print("Please delete the folder and try again.")
        exit()

# get Roboflow tokens from .env file
from dotenv import load_dotenv
load_dotenv()

ROBOFLOW_API = os.environ.get("ROBOFLOW_API")
ROBOFLOW_WORKSPACE = os.environ.get("ROBOFLOW_WORKSPACE")
ROBOFLOW_PROJECT = os.environ.get("ROBOFLOW_PROJECT")

# download dataset
from roboflow import Roboflow
rf = Roboflow(ROBOFLOW_API)
workspace = rf.workspace(ROBOFLOW_WORKSPACE)
project = workspace.project(ROBOFLOW_PROJECT)
print(f"Found project '{project.name}' in workspace '{workspace.name}'")

# get version number
import sys

PROJECT_VERSION = 1
if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print("Usage: dataset.py [version number, default is latest]")
        exit()
    else:
        try:
            PROJECT_VERSION = int(sys.argv[1])
        except ValueError:
            print("Version number needs to be an int")
            exit()
else:
    PROJECT_VERSION = project.versions()[0].version

print(f"Downloading version {PROJECT_VERSION}")
dataset = project.version(PROJECT_VERSION).download(model_format="yolov8", location="./dataset")
