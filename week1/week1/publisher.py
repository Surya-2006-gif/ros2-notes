import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Mynode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(Float32, 'chatter', 10)

        # try:
        #     data = float(input("Enter a number to publish: "))
        # except ValueError:
        #     print("Invalid input. Please enter a float value.")
        #     return  
        '''launch files doesnt support interactive input '''

        self.declare_parameter('data',12.4)
        data=self.get_parameter('data').value

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
