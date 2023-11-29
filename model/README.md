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
Use `train.py` to train the model after downloading the dataset. You can provide
the number of training epochs like so: `train.py [num epochs]`. If none are
provided, the default is 20. You can also use `-h` for a help message.

Pip packages used:
- `ultranalytics`
