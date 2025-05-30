import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from action_interface.action import Trial  # custom action

class RotationClient(Node):
    def __init__(self):
        super().__init__('rotation_client')
        self._action_client = ActionClient(self, Trial, 'rotation')

    def send_request(self, theta):
        goal_msg = Trial.Goal()
        goal_msg.theta = theta

        self.get_logger().info('Waiting for action server...')
        self._action_client.wait_for_server()

        self.get_logger().info('Action server available. Sending goal...')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback,
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected by server.')
            rclpy.shutdown()
            return

        self.get_logger().info('Goal accepted, waiting for result...')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Feedback: current_angle = {feedback_msg.feedback.current_angle:.2f}')

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result received: success = {result.success}')
        self.get_logger().info('Action completed. Shutting down.')
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = RotationClient()
    theta = 1.57  # ~90 degrees in radians
    node.send_request(theta)
    rclpy.spin(node)  # SPIN the node, not just spin()
    node.destroy_node()


if __name__ == '__main__':
    main()
