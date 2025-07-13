import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from geometry_msgs.msg import Twist
from action_interface.action import Shape
import math


class ShapeServer(Node):
    def __init__(self):
        super().__init__('shape_server')

        self._action_server = ActionServer(
            self,
            Shape,
            'shape',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
            callback_group=ReentrantCallbackGroup()
        )

        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def goal_callback(self, goal_request):
        self.get_logger().info(f'Received goal request: shape = {goal_request.shape}')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):
        sides = goal_handle.request.shape
        self.get_logger().info(f'Executing goal to draw shape with {sides} sides')

        turn_angle = (2 * math.pi) / sides
        steps_per_side = 20
        step_duration = 0.1  # seconds

        twist = Twist()

        for i in range(sides):
            # Move forward
            for _ in range(steps_per_side):
                if goal_handle.is_cancel_requested:
                    goal_handle.canceled()
                    self.get_logger().info('Goal canceled')
                    return Shape.Result(success=False)

                twist.linear.x = 2.0
                twist.angular.z = 0.0
                self.publisher.publish(twist)
                await rclpy.sleep(step_duration)

            # Turn
            for _ in range(10):
                if goal_handle.is_cancel_requested:
                    goal_handle.canceled()
                    self.get_logger().info('Goal canceled')
                    return Shape.Result(success=False)

                twist.linear.x = 0.0
                twist.angular.z = turn_angle / 10.0
                self.publisher.publish(twist)
                await rclpy.sleep(step_duration)

        # Stop turtle after completing the shape
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)

        goal_handle.succeed()
        self.get_logger().info('Shape drawing completed')
        return Shape.Result(success=True)


def main(args=None):
    rclpy.init(args=args)
    node = ShapeServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
