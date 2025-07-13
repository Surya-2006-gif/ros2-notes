import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, LaserScan
from cv_bridge import CvBridge
import cv2
import numpy as np
from message_filters import Subscriber, ApproximateTimeSynchronizer

class MultiSensorNode(Node):
    def __init__(self):
        super().__init__('multi_sensor_node')
        self.bridge = CvBridge()

        # Message filter subscribers (instead of rclpy.create_subscription)
        self.image_sub = Subscriber(self, Image, '/my_camera/image_raw')
        self.lidar_sub = Subscriber(self, LaserScan, '/scan')

        # Synchronize both topics (adjust slop as needed)
        self.ts = ApproximateTimeSynchronizer([self.image_sub, self.lidar_sub], queue_size=10, slop=0.05)
        self.ts.registerCallback(self.synced_callback)


    def synced_callback(self, image_msg, lidar_msg):
        # Convert ROS Image to OpenCV format
        image = self.bridge.imgmsg_to_cv2(image_msg, desired_encoding='bgr8')
        image_copy = image.copy()


        # Process the image (e.g. polygon approximation)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array([14, 119, 19])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(hsv_image, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Process LiDAR data



        ranges = np.array(lidar_msg.ranges)

        # Indices where range is not inf
        no_inf_indices = np.where(~np.isinf(ranges))

        # Get valid ranges
        no_inf_ranges = ranges[no_inf_indices]

        # Calculate corresponding angles
        angle_min = lidar_msg.angle_min
        angle_increment = lidar_msg.angle_increment
        angles = angle_min + no_inf_indices[0] * angle_increment

        # Calculate vertical distances
        vertical_distances = no_inf_ranges * np.cos(angles)

        diff_vertical_distances = np.diff(vertical_distances)

  
        has_positive = np.any(diff_vertical_distances > 0)
        has_negative = np.any(diff_vertical_distances < 0)       


        if contours:
            contour = max(contours, key=cv2.contourArea)
            epsilon = 0.001 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            cv2.drawContours(image_copy, [approx], -1, (0,255,0), 2)


            if len(approx) == 4 and not (has_positive and has_negative):
            #  self.get_logger().info(f"It is a box ")
             image = self.draw_rect('Box',contour,image)
             print(f'has_negative; {has_negative} , has_positive: {has_negative}' )

            elif len(approx) == 4 and (has_positive and has_negative):
                self.get_logger().info(f'It is a cylinder')
                image = self.draw_rect('cylinder',contour,image)

            elif  len(approx) == 6 and (has_positive and has_negative):
                self.get_logger().info(f'It is a box')
                image = self.draw_rect('box',contour,image)

            elif len(approx) == 7 or  len(approx) == 8:
                self.get_logger().info(f'It is a cylinder')
                image = self.draw_rect('cylinder',contour,image)                 



            elif len(approx) >= 10 and (has_positive and has_negative) :
                self.get_logger().info(f'It is a sphere')
                image = self.draw_rect('sphere',contour,image)


            else :
                self.get_logger().info(f'number of corners :{len(approx)}')   
                image = self.draw_rect('unknown',contour,image)






        # Display image
        cv2.imshow('Image with Approx Poly', image)
        cv2.imshow('window',image_copy)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            self.destroy_node()
            rclpy.shutdown()
    def draw_rect(self,shape,contour,image):

        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(image,shape,(x,y-3),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
        return image




def main(args=None):
    rclpy.init(args=args)
    node = MultiSensorNode()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
