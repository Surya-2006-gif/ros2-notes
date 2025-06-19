from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    talker = Node(
        package = 'action_server',
        executable='publisher',
        
    )

    listener =Node(
        package = 'action_server',
        executable = 'subscriber'
    )

    ld = LaunchDescription()
    ld.add_action(talker)
    ld.add_action(listener)

    return ld