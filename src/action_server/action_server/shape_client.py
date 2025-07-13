import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from action_interface.action import Shape

class ShapeClient(Node):
    def __init__(self):
        super().__init__('shape_client')
        self._action_client = ActionClient(self, Shape, 'shape')
        self._goal_handle = None

    def send_request(self, goal_value):
        goal_msg = Shape.Goal()
        goal_msg.shape = goal_value

        self.get_logger().info('Waiting for action server...')
        self._action_client.wait_for_server()

        self.get_logger().info('Sending goal...')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected by the server')
            return

        self.get_logger().info('Goal accepted')
        self._goal_handle = goal_handle
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f"Feedback: {feedback_msg.feedback.current_pos}")

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result received: {result}")
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = ShapeClient()
    node.send_request(4)  # You can pass any int
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
