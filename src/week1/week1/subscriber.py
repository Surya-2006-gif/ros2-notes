import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy, QoSProfile


class Subscriber(Node):

    def __init__(self):
        super().__init__('subscriber_node')

      

        self.qos = QoSProfile(
            history=QoSHistoryPolicy.KEEP_ALL,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
            reliability=QoSReliabilityPolicy.RELIABLE,
            liveliness=QoSLivelinessPolicy.AUTOMATIC,
         
        )

        self.subscriber = self.create_subscription(
            Float32,
            'chatter',
            self.listener_callback,
            self.qos  
        )

        self.timer = self.create_timer(0.5, self.check_for_publisher)
        self.msg_received = False

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard {msg.data} and the square of it is {msg.data**2}')
        self.msg_received = True

    def check_for_publisher(self):
        if not self.msg_received:
            self.get_logger().warn('No messages received yet. Please publish a message.')
        else:
            self.get_logger().info('Message received, shutting down.')
            self.timer.cancel()
            self.destroy_node()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    
if __name__ == '__main__':
    main()
