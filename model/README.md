# Model
YOLOv8 for image recognition

## Dataset
Use `dataset.py` to download the Roboflow dataset. Note that the API key,
project, and workspace code are stored in a separate .env file, which is not
included in the repository for security reasons. Teammates will need to obtain
the values and store in their own local .env file.

Some of the pip packages used:
- `roboflow`
- `python-dotenv`

## Training
Use `train.py` to train the model after downloading the dataset.git 

Pip packages used:
- `ultranalytics`
