import rclpy
from rclpy.node import Node
import numpy as np
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class HoughLinesEllipseCircleNode(Node):

    def __init__(self):
        super().__init__('hough_lines_ellipse_circle')
        self.bridge = CvBridge()

        self.subscriber = self.create_subscription(Image, '/my_camera/image_raw', self.callback, 10)

        # Create trackbars
        cv2.namedWindow('trackbar')
        cv2.createTrackbar('th1', 'trackbar', 50, 255, self.nothing)
        cv2.createTrackbar('th2', 'trackbar', 150, 255, self.nothing)
        cv2.createTrackbar('thresh', 'trackbar', 50, 300, self.nothing)
        cv2.createTrackbar('minLineLength', 'trackbar', 0, 300, self.nothing)
        cv2.createTrackbar('maxLineGap', 'trackbar', 0, 300, self.nothing)

    def callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array([14, 119, 19])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(image_hsv, lower, upper)

        th1 = cv2.getTrackbarPos('th1', 'trackbar')
        th2 = cv2.getTrackbarPos('th2', 'trackbar')
        canny = cv2.Canny(mask, th1, th2)

        thresh = cv2.getTrackbarPos('thresh', 'trackbar')
        minLineLength = cv2.getTrackbarPos('minLineLength', 'trackbar')
        maxLineGap = cv2.getTrackbarPos('maxLineGap', 'trackbar')

        lines = cv2.HoughLinesP(canny, 1, np.pi / 180, thresh,
                                minLineLength=minLineLength, maxLineGap=maxLineGap)

        list_line = []
        ROI = None

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if len(list_line) == 0 and y1 > y2:
                    list_line.append((x2, y2))
                elif len(list_line) == 0 and y2 > y1:
                    list_line.append((x1, y1))
                elif y1 > y2 and list_line[-1][0] > x1:
                    list_line.append((x2, y2))
                elif y2 > y1 and list_line[-1][0] > x2:
                    list_line.append((x1, y1))
                elif y1 > y2 and list_line[-1][0] < x1:
                    list_line.insert(0, (x2, y2))
                else:
                    list_line.insert(0, (x1, y1))

                cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

            self.get_logger().info(f'{len(lines)} line(s) detected')

            # Check for box
            if len(lines) == 4:
                self.get_logger().info('Box')

            # Check for cylinder
            elif len(lines) == 2 and len(list_line) == 2:
                y1 = list_line[0][-1]
                y2 = list_line[-1][-1]
                x1 = list_line[0][0]
                x2 = list_line[-1][0]
                ROI = mask[y1 - 20:y2 + 20, x2 - 10:x1 + 10]

                # Polynomial fit on ROI
                if ROI is not None and ROI.size != 0:
                    contours, _ = cv2.findContours(ROI, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                    if contours:
                        contour = max(contours, key=cv2.contourArea)
                        pts = contour.squeeze()

                        if len(pts.shape) == 2 and pts.shape[0] >= 3:
                            x = pts[:, 0]
                            y = pts[:, 1]

                            coeffs = np.polyfit(x, y, deg=3)
                            poly = np.poly1d(coeffs)

                            # Derivative w.r.t x
                            dy_dx = np.polyder(poly)
                            y_derivative = dy_dx(x)

                            if np.any(y_derivative > 0) and np.any(y_derivative < 0):
                                self.get_logger().info('Cylinder')

                            # Visualisation
                            x_fit = np.linspace(min(x), max(x), 500).astype(int)
                            y_fit = poly(x_fit).astype(int)
                            roi_color = cv2.cvtColor(ROI, cv2.COLOR_GRAY2BGR)
                            for xi, yi in zip(x_fit, y_fit):
                                if 0 <= xi < roi_color.shape[1] and 0 <= yi < roi_color.shape[0]:
                                    roi_color[yi, xi] = [0, 0, 255]  # Red curve

                            cv2.imshow('ROI with Polynomial Fit', roi_color)

        else:
            # If no lines detected, check for circle
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (9, 9), 2)
            circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=30,
                                       param1=50, param2=30, minRadius=10, maxRadius=200)
            if circles is not None:
                self.get_logger().info('Circle')
            else:
                self.get_logger().info('No lines or circles detected')

        if len(list_line) == 2:
            cv2.rectangle(image, (x1, y1 - 20), (x2, y2 + 10), (0, 0, 255), 2)

        cv2.imshow('Canny', canny)
        cv2.imshow('Hough Lines + Ellipse or Circles', image)
        cv2.imshow('Mask', mask)

        if cv2.waitKey(1) == 27:  # ESC to exit
            cv2.destroyAllWindows()
            self.destroy_node()
            rclpy.shutdown()

    def nothing(self, x):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = HoughLinesEllipseCircleNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
