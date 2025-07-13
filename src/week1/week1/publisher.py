import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy, QoSProfile

class Mynode(Node):
    def __init__(self):
        super().__init__('publisher_node')

       

        self.qos = QoSProfile(
            history=QoSHistoryPolicy.KEEP_ALL,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
            reliability=QoSReliabilityPolicy.RELIABLE,
            liveliness=QoSLivelinessPolicy.AUTOMATIC,
        
        )

        self.publisher_ = self.create_publisher(Float32, 'chatter', self.qos)

        self.declare_parameter('data', 12.4)
        data = self.get_parameter('data').value

        msg = Float32()
        msg.data = data
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
