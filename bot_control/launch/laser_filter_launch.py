from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='bot_control',
            executable='reading_laser',
            name='reading_laser',
            output='screen'
        )
    ])