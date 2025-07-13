import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from message_filters import Subscriber, ApproximateTimeSynchronizer

class DepthNode(Node):
    def __init__(self):
        super().__init__('depth_node')
        self.bridge = CvBridge()

        self.depth_sub = Subscriber(
            self,
            Image,
            '/my_camera/depth/image_raw',
        )
        self.image_sub = Subscriber(
            self,
            Image,
            '/my_camera/image_raw',
        )

        self.ts = ApproximateTimeSynchronizer([self.depth_sub, self.image_sub], 10, 0.05)
        self.ts.registerCallback(self.subscriber_callback)

    def subscriber_callback(self, depth_msg, image_msg):
        # Convert to OpenCV format
        depth_raw = self.bridge.imgmsg_to_cv2(depth_msg, desired_encoding='passthrough')
        image_raw = self.bridge.imgmsg_to_cv2(image_msg, desired_encoding='bgr8')

        # Ensure float32 type
        depth_float = depth_raw.astype(np.float32)

        # Normalize depth to [0,1]
        depth_norm = cv2.normalize(depth_float, None, 0.0, 1.0, cv2.NORM_MINMAX)

        # Convert to [0,255] uint8 for visualization
        depth_display = np.uint8(depth_norm * 255)

        # Image segmentation
        image_hsv = cv2.cvtColor(image_raw, cv2.COLOR_BGR2HSV)
        lower = np.array([14, 119, 19])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(image_hsv, lower, upper)

        # Apply mask to depth image
        depth_mask = cv2.bitwise_and(depth_display, depth_display, mask=mask)

        # Contour detection and shape approximation
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            contour = max(contours, key=cv2.contourArea)
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            cv2.drawContours(image_raw, [approx], -1, (0, 255, 0), 2)

            # Create a mask for the detected contour only
            contour_mask = np.zeros_like(depth_mask)
            cv2.drawContours(contour_mask, [contour], -1, 255, thickness=cv2.FILLED)

            # Extract ROI from depth_mask using contour mask
            depth_mask_float = depth_mask.astype(np.float32)
            depth_box_only = np.where(contour_mask > 0, depth_mask_float, np.nan)

            # Calculate gradient along columns within the box region
            gradient_cols = np.diff(depth_box_only, axis=1)

            # For each row, check if gradient has increase then decrease OR decrease then increase
            increase_decrease_detected = False
            for row in gradient_cols:
                row_no_nan = row[~np.isnan(row)]
                if row_no_nan.size >= 2:
                    signs = np.sign(row_no_nan)
                    # Check for decrease (negative) then increase (positive) OR vice versa
                    for i in range(len(signs)-1):
                        if (signs[i] < 0 and signs[i+1] > 0) or (signs[i] > 0 and signs[i+1] < 0):
                            increase_decrease_detected = True
                            break
                if increase_decrease_detected:
                    break

            if len(approx) == 4:
                self.get_logger().info("It is a box.")
            elif len(approx) == 6 and increase_decrease_detected:
                self.get_logger().info("It is a box with depth gradient pattern (increase-decrease or decrease-increase).")

        # Show images
        cv2.imshow('RGB Image', image_raw)
        cv2.imshow('Depth Image', depth_display)
        cv2.imshow('Mask', mask)
        cv2.imshow('Depth Mask', depth_mask)

        if cv2.waitKey(1) == 27:  # ESC key
            cv2.destroyAllWindows()
            self.destroy_node()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = DepthNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
