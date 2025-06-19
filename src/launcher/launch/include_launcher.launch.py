# from launch import LaunchDescription
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from ament_index_python import get_package_share_directory
# import os


# def generate_launch_description():
#     ld=LaunchDescription()
    
#     other_launch_files = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(get_package_share_directory('launcher'),
#                          "launch/launcher.launch.py")
#         )
#     )
#     ld.add_action(other_launch_files)
#     return ld

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    ld = LaunchDescription()

    other_launch_files = IncludeLaunchDescription(
        PathJoinSubstitution(
            FindPackageShare(
                'launcher'
            ),
        'launch/launcher.launch.py'
        )
    )

    return ld