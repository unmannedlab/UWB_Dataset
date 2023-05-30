<h1>WiDEVIEW: An UltraWideBand and Vision Dataset for Deciphering Pedestrian-Vehicle Interactions</h1>
<p align="center">
<a href="https://www.tamu.edu/"><img src="images/tamu_logo.png" alt="Texas A&M University" height="90px" width="450px"></a>&emsp;&emsp;&emsp;&emsp;<a href="https://www.hyundai.com/worldwide/en/"><img src="images/Hyundai_logo.png" alt="Hyundai Motor Company" height="90px" width="270px"></a></p>
<p align="center">
Jia Huang<sup>1</sup>, Alvika Gautam<sup>1</sup>, Junghun Choi<sup>2</sup> and Srikanth Saripalli<sup>1</sup><br>
1. <a href="https://www.tamu.edu/">Texas A&M University; </a>&emsp;2. <a href="https://www.hyundai.com/worldwide/en/">Hyundai Motor Company</a><br>
</p>

## Overview

### Recording Platform
* [Polaris GEM e6](https://autonomoustuff.com/)

### Sensor Setup
* One 32 Channels Lidar: [Velodyne Ultra Puck](https://velodynelidar.com/vlp-32c.html)
* Three point grey RGB Cameras: [TBA]() 
* Inertial Navigation System (GPS/IMU): [Vectornav VN-300 Dual Antenna GNSS/INS](https://www.vectornav.com/products/vn-300)
* Ultra-Wideband sensors(UWB): [Decawave (now Qorvo) modules (TREK 1000 RTLS evaluation kit with DW 1000 UWB chip configured as 4 Anchors and 6 Tags](https://www.qorvo.com/products/p/DWM1000)

![Sensor Setup Illustration](./images/golfcar_annotated_v3__med.png)


## Folder structure

<pre>
WiDEVIEW
├── 
├── 
├── 
├── 
├── 
├── 
├── 
      ├──             
      ├──      
      ├──
      ├── 
      ├── 
      ├── 
      ├── 
      ├── 
      └── 
</pre>

## Annotated Data:
The dataset contains 30936 frames which come from the front three cameras with 10312 frames each. Every 5-th frame was annotated manually and carefully in [Computer Vision Annotation Tool (CVAT)](https://github.com/opencv/cvat/) for the front middle camera frames while the ones in between are interpolated automatically without adjustment. There are a total of 8368 bounding boxes manually annotated for pedestrians and cyclists along with six tag IDs for those who carried tags, and 33239 bounding boxes are interpolated in CVAT. These annotations are exported in MOT 1.1 format for the following multi-object tracking task evaluation for images. The annotations for the left and right cameras frames are in progress and will be updated on the Github gradually.

### Images Statics:


### Image Download:


### Calibration Download:
The sensor suite cameras (left, middle and right on the autonomous shuttle roof rack) have a 30$^{\circ}$ overlapping field of view between adjacent cameras. The intrinsic and extrinsic camera parameters are estimated by the multiple camera calibration tool in the [Kalibr toolbox](https://github.com/ethz-asl/kalibr.git). A 6 x 6 aprilgrid target with spacing of 0.03m is used. We utilize a pinhole projection model for our cameras, where a three-dimensional scene is projected onto an image plane through a perspective transform. The calibration details can be found in the folder [UWB-gcart-camera-calibration](https://github.com/unmannedlab/UWB_Dataset/tree/main/UWB-gcart-camera-calibration).

## Benchmarks
### 2D object Detection and Tracking
Case | HOTA | MOTA | MOTP | IDF1 | FP | FN | ID Sw. | Recall | Precision | Dets | GT Dets | IDs | GT IDs | 
-----| ---- | ---- |------|------|----|----|--------| -------|-----------|------|---------|-----|--------|
1| 41.577 | 42.046  | 72.496  |  54.958  | 9144 | 11006  |  729  | 69.451 | 73.236 | 34165 | 36027 | 491 | 231 |
2| 45.873 | 44.204 | 78.173 | 57.293 | 1607 | 2038 | 398 | 71.874  | 76.42 | 6815 | 7246 | 425| 231|

### Benchmark Reproduction

To reproduce the results, please refer to [here](./benchmarks/README.md)

## ROS Bag Raw Data

Data included in raw ROS bagfiles:

Topic Name | Message Tpye | Message Descriptison
------------ | ------------- | ---------------------------------
/Decawave | decawave_ros/uwb_distance | 
/left/image_raw | sensor_msgs/Image | Images from the left camera        
/middle/image_raw | sensor_msgs/Image | Images from the middele camera         
/right/image_raw | sensor_msgs/Image | Images from the right camera        
/vectornav/fix | sensor_msgs/NavSatFix |  
/vectornav/gps | vn300/gps | INS data from VectorNav-VN300                
/vectornav/imu | vn300/sensors | Imu data from VectorNav-VN300            
/vectornav/ins | vn300/ins |                
/velodyne_points | sensor_msgs/PointCloud2 | PointCloud produced by the Velodyne Lidar


### ROS Bag Download
The following are the links for the ROS Bag files.

**Sequence 1**: ([12GB](https://drive.google.com/file/d/1bIb-6fWbaiI9Q8Pq9paANQwXWn7GJDtl/view?usp=sharing)) 
[![Sequence 1 Video](.jpg)](https://www.youtube.com/watch?v=Qc7IepWGKr8)


