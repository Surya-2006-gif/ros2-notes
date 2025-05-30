import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge




class Contour_Subscriber(Node):
    def __init__(self):
        super().__init__('contour_subscriber')
        self.subscriber = self.create_subscription(Image, 'image', self.listener_callback, 10)
        self.bridge = CvBridge()
        # self.window_name = 'Image'
        # cv2.namedWindow(self.window_name)


    def listener_callback(self,msg):
      frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
      gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      contours, hierarchy = cv2.findContours(gray_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

      cv2.imshow('image', frame)
      key = cv2.waitKey(1) & 0xFF
      if key == 27 or key == ord('q'):  # ESC or 'q' to quit
        print("Shutting down...")
        cv2.destroyAllWindows()
        self.destroy_node()
        rclpy.shutdown()




        cv2.imshow('image',frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):  # ESC or 'q' key to quit
            print("Shutting down...")
            cv2.destroyAllWindows()
            self.destroy_node()
            rclpy.shutdown()
       

def main(args=None):
    rclpy.init(args=args)

    node=Contour_Subscriber()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()



if __name__ =='__main__':
    main()