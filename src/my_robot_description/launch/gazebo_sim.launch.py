from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
import os 
from ament_index_python import get_package_share_directory
import xacro

def generate_launch_description():

    # Get package paths
    pkg_path = get_package_share_directory('my_robot_description')
    urdf_file_path = os.path.join(pkg_path, 'urdf', 'my_robot.urdf.xacro')
    world_file = os.path.join(pkg_path, 'worlds', 'my_world.world')

    urdf_file = xacro.process_file(urdf_file_path).toxml()

    # Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
             'robot_description': urdf_file,
            'use_sim_time': True
        }],
        output='screen'
    )


    # Launch Gazebo with your custom world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ]),
        launch_arguments={'world': world_file}.items()
    )


    # Spawn robot entity into Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'my_robot',
            # '-file' , '/home/surya/Documents/my_robot.urdf'

        ],
        output='screen'
    )
    stopper_node = Node(
        package = 'lidar_based_contoller',
        executable = 'lidar_stopper',
        output = 'screen'        )

    return LaunchDescription([
        robot_state_publisher,
        gazebo,
        spawn_entity,
        stopper_node
    ])
