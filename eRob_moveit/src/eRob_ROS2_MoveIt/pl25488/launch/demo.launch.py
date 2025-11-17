from moveit_configs_utils import MoveItConfigsBuilder
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Build MoveIt configuration
    moveit_config = MoveItConfigsBuilder("eRobo3", package_name="pl25488").to_moveit_configs()

    # Get package path
    package_path = get_package_share_directory("pl25488")

    # Move Group parameters with planning scene publishing enabled
    # CRITICAL: Use flat parameter structure, not nested dicts
    move_group_params = {
        # Planning scene monitor parameters
        'planning_scene_monitor.name': 'planning_scene_monitor',
        'planning_scene_monitor.robot_description': 'robot_description',
        'planning_scene_monitor.joint_state_topic': '/joint_states',
        'planning_scene_monitor.attached_collision_object_topic': '/attached_collision_object',
        'planning_scene_monitor.publish_planning_scene': True,
        'planning_scene_monitor.publish_geometry_updates': True,
        'planning_scene_monitor.publish_state_updates': True,
        'planning_scene_monitor.publish_transforms_updates': True,
        'planning_scene_monitor.publish_robot_description': True,
        'planning_scene_monitor.publish_robot_description_semantic': True,
        'planning_scene_monitor.publish_planning_scene_hz': 10.0,

        # Trajectory execution parameters
        'trajectory_execution.allowed_execution_duration_scaling': 1.5,
        'trajectory_execution.allowed_goal_duration_margin': 0.5,
        'trajectory_execution.allowed_start_tolerance': 0.1,  # Increased from 0.05 to prevent state deviation errors
    }

    # Static TF for world -> base_link
    static_tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="static_transform_publisher",
        output="log",
        arguments=["--x", "0.0", "--y", "0.0", "--z", "0.0",
                   "--roll", "0.0", "--pitch", "0.0", "--yaw", "0.0",
                   "--frame-id", "world", "--child-frame-id", "base_link"],
    )

    # Robot State Publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[moveit_config.robot_description],
    )

    # RViz
    rviz_config = os.path.join(package_path, "config", "moveit.rviz")
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config],
        parameters=[
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
        ],
    )

    # Move Group with planning scene publishing
    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[
            moveit_config.to_dict(),
            move_group_params,  # Add our custom parameters
        ],
    )

    # ros2_control using FakeSystem as hardware
    ros2_controllers_path = os.path.join(package_path, "config", "ros2_controllers.yaml")
    ros2_control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[moveit_config.robot_description, ros2_controllers_path],
        output="log",  # Changed from "screen" to reduce state spam
    )

    # Load controllers
    load_joint_state_broadcaster = ExecuteProcess(
        cmd=["ros2", "run", "controller_manager", "spawner", "joint_state_broadcaster"],
        output="log",
    )

    load_manipulator_controller = ExecuteProcess(
        cmd=["ros2", "run", "controller_manager", "spawner", "manipulator_controller"],
        output="log",
    )

    # GUI Bridge with parameters
    gui_bridge_params_path = os.path.join(package_path, "config", "gui_bridge_params.yaml")
    gui_bridge_node = Node(
        package="pl25488",
        executable="gui_bridge.py",
        output="screen",
        parameters=[gui_bridge_params_path] if os.path.exists(gui_bridge_params_path) else []
    )

    # Cartesian GUI
    cartesian_gui = Node(
        package="pl25488",
        executable="cartesian_gui.py",
        output="screen"
    )

    return LaunchDescription([
        static_tf,
        robot_state_publisher,
        ros2_control_node,
        move_group_node,  # Move Group with planning scene publishing enabled
        rviz_node,
        load_joint_state_broadcaster,
        load_manipulator_controller,
        gui_bridge_node,
        cartesian_gui,
    ])
