from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory, get_package_prefix
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os


def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_bot_world = os.path.join(get_package_share_directory('bot_world'))

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        ),
    )

    spawner_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        name="urdf_spawner",
        arguments=['-topic','/robot_description','-entity','bot'],
        output="screen"
    )

    return LaunchDescription([
         DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(pkg_bot_world, 'world', 'bot_world.world'), ''],
          description='SDF world file'),
          gazebo,
          spawner_node
    ])