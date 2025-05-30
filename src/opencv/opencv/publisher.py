import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSLivelinessPolicy, QoSReliabilityPolicy, QoSProfile

url = "http://surya:Surya@2006@192.168.146.42:8080/video"

class Publisher(Node):
    def __init__(self):
        qos = QoSProfile(
            history=QoSHistoryPolicy.KEEP_ALL,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
            liveliness=QoSLivelinessPolicy.AUTOMATIC
        )
        super().__init__('publisher')
        self.cap = cv2.VideoCapture(url)
        self.bridge = CvBridge()
        self.publisher = self.create_publisher(Image, 'vision', qos_profile=qos)
        self.timer = self.create_timer(0.033, self.timer_callback)  # ~30 FPS

    def timer_callback(self):
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warn('Error in grabbing frame')
        else:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher.publish(msg)
            self.get_logger().info('Published image frame')  


def main(args=None):
    rclpy.init(args=args)
    node = Publisher()           # Create an instance of the Publisher
    rclpy.spin(node)             # Spin the node to keep it alive and processing callbacks
    node.destroy_node()          # Clean up
    rclpy.shutdown()


if __name__ == '__main__':
    main()
