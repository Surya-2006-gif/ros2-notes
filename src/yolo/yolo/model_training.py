from ultralytics import YOLO
import os
import matplotlib.pyplot as plt

# ✅ Define dataset paths
dataset_path = os.path.join('/home/surya', 'Cone-Detection')

x_test = os.path.join(dataset_path, 'TraCon_dataset', 'images', 'test')
y_test = os.path.join(dataset_path, 'TraCon_dataset', 'labels', 'test')

datafile_path = os.path.join(dataset_path, 'TraCon_dataset', 'data.yaml')

# ✅ Load the YOLO model
model = YOLO('yolov8n.pt')  # using pre-trained YOLOv8 nano weights

# ✅ Train the model with necessary parameters
results = model.train(
    data=datafile_path,   # path to your data.yaml
    epochs=10,           # number of training epochs
    batch=16,             # batch size (adjust based on GPU memory)
    imgsz=640,            # input image size (default is 640)
    workers=4,            # number of data loading workers
    device='cpu',             # GPU device index, use 'cpu' if no GPU
    verbose=True          # show training logs
)

# ✅ After training, results are saved in results.save_dir
print("Training completed. Results saved at:", results.save_dir)


