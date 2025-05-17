import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.i = 0

    def run(self):
        rate = 2.0  # Hz
        period = 1.0 / rate  # seconds
        while rclpy.ok():
            msg = String()
            msg.data = f"Hello {self.i}"
            self.publisher.publish(msg)
            self.get_logger().info(f"Published: {msg.data}")
            self.i += 1
            time.sleep(period)


def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
