


import requests

response = requests.get(url= 'https://api.themoviedb.org/3/movie/550?api_key=0a0a74a1434517653eb9680e6a14e6fb')

print(response.text)