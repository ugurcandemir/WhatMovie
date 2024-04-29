
import tmdbv3api as mdb
db = mdb.TMDb()
db.api_key = 'API KEY'

# get movies
mov = db.Movie()

# get popular movies
movies = mov.popular()

# get movie details
movies[0].id
movies[0].title
movies[0].overview
movies[0].vote_average

# Get TV shows

tvShow = db.TV()
show = tvShow.search('Game of Thrones')
show[0].name
show[0].overview

# Fıt the model.
