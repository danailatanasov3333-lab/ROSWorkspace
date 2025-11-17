#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose, PoseArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray
from moveit_msgs.srv import GetPositionFK
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QGroupBox, QGridLayout, QTabWidget, QSlider,
                             QCheckBox, QSpinBox, QFileDialog, QComboBox, QScrollArea)
from PyQt6.QtCore import QTimer, pyqtSignal, QObject, Qt
from PyQt6.QtGui import QDoubleValidator, QImage, QPixmap
from scipy.spatial.transform import Rotation as R
import cv2
import numpy as np
import math


class ROS2Thread(QObject):
    """Handles ROS2 communication in a separate thread"""
    position_updated = pyqtSignal(list, list)  # [x, y, z], [rx, ry, rz]
    camera_frame_ready = pyqtSignal(object)  # For camera display
    command_completed = pyqtSignal()  # Signal when a command completes

    def __init__(self):
        super().__init__()
        self.node = None
        self.current_joint_state = None
        self.joint_names = ['Joint_1', 'Joint_2', 'Joint_3', 'Joint_4', 'Joint_5', 'Joint_6']

        # Current position - READ from MoveIt, NO computation!
        # Will be updated by subscribing to move_group's current state
        self.current_position_mm = [0.0, 0.0, 0.0]  # Will be populated from MoveIt
        self.current_orientation_deg = [-90.0, 0.0, -180.0]  # Will be populated from MoveIt

        # Command execution tracking for debouncing
        self.command_in_progress = False
        self.last_command_time = 0.0

        # Camera and contouring
        self.camera = None
        self.camera_id = 0
        self.camera_enabled = False

        # Background subtraction - MOG2 with shadow detection
        self.bg_subtractor = None
        self.background_subtraction_enabled = False
        self.mog2_history = 500  # Default history length

    def init_ros(self):
        """Initialize ROS2 node and publishers/subscribers"""
        if not rclpy.ok():
            rclpy.init()

        self.node = Node('cartesian_gui')

        # Publisher for cartesian commands
        self.cartesian_pub = self.node.create_publisher(
            Pose,
            '/gui_cartesian_command',
            10
        )

        # Publisher for joint commands (for home button)
        self.joint_pub = self.node.create_publisher(
            Float64MultiArray,
            '/gui_joint_command',
            10
        )

        # Publisher for waypoint batches (for contour following)
        self.waypoint_batch_pub = self.node.create_publisher(
            PoseArray,
            '/gui_waypoint_batch',
            10
        )

        # Publisher for speed scaling updates (for Pilz planner)
        from std_msgs.msg import Float32MultiArray
        self.speed_scaling_pub = self.node.create_publisher(
            Float32MultiArray,
            '/gui_speed_scaling',
            10
        )

        # Subscriber for current joint states (from ros2_control)
        self.joint_state_sub = self.node.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )

        # Subscribe to MoveIt's move_group/display_planned_path to get current state
        # MoveIt computes FK for us - we just READ the result!
        from moveit_msgs.msg import DisplayTrajectory
        self.display_trajectory_sub = self.node.create_subscription(
            DisplayTrajectory,
            '/display_planned_path',
            self.display_trajectory_callback,
            10
        )

        # Create a service client to query current EE pose from MoveIt
        from moveit_msgs.srv import GetPositionFK
        self.fk_client = self.node.create_client(GetPositionFK, '/compute_fk')

        # Timer to periodically update current pose from MoveIt (for display/safety checks)
        self.pose_update_timer = self.node.create_timer(0.5, self.update_current_pose_from_moveit)

        # Subscriber for waypoint batch completion
        from std_msgs.msg import Bool
        self.waypoint_complete_sub = self.node.create_subscription(
            Bool,
            '/gui_waypoint_batch_complete',
            self.waypoint_batch_complete_callback,
            10
        )

        # Subscribe to move_group action results to track command completion
        from moveit_msgs.action import MoveGroup
        from rclpy.action import ActionClient
        self._move_action_client = ActionClient(self.node, MoveGroup, '/move_action')

        # Subscribe to command completion feedback from gui_bridge
        from std_msgs.msg import Bool
        self.command_complete_sub = self.node.create_subscription(
            Bool,
            '/gui_command_complete',
            self.command_complete_callback,
            10
        )

        # Flag for pending home command
        self.pending_home_after_waypoints = False

    def joint_state_callback(self, msg):
        """Store joint states - will use for FK query"""
        if len(msg.position) >= 6:
            self.current_joint_state = msg

    def display_trajectory_callback(self, msg):
        """Read trajectory display - not used for position tracking"""
        pass

    def update_current_pose_from_moveit(self):
        """
        Query MoveIt for current EE pose using FK service.
        MoveIt does the FK computation, we just READ the result.
        Used ONLY for display and safety (Z height check).
        """
        if not self.current_joint_state:
            return

        if not self.fk_client:
            return

        if not self.fk_client.service_is_ready():
            # Service not ready yet - will retry on next timer tick
            return

        from moveit_msgs.srv import GetPositionFK
        req = GetPositionFK.Request()
        req.header.frame_id = 'base_link'
        req.fk_link_names = ['tool0']
        req.robot_state.joint_state.name = self.joint_names
        req.robot_state.joint_state.position = list(self.current_joint_state.position[:6])

        try:
            future = self.fk_client.call_async(req)
            future.add_done_callback(self.fk_result_callback)
        except Exception as e:
            if self.node:
                self.node.get_logger().debug(f'FK query failed: {e}')

    def fk_result_callback(self, future):
        """Handle FK result from MoveIt - just READ and store"""
        try:
            result = future.result()
            if result and len(result.pose_stamped) > 0:
                pose = result.pose_stamped[0].pose

                # Store position in mm (for display)
                x_mm = pose.position.x * 1000.0
                y_mm = pose.position.y * 1000.0
                z_mm = pose.position.z * 1000.0
                self.current_position_mm = [x_mm, y_mm, z_mm]

                # Store orientation (for display)
                from scipy.spatial.transform import Rotation as R
                quat = [pose.orientation.x, pose.orientation.y,
                        pose.orientation.z, pose.orientation.w]
                rot = R.from_quat(quat)
                euler = rot.as_euler('xyz', degrees=True)
                self.current_orientation_deg = euler.tolist()

                # Emit signal for GUI update
                self.position_updated.emit([x_mm, y_mm, z_mm], euler.tolist())

        except Exception as e:
            if self.node:
                self.node.get_logger().debug(f'FK result processing failed: {e}')

    def send_cartesian_command(self, x, y, z, rx, ry, rz):
        """Send cartesian position command"""
        if self.node is None:
            return

        # Check if a command is already in progress
        import time
        current_time = time.time()
        if self.command_in_progress:
            self.node.get_logger().warning('Command already in progress, ignoring new command')
            return

        # Debounce: prevent commands sent faster than 100ms
        if current_time - self.last_command_time < 0.1:
            self.node.get_logger().warning('Command sent too fast, debouncing')
            return

        self.command_in_progress = True
        self.last_command_time = current_time

        pose = Pose()
        # Convert from mm to meters
        pose.position.x = x / 1000.0
        pose.position.y = y / 1000.0
        pose.position.z = z / 1000.0

        # Convert euler angles (degrees) to quaternion
        rot = R.from_euler('xyz', [rx, ry, rz], degrees=True)
        quat = rot.as_quat()

        pose.orientation.x = quat[0]
        pose.orientation.y = quat[1]
        pose.orientation.z = quat[2]
        pose.orientation.w = quat[3]

        self.cartesian_pub.publish(pose)
        self.node.get_logger().info(f'Cartesian: X={x:.1f}, Y={y:.1f}, Z={z:.1f}, rX={rx:.1f}, rY={ry:.1f}, rZ={rz:.1f}')

        # Set timer to reset command_in_progress after reasonable timeout
        # This ensures we don't get stuck if gui_bridge doesn't respond
        timer = self.node.create_timer(5.0, self._reset_command_lock)
        self._timeout_timer = timer  # Store reference to cancel later if needed

    def send_home_command(self):
        """Send joint command to go to home position"""
        if self.node is None:
            return

        home_positions = [-1.57, -0.35, -0.7, -0.52, -1.57, 0.0]

        msg = Float64MultiArray()
        msg.data = home_positions

        self.joint_pub.publish(msg)
        self.node.get_logger().info('Sent HOME command')

        # Track command execution
        self.command_in_progress = True
        import time
        self.last_command_time = time.time()
        timer = self.node.create_timer(5.0, self._reset_command_lock)
        self._timeout_timer = timer  # Store reference

    def _reset_command_lock(self):
        """Reset command lock after timeout (safety mechanism)"""
        if self.command_in_progress:
            self.command_in_progress = False
            self.command_completed.emit()
            if self.node:
                self.node.get_logger().info('Command lock reset (timeout)')

        # Destroy the timer to make it one-shot
        if hasattr(self, '_timeout_timer') and self._timeout_timer:
            self._timeout_timer.cancel()
            self._timeout_timer = None

    def mark_command_complete(self):
        """Mark current command as completed (called by gui_bridge feedback)"""
        self.command_in_progress = False
        self.command_completed.emit()

        # Cancel timeout timer since command completed normally
        if hasattr(self, '_timeout_timer') and self._timeout_timer:
            self._timeout_timer.cancel()
            self._timeout_timer = None

        if self.node:
            self.node.get_logger().debug('Command completed')

    def command_complete_callback(self, msg):
        """Handle command completion feedback from gui_bridge"""
        self.mark_command_complete()

    def send_speed_scaling(self, velocity, acceleration):
        """Send speed scaling parameters to gui_bridge for Pilz planner"""
        if self.node is None:
            return

        from std_msgs.msg import Float32MultiArray
        msg = Float32MultiArray()
        msg.data = [velocity, acceleration]
        self.speed_scaling_pub.publish(msg)

    def start_camera(self, camera_id=0):
        """Start camera capture."""
        self.camera_id = camera_id
        self.camera = cv2.VideoCapture(camera_id)
        if self.camera.isOpened():
            self.camera_enabled = True
            self.node.get_logger().info(f'Camera {camera_id} opened successfully')
            return True
        else:
            self.node.get_logger().error(f'Failed to open camera {camera_id}')
            return False

    def stop_camera(self):
        """Stop camera capture."""
        self.camera_enabled = False
        if self.camera is not None:
            self.camera.release()
            self.camera = None

    def capture_frame(self):
        """Capture a frame from camera."""
        if self.camera is not None and self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                return frame
        return None

    def init_background_subtractor(self, history=500):
        """
        Initialize MOG2 background subtractor with shadow detection.

        Args:
            history: Number of frames in history (500 or 1000 recommended)
        """
        # Create MOG2 background subtractor
        # detectShadows=True enables shadow detection (shadows marked as gray value 127)
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=history,
            varThreshold=16,
            detectShadows=True
        )
        self.mog2_history = history
        self.node.get_logger().info(f'MOG2 background subtractor initialized (history={history}, shadows=ON)')
        return True

    def clear_background(self):
        """Clear the background subtractor."""
        self.bg_subtractor = None
        self.node.get_logger().info('MOG2 background subtractor cleared')

    def apply_background_subtraction(self, frame):
        """
        Apply MOG2 background subtraction with shadow detection.

        Args:
            frame: Current BGR frame

        Returns:
            Foreground mask (grayscale, shadows removed)
        """
        if self.bg_subtractor is None:
            # No background subtractor, return original grayscale
            return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply MOG2 background subtractor
        # Returns mask: 0=background, 127=shadow, 255=foreground
        fg_mask = self.bg_subtractor.apply(frame)

        # Remove shadows (convert 127 to 0, keep 255 as 255)
        # This treats shadows as background
        _, fg_mask_no_shadow = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)

        # Optional: Clean up noise with morphology
        kernel = np.ones((3, 3), np.uint8)
        fg_mask_clean = cv2.morphologyEx(fg_mask_no_shadow, cv2.MORPH_OPEN, kernel, iterations=2)
        fg_mask_clean = cv2.morphologyEx(fg_mask_clean, cv2.MORPH_CLOSE, kernel, iterations=2)

        return fg_mask_clean


    def detect_contours(self, frame, threshold_params):
        """
        Detect contours in frame using binary or adaptive thresholding.
        Includes advanced filtering: background removal, shadow detection, border removal.

        Args:
            frame: Input BGR image
            threshold_params: dict with:
                - 'method': 'binary' or 'adaptive'
                - 'threshold_value': for binary (0-255)
                - 'kernel_size': for Gaussian blur (odd number)
                - 'invert': True for BINARY_INV, False for BINARY
                - 'use_background_subtraction': Apply background subtraction
                - 'remove_background': Remove largest contour (usually background)
                - 'detect_shadows': Apply dilation+erosion for shadow removal
                - 'remove_border': Remove contours touching frame edges
                - 'border_margin': Percentage of frame size for border detection
                - 'filter_convexity': Filter out thin/linear contours
                - 'min_convexity': Minimum convexity ratio (0-100)

        Returns:
            (processed_frame, contours) tuple
        """
        # Apply background subtraction first if enabled
        if threshold_params.get('use_background_subtraction', False) and self.bg_subtractor is not None:
            gray = self.apply_background_subtraction(frame)
        else:
            # Convert to grayscale normally
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        kernel_size = threshold_params.get('kernel_size', 5)
        # Ensure kernel size is odd
        if kernel_size % 2 == 0:
            kernel_size += 1
        blurred = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

        # Shadow detection/removal (before thresholding)
        if threshold_params.get('detect_shadows', False):
            # Dilate then erode to remove shadows
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
            dilated = cv2.dilate(blurred, kernel, iterations=1)
            blurred = cv2.erode(dilated, kernel, iterations=1)

        # Choose thresholding method
        method = threshold_params.get('method', 'binary')
        invert = threshold_params.get('invert', True)

        if method == 'binary':
            # Binary thresholding with cv2.threshold
            threshold_value = threshold_params.get('threshold_value', 127)

            if invert:
                # Dark objects on light background (inverted)
                _, binary = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY_INV)
            else:
                # Light objects on dark background
                _, binary = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY)
        else:
            # Adaptive thresholding (for uneven lighting)
            block_size = threshold_params.get('adaptive_block_size', 11)
            # Ensure block size is odd and >= 3
            if block_size % 2 == 0:
                block_size += 1
            block_size = max(3, block_size)

            c_value = threshold_params.get('adaptive_c', 2)

            if invert:
                binary = cv2.adaptiveThreshold(
                    blurred, 255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY_INV,
                    block_size, c_value
                )
            else:
                binary = cv2.adaptiveThreshold(
                    blurred, 255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY,
                    block_size, c_value
                )

        # Optional: Apply morphological operations to clean up the binary image
        if threshold_params.get('use_morphology', False):
            kernel = np.ones((3, 3), np.uint8)
            # Remove small noise
            binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
            # Fill small holes
            binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)

        # Find contours
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours by minimum area
        min_area = threshold_params.get('min_area', 100)
        valid_contours = []

        # Get frame dimensions for border detection
        frame_h, frame_w = frame.shape[:2]
        border_margin_pct = threshold_params.get('border_margin', 2) / 100.0
        border_x_margin = int(frame_w * border_margin_pct)
        border_y_margin = int(frame_h * border_margin_pct)

        # Remove background (largest contour) if enabled
        if threshold_params.get('remove_background', False) and len(contours) > 0:
            # Find largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            largest_area = cv2.contourArea(largest_contour)
            # Remove it from list if it's significantly larger than others
            contours = [c for c in contours if cv2.contourArea(c) < largest_area * 0.8]

        for contour in contours:
            area = cv2.contourArea(contour)
            if area < min_area:
                continue

            # Border removal check
            if threshold_params.get('remove_border', False):
                # Check if contour touches frame edges
                x, y, w, h = cv2.boundingRect(contour)
                touches_border = (
                    x <= border_x_margin or
                    y <= border_y_margin or
                    x + w >= frame_w - border_x_margin or
                    y + h >= frame_h - border_y_margin
                )
                if touches_border:
                    continue  # Skip border contours

            # Convexity filtering (reject thin/linear shapes)
            if threshold_params.get('filter_convexity', False):
                hull = cv2.convexHull(contour)
                hull_area = cv2.contourArea(hull)
                if hull_area > 0:
                    convexity = (area / hull_area) * 100
                    min_convexity = threshold_params.get('min_convexity', 50)
                    if convexity < min_convexity:
                        continue  # Skip thin/linear contours

            valid_contours.append(contour)

        # Draw contours on original frame
        result = frame.copy()

        # Draw all valid contours in green
        for contour in valid_contours:
            cv2.drawContours(result, [contour], -1, (0, 255, 0), 3)

            # Draw contour area text
            area = cv2.contourArea(contour)
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.putText(result, f"{int(area)}", (cX, cY),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        # Show binary image in corner (for debugging)
        binary_rgb = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
        h, w = binary_rgb.shape[:2]
        small_binary = cv2.resize(binary_rgb, (w//4, h//4))
        result[0:small_binary.shape[0], 0:small_binary.shape[1]] = small_binary

        # Add info overlay
        info_text = f"Contours: {len(valid_contours)}"
        cv2.putText(result, info_text, (10, frame_h - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        return result, valid_contours

    def contours_to_waypoints(self, contours, pixel_to_mm_scale, camera_center, z_height, min_area=100):
        """
        Convert image contours to 3D waypoints in robot workspace.
        ALWAYS uses fixed HOME orientation (tool pointing down) - NO FK needed!

        Args:
            contours: OpenCV contours (already filtered by detect_contours)
            pixel_to_mm_scale: Scale factor (mm per pixel)
            camera_center: (x_mm, y_mm) camera center in robot coordinates
            z_height: Z coordinate for all waypoints (mm)
            min_area: Minimum contour area in pixels (optional, for double-checking)

        Returns:
            List of Pose messages
        """
        waypoints = []

        # ALWAYS use fixed HOME orientation (tool pointing down) - NO computation!
        from scipy.spatial.transform import Rotation as R
        fixed_orientation = [-90.0, 0.0, -180.0]  # rx, ry, rz in degrees
        rot = R.from_euler('xyz', fixed_orientation, degrees=True)
        fixed_quat = rot.as_quat()

        for contour in contours:
            # Contours are already filtered, but double-check
            if cv2.contourArea(contour) < min_area:
                continue

            # Approximate contour to reduce points
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Convert each point to robot coordinates
            for point in approx:
                px, py = point[0]

                # Convert pixel coordinates to mm (assuming camera is centered)
                # Invert Y axis (image Y goes down, robot Y goes up)
                x_mm = camera_center[0] + (px - camera_center[0]) * pixel_to_mm_scale
                y_mm = camera_center[1] - (py - camera_center[1]) * pixel_to_mm_scale

                # Create pose
                pose = Pose()
                pose.position.x = x_mm / 1000.0  # Convert to meters
                pose.position.y = y_mm / 1000.0
                pose.position.z = z_height / 1000.0

                # ALWAYS use fixed orientation (no computation!)
                pose.orientation.x = fixed_quat[0]
                pose.orientation.y = fixed_quat[1]
                pose.orientation.z = fixed_quat[2]
                pose.orientation.w = fixed_quat[3]

                waypoints.append(pose)

        return waypoints

    def send_waypoint_batch(self, waypoints):
        """Send batch of waypoints for contour following."""
        if self.node is None or len(waypoints) == 0:
            return

        msg = PoseArray()
        msg.header.frame_id = 'base_link'
        msg.poses = waypoints

        self.waypoint_batch_pub.publish(msg)
        self.node.get_logger().info(f'Sent batch of {len(waypoints)} waypoints for contour following')

    def waypoint_batch_complete_callback(self, msg):
        """Called when gui_bridge finishes executing all waypoints."""
        if msg.data and self.pending_home_after_waypoints:
            self.node.get_logger().info('Waypoint batch complete - sending HOME command now')
            self.send_home_command()
            self.pending_home_after_waypoints = False

    def spin_once(self):
        """Spin ROS2 node once"""
        if self.node:
            rclpy.spin_once(self.node, timeout_sec=0.01)


class CartesianGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ros_thread = ROS2Thread()
        self.ros_thread.init_ros()
        self.ros_thread.position_updated.connect(self.update_current_position)

        self.initUI()

        # Timer to spin ROS2
        self.ros_timer = QTimer()
        self.ros_timer.timeout.connect(self.ros_thread.spin_once)
        self.ros_timer.start(10)  # 100 Hz

    def initUI(self):
        self.setWindowTitle('Cartesian Movement Control with Vision')
        self.setGeometry(100, 100, 1400, 900)  # Increased from 1000x800 to 1400x900

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Create tab widget
        tabs = QTabWidget()
        main_layout.addWidget(tabs)

        # Manual control tab
        manual_tab = QWidget()
        manual_layout = QVBoxLayout()
        manual_tab.setLayout(manual_layout)
        tabs.addTab(manual_tab, "Manual Control")

        # Vision/Contouring tab with scroll area
        vision_scroll = QScrollArea()
        vision_scroll.setWidgetResizable(True)
        vision_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        vision_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        vision_tab = QWidget()
        vision_layout = QVBoxLayout()
        vision_tab.setLayout(vision_layout)
        vision_scroll.setWidget(vision_tab)
        tabs.addTab(vision_scroll, "Vision & Contouring")

        # Build manual control tab
        self._build_manual_tab(manual_layout)

        # Build vision tab
        self._build_vision_tab(vision_layout)

        # Status message (shared across tabs)
        self.status_label = QLabel("Ready - Waiting for robot data...")
        self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #f0f0f0; font-size: 12px; }")
        main_layout.addWidget(self.status_label)

        # Send initial speed scaling values to gui_bridge
        QTimer.singleShot(1000, self.update_speed_scaling)  # Wait 1s for gui_bridge to start

    def _build_manual_tab(self, layout):
        """Build the manual control tab."""
        # Current Position Display Group
        current_group = QGroupBox("Current Position")
        current_layout = QGridLayout()
        current_group.setLayout(current_layout)

        # Labels for current position with larger font
        label_style = "QLabel { font-size: 16px; font-weight: bold; padding: 5px; }"
        self.current_x_label = QLabel("X: -- mm")
        self.current_x_label.setStyleSheet(label_style)
        self.current_y_label = QLabel("Y: -- mm")
        self.current_y_label.setStyleSheet(label_style)
        self.current_z_label = QLabel("Z: -- mm")
        self.current_z_label.setStyleSheet(label_style)
        self.current_rx_label = QLabel("rX: -- °")
        self.current_rx_label.setStyleSheet(label_style)
        self.current_ry_label = QLabel("rY: -- °")
        self.current_ry_label.setStyleSheet(label_style)
        self.current_rz_label = QLabel("rZ: -- °")
        self.current_rz_label.setStyleSheet(label_style)

        current_layout.addWidget(self.current_x_label, 0, 0)
        current_layout.addWidget(self.current_y_label, 0, 1)
        current_layout.addWidget(self.current_z_label, 0, 2)
        current_layout.addWidget(self.current_rx_label, 1, 0)
        current_layout.addWidget(self.current_ry_label, 1, 1)
        current_layout.addWidget(self.current_rz_label, 1, 2)

        layout.addWidget(current_group)

        # Distance/Angle Input Group
        distance_group = QGroupBox("Step Size")
        distance_layout = QHBoxLayout()
        distance_group.setLayout(distance_layout)

        double_validator = QDoubleValidator()

        distance_layout.addWidget(QLabel("Linear (mm):"))
        self.linear_step = QLineEdit("10.0")
        self.linear_step.setValidator(double_validator)
        self.linear_step.setMaximumWidth(80)
        distance_layout.addWidget(self.linear_step)

        distance_layout.addWidget(QLabel("   Rotation (deg):"))
        self.rotation_step = QLineEdit("5.0")
        self.rotation_step.setValidator(double_validator)
        self.rotation_step.setMaximumWidth(80)
        distance_layout.addWidget(self.rotation_step)

        layout.addWidget(distance_group)

        # Pilz Planner Speed Controls
        speed_group = QGroupBox("Pilz Planner Speed (TracIK + LIN)")
        speed_layout = QHBoxLayout()
        speed_group.setLayout(speed_layout)

        speed_layout.addWidget(QLabel("Velocity:"))
        self.velocity_scale = QLineEdit("0.6")  # INCREASED - S-curve allows higher speeds smoothly
        self.velocity_scale.setValidator(double_validator)
        self.velocity_scale.setMaximumWidth(60)
        self.velocity_scale.setToolTip("Velocity scaling factor (0.0-1.0). Can go up to 0.8 with S-curve smoothing.")
        self.velocity_scale.editingFinished.connect(self.update_speed_scaling)
        speed_layout.addWidget(self.velocity_scale)

        speed_layout.addWidget(QLabel("   Accel:"))
        self.accel_scale = QLineEdit("0.6")  # INCREASED - S-curve jerk limiting provides smoothness
        self.accel_scale.setValidator(double_validator)
        self.accel_scale.setMaximumWidth(60)
        self.accel_scale.setToolTip("Acceleration scaling factor (0.0-1.0). Can go up to 0.8 with S-curve smoothing.")
        self.accel_scale.editingFinished.connect(self.update_speed_scaling)
        speed_layout.addWidget(self.accel_scale)

        speed_layout.addStretch()

        layout.addWidget(speed_group)

        # Movement Buttons Group
        movement_group = QGroupBox("Movement Controls")
        movement_layout = QGridLayout()
        movement_group.setLayout(movement_layout)

        button_style = "QPushButton { font-size: 14px; font-weight: bold; padding: 15px; min-width: 60px; }"
        pos_style = button_style + " background-color: #4CAF50; color: white; }"
        neg_style = button_style + " background-color: #f44336; color: white; }"

        # Position buttons
        movement_layout.addWidget(QLabel("X:"), 0, 0)
        self.x_minus_btn = QPushButton("X-")
        self.x_minus_btn.setStyleSheet(neg_style)
        self.x_minus_btn.clicked.connect(lambda: self.move_incremental(-1, 0, 0, 0, 0, 0))
        movement_layout.addWidget(self.x_minus_btn, 0, 1)

        self.x_plus_btn = QPushButton("X+")
        self.x_plus_btn.setStyleSheet(pos_style)
        self.x_plus_btn.clicked.connect(lambda: self.move_incremental(1, 0, 0, 0, 0, 0))
        movement_layout.addWidget(self.x_plus_btn, 0, 2)

        movement_layout.addWidget(QLabel("Y:"), 1, 0)
        self.y_minus_btn = QPushButton("Y-")
        self.y_minus_btn.setStyleSheet(neg_style)
        self.y_minus_btn.clicked.connect(lambda: self.move_incremental(0, -1, 0, 0, 0, 0))
        movement_layout.addWidget(self.y_minus_btn, 1, 1)

        self.y_plus_btn = QPushButton("Y+")
        self.y_plus_btn.setStyleSheet(pos_style)
        self.y_plus_btn.clicked.connect(lambda: self.move_incremental(0, 1, 0, 0, 0, 0))
        movement_layout.addWidget(self.y_plus_btn, 1, 2)

        movement_layout.addWidget(QLabel("Z:"), 2, 0)
        self.z_minus_btn = QPushButton("Z-")
        self.z_minus_btn.setStyleSheet(neg_style)
        self.z_minus_btn.clicked.connect(lambda: self.move_incremental(0, 0, -1, 0, 0, 0))
        movement_layout.addWidget(self.z_minus_btn, 2, 1)

        self.z_plus_btn = QPushButton("Z+")
        self.z_plus_btn.setStyleSheet(pos_style)
        self.z_plus_btn.clicked.connect(lambda: self.move_incremental(0, 0, 1, 0, 0, 0))
        movement_layout.addWidget(self.z_plus_btn, 2, 2)

        # Rotation buttons
        movement_layout.addWidget(QLabel("rX:"), 0, 3)
        self.rx_minus_btn = QPushButton("rX-")
        self.rx_minus_btn.setStyleSheet(neg_style)
        self.rx_minus_btn.clicked.connect(lambda: self.move_incremental(0, 0, 0, -1, 0, 0))
        movement_layout.addWidget(self.rx_minus_btn, 0, 4)

        self.rx_plus_btn = QPushButton("rX+")
        self.rx_plus_btn.setStyleSheet(pos_style)
        self.rx_plus_btn.clicked.connect(lambda: self.move_incremental(0, 0, 0, 1, 0, 0))
        movement_layout.addWidget(self.rx_plus_btn, 0, 5)

        movement_layout.addWidget(QLabel("rY:"), 1, 3)
        self.ry_minus_btn = QPushButton("rY-")
        self.ry_minus_btn.setStyleSheet(neg_style)
        self.ry_minus_btn.clicked.connect(lambda: self.move_incremental(0, 0, 0, 0, -1, 0))
        movement_layout.addWidget(self.ry_minus_btn, 1, 4)

        self.ry_plus_btn = QPushButton("rY+")
        self.ry_plus_btn.setStyleSheet(pos_style)
        self.ry_plus_btn.clicked.connect(lambda: self.move_incremental(0, 0, 0, 0, 1, 0))
        movement_layout.addWidget(self.ry_plus_btn, 1, 5)

        movement_layout.addWidget(QLabel("rZ:"), 2, 3)
        self.rz_minus_btn = QPushButton("rZ-")
        self.rz_minus_btn.setStyleSheet(neg_style)
        self.rz_minus_btn.clicked.connect(lambda: self.move_incremental(0, 0, 0, 0, 0, -1))
        movement_layout.addWidget(self.rz_minus_btn, 2, 4)

        self.rz_plus_btn = QPushButton("rZ+")
        self.rz_plus_btn.setStyleSheet(pos_style)
        self.rz_plus_btn.clicked.connect(lambda: self.move_incremental(0, 0, 0, 0, 0, 1))
        movement_layout.addWidget(self.rz_plus_btn, 2, 5)

        layout.addWidget(movement_group)

        # Home button
        home_layout = QHBoxLayout()
        self.home_button = QPushButton("Go to HOME")
        self.home_button.clicked.connect(self.send_home_command)
        self.home_button.setStyleSheet("QPushButton { background-color: #2196F3; color: white; padding: 15px; font-size: 16px; font-weight: bold; }")
        home_layout.addWidget(self.home_button)
        layout.addLayout(home_layout)

    def _build_vision_tab(self, layout):
        """Build the vision and contouring tab."""
        # Camera controls
        camera_group = QGroupBox("Camera Control")
        camera_layout = QVBoxLayout()
        camera_group.setLayout(camera_layout)

        # Camera selection and control
        cam_control_layout = QHBoxLayout()
        cam_control_layout.addWidget(QLabel("Camera ID:"))
        self.camera_id_spin = QSpinBox()
        self.camera_id_spin.setRange(0, 10)
        self.camera_id_spin.setValue(0)
        cam_control_layout.addWidget(self.camera_id_spin)

        self.camera_start_btn = QPushButton("Start Camera")
        self.camera_start_btn.clicked.connect(self.start_camera)
        cam_control_layout.addWidget(self.camera_start_btn)

        self.camera_stop_btn = QPushButton("Stop Camera")
        self.camera_stop_btn.clicked.connect(self.stop_camera)
        self.camera_stop_btn.setEnabled(False)
        cam_control_layout.addWidget(self.camera_stop_btn)

        camera_layout.addLayout(cam_control_layout)

        # MOG2 Background subtraction controls
        bg_subtract_layout = QVBoxLayout()

        # History selection
        history_layout = QHBoxLayout()
        history_layout.addWidget(QLabel("MOG2 History:"))
        self.mog2_history_combo = QComboBox()
        self.mog2_history_combo.addItems(["500 frames", "1000 frames"])
        self.mog2_history_combo.setCurrentIndex(0)  # Default 500
        self.mog2_history_combo.setToolTip("Number of frames in background model (more = slower adaptation)")
        history_layout.addWidget(self.mog2_history_combo)
        history_layout.addStretch()
        bg_subtract_layout.addLayout(history_layout)

        # Control buttons
        bg_btn_layout = QHBoxLayout()
        self.init_bg_btn = QPushButton("Initialize MOG2 (Learn Background)")
        self.init_bg_btn.clicked.connect(self.init_background_subtractor)
        self.init_bg_btn.setEnabled(False)
        self.init_bg_btn.setStyleSheet("QPushButton { background-color: #FF9800; color: white; padding: 8px; font-weight: bold; }")
        self.init_bg_btn.setToolTip("Start learning background model - let camera run for a few seconds")
        bg_btn_layout.addWidget(self.init_bg_btn)

        self.clear_bg_btn = QPushButton("Clear Background")
        self.clear_bg_btn.clicked.connect(self.clear_background)
        self.clear_bg_btn.setEnabled(False)
        self.clear_bg_btn.setToolTip("Clear MOG2 background model")
        bg_btn_layout.addWidget(self.clear_bg_btn)
        bg_subtract_layout.addLayout(bg_btn_layout)

        camera_layout.addLayout(bg_subtract_layout)

        self.use_bg_subtract_checkbox = QCheckBox("Use MOG2 Background Subtraction (with shadow detection)")
        self.use_bg_subtract_checkbox.setChecked(False)
        self.use_bg_subtract_checkbox.setEnabled(False)
        self.use_bg_subtract_checkbox.setStyleSheet("QCheckBox { padding: 5px; font-weight: bold; }")
        self.use_bg_subtract_checkbox.setToolTip("Enable MOG2 background removal - automatically adapts over time")
        camera_layout.addWidget(self.use_bg_subtract_checkbox)

        # Background status label
        self.bg_status_label = QLabel("MOG2 not initialized - Click 'Initialize' to learn background")
        self.bg_status_label.setStyleSheet("QLabel { padding: 5px; background-color: #f0f0f0; font-size: 11px; }")
        camera_layout.addWidget(self.bg_status_label)

        # Live contour detection toggle (enabled by default)
        self.live_contour_checkbox = QCheckBox("Live Contour Detection (always draw contours)")
        self.live_contour_checkbox.setChecked(True)  # ✓ Enabled by default
        self.live_contour_checkbox.setEnabled(False)
        self.live_contour_checkbox.stateChanged.connect(self._on_live_contour_toggled)
        self.live_contour_checkbox.setStyleSheet("QCheckBox { font-weight: bold; padding: 5px; }")
        camera_layout.addWidget(self.live_contour_checkbox)

        # Camera display
        self.camera_display = QLabel("No camera feed")
        self.camera_display.setStyleSheet("QLabel { background-color: #000; color: #fff; min-height: 400px; }")
        self.camera_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        camera_layout.addWidget(self.camera_display)

        layout.addWidget(camera_group)

        # Contour detection controls
        contour_group = QGroupBox("Contour Detection & Path Generation")
        contour_layout = QVBoxLayout()
        contour_group.setLayout(contour_layout)

        # Thresholding parameters
        threshold_group = QGroupBox("Threshold Settings")
        threshold_layout = QGridLayout()
        threshold_group.setLayout(threshold_layout)

        # Thresholding method selection
        threshold_layout.addWidget(QLabel("Method:"), 0, 0)
        self.threshold_method = QComboBox()
        self.threshold_method.addItems(["Binary", "Adaptive"])
        self.threshold_method.currentTextChanged.connect(self._on_threshold_method_changed)
        threshold_layout.addWidget(self.threshold_method, 0, 1)

        # Binary threshold value (0-255)
        threshold_layout.addWidget(QLabel("Threshold Value:"), 1, 0)
        self.threshold_value = QSlider(Qt.Orientation.Horizontal)
        self.threshold_value.setRange(0, 255)
        self.threshold_value.setValue(127)
        self.threshold_value.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.threshold_value.setTickInterval(25)
        threshold_layout.addWidget(self.threshold_value, 1, 1)
        self.threshold_value_label = QLabel("127")
        self.threshold_value.valueChanged.connect(lambda v: self.threshold_value_label.setText(str(v)))
        threshold_layout.addWidget(self.threshold_value_label, 1, 2)

        # Adaptive block size (only for adaptive mode)
        threshold_layout.addWidget(QLabel("Adaptive Block Size:"), 2, 0)
        self.adaptive_block_size = QSpinBox()
        self.adaptive_block_size.setRange(3, 51)
        self.adaptive_block_size.setSingleStep(2)
        self.adaptive_block_size.setValue(11)
        self.adaptive_block_size.setEnabled(False)
        threshold_layout.addWidget(self.adaptive_block_size, 2, 1)

        # Invert threshold checkbox
        self.invert_threshold = QCheckBox("Invert (dark objects on light background)")
        self.invert_threshold.setChecked(True)
        threshold_layout.addWidget(self.invert_threshold, 3, 0, 1, 3)

        # Morphology operations
        self.use_morphology = QCheckBox("Use morphology (clean up noise)")
        self.use_morphology.setChecked(False)
        threshold_layout.addWidget(self.use_morphology, 4, 0, 1, 3)

        contour_layout.addWidget(threshold_group)

        # Advanced filtering options
        advanced_group = QGroupBox("Advanced Filtering")
        advanced_layout = QGridLayout()
        advanced_group.setLayout(advanced_layout)

        # Background removal
        self.remove_background = QCheckBox("Remove background (largest contour)")
        self.remove_background.setChecked(True)
        advanced_layout.addWidget(self.remove_background, 0, 0, 1, 2)

        # Shadow detection
        self.detect_shadows = QCheckBox("Shadow detection (dilate+erode)")
        self.detect_shadows.setChecked(True)
        advanced_layout.addWidget(self.detect_shadows, 1, 0, 1, 2)

        # Frame border removal
        self.remove_border = QCheckBox("Remove frame border contour")
        self.remove_border.setChecked(True)
        advanced_layout.addWidget(self.remove_border, 2, 0, 1, 2)

        # Border margin percentage
        advanced_layout.addWidget(QLabel("Border margin %:"), 3, 0)
        self.border_margin = QSpinBox()
        self.border_margin.setRange(0, 20)
        self.border_margin.setValue(2)
        self.border_margin.setToolTip("Contours within this % of frame edge are considered borders")
        advanced_layout.addWidget(self.border_margin, 3, 1)

        # Convexity filtering
        self.filter_convexity = QCheckBox("Filter by convexity (reject thin/linear contours)")
        self.filter_convexity.setChecked(True)
        advanced_layout.addWidget(self.filter_convexity, 4, 0, 1, 2)

        # Convexity threshold
        advanced_layout.addWidget(QLabel("Min convexity:"), 5, 0)
        self.min_convexity = QSpinBox()
        self.min_convexity.setRange(0, 100)
        self.min_convexity.setValue(50)
        self.min_convexity.setSuffix("%")
        self.min_convexity.setToolTip("Reject contours with convexity below this (0-100%)")
        advanced_layout.addWidget(self.min_convexity, 5, 1)

        contour_layout.addWidget(advanced_group)

        # Detection parameters
        param_layout = QGridLayout()

        param_layout.addWidget(QLabel("Blur Kernel Size:"), 0, 0)
        self.kernel_size_spin = QSpinBox()
        self.kernel_size_spin.setRange(1, 15)
        self.kernel_size_spin.setSingleStep(2)
        self.kernel_size_spin.setValue(5)
        param_layout.addWidget(self.kernel_size_spin, 0, 1)

        param_layout.addWidget(QLabel("Min Contour Area (px):"), 1, 0)
        self.min_contour_area = QSpinBox()
        self.min_contour_area.setRange(10, 10000)
        self.min_contour_area.setValue(100)
        param_layout.addWidget(self.min_contour_area, 1, 1)

        param_layout.addWidget(QLabel("Pixel to mm scale:"), 2, 0)
        self.pixel_scale_input = QLineEdit("0.5")
        self.pixel_scale_input.setValidator(QDoubleValidator())
        param_layout.addWidget(self.pixel_scale_input, 2, 1)

        param_layout.addWidget(QLabel("Camera Center X (mm):"), 2, 0)
        self.camera_center_x = QLineEdit("0.0")
        self.camera_center_x.setValidator(QDoubleValidator())
        param_layout.addWidget(self.camera_center_x, 2, 1)

        param_layout.addWidget(QLabel("Camera Center Y (mm):"), 2, 2)
        self.camera_center_y = QLineEdit("0.0")
        self.camera_center_y.setValidator(QDoubleValidator())
        param_layout.addWidget(self.camera_center_y, 2, 3)

        param_layout.addWidget(QLabel("Working Height Z (mm):"), 3, 0)
        self.working_z = QLineEdit("200.0")
        self.working_z.setValidator(QDoubleValidator())
        param_layout.addWidget(self.working_z, 3, 1)

        contour_layout.addLayout(param_layout)

        # Control buttons
        contour_btn_layout = QHBoxLayout()
        self.detect_contours_btn = QPushButton("Generate Waypoints from Contours")
        self.detect_contours_btn.clicked.connect(self.detect_contours)
        self.detect_contours_btn.setEnabled(False)
        self.detect_contours_btn.setStyleSheet("QPushButton { background-color: #2196F3; color: white; padding: 10px; font-weight: bold; }")
        contour_btn_layout.addWidget(self.detect_contours_btn)

        self.execute_contours_btn = QPushButton("Execute Contour Path")
        self.execute_contours_btn.clicked.connect(self.execute_contour_path)
        self.execute_contours_btn.setEnabled(False)
        self.execute_contours_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; padding: 10px; font-weight: bold; }")
        contour_btn_layout.addWidget(self.execute_contours_btn)

        contour_layout.addLayout(contour_btn_layout)

        # Auto-return to home option
        self.auto_home_checkbox = QCheckBox("Return to HOME after contour path execution")
        self.auto_home_checkbox.setChecked(True)  # Enabled by default
        self.auto_home_checkbox.setStyleSheet("QCheckBox { padding: 5px; }")
        contour_layout.addWidget(self.auto_home_checkbox)

        # Contour info display
        self.contour_info_label = QLabel("No contours detected")
        self.contour_info_label.setStyleSheet("QLabel { padding: 10px; background-color: #f0f0f0; }")
        contour_layout.addWidget(self.contour_info_label)

        layout.addWidget(contour_group)

        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.update_camera_frame)
        self.detected_contours = None
        self.current_waypoints = None

        # Continuous contour detection mode (enabled by default)
        self.continuous_contour_mode = True

    def _on_threshold_method_changed(self, method):
        """Handle threshold method change - enable/disable relevant controls."""
        is_adaptive = (method == "Adaptive")
        self.adaptive_block_size.setEnabled(is_adaptive)
        self.threshold_value.setEnabled(not is_adaptive)
        self.threshold_value_label.setEnabled(not is_adaptive)

    def _on_live_contour_toggled(self, state):
        """Handle live contour detection toggle."""
        self.continuous_contour_mode = (state == Qt.CheckState.Checked.value)
        if self.continuous_contour_mode:
            self.status_label.setText("Live contour detection enabled")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #cce5ff; font-size: 12px; }")
        else:
            self.status_label.setText("Live contour detection disabled")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #f0f0f0; font-size: 12px; }")

    def update_current_position(self, position, rotation):
        """Update current position display"""
        self.current_x_label.setText(f"X: {position[0]:.2f} mm")
        self.current_y_label.setText(f"Y: {position[1]:.2f} mm")
        self.current_z_label.setText(f"Z: {position[2]:.2f} mm")
        self.current_rx_label.setText(f"rX: {rotation[0]:.2f}°")
        self.current_ry_label.setText(f"rY: {rotation[1]:.2f}°")
        self.current_rz_label.setText(f"rZ: {rotation[2]:.2f}°")

        if self.status_label.text() == "Ready - Waiting for robot data...":
            self.status_label.setText("Ready")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ccffcc; font-size: 12px; }")

    def move_incremental(self, dx, dy, dz, drx, dry, drz):
        """
        Move incrementally - NO computations!
        1. Read current position from MoveIt (it computed FK for us)
        2. Add increment
        3. Send to MoveIt
        """
        try:
            linear_step = float(self.linear_step.text())
            rotation_step = float(self.rotation_step.text())
        except ValueError:
            self.status_label.setText("ERROR: Invalid step size")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffcccc; color: red; font-size: 12px; }")
            return

        # Get current position from MoveIt (it computed FK, we just READ)
        current_x = self.ros_thread.current_position_mm[0]
        current_y = self.ros_thread.current_position_mm[1]
        current_z = self.ros_thread.current_position_mm[2]

        # Calculate new position
        new_x = current_x + dx * linear_step
        new_y = current_y + dy * linear_step
        new_z = current_z + dz * linear_step

        # Determine move type
        is_linear_move = (dx != 0 or dy != 0 or dz != 0)
        is_rotation_move = (drx != 0 or dry != 0 or drz != 0)

        if is_linear_move and not is_rotation_move:
            # Pure XYZ - ALWAYS use HOME orientation (tool down)
            new_rx = -90.0
            new_ry = 0.0
            new_rz = -180.0
        elif is_rotation_move and not is_linear_move:
            # Pure rotation - keep position, modify orientation from current
            new_x = current_x
            new_y = current_y
            new_z = current_z
            current_orientation = self.ros_thread.current_orientation_deg
            new_rx = current_orientation[0] + drx * rotation_step
            new_ry = current_orientation[1] + dry * rotation_step
            new_rz = current_orientation[2] + drz * rotation_step
        else:
            # Combined - use HOME orientation
            new_rx = -90.0
            new_ry = 0.0
            new_rz = -180.0

        # Workspace check - XY reach validation only
        # Z-axis collision with table is now handled automatically by MoveIt
        xy_distance = (new_x**2 + new_y**2)**0.5
        max_reach_mm = 700  # 700mm typical reach for small robot
        if xy_distance > max_reach_mm:
            self.status_label.setText(f"❌ WARNING: Position unreachable! Distance {xy_distance:.0f}mm exceeds max reach {max_reach_mm}mm")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffcccc; color: red; font-size: 12px; }")
            return

        # Send to MoveIt - it does ALL planning/IK/execution AND table collision avoidance
        self.ros_thread.send_cartesian_command(new_x, new_y, new_z, new_rx, new_ry, new_rz)

    def update_speed_scaling(self):
        """Send updated velocity/acceleration scaling to gui_bridge for Pilz planner"""
        try:
            velocity = float(self.velocity_scale.text())
            accel = float(self.accel_scale.text())

            # Clamp to valid range
            velocity = max(0.01, min(1.0, velocity))
            accel = max(0.01, min(1.0, accel))

            # Update display if clamped
            self.velocity_scale.setText(f"{velocity:.2f}")
            self.accel_scale.setText(f"{accel:.2f}")

            # Send to gui_bridge
            self.ros_thread.send_speed_scaling(velocity, accel)
            self.status_label.setText(f"Speed updated: vel={velocity:.2f}, accel={accel:.2f}")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #cce5ff; font-size: 12px; }")
        except ValueError:
            self.status_label.setText("ERROR: Invalid speed scaling values")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffcccc; color: red; font-size: 12px; }")

        move_desc = []
        if dx: move_desc.append(f"X{dx:+.0f}")
        if dy: move_desc.append(f"Y{dy:+.0f}")
        if dz: move_desc.append(f"Z{dz:+.0f}")
        if drx: move_desc.append(f"rX{drx:+.0f}")
        if dry: move_desc.append(f"rY{dry:+.0f}")
        if drz: move_desc.append(f"rZ{drz:+.0f}")

        self.status_label.setText(f"Moving: {' '.join(move_desc)}")
        self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #cce5ff; font-size: 12px; }")

    def send_home_command(self):
        """Send home command"""
        self.ros_thread.send_home_command()
        self.status_label.setText("Moving to HOME position...")
        self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffffcc; font-size: 12px; }")

    def start_camera(self):
        """Start camera capture."""
        camera_id = self.camera_id_spin.value()
        if self.ros_thread.start_camera(camera_id):
            self.camera_start_btn.setEnabled(False)
            self.camera_stop_btn.setEnabled(True)
            self.detect_contours_btn.setEnabled(True)
            self.live_contour_checkbox.setEnabled(True)
            self.init_bg_btn.setEnabled(True)
            self.camera_timer.start(33)  # ~30 FPS
            self.status_label.setText(f"Camera {camera_id} started")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ccffcc; font-size: 12px; }")
        else:
            self.status_label.setText(f"Failed to start camera {camera_id}")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffcccc; font-size: 12px; }")

    def stop_camera(self):
        """Stop camera capture."""
        self.camera_timer.stop()
        self.ros_thread.stop_camera()
        self.camera_start_btn.setEnabled(True)
        self.camera_stop_btn.setEnabled(False)
        self.detect_contours_btn.setEnabled(False)
        self.execute_contours_btn.setEnabled(False)
        self.live_contour_checkbox.setEnabled(False)
        self.live_contour_checkbox.setChecked(False)
        self.init_bg_btn.setEnabled(False)
        self.clear_bg_btn.setEnabled(False)
        self.use_bg_subtract_checkbox.setEnabled(False)
        self.use_bg_subtract_checkbox.setChecked(False)
        self.camera_display.setText("No camera feed")
        self.status_label.setText("Camera stopped")
        self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #f0f0f0; font-size: 12px; }")

    def init_background_subtractor(self):
        """Initialize MOG2 background subtractor with selected history."""
        # Get history from combo box
        history_text = self.mog2_history_combo.currentText()
        history = 500 if "500" in history_text else 1000

        if self.ros_thread.init_background_subtractor(history):
            self.bg_status_label.setText(f"✓ MOG2 learning background (history={history}) - Let run for few seconds")
            self.bg_status_label.setStyleSheet("QLabel { padding: 5px; background-color: #ffffcc; font-size: 11px; }")
            self.clear_bg_btn.setEnabled(True)
            self.use_bg_subtract_checkbox.setEnabled(True)
            self.status_label.setText(f"MOG2 initialized - Learning background model...")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #cce5ff; font-size: 12px; }")

            # After a few seconds, update status
            QTimer.singleShot(3000, self._update_mog2_status)
        else:
            self.status_label.setText("Failed to initialize MOG2")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffcccc; font-size: 12px; }")

    def _update_mog2_status(self):
        """Update MOG2 status after learning period."""
        self.bg_status_label.setText("✓ MOG2 ready - Background model learned (adapts continuously)")
        self.bg_status_label.setStyleSheet("QLabel { padding: 5px; background-color: #ccffcc; font-size: 11px; }")
        self.status_label.setText("MOG2 ready - Place objects to detect")
        self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ccffcc; font-size: 12px; }")

    def clear_background(self):
        """Clear the MOG2 background model."""
        self.ros_thread.clear_background()
        self.bg_status_label.setText("MOG2 not initialized - Click 'Initialize' to learn background")
        self.bg_status_label.setStyleSheet("QLabel { padding: 5px; background-color: #f0f0f0; font-size: 11px; }")
        self.clear_bg_btn.setEnabled(False)
        self.use_bg_subtract_checkbox.setEnabled(False)
        self.use_bg_subtract_checkbox.setChecked(False)
        self.status_label.setText("MOG2 cleared")
        self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #f0f0f0; font-size: 12px; }")

    def update_camera_frame(self):
        """Update camera display with latest frame."""
        frame = self.ros_thread.capture_frame()
        if frame is not None:
            # If live contour detection is enabled, process frame with contour detection
            if self.continuous_contour_mode:
                # Get current threshold parameters
                method = self.threshold_method.currentText().lower()
                threshold_params = {
                    'method': method,
                    'kernel_size': self.kernel_size_spin.value(),
                    'threshold_value': self.threshold_value.value(),
                    'adaptive_block_size': self.adaptive_block_size.value(),
                    'adaptive_c': 2,
                    'invert': self.invert_threshold.isChecked(),
                    'use_morphology': self.use_morphology.isChecked(),
                    'min_area': self.min_contour_area.value(),
                    # Advanced filtering
                    'use_background_subtraction': self.use_bg_subtract_checkbox.isChecked(),
                    'remove_background': self.remove_background.isChecked(),
                    'detect_shadows': self.detect_shadows.isChecked(),
                    'remove_border': self.remove_border.isChecked(),
                    'border_margin': self.border_margin.value(),
                    'filter_convexity': self.filter_convexity.isChecked(),
                    'min_convexity': self.min_convexity.value()
                }

                # Detect contours and get processed frame
                processed_frame, contours = self.ros_thread.detect_contours(frame, threshold_params)

                # Store detected contours for potential execution
                self.detected_contours = contours

                # Use processed frame with contours drawn
                frame_to_display = processed_frame
            else:
                # Just show raw camera feed
                frame_to_display = frame

            # Convert BGR to RGB
            rgb_frame = cv2.cvtColor(frame_to_display, cv2.COLOR_BGR2RGB)

            # Convert to QImage
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)

            # Scale to display size
            scaled_pixmap = QPixmap.fromImage(qt_image).scaled(
                self.camera_display.width(),
                self.camera_display.height(),
                Qt.AspectRatioMode.KeepAspectRatio
            )

            self.camera_display.setPixmap(scaled_pixmap)

    def detect_contours(self):
        """Detect contours in current camera frame and generate waypoints."""
        # If live mode is on, use already-detected contours
        if self.continuous_contour_mode and self.detected_contours is not None:
            contours = self.detected_contours
        else:
            # Manual detection - capture and process frame
            frame = self.ros_thread.capture_frame()
            if frame is None:
                self.status_label.setText("No camera frame available")
                return

            # Get parameters from GUI controls
            method = self.threshold_method.currentText().lower()
            threshold_params = {
                'method': method,
                'kernel_size': self.kernel_size_spin.value(),
                'threshold_value': self.threshold_value.value(),
                'adaptive_block_size': self.adaptive_block_size.value(),
                'adaptive_c': 2,
                'invert': self.invert_threshold.isChecked(),
                'use_morphology': self.use_morphology.isChecked(),
                'min_area': self.min_contour_area.value(),
                # Advanced filtering
                'use_background_subtraction': self.use_bg_subtract_checkbox.isChecked(),
                'remove_background': self.remove_background.isChecked(),
                'detect_shadows': self.detect_shadows.isChecked(),
                'remove_border': self.remove_border.isChecked(),
                'border_margin': self.border_margin.value(),
                'filter_convexity': self.filter_convexity.isChecked(),
                'min_convexity': self.min_convexity.value()
            }

            # Detect contours
            processed_frame, contours = self.ros_thread.detect_contours(frame, threshold_params)
            self.detected_contours = contours

            # Display processed frame with contours (only if not in live mode)
            if not self.continuous_contour_mode:
                rgb_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                scaled_pixmap = QPixmap.fromImage(qt_image).scaled(
                    self.camera_display.width(),
                    self.camera_display.height(),
                    Qt.AspectRatioMode.KeepAspectRatio
                )
                self.camera_display.setPixmap(scaled_pixmap)

        # Convert contours to waypoints
        try:
            pixel_scale = float(self.pixel_scale_input.text())
            cam_center_x = float(self.camera_center_x.text())
            cam_center_y = float(self.camera_center_y.text())
            z_height = float(self.working_z.text())
            min_area = self.min_contour_area.value()

            # Generate contour waypoints (uses fixed HOME orientation internally)
            contour_waypoints = self.ros_thread.contours_to_waypoints(
                contours,
                pixel_scale,
                (cam_center_x, cam_center_y),
                z_height,
                min_area
            )

            # Prepend Z-positioning waypoint
            # Move to target Z height at current XY position first
            if len(contour_waypoints) > 0:
                # Create Z-positioning waypoint using first waypoint's XY but current Z approach
                z_prep_waypoint = Pose()

                # Get current position from LOCAL tracking (no FK!)
                current_x = self.ros_thread.current_position_mm[0] / 1000.0  # mm to meters
                current_y = self.ros_thread.current_position_mm[1] / 1000.0

                # Use current XY, target Z height
                z_prep_waypoint.position.x = current_x
                z_prep_waypoint.position.y = current_y
                z_prep_waypoint.position.z = z_height  # Target working height

                # ALWAYS use fixed HOME orientation (tool pointing down)
                from scipy.spatial.transform import Rotation as R
                fixed_orientation = [-90.0, 0.0, -180.0]  # HOME orientation
                rot = R.from_euler('xyz', fixed_orientation, degrees=True)
                quat = rot.as_quat()
                z_prep_waypoint.orientation.x = quat[0]
                z_prep_waypoint.orientation.y = quat[1]
                z_prep_waypoint.orientation.z = quat[2]
                z_prep_waypoint.orientation.w = quat[3]

                # Insert Z-prep waypoint at the beginning
                waypoints = [z_prep_waypoint] + contour_waypoints
                self.ros_thread.node.get_logger().info(f'Added Z-positioning waypoint: moving to Z={z_height}mm first')
            else:
                waypoints = contour_waypoints

            self.current_waypoints = waypoints

            # Update info
            num_contours = len([c for c in contours if cv2.contourArea(c) >= 100])
            num_waypoints = len(waypoints)
            self.contour_info_label.setText(
                f"Detected {num_contours} contours → {num_waypoints} waypoints"
            )

            if num_waypoints > 0:
                self.execute_contours_btn.setEnabled(True)
                self.status_label.setText(f"Ready to execute {num_waypoints} waypoints")
                self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #cce5ff; font-size: 12px; }")
            else:
                self.execute_contours_btn.setEnabled(False)
                self.status_label.setText("No valid contours found")
                self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffffcc; font-size: 12px; }")

        except ValueError as e:
            self.status_label.setText(f"Parameter error: {e}")
            self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffcccc; font-size: 12px; }")

    def execute_contour_path(self):
        """Execute the contour path with detected waypoints."""
        if self.current_waypoints is None or len(self.current_waypoints) == 0:
            self.status_label.setText("No waypoints to execute")
            return

        # Set flag if auto-home is enabled
        if self.auto_home_checkbox.isChecked():
            self.ros_thread.pending_home_after_waypoints = True

        # Send waypoint batch to GUI bridge
        self.ros_thread.send_waypoint_batch(self.current_waypoints)

        self.status_label.setText(f"Executing contour path with {len(self.current_waypoints)} waypoints...")
        self.status_label.setStyleSheet("QLabel { padding: 10px; background-color: #ffffcc; font-size: 12px; }")

        # Disable button during execution
        self.execute_contours_btn.setEnabled(False)

        # Re-enable button after estimated time (for UI feedback only)
        expected_time_ms = len(self.current_waypoints) * 2000 + 5000
        QTimer.singleShot(expected_time_ms, lambda: self.execute_contours_btn.setEnabled(True))


    def closeEvent(self, event):
        """Clean up on window close"""
        self.ros_timer.stop()
        if hasattr(self, 'camera_timer'):
            self.camera_timer.stop()
        self.ros_thread.stop_camera()
        if self.ros_thread.node:
            self.ros_thread.node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
        event.accept()


def main():
    app = QApplication(sys.argv)
    gui = CartesianGUI()
    gui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

