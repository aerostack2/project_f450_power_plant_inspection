#!/bin/python3

from time import sleep
import rclpy
from as2_python_api.drone_interface_gps import DroneInterfaceGPS as DroneInterface
from as2_msgs.msg import YawMode


def drone_run(drone_interface: DroneInterface):

    speed = 2.0
    takeoff_height = 1.0
    height = 2.0

    sleep_time = 2.0
    yaw_mode = YawMode()
    yaw_mode.mode = YawMode.PATH_FACING

    dim = 2.0
    path = [
        [dim, dim, height],
        [dim, -dim, height],
        [-dim, dim, height],
        [-dim, -dim, height],
        [0.0, 0.0, takeoff_height],
    ]

    print("Start mission")

    ##### ARM OFFBOARD #####
    drone_interface.offboard()
    drone_interface.arm()

    ##### TAKE OFF #####
    print("Take Off")
    drone_interface.takeoff(takeoff_height, speed=1.0)
    print("Take Off done")
    sleep(sleep_time)

    ##### LAND #####
    print("Landing")
    drone_interface.land(speed=0.5)
    print("Land done")

    drone_interface.disarm()


if __name__ == '__main__':
    rclpy.init()
    # Get environment variable AEROSTACK2_SIMULATION_DRONE_ID
    uav_name = "drone_sim_0"
    uav = DroneInterface(uav_name, verbose=False, use_sim_time=True)

    drone_run(uav)

    uav.shutdown()
    rclpy.shutdown()

    print("Clean exit")
    exit(0)
