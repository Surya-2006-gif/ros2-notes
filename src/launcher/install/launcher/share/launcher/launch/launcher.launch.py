from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld=LaunchDescription()

    talker=Node(
        package=week1,
        executable= publisher

    )

    listener_=Node(
        package=week1,
        executable=listener
    )


    return ld([tallker,listener])