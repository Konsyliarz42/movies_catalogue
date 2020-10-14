import requests

API_KEY = "ee51b619aa97bfee8dc90c91dda1954f"

def get_movies_list(type_list):
    endpoint    = f"https://api.themoviedb.org/3/movie/{type_list}"
    response    = requests.get(endpoint, params={"api_key":API_KEY})

    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, type_list):
    data = get_movies_list(type_list)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint    = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response    = requests.get(endpoint, params={"api_key":API_KEY})

    return response.json()
    

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response    = requests.get(endpoint, params={"api_key":API_KEY})

    return response.json()["cast"]

