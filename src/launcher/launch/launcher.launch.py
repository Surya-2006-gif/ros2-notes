from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    talker = Node(
        package='week1',
        executable='publisher',
        name='talker_node',
        parameters=[{'data': 42.0}], 
        output='screen'
    )

    listener = Node(
        package='week1',
        executable='listener',
        name='listener_node',
        output='screen'
    )

    return LaunchDescription([
        talker,
        listener
    ])
