
import requests
import config
import json

response = requests.get(url= 'https://api.themoviedb.org/3/movie/550?api_key={}'.format(config.api_key))

# Your code here
with open("movie.json", "w") as f:
    json.dump(response.json(), f, indent=4)
