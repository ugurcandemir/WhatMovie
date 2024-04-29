
# In this script we fetch a random set of movies based on pupularity to be used later on.
import requests
import config
import json
import time
import os
import json

# We set the url.
url = 'https://api.themoviedb.org/3/discover/movie'

# We run a for loop here.
for i in range(1 , 100) :


    print( i )


    params = {
        
        'page': i ,
        'sort_by': 'popularity.desc'
    }
    headers = {
        'Authorization': f'Bearer {config.api_access_token}',
        'accept': 'application/json'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        new_data = data["results"]
      
    else:
        print("Error:", response.status_code)

    with open(f"data/movie_data_{i}.json", "a") as f:
        json.dump(new_data , f)

    
# We wait not to hit the rate limit.
    time.sleep(0.5)
    

# Now we read and merge all the data we fetched.
directory = "data"
files = os.listdir(directory)
movie_data_files = [file for file in files if file.startswith("movie_data")]

merged_data = []

# Read and merge data from each file
for file in movie_data_files:
    with open(os.path.join(directory, file), "r") as f:
        data = json.load(f)
        merged_data.extend(data)

# Write the merged data to a new file
output_file = "data/movie_discovery_data.json"
with open(output_file, "w") as f:
    json.dump(merged_data, f)

# Delete the original "movie_data" files
for file in movie_data_files:
    os.remove(os.path.join(directory, file))

print("Merged data written to 'movie_discovery_data.json' and original 'movie_data' files deleted.")

