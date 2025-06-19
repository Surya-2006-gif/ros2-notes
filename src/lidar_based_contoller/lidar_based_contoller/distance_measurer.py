import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class StopperNode(Node):
    def __init__(self):
        super().__init__('stopper_node')

        self.subscriber = self.create_subscription(
            LaserScan, '/scan', self.listener_callback, 10)
        self.publisher = self.create_publisher(
            Twist, '/cmd_vel', 10)

        self.stop_distance = 0.5  # meters
        self.tilted_angle = 0.2   # radians
        self.tilted_stop_distance = self.stop_distance / np.cos(self.tilted_angle)

        self.allow = True

    def listener_callback(self, msg):
        if not self.allow:
            return

        if all(np.isinf(r) for r in msg.ranges):
            return

        for dist in msg.ranges:
            if dist <= self.tilted_stop_distance:
                stop_msg = Twist()
                stop_msg.linear.x = 0.0
                stop_msg.angular.z = 0.0
                self.publisher.publish(stop_msg)
                self.get_logger().info("Obstacle detected. Stopping robot.")
                self.allow = False
                self.destroy_node()
                rclpy.shutdown()
                break


def main(args=None):
    rclpy.init(args=args)
    node_ = StopperNode()
    rclpy.spin(node_)


if __name__ == '__main__':
    main()
