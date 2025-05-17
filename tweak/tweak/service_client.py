from my_custom_interface.srv import Demo
from geometry_msgs.msg import Point
import rclpy
from rclpy.node import Node

class service_client(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(Demo, 'demo')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, waiting again...")
        self.req=Demo.Request()



    def send_request(self,a,b,c):
        self.req.a=a
        self.req.b=b
        self.req.c=c
        return self.client.call_async(self.req)



def main(args=None):
    rclpy.init(args=args)
    node=service_client()
    a,b,c=int(input("Enter three numbers: ")),int(input("Enter another number: ")),int(input("Enter another number: "))
    future = node.send_request(a,b,c)
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        print("Result: ", future.result().result)
    node.destroy_node()
    rclpy.shutdown()



if __name__ =='__main__':
    main()

