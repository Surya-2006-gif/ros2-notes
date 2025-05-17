import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from std_msgs.msg import Int32MultiArray
from rcl_interfaces.msg import SetParametersResult



class GamePublisher(Node):

    def __init__(self):
        super().__init__('game_publisher')

        # Declare speed parameter
        self.declare_parameter('speed', 1)

        # Random starting lane
        self.current_lane = np.random.randint(1, 3)

        # Publisher
        self.publisher = self.create_publisher(Int32MultiArray, "game", 10)

        # Parameter callback
        self.add_on_set_parameters_callback(self.parameter_update_callback)

        # Create initial timer
        self.set_timer_with_speed()

    def set_timer_with_speed(self):
        speed = self.get_parameter('speed').value
        if speed <= 0:
            self.get_logger().warn("Speed must be > 0. Resetting to 1.")
            speed = 1
        period = 1.0 / speed  # Convert speed to timer period

        # Cancel existing timer if it exists
        if hasattr(self, 'timer'):
            self.timer.cancel()

        self.timer = self.create_timer(period, self.timer_callback)
        self.get_logger().info(f"Timer set with period {period:.3f} seconds (speed={speed})")

    def parameter_update_callback(self, params):
        for param in params:
            if param.name == 'speed' and param.type_ == Parameter.Type.INTEGER:
                self.get_logger().info(f"Speed updated to {param.value}. Resetting timer.")
                self.set_timer_with_speed()
                return SetParametersResult(successful=True)
        return SetParametersResult(successful=False)

    def timer_callback(self):
        # Randomly generate lane map (obstacle presence)
        num = np.random.randint(0, 2, 2)
        self.lane1_map = int(num[0])
        self.lane2_map = int(num[1])

        # Decide current lane or stop
        if self.lane1_map == 0 and self.lane2_map:
            self.current_lane = 1
        elif self.lane1_map and self.lane2_map == 0:
            self.current_lane = 2
        elif self.lane1_map and self.lane2_map:
            self.current_lane = np.random.randint(1, 3)
        else:
            self.get_logger().info("Obstacles are present in both lanes. Stopping the vehicle and shutting down node.")
            self.destroy_node()
            rclpy.shutdown()
            return

        # Publish current state
        msg = Int32MultiArray()
        msg.data = [
            self.lane1_map,
            self.lane2_map,
            self.current_lane,
            int(self.get_parameter('speed').value)
        ]
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = GamePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
