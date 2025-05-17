import rclpy
from rclpy.node import Node


from example_interfaces.srv import AddTwoInts

class ServiceServer(rclpy.node.Node):

    def __init__(self):
        super().__init__('add_two_ints_server')
        # Creating the service
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        # Processing the request
        response.sum = request.a + request.b
        self.get_logger().info(f'Received request: x={request.a}, y={request.b}')
        return response

def main(args=None):
    rclpy.init(args=args)

    service_node = ServiceServer()

    # Spinning the node to keep it alive and listen for requests
    rclpy.spin(service_node)

    # Cleanup
    service_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
