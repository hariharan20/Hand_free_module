# Hand_free_module
This repository contains filles which can be used to make teleoperate robots handsfree
## This project aims to make a attempt of handsfree driving of vehicles

This is ROS based project and also requires the user to have installed ROS-serial module 

Arudino UNO and ultrasonic sensor have been used to test the results of the project.
## To run the project :
### open terminal
##### 1) ```cd ~/catkin_ws/src ```
##### 2) ```git clone https://github.com/hariharan20/Hand_free_module```
##### 3) ```cd .. & catkin_make ```
##### 4) ```roscore```
##### 5) ```rosrun Hand_free_module sent_go.py ```

## The Node graph :
![Image of Node graph](https://github.com/hariharan20/Hand_free_module/blob/main/src/images/rosgraph.png)
