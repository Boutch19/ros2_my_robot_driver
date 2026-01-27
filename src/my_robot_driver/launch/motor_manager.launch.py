import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Récupération du chemin vers le fichier de config installé
    config = os.path.join(
        get_package_share_directory('my_robot_driver'),
        'config',
        'motors.yaml'
    )

    return LaunchDescription([
        Node(
            package='my_robot_driver',
            executable='motor_manager',
            name='motor_manager_node',
            output='screen',
            emulate_tty=True,  # Conserve les couleurs des logs dans la console
            parameters=[config]
        )
    ])