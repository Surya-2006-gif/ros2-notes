import rclpy
from rclpy.node import Node
from my_custom_interface.msg import TargetCoordinates
import numpy as np



class framepublisher(Node):

    def __init__(self):
        super().__init__('framepublisher')
        self.publisher = self.create_publisher(TargetCoordinates,'transform',10)
        self.timer = self.create_timer(3,self.timer_callback)



    def timer_callback(self):
        msg=TargetCoordinates()
        msg.translation.x = np.random.random()
        msg.translation.y = np.random.random()
        msg.translation.z = np.random.random()


        msg.orientation.x = np.random.random()
        msg.orientation.y = np.random.random()
        msg.orientation.z = np.random.random()


        self.publisher.publish(msg)
        self.get_logger().info(f'published msg')






def main(args=None):
    rclpy.init(args=args)
    node = framepublisher()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()    


main()