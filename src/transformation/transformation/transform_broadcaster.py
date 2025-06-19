import rclpy
from rclpy.node import Node
from my_custom_interface.msg import TargetCoordinates
from tf2_ros.transform_broadcaster import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from scipy.spatial.transform import Rotation as R  # <-- Use this for Euler to quaternion conversion
import numpy as np


class TransformBroadcasterNode(Node):
    def __init__(self):
        super().__init__('transform_broadcaster')
        self.tf_broadcaster = TransformBroadcaster(self)
        self.subscriber = self.create_subscription(
            TargetCoordinates, 'transform', self.subscriber_callback, 10)

    def subscriber_callback(self, msg):
        # Extract translation
        x = msg.translation.x
        y = msg.translation.y
        z = msg.translation.z

        # Extract Euler angles
        roll = msg.orientation.x
        pitch = msg.orientation.y
        yaw = msg.orientation.z

        # Convert Euler to quaternion
        quat = R.from_euler('xyz', [roll, pitch, yaw]).as_quat()  # [x, y, z, w]

        # Create TransformStamped message
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'world'
        t.child_frame_id = 'target'

        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = z

        t.transform.rotation.x = quat[0]
        t.transform.rotation.y = quat[1]
        t.transform.rotation.z = quat[2]
        t.transform.rotation.w = quat[3]

        # Broadcast transform
        self.tf_broadcaster.sendTransform(t)

        self.get_logger().info('Broadcasted transform.')


def main(args=None):
    rclpy.init(args=args)
    node = TransformBroadcasterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


main()