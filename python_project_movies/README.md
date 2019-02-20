# Project movie database

Project for education purposes which should result in web application with database using [flask](http://flask.pocoo.org/) and [sqlalchemy](https://www.sqlalchemy.org/)

# Dependencies
* pytest (for running tests)

# Usage

The tests/test_db.py provide example how to store movies into a database, no client support for that yet

e.g.:
```python
import moviedb.db
# define a movie
film = moviedb.db.Film(" The Shawshank Redemption", 142, ["drama"])
# define a db
db = moviedb.db.MemoryFilmStorage()
# save movie into the db
db.store(film)
# save the db into the db.json
moviedb.db.save_database(db, 'db.json')
```

Then you can read the db using client.py like so:
```sh
$ python movie.db/client.py list db.json
```

Where db.json is json file saved by the example above

# Roadmap
- client supporting reading from sqlite database, not just json
- adding movies via client
- GUI frontend in flask

# Docker image
* Based on latest [alpine](https://hub.docker.com/_/alpine)
* uses czech mirrors
* installs python3 and py3-flask with its dependencies
* copies moviedb folder, server.py and films.json in WORKDIR=/var/www
* exposes default internal port 5000 to containers 5000
* ENTRYPOINT is $(ip a) and flask run --host 0.0.0.0, FLASK_APP is set to server.py
* **currently** it's set to debug the web_app, production should use something like [gunicorn](https://gunicorn.org/) 
