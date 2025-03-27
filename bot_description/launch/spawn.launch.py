from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from ament_index_python import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py")),
             )

    spawner_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        name="urdf_spawner",
        arguments=['-topic','/robot_description','-entity','bot'],
        output="screen"
    )

    return LaunchDescription([
        gazebo,
        spawner_node,
        DeclareLaunchArgument(
            'use_sim_time',
            default_value= 'true',
            description= 'Use Sim time'
        )
    ])