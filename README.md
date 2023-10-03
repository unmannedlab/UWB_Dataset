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

### Annotations  and Annotation tasks (include original videos) Download:
Annotations include raw images in the img1 folder, annotation tasks include the raw videos named output.mp4 used for annotation in CVAT.

#### Annotation folder structure
<pre>
rosbag_filename(subfolder_middle_annotation).zip
├── gt
      ├── gt.txt           
      └── labels.txt 
├── img1
      ├── 000001.PNG          
      ├── 000002.PNG     
      └── ......
</pre>

Example of rosbag_filename(subfolder_middle_annotation).zip : 2023-02-04-16-04-35_0(1_middle_annotation)

#### Annotation task folder structure
<pre>
rosbag_filename(subfolder_middle_task).zip
├── annotations.json
├── task.json
├── data
      ├── index.json          
      ├── manifest.jsonl     
      └── output.mp4
</pre>

Example of rosbag_filename(subfolder_middle_task).zip : 2023-02-04-16-04-35_0(1_middle_task)

**Sequence 1_1: 2023-02-04-16-04-35_0.bag**: ([Annotation](https://drive.google.com/file/d/1LsmbA9JuGuIn2_gIiLig2MAjlx8LoV9u/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1qSWWbyzMAGpsMCUhW_IvBYoL85QEgz0a/view?usp=share_link)) 

**Sequence 1_2: 2023-02-04-16-04-35_0.bag**: ([Annotation](https://drive.google.com/file/d/1TCfUw0TQ-ouDZh70veOrVEDGhan37P2e/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1JeP_fu3MVKpbrNlCa5-AFKTfvY3gaMPK/view?usp=share_link))

**Sequence 2: 2023-02-10-15-23-44_0.bag**: ([Annotation](https://drive.google.com/file/d/10I79KbHd-jaw5HL7077-nW3pb5vjlru6/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1w4uGxJtGEkMPCmc1jjzsjC4V7NfZ-kG4/view?usp=share_link))

**Sequence 3_1: 2023-02-10-15-26-14_1.bag**:([Annotation](https://drive.google.com/file/d/1GECn_9_ScWeZSdkJvUyunW9NcgwyL-Zx/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1-7doOtX5VA3rKVP2AipF-3fWFMREdfj4/view?usp=share_link))

**Sequence 3_2: 2023-02-10-15-26-14_1.bag**:([Annotation](https://drive.google.com/file/d/1g25FNvCcM3B1ETdu_t0lVEecV7xyte-h/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1xcNCIm5iryk6TPbWWCBrIAEt2v-oMVWD/view?usp=share_link))

**Sequence 4: 2023-02-10-15-28-44_2.bag**: ([Annotation](https://drive.google.com/file/d/1CyNSEGC6Cp8BSbOohmVM53X1JA5mbwT8/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1MjOCwx9bqJs0DlB-mHIm4wu2isEeiWNi/view?usp=share_link))

**Sequence 5_1: 2023-02-10-15-35-56_0.bag**: ([Annotation](https://drive.google.com/file/d/1-noXvdEMBUDyivlWhwxi8Ra0vYkwYvGu/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1I7e1_X1MyF5m03Xp_joT2p1DusQOGhdQ/view?usp=share_link))

**Sequence 5_2: 2023-02-10-15-35-56_0.bag**: ([Annotation](https://drive.google.com/file/d/1Mx3yRENpXvoFm2Wr6xYng78B8bqnrITT/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1tjqMpzWYwPktBRt_JC6QnKzbtPXnhEgB/view?usp=share_link))

**Sequence 6: 2023-02-10-15-38-30_0.bag**: ([Annotation](https://drive.google.com/file/d/1AmisAnvkJijHN7ZyUNc_h6qoUmJ_TYN0/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1sNU0yB9LkP5Y9ltCBn5m0AAlbfuupEH-/view?usp=share_link))

**Sequence 7: 2023-02-12-13-59-09_0.bag**: ([Annotation](https://drive.google.com/file/d/1zfPpB2A7WdJgCcBcFtXIsW01Ql-uLK34/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1AoPFfQRIqsiVBF1_RyZfdOdwAvgw_a9Q/view?usp=share_link))

**Sequence 8: 2023-02-12-14-13-00_0.bag**: ([Annotation](https://drive.google.com/file/d/1StObC9cAjsA7ttuguH5-0KNHO7wzt7d8/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1O5PxlbKu__c_l9mxyu3Nck2BWkg_sa7f/view?usp=share_link))

**Sequence 9: 2023-02-12-14-14-40_0.bag**: ([Annotation](https://drive.google.com/file/d/1guySPOC5Pcy0vOqpO0kB4_wD4aUsLYR5/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1WX8n6XQXC67cPSrbKWj-dqXV1GXqDfWo/view?usp=share_link))

**Sequence 10:2023-02-12-14-20-14_0.bag**: ([Annotation](https://drive.google.com/file/d/1M8uYpmS-Q8eS4eyJ1z51zaS7nGGNDedO/view?usp=share_link)) ([Task](https://drive.google.com/file/d/17rmr_QyuoH2AckeLOtLef0ZYnRx_jTPr/view?usp=share_link))

**Sequence 11:2023-02-12-14-24-09_0.bag**: ([Annotation](https://drive.google.com/file/d/1VBxiZXEG5ZJ0ea9brwuzfYJkH-y4rn12/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1N7R-zuxFgyASX-yvBQOzF3LyGpRzWx0s/view?usp=share_link))

**Sequence 12:2023-02-12-14-25-15_0.bag**: ([Annotation](https://drive.google.com/file/d/1hHHW9LqBvi22J9qPVtxzWvhtEpX_0Aip/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1gOHyPplGr-UAaAQCBq7ei_MrphfPuxEN/view?usp=share_link))

**Sequence 13:2023-02-12-14-31-29_0.bag**: ([Annotation](https://drive.google.com/file/d/1URv1pL3FI9otXiFcENDAyhqcRGXXg7W0/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1WqyaDFnfAWn_pDT3ZWwCFO8Eh7VH4hvq/view?usp=share_link))

**Sequence 14:2023-02-17-15-40-11_0.bag**: ([Annotation](https://drive.google.com/file/d/1uiMv20VU3-uyos-0qwqVAkce6haIaVUd/view?usp=share_link)) ([Task](https://drive.google.com/file/d/14AlhnkG9j2XQll1p6TME6fOtU9VVlVGr/view?usp=share_link))

**Sequence 15:2023-02-17-15-42-27_0.bag**: ([Annotation](https://drive.google.com/file/d/1ZRgONHIcYv7fW8wMBPQY72r5LDWT3R8t/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1KNmULjNgm_qPIh_D-_Q0aYOb2YJCrigX/view?usp=share_link))

**Sequence 16:2023-02-17-15-44-23_0.bag**: ([Annotation](https://drive.google.com/file/d/1rCGH_zJmtOjIF0Kj-Bqlq9EEOVTOCf7X/view?usp=share_link)) ([Task](https://drive.google.com/file/d/11AMyQU1SXBmvqVRVvX6fBAGoXTtRZvAr/view?usp=share_link))

**Sequence 17:2023-02-17-16-00-23_0.bag**: ([Annotation](https://drive.google.com/file/d/1HvPEdnR0_H9Ocwu9FpDnoDM10MASPy3O/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1ivXXXg5_dv2Q4CR48pnR9WjjTow8Zdr2/view?usp=share_link))

**Sequence 18_1:2023-02-17-16-53-27_0.bag**: ([Annotation](https://drive.google.com/file/d/1jqOvKDczeIFeVP3htUCVMPVeEFGMJUtR/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1A_dAVGhpxs92buIVOKPvvoZQN8eI_Pjk/view?usp=share_link))

**Sequence 18_2:2023-02-17-16-53-27_0.bag**: ([Annotation](https://drive.google.com/file/d/1JH_sk01CWI6a1XIdjbmpbnMQCdaDk92J/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1YJyxO8XqDwD93mn6xBioZfojwFQHtbLu/view?usp=share_link))

**Sequence 19:2023-02-17-16-54-38_0.bag**: ([Annotation](https://drive.google.com/file/d/1BFJzefZZzlSl5TsEIEsf_op3zcNPg80G/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1txbZah34Z9jTI6L3iC-t2rX1MmAeSsjU/view?usp=share_link))

**Sequence 20:2023-02-17-17-01-15_0.bag**: ([Annotation](https://drive.google.com/file/d/1pj-ZQwP4Eifkas7KRY6kUfRlArBNDuA8/view?usp=share_link)) ([Task](https://drive.google.com/file/d/11hFT3vkYhYlg3azLVHuy-lc7GP_4IpyB/view?usp=share_link))

**Sequence 21:2023-02-17-17-03-49_0.bag**: ([Annotation](https://drive.google.com/file/d/1h6BduvwpJZQpFJw0siFgxSWT9LV6IDJ4/view?usp=share_link)) ([Task](https://drive.google.com/file/d/1TDnjRFhmFhlwWZq47bZLR2ggXBjYfwMA/view?usp=share_link))


## Calibration:
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
The ROS bag information can be found on the google drive [link](https://docs.google.com/spreadsheets/d/1O6mdmZg2sbJnEaPZ3xWUrlm8tNaf2nq4JykF0rs8nSA/edit?usp=sharing).
The following are the google drive links for the ROS Bag files.

**Sequence 1: 2023-02-04-16-04-35_0.bag**: ([19.91GB](https://drive.google.com/file/d/1tOMAYwOUGYVq7jfs5F5ZCDDZ7fwEFXc2/view?usp=sharing)) 


**Sequence 2: 2023-02-10-15-23-44_0.bag**: ([19.94GB](https://drive.google.com/file/d/1hmkmC3KwE1jkIi5df38B_hfaE9owscdu/view?usp=sharing))


**Sequence 3: 2023-02-10-15-26-14_1.bag**: ([20.07GB](https://drive.google.com/file/d/1PwoA0ik7FMCpiS4KSIs_cBOI4ol7qva0/view?usp=sharing))

**Sequence 4: 2023-02-10-15-28-44_2.bag**: ([18.42GB](https://drive.google.com/file/d/1Lt28cGu4xsc_9XcvLRnotx-tfjuca-Rw/view?usp=sharing))


**Sequence 5: 2023-02-10-15-35-56_0.bag**: ([7.29GB](https://drive.google.com/file/d/1O3oExGM51-mb4aSCWnL--RHBzU6Bu7AV/view?usp=sharing))


**Sequence 6: 2023-02-10-15-38-30_0.bag**: ([8.04GB](https://drive.google.com/file/d/1yf41QIu9tAkkHrDbitIVVxPuCgrfUB_H/view?usp=sharing))


**Sequence 7: 2023-02-12-13-59-09_0.bag**: ([6.66GB](https://drive.google.com/file/d/1LYnXARNPOa090WUgWJ1pjzvNgOrbJEzv/view?usp=sharing))


**Sequence 8: 2023-02-12-14-13-00_0.bag**: ([5.97GB](https://drive.google.com/file/d/1cw_GAMIQHgyR2AIFBA5sgqe04AZGipq7/view?usp=sharing))


**Sequence 9: 2023-02-12-14-14-40_0.bag**: ([15.71GB](https://drive.google.com/file/d/1pYKhGZqiWrHSZz-BKo94vNBl2uCirPnP/view?usp=sharing))


**Sequence 10:2023-02-12-14-20-14_0.bag**: ([5.69GB](https://drive.google.com/file/d/1H4Ew-PoaRVRCLaKCCCsnr4liDttUcFc6/view?usp=sharing))


**Sequence 11:2023-02-12-14-24-09_0.bag**: ([9.16GB](https://drive.google.com/file/d/1R_eH_XIDQuvs8YTvZscE6_3KZxxSYzCa/view?usp=sharing))


**Sequence 12:2023-02-12-14-25-15_0.bag**: ([8.66GB](https://drive.google.com/file/d/1GtEjVBTcnnAO3vjntoFHLng1el62n7iA/view?usp=sharing))


**Sequence 13:2023-02-12-14-31-29_0.bag**: ([5.59GB](https://drive.google.com/file/d/1IepkUWUAddwscMZQaJOpmNfpt5ulXUvP/view?usp=sharing))


**Sequence 14:2023-02-17-15-40-11_0.bag**: ([4.26GB](https://drive.google.com/file/d/1LRQx3DmVfntgYOqxWzUtRLOWX-OfTJu8/view?usp=sharing))


**Sequence 15:2023-02-17-15-42-27_0.bag**: ([7.53GB](https://drive.google.com/file/d/13ZaLquhE9lTFkY6B1tFXxO_CN73Dz7lj/view?usp=sharing))


**Sequence 16:2023-02-17-15-44-23_0.bag**: ([16.47GB](https://drive.google.com/file/d/1CfOsMuUk0_Qf-EU9b9sQJ3g1TIuD5nmE/view?usp=sharing))


**Sequence 17:2023-02-17-16-00-23_0.bag**: ([7.04GB](https://drive.google.com/file/d/1PQkicEU100fFV-wh5pPPQJz-mP1u9lnM/view?usp=sharing))


**Sequence 18:2023-02-17-16-53-27_0.bag**: ([3.93GB](https://drive.google.com/file/d/1bTUPD8kgx-aMJ4uTabYGc6oRfFZP60rU/view?usp=sharing))


**Sequence 19:2023-02-17-16-54-38_0.bag**: ([6.57GB](https://drive.google.com/file/d/1a-UX6ZzPcFR9m2Pf3m28aDWCP1e4XJGR/view?usp=sharing))


**Sequence 20:2023-02-17-17-01-15_0.bag**: ([6.57GB](https://drive.google.com/file/d/1a-UX6ZzPcFR9m2Pf3m28aDWCP1e4XJGR/view?usp=sharing))


**Sequence 21:2023-02-17-17-03-49_0.bag**: ([4.43GB](https://drive.google.com/file/d/154NPXti0aZ84g5w4pYBAAMYgMdppgl3N/view?usp=sharing))

## Citation
```
@misc{huang2023wideview,
      title={WiDEVIEW: An UltraWideBand and Vision Dataset for Deciphering Pedestrian-Vehicle Interactions}, 
      author={Jia Huang and Alvika Gautam and Junghun Choi and Srikanth Saripalli},
      year={2023},
      eprint={2309.16057},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```



## License
All datasets and code on this page are copyright by us and published under the GNU General Public License v2.0.




