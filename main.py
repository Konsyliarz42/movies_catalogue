from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    selected    = request.args.get('list_type', "popular")
    results     = request.args.get('results', "8")
    types       = ['top_rated', 'upcoming', 'popular', 'now_playing']
    quantity    = [4, 8, 12, 16, 20]
    
    try:
        results = int(results)
    except ValueError:
        results = 8

    if selected not in types:
        selected = 'popular'

    movies = tmdb_client.get_movies(results, selected)
    return render_template("homepage.html", movies=movies, selected=selected, types=types, results=results, quantity=quantity)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast)

#================================================================
if __name__ == '__main__':
    app.run(debug=True)