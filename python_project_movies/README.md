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


