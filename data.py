
import requests
import config

response = requests.get(url= 'https://api.themoviedb.org/3/movie/550?api_key={}'.format(config.api_key))

print(response.text)
