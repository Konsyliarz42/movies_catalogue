from . import requests, API_KEY, Mock, tmdb_client

#================================================================
def call_tmdb(endpoint):
    url         = f"https://api.themoviedb.org/3/{endpoint}"
    response    = requests.get(url, params={"api_key":API_KEY})

    response.raise_for_status()
    return response.json()

#--------------------------------
def get_movies_list(list_type):
    return call_tmdb(f"movie/{list_type}")

#--------------------------------
def get_single_movie(movie_id):
    return call_tmdb(f"movie/{movie_id}")

#--------------------------------
def get_single_movie_cast(movie_id):
    return call_tmdb(f"movie/{movie_id}/credits")

#================================================================
def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']
    requests_mock    = Mock()

    response                 = requests_mock.return_value.json
    response.return_value    = mock_movies_list

    monkeypatch.setattr("library.tmdb_client.requests.get", requests_mock)

    movies_list = get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list

#--------------------------------
def test_get_single_movie(monkeypatch):
    mock_movie      = 'Movie'
    requests_mock   = Mock()

    response                 = requests_mock.return_value.json
    response.return_value    = mock_movie

    monkeypatch.setattr("library.tmdb_client.requests.get", requests_mock)

    movie = get_single_movie(528085)
    assert movie == mock_movie

#--------------------------------
def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = 'Movie cast'
    requests_mock   = Mock()

    response                 = requests_mock.return_value.json
    response.return_value    = mock_movie_cast

    monkeypatch.setattr("library.tmdb_client.requests.get", requests_mock)

    movie_cast = get_single_movie_cast(528085)
    assert movie_cast == mock_movie_cast

#--------------------------------
def test_get_poster_url(monkeypatch):
    movie_image = "https://image.tmdb.org/t/p/w780/86L8wqGMDbwURPni2t7FQ0nDjsH.jpg"
    image = tmdb_client.get_poster_url("86L8wqGMDbwURPni2t7FQ0nDjsH.jpg", size="w780")
    assert image == movie_image