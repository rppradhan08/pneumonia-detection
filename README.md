![GitHub Repo stars](https://img.shields.io/github/stars/rppradhan08/pneumonia-detection)
![GitHub forks](https://img.shields.io/github/forks/rppradhan08/pneumonia-detection?color=green)
![contributors-shield](https://img.shields.io/github/contributors/rppradhan08/pneumonia-detection)
[![LinkedIn][linkedin-shield]](https://in.linkedin.com/in/raj-praveen-pradhan-306625101)

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/rppradhan08/pneumonia-detection">
    <img src="https://raw.githubusercontent.com/rppradhan08/pneumonia-detection/master/images/logo.PNG" alt="Logo" width="200px" height="100px">
  </a>

  <p align="center">
    Pneumonia Detection using CNN
    <br />
    <a href="https://github.com/rppradhan08/pneumonia-detection"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rppradhan08/pneumonia-detection">View Demo</a>
    ·
    <a href="https://github.com/rppradhan08/pneumonia-detection/issues">Report Bug</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Steps involved](#steps-involved)
  - [Tools used](#tools-used)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Data Analysis and Model Building](#data-analysis-and-model-building)
  - [Application Development](#application-development)
- [Usage](#usage)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

<p align="center">
  <img src="https://raw.githubusercontent.com/rppradhan08/pneumonia-detection/master/images/person1661_virus_2872.jpeg" height="250px" width="300px">
</p>
This project uses <a href="https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia">Chest X-Ray dataset</a> from kaggle.
The dataset is organized into 3 folders (train, val & test) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal). These images are used for building an CNN model using keras to detect pneumonia in patients based on X-ray reports. After model building the best performing model is used to build a flask base web application.

### Steps involved

- Reading data from source and preprocessing it using OpenCV.
- Performing data preprocessing before feeding the data to the model.
- Building sequential model architecture using keras.
- Using data augmentating to prevent the model from overfitting during training phase.
- Creating web application using flask to detect Pneumonia upon receiving the preprocessed X-ray.

### Tools used

Following are the tools/frameworks used in developing the application:

- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)
- [Flask](https://palletsprojects.com/p/flask/)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/)

## Getting Started

### Installation

For proper execution of application firstly create an environment, then to install prerequisite libraries execute below command in terminal.

```
pip install -r requirements.txt
```

### Data Analysis and Model Building

Refer `Pneumonia_Detection_CNN.ipynb` to find details regarding data analysis and model building.

Since this is a classification problem, to check model performance `Confusion Matrix` and `Classification Report` are used.

<p align="center">
<b>Confusion Matrix</b><br>
<img src="https://raw.githubusercontent.com/rppradhan08/pneumonia-detection/master/images/cunfusion_mat.png" height="200px">
</p>

### Application Development

After model development, the web application is developed using `flask` which is a python based web-framework. For source code refer `app.py`.

Below are few snapshots of application in use:

- Step 1 Uploading X-Ray
  <p align="center">
    <img src="https://raw.githubusercontent.com/rppradhan08/pneumonia-detection/master/images/home.PNG" height="300px">
  </p>
- Step 2 Displaying Result
  <p align="center">
    <img src="https://raw.githubusercontent.com/rppradhan08/pneumonia-detection/master/images/normal.PNG" height="200px">
  </p>

<!-- CONTACT -->

## Usage

To run this application firstly execute `python app.py`, after which the flask built-in server would start hosting the application at localhost i.e.
`http://127.0.0.1:5000/`

## Contact

Raj Praveen Pradhan - [LinkedIn](https://in.linkedin.com/in/raj-praveen-pradhan-306625101)

Kaggle Kernel: [https://www.kaggle.com/rajpraveenpradhan/keras-based-cnn-model-for-pneumonia-detection](https://www.kaggle.com/rajpraveenpradhan/keras-based-cnn-model-for-pneumonia-detection)
