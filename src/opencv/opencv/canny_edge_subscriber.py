import cv2
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


class CannyEdgeSubscriber(Node):
    def __init__(self):
        super().__init__('canny_edge_subscriber')
        self.subscriber = self.create_subscription(Image, 'image', self.listener_callback, 10)
        self.bridge = CvBridge()
        self.window_name = 'Image'
        cv2.namedWindow(self.window_name)

        # Initialize trackbars
        cv2.createTrackbar('thresh1', self.window_name, 100, 500, lambda x: None)
        cv2.createTrackbar('thresh2', self.window_name, 200, 500, lambda x: None)
        cv2.createTrackbar('Scale',self.window_name,100,200,lambda x: None)

    def listener_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')  # You can use 'bgr8' or 'rgb8'
        except Exception as e:
            self.get_logger().error(f"Bridge conversion failed: {e}")
            return

        # Get threshold values
        th1 = cv2.getTrackbarPos('thresh1', self.window_name)
        th2 = cv2.getTrackbarPos('thresh2', self.window_name)
        scale= cv2.getTrackbarPos('Scale',self.window_name)

        scale=max(scale,10)

        width=frame.shape[1]
        height=frame.shape[0]

        scaled_width=int(width*scale/100)
        scaled_height=int(height*scale/100)

        frame=cv2.resize(frame,(scaled_width,scaled_height),interpolation=cv2.INTER_LINEAR)

        # Apply Canny edge detection
        edges = cv2.Canny(frame, th1, th2)
        cv2.imshow(self.window_name, edges)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):  # ESC or 'q' key to quit
            print("Shutting down...")
            cv2.destroyAllWindows()
            self.destroy_node()
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = CannyEdgeSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Keyboard Interrupt detected. Shutting down.")
        node.destroy_node()
        cv2.destroyAllWindows()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
