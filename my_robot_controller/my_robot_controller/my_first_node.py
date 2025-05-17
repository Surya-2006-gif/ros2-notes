#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
  

  def __init__(self):
    super().__init__("first_node")


def main(args=None):
   rclpy.init(args=args)

   Node = MyNode()x
 

   rclpy.shutdown()

    # TODO: Add your ROS 2 code here

   rclpy.shutdown()



if __name__ == '__main__':
   main()