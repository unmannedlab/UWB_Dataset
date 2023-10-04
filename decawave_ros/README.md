# decawave_ros

This is a ROS python package for interfacing with the DecaWave TREK1000 modules. This package includes a python package that can parse the TREK1000 serial messages and a basic script to evaluate the module. Currently, the node only publishes the received distance measurements from the anchors/tags. Future work will include incorportating localization filter nodes.  

## Quickstart

Clone the package to your catkin workspace<br>
`git clone https://github.com/unmannedlab/decawave_ros.git`

Build the packages in catkin workspace<br>
```
cd ~/catkin_ws
catkin_make
```

Start the ROS core service<br>
`roscore`

Launch the publisher<br>
`roslaunch decawave_ros decawave_publisher.launch`

