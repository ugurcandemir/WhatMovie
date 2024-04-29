# In this script we fetch a random set of movies based on pupularity to be used later on.
import requests
import config
import json
import time
import os
import json

# We set the url.
url = 'https://api.themoviedb.org/3/discover/movie'

movie_data = []

with open("data/movie_discovery_data.json" , "r") as f :
    movie_discovrey_data = json.load(f)

movie_ids = [each_movie["id"] for each_movie in movie_discovrey_data]

# Loop through movie IDs
for each_movie_id in movie_ids[:500]:  # Adjust the range as needed
    print("Fetching data for movie ID:", each_movie_id)

    params = {
        'api_key': config.api_key  # Provide the API access token as 'api_key'
    }

    # Construct the URL with the movie_id
    movie_url = f"{url}/{each_movie_id}"

    url = f'https://api.themoviedb.org/3/movie/{each_movie_id}?api_key={config.api_key}'


    # Make the request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movie_data.append(data)
        # new_data = data["results"]
      
    else:
        print("Error:", response.status_code)

# We wait not to hit the rate limit.
    time.sleep(0.5)
    


with open(f"data/movie_info.json", "a") as f:
    json.dump(movie_data , f )

    