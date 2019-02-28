import moviedb.db
import moviedb.sqla

import flask
from flask import Flask
from flask import jsonify
app = Flask(__name__)


db_instance = moviedb.sqla.SqlAlchemyFilmStorage(
    "sqlite:///sqla.db")


@app.route('/')
def hello_world():
    all_movies = db_instance.get_all()
    return flask.render_template(
        "sample.html", all_movies=all_movies)


@app.route('/film/<wanted_film>')
def show_film(wanted_film):
    "loads json.database and returns a movie or all in json"
    print('looking for', wanted_film)  # for debug
    # populate a db
    empty_db = moviedb.db.MemoryFilmStorage()
    populated_db = moviedb.db.restore_database(empty_db, 'films.json')

    # define empty dict for result
    result = {}
    if wanted_film == '*':  # get all movies
        list_of_films = [film.to_dict() for film in populated_db]
        # save list_of_films to result with title as a key
        for film in list_of_films:
            result[film["title"]] = film
    else:  # return only wanted_film
        for film in populated_db:
            if film.title == wanted_film:
                result[wanted_film] = film.to_dict()
    # use flask.jsonify for return json
    return jsonify(**result)


app.run('0.0.0.0', 5000, True)
