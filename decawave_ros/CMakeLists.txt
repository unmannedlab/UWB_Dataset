cmake_minimum_required(VERSION 2.8.3)
project(decawave_ros)

## Find catkin macros and libraries
find_package( catkin REQUIRED COMPONENTS 
              message_generation 
              std_msgs 
              geometry_msgs)

##################
## Run setup.py ##
##################
catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

# Generate messages in the 'msg' folder
add_message_files(
  DIRECTORY msg
  FILES
  uwb_distance.msg
  anchor.msg
  tag.msg
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)


###################################
## catkin specific configuration ##
###################################

# Declare things to be passed to dependent projects
catkin_package(
  CATKIN_DEPENDS 
  message_runtime
  std_msgs
)

###########
## Build ##
###########

# Specify additional locations of header files
include_directories()
