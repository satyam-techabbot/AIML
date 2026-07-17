# **Modern Computer Vision**

--- 

## Image Classification
Image classification is the process of assigning a predefined label to an image based on its visual content.

### Types:
- **Binary Classification**
- **Multiclass Classification**
- **multilabel Classification**
- **Hierarchical Classification**

### Image classification vs Object Localization vs Object Detection

- **Image Classification:** Assigns a single label to the entire image, such as cat, dog, or bird. It typically uses models like CNNs and transfer learning.

- **Object Localization:** Identifies the main object in an image and marks its position using a bounding box.

- **Object Detection:** Combines classification and localization to detect multiple objects in an image, each with its own label and bounding box


### Working
1. **Data Collection and Preprocessing:** A large labeled image dataset is collected and preprocessed through resizing, normalization, and augmentation to improve model robustness.

2. **Feature Extraction:** Traditional methods rely on manual features like edges and textures, while CNNs automatically learn features directly from raw pixel data.

3. **Model Training:** The dataset is split into training and validation sets, and a CNN is trained using backpropagation and gradient descent to minimize prediction error while reducing overfitting.

4. **Evaluation and Testing:** The model is evaluated on unseen data using metrics such as accuracy, precision, and recall to measure performance.

5. **Deployment:** The trained model is deployed for real-time or batch image classification in practical applications.


### Algorithms
Some of the algorithms used for Image Classification are:

- **Supervised Learning:** 
Labeled datasets where each image has a known class. Algorithms like SVM and Decision Trees learn to predict labels for new images based on these examples.

- **Unsupervised Learning:** 
When image labels are unavailable, techniques such as clustering and autoencoders group or represent images based on visual similarities and patterns without predefined categories.

- **Deep Learning:** 
CNN automatically learn complex features from raw pixel data improving accuracy over traditional methods.

- **Transfer Learning:** 
Transfer Learning uses pre-trained CNN models and fine tunes them for specific classification tasks reducing training time and resources and achieving high accuracy even with smaller datasets.


### Evaluation Metrics
1. **Accuracy:** The overall percentage of correctly classified images is called Accuracy.

2. **Precision:** How many of the images predicted as a certain class are actually correct is calculated using Precision.

3. **Recall:** The proportion of actual images of a class that were correctly identified is called Recall.

4. **F1-Score:** The harmonic mean of precision and recall, balancing both metrics is called F1 Score.

5. **Confusion Matrix:** A tabular summary showing correct and incorrect predictions for each class is called Confusion Matrix.


### Applications
- Medical Imaging
- Autonomous Vehicles
- Facial Recognition
- Retail and E-commerce
- Environmental Monitoring

--- 

## Object Detection
Object Detection is a computer vision task that identifies and locates multiple objects within an image or video.

### Types

- **Image Classification:** Assigns a single label to the entire image based on its content. It determines what is present in the image but does not indicate the object's location.

- **Object Localization:** Identifies an object and determines its position within the image by drawing a bounding box around it.

- **Object Detection:** Combines image classification and localization to identify multiple objects in an image, assign labels to them, and provide their locations using bounding boxes.


### Working
1. **Input Image:** The process begins with an input image or video frame.
2. **Pre-processing:** The image is resized, normalized, or transformed into a suitable format for the model.
3. **Feature Extraction:** Important visual features are extracted to identify object patterns.
4. **Classification:** Detected regions are classified into predefined object categories.
5. **Localization:** Bounding boxes are generated to determine the location of each object.
6. **Non-Maximum Suppression (NMS):** Overlapping bounding boxes are filtered to retain the most accurate detections.
7. **Output:** The final image is displayed with labeled bounding boxes around the detected objects.


### Deep Learning Methods for Object Detection
Object detection methods are broadly classified into two categories:

1. **Two-Stage Detectors** :
These methods first generate potential object regions and then classify them.

    - **R-CNN(Region-Based Convolutional Neural Networks):** Uses selective search to generate region proposals and classifies each region using a CNN.
    - **Fast R-CNN:** Processes the entire image once and uses ROI pooling for classification and localization.
    - **Faster R-CNN:** Introduces a Region Proposal Network (RPN) for faster and more accurate region generation.

2. **Single-Stage Detectors**
These methods perform object localization and classification in a single pass, making them faster.

    - **SSD (Single Shot MultiBox Detector):** Predicts bounding boxes and class probabilities directly from feature maps.
    - **YOLO (You Only Look Once):** Divides the image into a grid and predicts bounding boxes and class probabilities in a single evaluation.


### Applications
- Autonomous Vehicles
- Security and Surveillance
- Healthcare
- Retail
- Robotics


--- 
## Image Segmentation (U-Net, Mask R-CNN)
Image Segmentation is a computer vision technique used to divide an image into multiple segments or regions, making it easier to analyze and understand specific parts of the image.


### Types of Image Segmentation

1. **Semantic Segmentation**
    - Involves assigning a class label to every pixel in an image based on shared characteristics such as colour, texture and shape.
    - This method treats all pixels belonging to the same class as identical without distinguishing between individual objects.
    - For example: In an image with multiple trees all pixels corresponding to any tree would be labelled as "tree" regardless of how many trees appear in the image.

2. **Instance segmentation**
    - Instance Segmentation extends semantic segmentation by not only labelling colour of each pixel but also distinguishing between individual objects of the same class.
    - This approach identifies each object of the same class as a unique instance.

3. Panoptic Segmentation
    - Panoptic segmentation combines both semantic and instance segmentation techniques providing a complete image analysis.
    - It assigns a class label to every pixel and also detects individual objects. This combines both broad categories and detailed object boundaries simultaneously.
    - For example: In a traffic scene it would label all pedestrians and cars which is semantic segmentation while also outlining the location of each individual person and car which is instance segmentation





--- 

## Pose Estimation


--- 

## OCR



--- 

## Face Recognition


--- 

## Tracking


--- 

## Vision Transformers (ViT)



--- 

## Multimodal models (e.g. CLIP)



--- 

## Diffusion models

https://www.geeksforgeeks.org/artificial-intelligence/diffusion-models-in-machine-learning/

--- 

## 3D Vision


--- 

## SLAM
**SLAM (Simultaneous Localization and Mapping)** is the process by which a robot:

1. **Determines its own position** (Localization).
2. **Builds a map** of an unknown environment (Mapping).

Both tasks occur **simultaneously**, because:

* A robot needs a map to know where it is.
* It also needs to know where it is to create the map.

This creates a "chicken-and-egg" problem that SLAM solves.

---

### Why is SLAM Important?

SLAM enables autonomous robots to operate in environments where:

* GPS is unavailable or unreliable.
* No pre-existing map exists.
* The environment changes over time.

#### Applications

* Autonomous Mobile Robots (AMRs)
* Automated Guided Vehicles (AGVs)
* Robot vacuum cleaners
* Warehouse robots
* Delivery robots
* Autonomous vehicles
* Drones

---

### Two Main Components of SLAM

#### 1. Localization

Localization answers:

> **"Where am I?"**

The robot estimates its **pose**, which includes:

* Position (x, y, z)
* Orientation (roll, pitch, yaw)

It uses sensors such as:

* LiDAR
* Cameras
* IMU
* GPS (when available)
* Wheel encoders

---

#### 2. Mapping

Mapping answers:

> **"What does the environment look like?"**

The robot:

* Collects sensor measurements.
* Detects important features.
* Builds a map while moving.

Maps may include:

* Walls
* Corners
* Doors
* Obstacles
* Objects

---

### Why Localization and Mapping Depend on Each Other

Without localization:

* Sensor data cannot be placed correctly on a map.

Without a map:

* The robot cannot determine where it is.

Therefore, both processes must continuously improve each other.

---

# General SLAM Workflow

1. Robot starts moving.
2. Sensors observe the environment.
3. Detect distinctive features.
4. Estimate robot movement.
5. Update robot position.
6. Add new observations to the map.
7. Repeat continuously.

---

### Sensors Used in SLAM

#### LiDAR

Measures distances using laser pulses.

Advantages:

* Accurate distance measurements
* Works in darkness
* Produces detailed 3D point clouds

Disadvantages:

* Higher cost
* Can struggle with highly reflective or transparent surfaces

---

#### Cameras

Capture visual information.

Advantages:

* Rich color and texture information
* Low cost

Disadvantages:

* Sensitive to lighting conditions
* Challenging in low-light environments

---

#### IMU (Inertial Measurement Unit)

Measures:

* Acceleration
* Angular velocity

Advantages:

* Fast motion estimation
* Helps during rapid movements

Disadvantages:

* Errors accumulate over time (drift)

---

#### GPS

Useful mainly outdoors.

Advantages:

* Provides global position

Limitations:

* Poor performance indoors
* Insufficient precision for many robotic tasks

---

### Types of SLAM

#### 1. LiDAR SLAM

Uses laser scans to create maps.

Best for:

* Warehouses
* Autonomous vehicles
* Outdoor robotics

Pros:

* High accuracy
* Robust in low-light conditions

Cons:

* Expensive sensors

---

#### 2. Visual SLAM (V-SLAM)

Uses one or more cameras.

Pros:

* Affordable
* Rich visual information

Cons:

* Sensitive to lighting and texture

---

#### 3. RGB-D SLAM

Uses cameras that capture:

* Color (RGB)
* Depth

Common in:

* Indoor robots
* Consumer devices

---

#### 4. Visual-Inertial SLAM (VI-SLAM)

Combines:

* Cameras
* IMU

Advantages:

* Better robustness
* Improved motion estimation

---

# Loop Closure

One of the most important concepts in SLAM.

When a robot revisits a previously explored location:

* It recognizes the place.
* Corrects accumulated localization errors.
* Improves map consistency.

Without loop closure:

* Maps gradually become distorted.

---

### Feature Extraction

SLAM identifies recognizable landmarks such as:

* Corners
* Edges
* Poles
* Doors
* Road signs

These stable features help the robot recognize locations over time.

---

### Pose Estimation

**Pose = Position + Orientation**

The robot continuously estimates:

* Where it is
* Which direction it is facing

This estimate is updated using sensor data.

---

### Challenges in SLAM

* Sensor noise
* Dynamic environments (moving people, vehicles)
* Similar-looking locations
* Lighting changes
* Large-scale environments
* Computational complexity
* Drift over long distances

---

### Semantic SLAM

Traditional SLAM builds only geometric maps.

Semantic SLAM adds understanding by recognizing objects such as:

* Cars
* Trees
* People
* Chairs
* Traffic signs

Benefits:

* Richer environment understanding
* Better navigation
* Improved decision-making

---

### Role of Modern Hardware

Recent advances have significantly improved SLAM performance:

* Faster edge computing
* More accurate LiDAR sensors
* Improved cameras
* Better GPUs
* AI-assisted perception

These advancements enable more reliable, real-time autonomous systems.

---

### Key Terms

| Term          | Meaning                                                               |
| ------------- | --------------------------------------------------------------------- |
| Localization  | Estimating the robot's current position                               |
| Mapping       | Creating a representation of the environment                          |
| Pose          | Position + orientation                                                |
| Feature       | Distinct landmark used for localization                               |
| Point Cloud   | Collection of 3D points generated by LiDAR                            |
| Loop Closure  | Recognizing a previously visited location to reduce accumulated error |
| Drift         | Gradual accumulation of localization error                            |
| Semantic SLAM | SLAM enhanced with object recognition and scene understanding         |

---

### Summary

* SLAM enables robots to **localize themselves while simultaneously building a map**.
* It is fundamental for autonomous navigation where GPS or prior maps are unavailable.
* SLAM relies on sensor fusion from LiDAR, cameras, IMUs, and sometimes GPS.
* Different variants (LiDAR, Visual, RGB-D, Visual-Inertial) suit different applications.
* Loop closure and feature extraction are critical for maintaining accurate maps.
* Modern SLAM increasingly incorporates semantic understanding and benefits from advances in sensing and edge computing. 




--- 

## Medical Imaging



--- 

## Video Understanding



--- 

## Generative AI for images



--- 