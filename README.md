![GitHub Repo stars](https://img.shields.io/github/stars/rppradhan08/Car_Price_Prediction)
![GitHub forks](https://img.shields.io/github/forks/rppradhan08/Car_Price_Prediction?color=green)
![contributors-shield](https://img.shields.io/github/contributors/rppradhan08/Car_Price_Prediction)
[![LinkedIn][linkedin-shield]](https://in.linkedin.com/in/raj-praveen-pradhan-306625101)

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/rppradhan08/Car_Price_Prediction">
    <img src="https://raw.githubusercontent.com/rppradhan08/Car_Price_Prediction/master/images/prj_name.PNG" alt="Logo" width="200px" height="40px">
  </a>

  <p align="center">
    Pneumonia Detection using CNN
    <br />
    <a href="https://github.com/rppradhan08/Car_Price_Prediction"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rppradhan08/Car_Price_Prediction">View Demo</a>
    ·
    <a href="https://github.com/rppradhan08/Car_Price_Prediction/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Steps involved](#steps-involved)
  - [Tools used](#tools-used)
  - [Libraries](#libraries)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Data Analysis and Model Selection](#data-analysis-and-model-selection)
  - [Application Development](#application-development)
  - [Model Deployment](#model-deployment)
- [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center">
    <a href="https://carprizpred.herokuapp.com">
        <img src="images/prj_home.PNG" height="35%" width="50%">
    </a>
</p>
This project uses <a href="https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho?select=car+data.csv">vehicle dataset</a> from cardekho to predict car price.
Dataset contains information about used cars listed on www.cardekho.com.

### Steps involved
* Reading data from source and performing EDA
* Performing feature engineering to feed desired data into ML model
* Finding best set of hyper-parameters using Randomized Search CV to train the model
* Evaluating various Regressor ML models using cross-validation and residual plot
* Creating web application using flask to predict car price based on various attributes.
* Finally, deploying the web application on cloud based platform (i.e. Heroku) 

### Tools used
Following are the tools/frameworks used in developing the application:
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [Python](https://www.python.org/)
* [Flask](https://palletsprojects.com/p/flask/)
* [HTML](https://en.wikipedia.org/wiki/HTML)
* [Heroku](https://www.heroku.com/)
  
### Libraries
Below is the list of python libraries used in this project:
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sklearn
import flask
```
## Getting Started

### Installation

To install any of the aforementioned libraries, below command can be written in the Anaconda prompt or terminal :

```
pip install <package_name>
```

### Data Analysis and Model Selection

Refer `Car_Price_Prediction.ipynb` to find details regarding data analysis and model selection.

To check model performance, `Residual plot` and scatter plot between `y_test`-`y_pred` are used.

<p align="center">
<img src="https://raw.githubusercontent.com/rppradhan08/Car_Price_Prediction/master/images/resuidual_plot.png">
</p>

Below are the final metrics obtained for various models that were considered in analysis.

<p align="center">
<img src="https://raw.githubusercontent.com/rppradhan08/Car_Price_Prediction/master/images/model_metrics.PNG" height="150px">
</p>


### Application Development

After model selection, the web application is developed using `flask` which is a python based web-framework. For source code refer `app.py`.

Below are few snapshots of application in use:
* Step 1 Filling attributes related to car
  <p align="center">
    <img src="https://raw.githubusercontent.com/rppradhan08/Car_Price_Prediction/master/images/step_1.PNG" height="300px">
  </p>
* Step 2 Displaying predicted cost 
  <p align="center">
    <img src="https://raw.githubusercontent.com/rppradhan08/Car_Price_Prediction/master/images/step_2.PNG" height="100px">
  </p>

### Model Deployment

Model is deployed on `heroku` which is a cloud based PaaS. 

Application link : https://carprizpred.herokuapp.com/

<!-- CONTACT -->
## Contact

Raj Praveen Pradhan - [LinkedIn](https://in.linkedin.com/in/raj-praveen-pradhan-306625101)

Project Link: [https://github.com/rppradhan08/Car_Price_Prediction](https://github.com/rppradhan08/Car_Price_Prediction)







