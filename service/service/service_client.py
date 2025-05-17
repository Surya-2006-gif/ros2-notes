import sys
from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node




class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')

        # Creating the client
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        
        # Wait for the service to be available
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

        # Creating the request
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    client_node = ServiceClient()

    try:
        # Taking user input
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
    except ValueError:
        print("Error: Please enter valid integers.")
        sys.exit(1)

    # Sending the request asynchronously
    future = client_node.send_request(a, b)

    # Waiting for the result
    while not future.done():
        rclpy.spin_once(client_node)

    # Checking the result
    if future.result() is not None:
        client_node.get_logger().info(f'Result: {future.result().sum}')
    else:
        client_node.get_logger().error('Failed to get a valid response.')

    # Cleanup
    client_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
