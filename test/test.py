import requests
import json

url = 'http://localhost:5000/predict'
 
# Load input data from file
with open('test/test_input.json', 'r') as file:
    input_data = json.load(file)

response = requests.post(url, json=input_data)
predictions = response.json()['predictions']
print(predictions)



