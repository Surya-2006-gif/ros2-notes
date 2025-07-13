import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):  # Use PascalCase for class names (PEP8)
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.subscription_callback,
            10  # This is the QoS depth (required)
        )

    def subscription_callback(self, msg):
        self.get_logger().info(f"Received msg: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
