<center><font size=7>   Udacity Self-Driving Car Engineer Nanodegree  </font>  </center>
<center> Shuai Wang </center>
<center>USTC, February 1, 2020



![car2](./assets/car2.jpg)



<center> <font color=blue> Copyright (c) 2020 Shuai Wang. All rights reserved. </font> </center>
---

In this repository I will share the **source code** of all the projects of **[Udacity Self-Driving Car Engineer Nanodegree](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013)**.  

# Projects  

## Term 1: Computer Vision and Deep Learning

----

![term1](./assets/term1.jpg)

| [Getting Started for Term 1](./term1_How_to_get_started)       | [![T1P1](./term1_project1_lane_finding/results/white_giphy.gif)](./term1_project1_lane_finding/results/white.webm)<br>**Project 1:<br>Finding Lane Lines on the road**<br>[Code](./term1_project1_lane_finding)       | ![T1P2](./term1_project2_traffic_sign_classifier/img/traffic_sign_02.jpg)<br>**Project 2:<br>Traffic Sign Classifier**<br>[Code](./term1_project2_traffic_sign_classifier)       |
| :---:         |     :---:      |          :---: |
| [![T1P3](./term1_project3_behavioral_cloning/results/p3_behavioral_cloning_21s.gif)](./term1_project3_behavioral_cloning/results/p3_behavioral_cloning.webm)<br>**Project 3:<br>Behavioral Cloning**<br>[Code](./term1_project3_behavioral_cloning)       | [![T1P4](./term1_project4_advanced_lane_finding/results/P4_adv_lane_lines_project_video.gif)](./term1_project4_advanced_lane_finding/results/P4_adv_lane_lines_project_video.webm)<br>**Project 4:<br>Advanced Lane Finding**<br>[Code](./term1_project4_advanced_lane_finding)       |[![T1P5](./term1_project5_vehicle_detection/results/p5_vehicle_detection.gif)](./term1_project5_vehicle_detection/results/p5_vehicle_detection.mp4)<br>**Project 5:<br>Vehicle Tracking**<br>[Code](./term1_project5_vehicle_detection)|


### [P1 - Finding Lane Lines on the road](./Term1/term1_project1_lane_finding)
 - **Summary:** Detect lane lines on a highway within a video stream. Use OpencV image analysis techniques to identify lines of different colors.
 - **Keywords:** Python, Computer Vision, Hough Transforms, Canny edge detection


### [P2 - Traffic Sign Classification](./Term1/term1_project2_traffic_sign_classifier)
 - **Summary:** Build and train a deep neural network to classify traffic signs, using TensorFlow. Experiment with different network architectures. Performe image pre-processing and validation to guard against overfitting.
 - **Keywords:** Python, Deep Learning, Convolutional Neural Networks, TensorFlow, Overfitting, Generalisation, Augmentation, Optimizer

### [P3 - Behavioral Cloning](./Term1/term1_project3_behavioral_cloning)
 - **Summary:** Build and train a convolutional neural network for end-to-end driving in a simulator, using TensorFlow and Keras. Use optimization techniques such as data augmentation and dropout to generalize the network for driving on multiple tracks.
 - **Keywords:** Python, Deep Learning, Keras, Convolutional Neural Networks, Generalisation


### [P4 - Advanced Lane Finding](./Term1/term1_project4_advanced_lane_finding)
 - **Summary:** Write a software pipeline to identify the lane boundaries in a video from a front-facing camera on a car. Use distortion correction, image rectification, color transforms and gradient thresholding. Identify lane curvature and vehicle displacement with means of perspective transform and polynomial fit. Overcome environmental challenges such as shadows and pavement changes.
 - **Keywords:** Python, OpenCV, Sobel Operator, Color Spaces, Polynomial Fit  

### [P5 - Vehicle Detection and Tracking](./Term1/term1_project5_vehicle_detection)
 - **Summary:** Create a vehicle detection and tracking pipeline with OpenCV. Use techniques like 'histogram of oriented gradients' (HOG) and train a classifier (e.g. support vector machines (SVM)) to identify cars. Implement the model in a pipeline. Use sliding windows to detect cars on video data from an automotive camera taken during highway driving. Use heat-map technique to combine overlapping detections and remove false positives.
 - **Keywords:** Python, Object Detection and Tracking, Linear SVC, SVC, Logistic Regression, MLP Classifier, Ensemble Classifier (Ada Boost, Bagging), Grid Search, Hard Negativ Minig, HOG, Sliding Window, Heatmap, False Positives  

---

## Term 2: Sensor Fusion, Localization and Control

---

![term2](./assets/term2.jpg)

|[Getting Started for Term 2](./term2_How_to_get_started)        |[![T2P6](./term2_project6_extended_kalman_filters/results/Extended_Kalman_Filters_V01.gif)](https://drive.google.com/open?id=1fBMSefw1EDetCwyycY5tPYXKwe1AOi4H)<br>**Project 6:<br>Extended Kalman Filters**<br>[Code](./term2_project6_extended_kalman_filters)| [![T2P7](./term2_project7_unscented_kalman_filters/results/Unscented_Kalman_Filter.gif)](https://drive.google.com/open?id=1fBMSefw1EDetCwyycY5tPYXKwe1AOi4H)<br>**Project 7:<br>Unscented Kalman Filters**<br>[Code](./term2_project7_unscented_kalman_filters)|
| :---:         |     :---:      |          :---: |
|[![T2P8](./term2_project8_particle_filter_kidnapped_vehicle/results/particle_filter_kidnapped_vehicle.gif)](https://drive.google.com/open?id=1fBMSefw1EDetCwyycY5tPYXKwe1AOi4H)<br>**Project 8:<br>Particle Filer - Kidnapped Vehicle**<br>[Code](./term2_project8_particle_filter_kidnapped_vehicle)|[![T2P9](./term2_project9_PID_controller/results/PID_controller_simulator_01.gif)](https://drive.google.com/open?id=1fBMSefw1EDetCwyycY5tPYXKwe1AOi4H)<br>**Project 9:<br>PID Controller** <br>[Code](./term2_project9_PID_controller)|[![T2P10](./term2_project10_Model_Predictive_Control/results/Model_Predictive_Control.gif)](https://drive.google.com/open?id=1fBMSefw1EDetCwyycY5tPYXKwe1AOi4H)<br>**Project 10:<br>Model Predictive Control** <br>[Code](./term2_project10_Model_Predictive_Control)|

---


### [P6 - Extended Kalman Filter](./Term2/term2_project6_extended_kalman_filters)
 - **Summary:** Implement the extended Kalman filter in C++. Simulated lidar and radar measurements are used to track a bicycle's position and velocity that travels around your vehicle.
 - **Keywords:** C++, Kalman Filter, CV motion model, Sensor fusion, Lidar, Radar

### [P7 - Unscented Kalman Filter](./Term2/term2_project7_unscented_kalman_filters)
 - **Summary:**  Utilize an Unscented Kalman Filter to estimate the state of a moving object of interest with noisy lidar and radar measurements. A CTRV motion model, lidar measurements and radar measurements are used to track the bicycle's position and velocity. A consistency check with Normalized Innovation Squared (NIS) values is done. 
 - **Keywords:** C++, Unscented Kalman Filter, CTRV motion model, Sigma Points, Consistency Check, NIS

### [P8 - Kidnapped Vehicle](./Term2/term2_project8_particle_filter_kidnapped_vehicle)
 - **Summary:** Your robot has been kidnapped and transported to a new location! Luckily it has a map of this location, a (noisy) GPS estimate of its initial location, and lots of (noisy) sensor and control data. In this project you will implement a 2 dimensional particle filter in C++. Your particle filter will be given a map and some initial localization information (analogous to what a GPS would provide). At each time step your filter will also get observation and control data.
 - **Keywords:** C++, Particle Filter

### [P9 - PID Control](./Term2/term2_project9_PID_controller)
 - **Summary:** Implement a PID controller for keeping the car on track by appropriately adjusting the steering angle and try to get as near to 100mph by controlling the throttle at the same time.
 - **Keywords:** C++, PID Controller

### [P10 - Model Predictive Control](./Term2/term2_project10_Model_Predictive_Control)
- **Summary:** Implement a  MPC controller for keeping the car on track by appropriately adjusting the steering angle. Differently from previously implemented PID controller, MPC controller has the ability to anticipate future events and can take control actions accordingly. Indeed, future time steps are taking into account while optimizing current time slot.
- **Keywords:** C++, Model Predictive Control (MPC)

---

## Term 3: Path Planning, Concentration and System Integration

---

![term3](./assets/term3.jpg)

|[Getting Started for Term 3](./term3_How_to_get_started)       |[![T3P11](./term3_project11_path_planning/results/SDC_Path_Planning_Project.gif)](./term3_project11_path_planning/results/SDC_Path_Planning_Project.mp4)<br>**Project 11:<br>Path Planning Project**<br>[Code](./term3_project11_path_planning)|[![T3P12](./term3_project12_semantic_segmentation/results/umm_000033.png)](./term3_project12_semantic_segmentation/results/)<br>**Project 12:<br>Semantic Segmentation**<br>[Code](./term3_project12_semantic_segmentation)|
| :---:         |     :---:      |          :---: |
|![T3P13](./term3_project13_functional_safety_plan/img/Full_V_Model.PNG)<br>**Project 13:<br>Functional Safety**<br>[Code](./term3_project13_functional_safety_plan)|<br>**CAPSTONE PROJECT**<br>**System Integration**<br>[Introduction](./term3_capstone_project)|[![T3P14](./term3_project14_capstone_project/results/system_integration_project_320.gif)](./term3_project14_capstone_project/results/system_integration_project.mp4)<br>**Project 14:<br>Programming a Real Self-Driving Car**<br>[Code](./term3_project14_capstone_project)|

---

### [P11 - Path Planning](./Term3/term3_project11_path_planning)
- **Summary:** The goal in this project is to build a path planner that is able to create smooth, safe trajectories for the car to follow. The highway track has other vehicles, all going different speeds, but approximately obeying the 50 MPH speed limit. The car transmits its location, along with its sensor fusion data, which estimates the location of all the vehicles on the same side of the road.
- **Keywords:** C++,  Behavior Planning, Predictions, Cost Functions, Path Planning, Trajectory Planning

### [P12 - Road Segmentation](./Term3/term3_project12_semantic_segmentation)
- **Summary:** Implement the road segmentation using a fully-convolutional network.
- **Keywords:** Python, TensorFlow, Semantic Segmentation

### [P13 - Functionl Safety Plan](./Term3/term3_project13_functional_safety_plan)
- **Summary:** Construct part of a safety case for a lane departure warning feature. This starts with the hazard analysis and risk assessment, and further documentation for functional and technical safety concepts have to be created.
- **Keywords:** Safety Plan, Hazard Analysis and Risk Assessment, Functional Safety Concept, Technical Safety Concept, Software Requirements

### [P14 - CAPSTONE PROJECT - Programming a Real Self-Driving Car](./Term3/term3_project14_capstone_project)
- **Summary:** Programming a Real Self-Driving Car which should stay on a track and stop at traffic lights, if necessary.
- **Keywords:** C++, ROS, CNN, Traffic Light Classification, Path Planning, Simulator & Real Car

## Contributing



## License

**UDACITY-self-driving-car** results are released under the [MIT License](./LICENSE).