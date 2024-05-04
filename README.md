# WhatMovie

Movie Budget Estimation API. WhatMovie is a complete and ready-to-be-used regression project . It includes 

 - Data fetching through a REST API

 - Exploratory Data Analysis

 - Machine Learning modeling (sci-kit learn)

 - An API development (Flask) in order to productize it.
 
This project is a machine learning-based API built with Flask for estimating movie budgets. It utilizes a trained regression model to predict movie budgets based on various features such as popularity, revenue, runtime, vote average, vote count, and genres. The API provides a convenient way to make predictions for new movie data, making it useful for filmmakers, production companies, and movie enthusiasts.

Usage:

Send a POST request to the API endpoint with movie data.
Receive predicted budget estimation as the response.
How to Use:

Clone the repository.
Install necessary dependencies using pip install -r requirements.txt.
Run the Flask app using python app.py.
Send POST requests to the API endpoint http://localhost:5000/predict with movie data in JSON format.