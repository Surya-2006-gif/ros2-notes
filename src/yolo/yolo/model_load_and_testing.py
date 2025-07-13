from ultralytics import YOLO

# Load trained model
model = YOLO('/home/surya/ros2_ws/src/yolo/runs/detect/train2/weights/best.pt')

# Predict on test images folder
results = model.predict(
    source='/home/surya/Cone-Detection/TraCon_dataset/images/test',
    save=True  # saves images with bounding boxes
)
