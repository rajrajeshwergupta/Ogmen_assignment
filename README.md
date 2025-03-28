# Robot Software Engineer Intern - Coding Round
---

## Overview
This repository contains packages for different tasks and conatins all required launch files and URDF and scripts. To test this package first clone this repo all packages and build this in your workspace.

## Repository Structure

```
Ogmen_assignment/
├── bot_description/
│   ├── launch/            # Conatains Launch file for rviz, spwaner in gazebo and teleop using Keyboard
│   ├── urdf/            # URDF files for bot
│   └── README.md/            # Instructions for the package
├── bot_contol/
│   ├── launch/            # Conatains Launch file launching remapping executable
│   ├── src/              # scripts
│   └── README.md          # Instructions for the package
├── bot_world/
│   ├── launch/            # Conatains Launch file for gazebo and load the world and spawn urdf in gazebo centre.
│   └── world/             # Gazebo world
|   └── README.md          # Instructions for the package
└── README.md              # Instructions for the assignment
```

## System Requirements

- ROS2 Humble installed.
- Gazebo simulator (version 11.10.2 is compatible with ROS2 Humble).

## Instructions

### 1. Setting Up the Repository
1. Create your workspace:
    ```bash
    mkdir -p ~/assignment_ws/src
    ```
2. Clone this repository:
   ```bash
   cd ~/assignment_ws/src
   git clone <repository-url>
   ```
2. Build the workspace:
   ```bash
   cd ~/assignment_ws/
   colcon build
   source install/setup.bash
   ```

### 2. Visulaize the robot in Rviz
   ```bash
   ros2 launch bot_description rviz.launch.py
   ```
   This brings up the robot in Rviz.

### 3. Load gazebo world and spawn URDF in centre
   ```bash
   ros2 launch bot_world simulation.launch.py
   ```
   This will load the URDF of robot model in Gazebo world.

### 4. Launch laser_filter to get filtered data on /filtered_scan
   ```bash
    ros2 launch bot_control laser_filter_launch.py
   ```

### 5. Teleop the robot in gazebo using Keyboard
   ```bash
   ros2 launch bot_description control.launch.py
   ```
   This starts the teleop_twist_keyboard package.
    **NOTE: Keep the terminal running front while running the robot in gazebo**

## 6. Changes in RVIZ for visualization
- Add LaseScan in rviz and subscribe to topics /scan and /filtered_scan to visulaize laser data.
- Change fixed_frame to odom to visulaize robot motion in rviz.
- Increase size in LaserScan approx to 0.05 for better visulaization of laser data.

## 7. Note:
These instruction will help you to launch the robot in rviz and gazebo and filter lidar data while controlling with teleop_twist_keyboard. Each package has own `README.md` file please refer those for particular functinalities.