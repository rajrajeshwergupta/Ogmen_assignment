## Bot_world
This package contains Custom gazebo world and launch file to laod world in gazebo.

## Package Structure

```
ros_bot_description/
├── launch/            # Conatains Launch file for gazebo and load the world and spawn urdf in gazebo centre.
└── world/             # Gazebo world
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

### 4. Teleop the robot in gazebo using Keyboard
   ```bash
   ros2 launch bot_description control.launch.py
   ```
   This starts the teleop_twist_keyboard package 
    **NOTE: Keep the terminal running front while running the robot in gazebo**
