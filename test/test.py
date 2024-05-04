import requests

url = 'http://localhost:5000/predict'
data = {
    "adult": False,
    "popularity": 7.2,
    "revenue": 50000000,
    "runtime": 120,
    "vote_average": 7.5,
    "vote_count": 1500,
    "genres_1_name_Adventure": 0,
    "genres_1_name_Animation": 0,
    "genres_1_name_Comedy": 1,
    "genres_1_name_Crime": 0,
    "genres_1_name_Drama": 0,
    "genres_1_name_Family": 0,
    "genres_1_name_Fantasy": 0,
    "genres_1_name_History": 0,
    "genres_1_name_Horror": 0,
    "genres_1_name_Music": 0,
    "genres_1_name_Mystery": 0,
    "genres_1_name_Romance": 0,
    "genres_1_name_Science Fiction": 1,
    "genres_1_name_Thriller": 0,
    "genres_1_name_War": 0,
    "genres_1_name_Western": 0
}

response = requests.post(url, json=data)
predictions = response.json()['predictions']
print(predictions)
