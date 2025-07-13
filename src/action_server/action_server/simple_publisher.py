import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.publisher=self.create_publisher(String,'chatter',10)
        self.timer=self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        msg= String()
        msg.data = 'hello world'
        self.publisher.publish(msg)
        self.get_logger().info("published msg")





def main(args=None):
    rclpy.init(args=args)
    node = publisher()
    rclpy.spin(node)
    node.destroy_node()

    
    rclpy.shutdown()




if __name__ == '__main__':
    main()