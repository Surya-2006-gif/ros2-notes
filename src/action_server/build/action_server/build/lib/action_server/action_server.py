import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from example_interfaces.action import Fibonacci
import time
import action_interface


class FibonacciActionServer(Node):
    def __init__(self):
        super().__init__('fibonacci_action_server')

        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )

    def goal_callback(self, goal_request):
        self.get_logger().info(f'Received goal request: order={goal_request.order}')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]

        for i in range(2, goal_handle.request.order):
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return Fibonacci.Result()

            next_number = feedback_msg.partial_sequence[i - 1] + feedback_msg.partial_sequence[i - 2]
            feedback_msg.partial_sequence.append(next_number)

            self.get_logger().info(f'Publishing feedback: {feedback_msg.partial_sequence}')
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)  # simulate work

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence
        self.get_logger().info(f'Goal succeeded: {result.sequence}')
        return result


def main(args=None):
    rclpy.init(args=args)
    node = FibonacciActionServer()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
