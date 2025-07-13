import rclpy
from rclpy.node import Node
from yolov8_msgs.msg import Detections

class yolo_sub(Node):

    def __init__(self):
        super().__init__('yolo_sub')

        # Create subscriber to 'yolo_detections' topic
        self.subscription = self.create_subscription(
            Detections,
            'yolo_detections',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f"Received {len(msg.detections)} detections:")
        
        for det in msg.detections:
            self.get_logger().info(
                f"Class: {det.class_name}, "
                f"ID: {det.class_id}, "
                f"Conf: {det.confidence:.2f}, "
                f"Box: ({det.x1:.1f}, {det.y1:.1f}, {det.x2:.1f}, {det.y2:.1f})"
            )

def main(args=None):
    rclpy.init(args=args)
    node = yolo_sub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
