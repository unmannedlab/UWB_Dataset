import rospy
import rosbag

from sensor_msgs.msg import Image, PointCloud2
import sensor_msgs.point_cloud2 as pc2
from decawave_ros.msg import uwb_distance

from cv_bridge import CvBridge
import cv2

import os
import math
from ctypes import * # convert float to uint32
import numpy as np
import open3d as o3d

# Bit operations
BIT_MOVE_16 = 2**16
BIT_MOVE_8 = 2**8
convert_rgbUint32_to_tuple = lambda rgb_uint32: (
    (rgb_uint32 & 0x00ff0000)>>16, (rgb_uint32 & 0x0000ff00)>>8, (rgb_uint32 & 0x000000ff)
)
convert_rgbFloat_to_tuple = lambda rgb_float: convert_rgbUint32_to_tuple(
    int(cast(pointer(c_float(rgb_float)), POINTER(c_uint32)).contents.value)
)

def convertImageFromRosToCV2(ros_img_msg):
    print("Received an image!")
    # Convert your ROS Image message to OpenCV2
    # Instantiate CvBridge
    bridge = CvBridge()
    cv2_img = bridge.imgmsg_to_cv2(ros_img_msg, "bgr8")
    return cv2_img

def convertCloudFromRosToOpen3d(ros_cloud_msg):
    # Get cloud data from ros_cloud msg
    field_names=[field.name for field in ros_cloud_msg.fields]
    # print(field_names)
    cloud_data = list(pc2.read_points(ros_cloud_msg, skip_nans=True, field_names = field_names))

    # Check empty
    open3d_cloud = o3d.geometry.PointCloud()
    if len(cloud_data)==0:
        print("Converting an empty cloud")
        return None

    # Set open3d_cloud
    if "rgb" in field_names:
        IDX_RGB_IN_FIELD=3 # x, y, z, rgb
        
        # Get xyz
        xyz = [(x,y,z) for x,y,z,rgb in cloud_data ] # (why cannot put this line below rgb?)

        # Get rgb
        # Check whether int or float
        if type(cloud_data[0][IDX_RGB_IN_FIELD])==float: # if float (from pcl::toROSMsg)
            rgb = [convert_rgbFloat_to_tuple(rgb) for x,y,z,rgb in cloud_data ]
        else:
            rgb = [convert_rgbUint32_to_tuple(rgb) for x,y,z,rgb in cloud_data ]

        # combine
        open3d_cloud.points = o3d.utility.Vector3dVector(np.array(xyz))
        open3d_cloud.colors = o3d.utility.Vector3dVector(np.array(rgb)/255.0)
    else:
        # print(cloud_data[0])
        xyz = [(x,y,z) for x,y,z,intensity,ring in cloud_data] # get xyz
        open3d_cloud.points = o3d.utility.Vector3dVector(np.array(xyz))

    # return
    return open3d_cloud

bag = rosbag.Bag('/home/jh/Downloads/2023-02-04-16-04-35_0.bag')
start_time_bag = bag.get_start_time()
start_time = rospy.Time(start_time_bag)
time_2 = float(2)
end_time=rospy.Time(start_time_bag+time_2)

image_msgs = []
pc_msgs = []
uwb_msgs = []

image_ts = []
pc_ts = []
uwb_ts = []

# Select image, point cloud and uwb messages and corresponding time stamps 
# from the rosbag by using the appropriate topic names. 
for topic,msg,t in bag.read_messages(topics=['/middle/image_raw','/velodyne_points','/Decawave'],  start_time=start_time, end_time=end_time):
    # print(msg)
    # print(type(msg))
    # t = t-start_time
    if msg._has_header:
        # ts = msg.header.stamp.to_sec()
        ts = math.fabs(msg.header.stamp.to_sec()-start_time.to_sec())
        if topic == "/middle/image_raw": 
            # print("image_ts",ts)
            image_ts.append(ts)
            image_msgs.append(msg)
            
        elif topic == "/velodyne_points":
            # print("lidar_ts",ts)
            pc_ts.append(ts)
            pc_msgs.append(msg)

        elif topic == '/Decawave':
            print('uwb_ts',ts)
            uwb_ts.append(ts)
            uwb_msgs.append(msg)

# print(len(image_msgs))
# print(len(pc_msgs))
print(len(uwb_msgs))

# For accurate calibration, images and point clouds must be captured with
# the approximate timestamps.  
idx = []
if len(pc_ts)>len(image_ts):
    for i in range(len(image_ts)):
        val = min(abs(image_ts[i]-np.array(pc_ts)))
        if val <=0.1:
            indx = np.argmin(abs(image_ts[i]-np.array(pc_ts)))
            idx.append([i,indx])
   
else:
    for i in range(len(pc_ts)):
        val = min(abs(pc_ts[i]-image_ts))
        if val <=0.1:
            indx = np.argmin(abs(pc_ts[i]-np.array(image_ts)))
            idx.append([indx,i])

idx = np.array(idx).reshape((-1,2))
# print(idx)

# Create directories to save the valid images and point clouds.
pc_path = '/home/jh/Downloads/pc'
image_path = '/home/jh/Downloads/image'
uwb_path = '/home/jh/Downloads/uwb'

for path in [pc_path,image_path,uwb_path]:
    if not os.path.exists(path):
        os.makedirs(path)
        print("Directory created successfully!")
    else:
        print("Directory already exists!")

# Extract the images and point clouds. Name and save the files in their 
# respective folders. Save corresponding image and point clouds under the 
# same number.
for i in range(len(idx)):
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(image_msgs[idx[i,0]], "bgr8")
    cv2.imwrite(image_path+'/'+'{:04d}'.format(i)+'.jpeg', img)
    
    np_pcd = np.array(list(pc2.read_points(pc_msgs[idx[i,1]])), dtype=np.float32)[:, 0:3]
    pcd = o3d.geometry.PointCloud()
    v3d = o3d.utility.Vector3dVector
    pcd.points = v3d(np_pcd)
    o3d.io.write_point_cloud(pc_path+'/' + '{:04d}'.format(i)+ '.pcd', pcd)

    # #OR use functions to save image and point cloud data
    # img = convertImageFromRosToCV2(image_msgs[idx[i,0]])
    # cv2.imwrite(image_path+'/'+'{:04d}'.format(i)+'.jpeg', img)

    # pcd = convertCloudFromRosToOpen3d(pc_msgs[idx[i,1]])
    # o3d.io.write_point_cloud(pc_path+'/' + "{:04d}".format(i) + '.pcd', pcd)
    
bag.close()
