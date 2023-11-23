# YOLOv8 Webcam Test
This branch is to test how to use the webcam in conjunction with YOLOv8. I'm
looking at [this tutorial](https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993).

1. `pip install opencv-python`
    - I also had to `pip install opencv-contrib-python` to resolve some weird errors
2. Use this Python code to open up a webcam window:
    ```Python
    import cv2

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        ret, img= cap.read()
        cv2.imshow('Webcam', img)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```
3. Going to use coco128 (a global dataset) to train some pseudo data:
`yolo train data=coco128.yaml model=yolov8n.pt epochs=10 lr0=0.01`
4. After training, we can use the `best.pt` found under the run
5. Use some math to draw the rectangle and display class name + confidence
6. Result:<br>![result](result.png) 

Some notes:
- FPS is around 27, which is sufficient, but I would like to see if I can achieve 40
- The `classNames` list has to be a certain way since the YOLO model only returns
the index. Right now, I'm not sure how to find the mapping between index and
class name
- The middleware code could be in the same file as webcam code since as the model
gives an output, we immediately send the corresponding signal to Minecraft. This
would be simpler than having 2 separate programs running that somehow communicated
with each other
- I would like to see whether I can track movement (ex: instead of classifying a
standalone image, it would track a whole movement. This might be more of a code
thing instead of training thing).
- ^ building off of that, we need to have some robustness. For example, sometimes
the model may accidentally classify a single frame incorrectly. We don't want this
small mistake to actually affect the gameplay. So we could introduce something
like a counter where some classification $C$ had to be persistent across $n$ frames
before triggering Minecraft
