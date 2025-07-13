from yolov8_msgs.msg import Yolo, Detections
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import rclpy
from rclpy.node import Node
from ultralytics import YOLO

class yolo_pub(Node):

    def __init__(self):
        super().__init__('yolo_pub')

        # Publisher for Detections msg
        self.yolo_publisher = self.create_publisher(Detections, 'yolo_detections', 10)

        # Subscriber to camera image
        self.subscriber = self.create_subscription(Image, '/my_camera/image_raw', self.subscriber_callback, 10)

        self.bridge = CvBridge()

        # Load YOLO model
        self.model = YOLO('yolov8n.pt')  # Replace with your actual model file if needed

    def subscriber_callback(self, image_raw):
        # Convert ROS image to OpenCV image
        image = self.bridge.imgmsg_to_cv2(image_raw, 'bgr8')

        # Predict with YOLO
        results = self.model.predict(image)
        result = results[0]  # Get the first (and only) result

        # Create Detections message
        msg = Detections()

        boxes = result.boxes
        cls = boxes.cls
        conf = boxes.conf
        xyxy = boxes.xyxy

        # Loop through detections
        for i in range(len(cls)):
            det = Yolo()  # Using Yolo message type here
            det.class_id = int(cls[i].item())
            det.class_name = result.names[det.class_id]
            det.confidence = float(conf[i].item())
            det.x1 = float(xyxy[i][0].item())
            det.y1 = float(xyxy[i][1].item())
            det.x2 = float(xyxy[i][2].item())
            det.y2 = float(xyxy[i][3].item())

            msg.detections.append(det)

        # Publish detections
        self.yolo_publisher.publish(msg)
        annotated_img = result.plot()
        cv2.imshow("YOLOv8 Detections", annotated_img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = yolo_pub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
