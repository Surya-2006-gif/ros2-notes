import rclpy
from rclpy.node import Node
from std_msgs.msg import String



class subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')

        self.subscription = self.create_subscription(
            String, 'chatter', self.chatter_callback, 10)
        self.subscription
        self.timer=self.create_timer(1.0, self.timer_callback)
        self.i=0
        self.heard=False
        self.previous_time=None
        self.curent_time=None


    def chatter_callback(self, msg):
        self.get_logger().info(f'I heard {msg.data}')
        self.heard=True

    def timer_callback(self):
             if self.heard==False and self.previous_time is None:
                  self.previous_time=self.i
                #   self.current_time=self.i

             elif  self.heard==False and self.previous_time is not None:
                  self.current_time=self.i
                  if self.current_time-self.previous_time>3:
                       self.get_logger().info(f'No heartbeat received after {self.current_time-self.previous_time} seconds')
                  
                  


        
def main(args=None):
    rclpy.init(args=args)

    node=subscriber()


    

    rclpy.shutdown()



if __name__ == '__main__':
    main()