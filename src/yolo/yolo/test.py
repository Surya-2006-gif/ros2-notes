import os
from ultralytics import YOLO
import cv2

model  = YOLO('/home/surya/ros2_ws/src/yolo/runs/detect/train2/weights/best.pt')


image = '/home/surya/Downloads/test.jpg'

results = model.predict(image)

result = results[0]

annotations = result.plot()

cv2.imshow('window',annotations)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

