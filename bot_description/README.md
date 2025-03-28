## Bot_description
Conatains bot description urdf and required launch files.

## Package Structure

```
ros_nav2_assignment/
├── bot_description/
│   ├── launch/            # Conatains Launch file for rviz, spwaner in gazebo and teleop using Keyboard
│   └── urdf/              # URDF files for bot
└── README.md              # Instructions for the package
```


## Instructions

### 1. Setting Up the Repository
1. Create your workspace:
    ```bash
    mkdir -p ~/test_ws/src
    ```
2. Clone this repository:
   ```bash
   cd ~/test_ws/src
   git clone <repository-url>
   ```
2. Build the workspace:
   ```bash
   cd ~/test_ws/
   colcon build
   source install/setup.bash
   ```

### 2. Visulaize the robot in Rviz
1.  ```bash
   ros2 launch bot_description rviz.launch.py ```
   
   This brings up the robot in Rviz.

### 3. Load the URDF in Gazebo empty world
1.  ```bash
   ros2 launch bot_description spawn.launch.py```
   
   This will laod the URDF of robot model in Gazebo empty world.

### 4. Teleop the robot in gazebo using Keyboard
1.  ```bash
   ros2 launch bot_description control.launch.py
   ```
   This starts the teleop_twist_keyboard package 
    **NOTE: Keep the terminal front while running the robot in gazebo**
