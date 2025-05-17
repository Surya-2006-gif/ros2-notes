from my_custom_interface.srv import Demo
from geometry_msgs.msg import Point
import rclpy
from rclpy.node import Node


class service_server(Node):
    def __init__(self):
        super().__init__('server')
        self.server=self.create_service(Demo,'demo',self.server_callback)



    def server_callback(self,request,response):
        response.sum=request.a + request.b + request.c
        self.get_logger().info(f'recived requests a:{request.a} b:{request.b} c:{request.c}')
        return response









def main(args=None):
    rclpy.init(args=args)
    node=service_server()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ =='__main__':
    main()

