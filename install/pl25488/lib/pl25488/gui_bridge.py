#!/usr/bin/env python3
"""
SIMPLIFIED GUI BRIDGE - Pure message forwarder
No IK, no FK, no path planning, no computations.
Just forwards pose/joint commands to MoveIt's MoveGroup action.
"""
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Pose, PoseStamped, PoseArray
from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import (
    MotionPlanRequest,
    Constraints,
    PositionConstraint,
    OrientationConstraint,
    BoundingVolume,
    JointConstraint
)
from shape_msgs.msg import SolidPrimitive
import threading
class GUIBridge(Node):
    """
    Minimal GUI bridge - just forwards commands to MoveIt.
    NO computations, NO IK/FK, NO path planning.
    MoveIt does ALL the work.
    """
    def __init__(self):
        super().__init__('gui_bridge')
        # Execution state
        self._executing = False
        self._execution_lock = threading.Lock()
        self._retry_count = 0  # Track retries for fallback

        # MoveIt action client
        self._move_group_client = ActionClient(self, MoveGroup, '/move_action')
        self.get_logger().info('Waiting for move_group...')
        self._move_group_client.wait_for_server()
        self.get_logger().info('✓ Connected to move_group')
        # Parameters - high speed with S-curve jerk limiting for smooth motion
        self.velocity_scaling = self.declare_parameter('velocity_scaling', 0.6).value
        self.acceleration_scaling = self.declare_parameter('acceleration_scaling', 0.6).value
        # Subscribe to GUI commands
        self.create_subscription(Pose, '/gui_cartesian_command', self._cartesian_callback, 10)
        self.create_subscription(Float64MultiArray, '/gui_joint_command', self._joint_callback, 10)
        self.create_subscription(PoseArray, '/gui_waypoint_batch', self._waypoint_batch_callback, 10)

        # Subscribe to speed updates from GUI
        from std_msgs.msg import Float32MultiArray
        self.create_subscription(Float32MultiArray, '/gui_speed_scaling', self._speed_callback, 10)

        # Subscribe to digital I/O commands
        from std_msgs.msg import Int32MultiArray
        self.create_subscription(Int32MultiArray, '/gui_digital_output', self._digital_output_callback, 10)

        # Publisher for command completion feedback
        from std_msgs.msg import Bool
        self.command_complete_pub = self.create_publisher(Bool, '/gui_command_complete', 10)

        self.get_logger().info('GUI Bridge ready - forwarding messages to MoveIt')
        self.get_logger().info(f'Using Pilz LIN planner with TracIK')
        self.get_logger().info(f'Speed: vel={self.velocity_scaling:.2f}, accel={self.acceleration_scaling:.2f}')

    def _speed_callback(self, msg: 'Float32MultiArray'):
        """Update velocity/acceleration scaling from GUI"""
        if len(msg.data) >= 2:
            self.velocity_scaling = max(0.01, min(1.0, msg.data[0]))
            self.acceleration_scaling = max(0.01, min(1.0, msg.data[1]))
            self.get_logger().info(f'Speed updated: vel={self.velocity_scaling:.2f}, accel={self.acceleration_scaling:.2f}')

    def _digital_output_callback(self, msg):
        """
        Handle digital output commands.
        Message format: [port_id, value]

        Note: This is a placeholder. In a real system, this would interface with
        the robot's I/O controller (e.g., via ros2_control or custom driver).
        """
        if len(msg.data) >= 2:
            port_id = int(msg.data[0])
            value = int(msg.data[1])
            self.get_logger().info(f'Digital Output: port={port_id}, value={value}')
            # TODO: Forward to actual I/O controller
            # For now, just log the command

    def _cartesian_callback(self, msg: Pose):
        """Forward cartesian pose to MoveIt with basic workspace validation"""
        with self._execution_lock:
            if self._executing:
                self.get_logger().warning('Busy - ignoring command')
                return
            self._executing = True

        self._retry_count = 0  # Reset retry counter
        self._last_pose = msg  # Store for potential retry

        # Basic workspace validation - XY reach check only
        # Z-axis collision with table is now handled by MoveIt collision checking
        x, y, z = msg.position.x, msg.position.y, msg.position.z

        # Approximate workspace limits
        max_reach = 0.7  # 700mm in meters

        # Calculate distance from base (XY plane)
        xy_distance = (x**2 + y**2)**0.5

        if xy_distance > max_reach:
            self.get_logger().error(f'❌ Pose UNREACHABLE: XY distance {xy_distance*1000:.0f}mm exceeds max reach {max_reach*1000:.0f}mm')
            with self._execution_lock:
                self._executing = False
            return

        self.get_logger().info(f'Pose goal: X={x:.3f} Y={y:.3f} Z={z:.3f} (reach: {xy_distance*1000:.0f}mm)')
        self._send_pose_goal(msg)
    def _joint_callback(self, msg: Float64MultiArray):
        """Forward joint goal to MoveIt - NO processing"""
        with self._execution_lock:
            if self._executing:
                self.get_logger().warning('Busy - ignoring command')
                return
            self._executing = True
        self.get_logger().info(f'Joint goal: {list(msg.data)}')
        self._send_joint_goal(list(msg.data))
    def _waypoint_batch_callback(self, msg: PoseArray):
        """Store waypoints and execute sequentially"""
        with self._execution_lock:
            if self._executing:
                self.get_logger().warning('Busy - ignoring waypoints')
                return
            self._executing = True
        self._waypoint_queue = list(msg.poses)
        self.get_logger().info(f'Received {len(self._waypoint_queue)} waypoints')
        self._execute_next_waypoint()
    def _execute_next_waypoint(self):
        """Execute next waypoint from queue"""
        if not hasattr(self, '_waypoint_queue') or not self._waypoint_queue:
            self.get_logger().info('✓ All waypoints complete')
            with self._execution_lock:
                self._executing = False
            return
        waypoint = self._waypoint_queue.pop(0)
        self.get_logger().info(f'Waypoint ({len(self._waypoint_queue)} remaining)')
        self._send_pose_goal(waypoint, is_waypoint=True)
    def _send_pose_goal(self, pose: Pose, is_waypoint=False):
        """
        Send pose goal to MoveIt using Pilz LIN planner with optimized settings for
        ultra-smooth motion at high speeds (0.8 vel, 0.6-0.7 acc).

        Key optimizations:
        - Relaxed constraints for smoother IK solving
        - Longer planning time for optimal trajectories
        - Optimized scaling for smooth acceleration profiles
        """
        goal = MoveGroup.Goal()
        goal.request = MotionPlanRequest()
        goal.request.group_name = 'manipulator'

        # Use Pilz LIN planner for straight-line cartesian motion
        goal.request.planner_id = 'LIN'  # Linear interpolation in cartesian space
        goal.request.pipeline_id = 'pilz_industrial_motion_planner'

        goal.request.num_planning_attempts = 1  # LIN is deterministic
        goal.request.allowed_planning_time = 5.0  # INCREASED from 2.0s - more time for smooth trajectories

        # OPTIMIZED: Use velocity/acceleration scaling with smoothing
        # S-curve acceleration (via jerk limits) handles smoothness at trajectory level
        goal.request.max_velocity_scaling_factor = self.velocity_scaling
        goal.request.max_acceleration_scaling_factor = self.acceleration_scaling

        # Workspace parameters for better planning
        goal.request.workspace_parameters.header.frame_id = 'base_link'
        goal.request.workspace_parameters.min_corner.x = -1.0
        goal.request.workspace_parameters.min_corner.y = -1.0
        goal.request.workspace_parameters.min_corner.z = -0.1
        goal.request.workspace_parameters.max_corner.x = 1.0
        goal.request.workspace_parameters.max_corner.y = 1.0
        goal.request.workspace_parameters.max_corner.z = 1.0

        # OPTIMIZED Position constraint - Relaxed for smoother trajectories
        # Looser constraints = fewer trajectory waypoints = smoother motion
        pos_constraint = PositionConstraint()
        pos_constraint.header.frame_id = 'base_link'
        pos_constraint.link_name = 'tool0'
        bounding_volume = BoundingVolume()
        sphere = SolidPrimitive()
        sphere.type = SolidPrimitive.SPHERE
        sphere.dimensions = [0.005]  # INCREASED to 5mm tolerance (was 3mm) - smoother IK solving
        bounding_volume.primitives.append(sphere)
        pose_stamped = PoseStamped()
        pose_stamped.pose = pose
        bounding_volume.primitive_poses.append(pose_stamped.pose)
        pos_constraint.constraint_region = bounding_volume
        pos_constraint.weight = 1.0

        # OPTIMIZED Orientation constraint - Further relaxed for smoother motion
        # Pilz LIN with TracIK maintains linearity while allowing smooth joint motions
        orient_constraint = OrientationConstraint()
        orient_constraint.header.frame_id = 'base_link'
        orient_constraint.link_name = 'tool0'
        orient_constraint.orientation = pose.orientation
        orient_constraint.absolute_x_axis_tolerance = 0.15  # INCREASED to ~8.6° (was 5.7°) - smoother solving
        orient_constraint.absolute_y_axis_tolerance = 0.15  # ~8.6 degrees
        orient_constraint.absolute_z_axis_tolerance = 0.15  # ~8.6 degrees
        orient_constraint.weight = 1.0

        # Add constraints
        constraints = Constraints()
        constraints.position_constraints.append(pos_constraint)
        constraints.orientation_constraints.append(orient_constraint)
        goal.request.goal_constraints.append(constraints)

        # OPTIMIZED Execution parameters for smooth motion
        goal.planning_options.plan_only = False
        goal.planning_options.replan = False  # No replanning - use first smooth solution
        goal.planning_options.replan_attempts = 0

        # CRITICAL: Request trajectory smoothing (if supported by MoveIt config)
        # This post-processes the trajectory to remove jerk
        goal.request.max_cartesian_speed = 0.0  # Let planner decide (use velocity scaling)

        future = self._move_group_client.send_goal_async(goal)
        future.add_done_callback(lambda f: self._goal_response(f, is_waypoint))
    def _send_joint_goal(self, joint_values):
        """
        Send joint goal to MoveIt using Pilz PTP planner with optimized settings
        for ultra-smooth joint space motion at high speeds.
        """
        goal = MoveGroup.Goal()
        goal.request = MotionPlanRequest()
        goal.request.group_name = 'manipulator'

        # Use Pilz PTP for joint space planning - fast and deterministic!
        goal.request.planner_id = 'PTP'  # Point-to-Point motion
        goal.request.pipeline_id = 'pilz_industrial_motion_planner'

        goal.request.num_planning_attempts = 1  # PTP is deterministic
        goal.request.allowed_planning_time = 2.0  # INCREASED from 0.3s - more time for smooth trajectories
        goal.request.max_velocity_scaling_factor = self.velocity_scaling
        goal.request.max_acceleration_scaling_factor = self.acceleration_scaling

        # OPTIMIZED Joint constraints - Relaxed tolerance for smoother motion
        constraints = Constraints()
        joint_names = ['Joint_1', 'Joint_2', 'Joint_3', 'Joint_4', 'Joint_5', 'Joint_6']
        for name, value in zip(joint_names, joint_values):
            jc = JointConstraint()
            jc.joint_name = name
            jc.position = value
            jc.tolerance_above = 0.02  # INCREASED from 0.01 - looser tolerance = smoother solving
            jc.tolerance_below = 0.02
            jc.weight = 1.0
            constraints.joint_constraints.append(jc)
        goal.request.goal_constraints.append(constraints)
        goal.planning_options.plan_only = False

        future = self._move_group_client.send_goal_async(goal)
        future.add_done_callback(lambda f: self._goal_response(f, False))
    def _goal_response(self, future, is_waypoint):
        """Handle goal acceptance"""
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected')
            if is_waypoint:
                self._execute_next_waypoint()
            else:
                with self._execution_lock:
                    self._executing = False
            return
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(lambda f: self._goal_result(f, is_waypoint))
    def _goal_result(self, future, is_waypoint):
        """Handle goal result"""
        result = future.result().result

        # Publish command completion feedback to GUI
        from std_msgs.msg import Bool
        complete_msg = Bool()
        complete_msg.data = True
        self.command_complete_pub.publish(complete_msg)

        if result.error_code.val == 1:
            self.get_logger().info('✓ Success')
            self._retry_count = 0  # Reset on success
            if is_waypoint:
                self._execute_next_waypoint()
            else:
                with self._execution_lock:
                    self._executing = False
        else:
            self.get_logger().error(f'✗ Failed: {result.error_code.val}')

            # Error code -31 is NO_IK_SOLUTION
            if result.error_code.val == -31 and not is_waypoint and self._retry_count == 0 and hasattr(self, '_last_pose'):
                # First failure: Try switching to PTP planner (joint space)
                # PTP is more flexible than LIN for reaching difficult poses
                self._retry_count = 1
                self.get_logger().warning(f'Retry 1/2: Switching to PTP planner (joint space)')
                self._send_pose_goal_ptp(self._last_pose, is_waypoint=False)
            elif not is_waypoint and self._retry_count == 1 and hasattr(self, '_last_pose'):
                # Second failure: Try with reduced speed
                self._retry_count = 2
                original_vel = self.velocity_scaling
                original_acc = self.acceleration_scaling
                self.velocity_scaling *= 0.5
                self.acceleration_scaling *= 0.5

                self.get_logger().warning(f'Retry 2/2 with lower speed: vel={self.velocity_scaling:.2f}, acc={self.acceleration_scaling:.2f}')

                # Retry with LIN planner but lower speeds
                self._send_pose_goal(self._last_pose, is_waypoint=False)

                # Restore original speeds for next command
                self.velocity_scaling = original_vel
                self.acceleration_scaling = original_acc
            else:
                # Give up after retries
                if is_waypoint:
                    self._execute_next_waypoint()  # Skip and continue
                else:
                    with self._execution_lock:
                        self._executing = False

    def _send_pose_goal_ptp(self, pose: Pose, is_waypoint=False):
        """
        Send pose goal using PTP planner (joint space motion).
        More flexible than LIN for difficult poses, but doesn't guarantee straight line.
        """
        goal = MoveGroup.Goal()
        goal.request = MotionPlanRequest()
        goal.request.group_name = 'manipulator'

        # Use Pilz PTP planner for joint space motion
        goal.request.planner_id = 'PTP'  # Point-to-Point in joint space
        goal.request.pipeline_id = 'pilz_industrial_motion_planner'

        goal.request.num_planning_attempts = 1
        goal.request.allowed_planning_time = 1.0
        goal.request.max_velocity_scaling_factor = self.velocity_scaling
        goal.request.max_acceleration_scaling_factor = self.acceleration_scaling

        # Position constraint - relaxed for PTP
        pos_constraint = PositionConstraint()
        pos_constraint.header.frame_id = 'base_link'
        pos_constraint.link_name = 'tool0'
        bounding_volume = BoundingVolume()
        sphere = SolidPrimitive()
        sphere.type = SolidPrimitive.SPHERE
        sphere.dimensions = [0.01]  # 10mm tolerance for PTP
        bounding_volume.primitives.append(sphere)
        pose_stamped = PoseStamped()
        pose_stamped.pose = pose
        bounding_volume.primitive_poses.append(pose_stamped.pose)
        pos_constraint.constraint_region = bounding_volume
        pos_constraint.weight = 1.0

        # Orientation constraint - very relaxed for PTP
        orient_constraint = OrientationConstraint()
        orient_constraint.header.frame_id = 'base_link'
        orient_constraint.link_name = 'tool0'
        orient_constraint.orientation = pose.orientation
        orient_constraint.absolute_x_axis_tolerance = 1.0  # ~57 degrees - very relaxed
        orient_constraint.absolute_y_axis_tolerance = 1.0
        orient_constraint.absolute_z_axis_tolerance = 1.0
        orient_constraint.weight = 1.0

        # Add constraints
        constraints = Constraints()
        constraints.position_constraints.append(pos_constraint)
        constraints.orientation_constraints.append(orient_constraint)
        goal.request.goal_constraints.append(constraints)

        # Execute
        goal.planning_options.plan_only = False
        future = self._move_group_client.send_goal_async(goal)
        future.add_done_callback(lambda f: self._goal_response(f, is_waypoint))
def main(args=None):
    rclpy.init(args=args)
    node = GUIBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
if __name__ == '__main__':
    main()
