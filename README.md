# MinecraftAI
This project is for playing Minecraft but with hand gestures. Generally
speaking, the project outline is:
1. Gesture Recognition
    - Dataset preparation
    - Model training
2. Connecting to Minecraft

## Tasks
- Tikki: training model
    - Use YOLOv8 and have it utilize the webcam
    - Get a decent FPS of ~30-40
    - Achieve ideal accuracy (~90%)
- Eugene: creating middleware
    - Works with YOLO output
    - Connect to Minecraft and map YOLO output to Minecraft actions
- Louis: design data collection
    - Design which gestures corresponds to which Minecraft actions
    - Outline what the data will look like
        - Image dimensions and quality
        - How the gesture looks like
- Sam: annotate and prepare date
    - Break apart videos into frames
    - Annotate each frame with RoboFlow
    - Send data to Tikki for model training

## Project Workflow
We will be using GitHub to store all our work. Communication will occur in the group chat (either iMessage or Discord). We will be using **branching** and **pull requests** to update the codebase.
