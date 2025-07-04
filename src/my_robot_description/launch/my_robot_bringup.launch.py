from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command

def generate_launch_description():
    urdf_file_path = os.path.join(
        get_package_share_directory('my_robot_description'),
        'urdf',
        'my_robot.urdf.xacro'
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro',' ', urdf_file_path])}],
        output='screen'
    )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

   

    ld = LaunchDescription()
    ld.add_action(robot_state_publisher)
    ld.add_action(joint_state_publisher_gui)
    ld.add_action(rviz_node)

    return ld
