from launch import LaunchDescription
from ament_index_python import get_package_share_directory
from launch.substitutions import Command
from launch_ros.actions import Node
import os

def generate_launch_description():

    pkg_path = os.path.join(get_package_share_directory('bot_description'))
    xacro_file = os.path.join(pkg_path,'urdf','bot.urdf.xacro')

    robot_description = Command(['xacro ',xacro_file])

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description":robot_description}]
    )

    rviz_node = Node(
        package= "rviz2",
        executable= "rviz2",
        name= "rviz2",
        output= "screen"
    )

    return LaunchDescription([  
        robot_state_publisher_node,
        rviz_node
    ])