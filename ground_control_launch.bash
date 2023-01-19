#!/bin/bash

# Arguments
drone_namespace="drone0"
use_sim_time=false

# ros2 launch as2_keyboard_teleoperation as2_keyboard_teleoperation_launch.py drone_id:=$drone_namespace use_sim_time:=$use_sim_time verbose:=false &

ros2 run as2_alphanumeric_viewer as2_alphanumeric_viewer_node --ros-args -r  __ns:=/$drone_namespace
