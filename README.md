# WhatMovie

Movie Budget Estimation API. WhatMovie is a complete and ready-to-be-used regression project . It includes 

 - Data fetching through a REST API

 - Exploratory Data Analysis

 - Machine Learning modeling (sci-kit learn)

 - An API development (Flask) in order to productize it.
 
This project is a machine learning-based API built with Flask for estimating movie budgets. It utilizes a trained regression model to predict movie budgets based on various features such as popularity, revenue, runtime, vote average, vote count, and genres. The API provides a convenient way to make predictions for new movie data, making it useful for filmmakers, production companies, and movie enthusiasts.

## Usage:

 - Install necessary dependencies using pip install -r requirements.txt.

 - The data is already in the repo. However if you want to fetch more data you can run **data/movie_discovery.py** , **data/movie_info.py** and **data/flatten_movie_data.py** in that order , from the project directory. To fetch your own data you also have to create a **data/config.py** file to store your credentials like **api_key** and **api_access_token**. To obtain the credentials you can visit the [TMDB website](https://developer.themoviedb.org/)

 - If you are OK with current data and current model that comes with the repo , you can run the following command from the project directory to start the API.

```python
python app/api.py
```

 - If API gets deployed locally **(e.g. , http://localhost:5000)** , you can send **POST** requests to **http://localhost:5000/about/predict** endpoint. To test it you can run the following command from the project directory. It uses the content of the file **test/test_input.json** and sends a **POST** request. You can also consult to **test/test_input.json** to see the accepted fields by the model.

```py
python test/test.py

```

## Contributing:
Contributions are welcome! Open an issue or pull request for improvements.

## License:
This project is licensed under the GNU General Public License.


