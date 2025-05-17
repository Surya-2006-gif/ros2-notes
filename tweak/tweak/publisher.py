import rclpy
from rclpy.node import Node
from std_msgs.msg import String



class publisher(Node):
     

     def __init__(self):
          super().__init__('publisher')
          self.publisher_=self.create_publisher(String, 'chatter', 10)
          self.timer_=self.create_timer(1.0, self.timer_callback)
          self.i=1



     def timer_callback(self):
          message=String()
          message.data= f'Heartbeat #{self.i}'
          self.publisher_.publish(message)
          self.get_logger().info(f'Message published: {message.data}''')
          self.i+=1     











def main(args=None):
     rclpy.init(args=args)
     node=publisher()
     rclpy.spin(node)
     node.destroy_node()

     rclpy.shutdown()



if __name__=='__main__':
     main()