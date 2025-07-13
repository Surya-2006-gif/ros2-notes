import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from geometry_msgs.msg import Twist
from action_interface.action import Trial  # Your custom action
import time


class RotationServer(Node):
    def __init__(self):
        super().__init__('rotation_server')

        self._action_server = ActionServer(
            self,
            Trial,
            'rotation',
            execute_callback=self.execute_callback,  # FIXED typo in function name
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
            callback_group=ReentrantCallbackGroup()
        )

        self._publisher = self.create_publisher(Twist, 'cmd_vel', 10)  # FIXED: match name to usage

    def goal_callback(self, goal_request):
        self.get_logger().info(f'Received goal request: angle={goal_request.theta}')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):  # FIXED typo: was "execute_callbaxck"
        feedback_msg = Trial.Feedback()
        feedback_msg.current_angle = 0.0
        goal = goal_handle.request.theta  # FIXED: should be "theta" if that's the goal field

        twist = Twist()

        while feedback_msg.current_angle < goal:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return Trial.Result(success=False)

            twist.angular.z = 0.5
            self._publisher.publish(twist)

            feedback_msg.current_angle += 0.5
            goal_handle.publish_feedback(feedback_msg)

            time.sleep(1)

        twist.angular.z = 0.0
        self._publisher.publish(twist)

        goal_handle.succeed()
        result = Trial.Result()
        result.success = True  # FIXED: typo "sccess"
        return result


def main(args=None):
    rclpy.init(args=args)
    node = RotationServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
