import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportRelative

class SquarePublisher(Node):
    def __init__(self):
        super().__init__('square_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.publish_square_shape)  # 10 Hz

        self.square_length = 20
        self.i = 1
        self.state = 'forward'

        self.client = self.create_client(TeleportRelative, '/turtle1/teleport_relative')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for teleport_relative service...')
        self.req = TeleportRelative.Request()

    def publish_square_shape(self):
        msg = Twist()

        if self.state == 'forward':
            msg.linear.x = 1.0
            self.publisher_.publish(msg)
            if self.i % self.square_length == 0:
                self.state = 'turn'
            self.i += 1

        elif self.state == 'turn':
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)

            self.req.linear = 0.0
            self.req.angular = 1.5708  

            future = self.client.call_async(self.req)
            rclpy.spin_until_future_complete(self, future)

            self.state = 'forward'
            self.i = 1

def main(args=None):
    rclpy.init(args=args)
    node = SquarePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
