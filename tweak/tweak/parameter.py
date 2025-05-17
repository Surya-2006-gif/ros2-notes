import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter


class ParamExampleNode(Node):
    def __init__(self):
        super().__init__('param_')

        self.declare_parameter('example_param', 10)


       



def main(args=None):
    rclpy.init(args=args)
    node = ParamExampleNode()

    rclpy.spin(node)

    node.destroy_node()


    rclpy.shutdown()


if __name__ == '__main__':
    main()
