import rclpy
from rclpy.node import Node
import numpy as np
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import LaserScan, Image
from message_filters import Subscriber, ApproximateTimeSynchronizer

class corner_node(Node):
    def __init__(self):
        super().__init__('corner_node')

        self.bridge = CvBridge()

        self.image_sub = Subscriber(self, Image, '/my_camera/image_raw')
        self.lidar_sub = Subscriber(self, LaserScan, '/scan')

        self.ts = ApproximateTimeSynchronizer([self.image_sub, self.lidar_sub], queue_size=10, slop=0.05)
        self.ts.registerCallback(self.synced_callback)

        cv2.namedWindow('window', cv2.WINDOW_NORMAL)
        cv2.createTrackbar('thresh', 'window', 0, 255, self.nothing)

    def nothing(self, x):
        pass

    def synced_callback(self, image_msg, lidar_msg):
        frame = self.bridge.imgmsg_to_cv2(image_msg, 'bgr8')

        thresh = cv2.getTrackbarPos('thresh', 'window')

        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower = np.array([14, 119, 19])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(hsv_image, lower, upper)

        result = cv2.bitwise_and(frame, frame, mask=mask)

        mask_float = np.float32(mask)

        corners = cv2.goodFeaturesToTrack(mask_float, 6, 0.04, 0.4)

        if corners is not None:
            for corner in corners:
                x, y = corner.ravel()
                cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

            self.get_logger().info('no of corners detected: ' + str(len(corners)))
        else:
            self.get_logger().info('no corners detected.')

        ranges = np.array(lidar_msg.ranges)

        no_inf_indices = np.where(~np.isinf(ranges))

        no_inf_ranges = ranges[no_inf_indices]

        angle_min = lidar_msg.angle_min
        angle_increment = lidar_msg.angle_increment
        angles = angle_min + no_inf_indices[0] * angle_increment

        vertical_distances = no_inf_ranges * np.cos(angles)

        threshold = 0.3

        if len(corners) == 4:
            self.get_logger().info('It is box')

        elif  len(corners) == 6 and np.max(vertical_distances) - np.min(vertical_distances) > threshold :
                self.get_logger().info(f'It is a box')


        else :
                self.get_logger().info(f"number of corners {len(corners)} and diff = {np.max(vertical_distances) - np.min(vertical_distances) }")

      

        cv2.imshow('original', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)

        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            self.destroy_node()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = corner_node()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
