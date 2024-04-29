## Import the libraries.
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd

import json

# Get the data here.

import json

with open("movie.json"  , "r+") as f :
    movie_data = json.load(f)

print(movie_data)


