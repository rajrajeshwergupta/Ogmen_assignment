## Bot_control
This package conatains the script to remap the lidar data.

## Package Structure

```
ros_bot_description/
├── launch/            # Conatains Launch file launching remapping executable
└── src/              # scripts
└── README.md          # Instructions for the package
```


## Instructions

### 1. Setting Up the Repository
   Build the workspace:
   ```bash
   cd ~/test_ws/
   colcon build
   source install/setup.bash
   ```

### 2. Visulaize the robot in Rviz
  ```bash
   ros2 launch bot_description rviz.launch.py
   ```
   This brings up the robot in Rviz and launch robot_state_publishers, publishing joints and links on /robot_description

### 3. Load gazebo world and spawn URDF in centre
   ```bash
   ros2 launch bot_world simulation.launch.py
   ```
   This will laod the URDF of robot model in Gazebo world.

### 4. Launch lase_filter to get filtered data on /filtered_scan
   ```bash
    ros2 launch bot_control laser_filter_launch.py
   ```

### 5. Teleop the robot in gazebo using Keyboard
   ```bash
   ros2 launch bot_description control.launch.py
   ```
   This starts the teleop_twist_keyboard package 
    **NOTE: Keep the terminal running front while running the robot in gazebo**

