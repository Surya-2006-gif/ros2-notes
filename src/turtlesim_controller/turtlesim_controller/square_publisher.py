import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SquarePublisher(Node):
    def __init__(self):
        super().__init__('square_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.publish_square_shape)  # 10 Hz
        self.state = 'forward'
        self.step_count = 0
        self.steps_per_side = 1  # Tune this for length
        self.steps_per_turn = 1  # Tune this for 90 degrees
        self.side_number = 0
        self.max_sides = 6

    def publish_square_shape(self):
        msg = Twist()

        if self.side_number >= self.max_sides:
            # Stop the turtle
            self.get_logger().info('Square complete')
            self.publisher_.publish(Twist())  # zero velocities
            self.timer_.cancel()
            return

        if self.state == 'forward':
            msg.linear.x = 1.0
            self.step_count += 1
            if self.step_count >= self.steps_per_side:
                self.state = 'turn'
                self.step_count = 0

        elif self.state == 'turn':
            msg.angular.z = 0.1  # approx 90 degrees/sec
            self.step_count += 1
            if self.step_count >= self.steps_per_turn:
                self.state = 'forward'
                self.step_count = 0
                self.side_number += 1

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SquarePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
