import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

class Maze(Node):
    def __init__(self):
        super().__init__('maze_solver')

        self.left_most = 0
        self.right_most = 719
        self.front_left_boundary = 180
        self.front_right_boundary = 540

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscriber = self.create_subscription(LaserScan, '/scan', self.subscriber_callback, 10)

        self.front_mean_threshold = 0.5
        self.imbalance_threshold = 3.15

        self.angular_speed = 1.0  # rad/s
        self.turning = False

        # Timer-related attributes
        self.turn_timer = None
        self.turn_count = 0
        self.turn_max_steps = 0
        self.turn_direction = None

    def safe_mean(self, ranges):
        valid = [r for r in ranges if not math.isinf(r) and not math.isnan(r)]
        return sum(valid) / len(valid) if valid else float('inf')

    def turn_90_degrees(self, direction):
        self.turning = True
        self.turn_direction = direction
        self.turn_count = 0
        self.turn_max_steps = 15  # 90° at 1 rad/s, 10 Hz = 1.57 s ≈ 15 steps
        self.get_logger().info(f'Action: TURN {direction} — Turning 90 degrees using timer')

        # Create timer that triggers every 0.1 seconds
        self.turn_timer = self.create_timer(0.1, self.turn_timer_callback)

    def turn_timer_callback(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = self.angular_speed if self.turn_direction == 'LEFT' else -self.angular_speed

        if self.turn_count < self.turn_max_steps:
            self.publisher.publish(twist)
            self.turn_count += 1
        else:
            # Stop turning
            twist.angular.z = 0.0
            self.publisher.publish(twist)
            self.turn_timer.cancel()
            self.turn_timer = None
            self.turning = False
            self.get_logger().info(f'Finished turning {self.turn_direction}')

    def subscriber_callback(self, msg):
        if self.turning:
            return  # Ignore scans during turning

        ranges = msg.ranges
        twist = Twist()

        # Region indexing
        right_region = ranges[self.left_most : self.front_left_boundary]         # 0 to 179
        front_region = ranges[self.front_left_boundary : self.front_right_boundary]  # 180 to 539
        left_region = ranges[self.front_right_boundary : self.right_most + 1]    # 540 to 719

        # Compute mean distances
        left_mean = self.safe_mean(left_region)
        front_mean = self.safe_mean(front_region)
        right_mean = self.safe_mean(right_region)

        imbalance = left_mean - right_mean

        self.get_logger().info(
            f'Left Mean: {left_mean:.2f} | Right Mean: {right_mean:.2f} | '
            f'Imbalance: {imbalance:.2f} | Front Mean: {front_mean:.2f}'
        )

        # Case 1: Stop if front is blocked
        if abs(imbalance) < self.imbalance_threshold and front_mean <= self.front_mean_threshold:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.get_logger().info('Action: STOP — Front blocked and balanced')
            self.publisher.publish(twist)

        # Case 2: Move forward
        elif abs(imbalance) < self.imbalance_threshold and front_mean > self.front_mean_threshold:
            twist.linear.x = 0.7
            twist.angular.z = 0.0
            self.get_logger().info('Action: MOVE FORWARD')
            self.publisher.publish(twist)

        # Case 3: Imbalance detected — turn 90 degrees
        else:
            direction = 'LEFT' if imbalance > 0 else 'RIGHT'
            self.turn_90_degrees(direction)

def main(args=None):
    rclpy.init(args=args)
    node = Maze()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
