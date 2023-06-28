## Import the libraries.
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd

# Get the data here.

import json

with open("movie.json"  , "r+") as f :
    data = json.load(f)


# Opening JSON file
# f = open('data.json')
  
# returns JSON object as 
# a dictionary

  
# Iterating through the json
# list
# for i in data['emp_details']:
    # print(i)
  
# Closing file
# f.close()d

# Fit the model.
