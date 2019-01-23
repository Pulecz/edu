import json
import sqlite3


class Film(object):
    def __init__(self, title, duration, genres, rating=None):
        self.title = title
        self.duration = duration
        self.genres = set(genres)
        self.rating = rating

    def to_dict(self):
        result = dict()
        result["title"] = self.title
        result["duration"] = self.duration
        result["genres"] = list(self.genres)
        result["rating"] = self.rating
        return result

    def __eq__(self, rhs):
        if self.title != rhs.title:
            return False
        if self.duration != rhs.duration:
            return False
        if self.genres != rhs.genres:
            return False
        if self.rating != rhs.rating:
            return False
        return True

    @staticmethod
    def from_dict(d):
        result = Film(
            d["title"], d["duration"],
            d["genres"], d["rating"])
        return result


class FilmStorage(object):
    def store(self, film):
        raise NotImplementedError()

    def get_by_title(self, title):
        raise NotImplementedError()


class MemoryFilmStorage(FilmStorage):
    def __init__(self):
        self._database = []

    def __iter__(self):
        return self._database.__iter__()

    def store(self, film):
        self._database.append(film)

    def get_by_title(self, title):
        for film in self._database:
            if film.title == title:
                return film


class SqliteFilmStorage(FilmStorage):
    def __init__(self):
        self._conn = sqlite3.connect('dbfile.db')
        self._c = self._conn.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS movies (
            title TEXT,
            duration INTEGER,
            genres TEXT,
            rating REAL
            )
        '''
        self._c.execute(sql)

    def __iter__(self):
        return self._c.__iter__()

    def store(self, film):
        sql = '''
        INSERT INTO movies (
            title,
            duration,
            genres,
            rating
        ) VALUES (?,?,?,?)
        '''
        film_dict = film.to_dict()
        film_dict["genres"] = ",".join(film_dict["genres"])
        values = tuple(film_dict.values())
        self._c.execute(sql, values)
        self._conn.commit()

    def get_by_title(self, title):
        self._c.row_factory = sqlite3.Row

        sql = '''
        SELECT * FROM movies
        WHERE title = ?
        '''
        self._c.execute(sql, (title, ))
        data = self._c.fetchone()

        if not data:
            return None
        else:
            genres = data['genres'].split(",")
            return Film(data['title'], data['duration'], genres, data['rating'])

    def close(self):
        self._c.close()


def save_database(db, filename):
    db_of_dicts = [f.to_dict() for f in db]
    with open(filename, "w") as save_file:
        json.dump(db_of_dicts, save_file)


def restore_database(empty_db, filename):
    with open(filename, "r") as restore_file:
        db_of_dicts = json.load(restore_file)

    for d in db_of_dicts:
        f = Film.from_dict(d)
        empty_db.store(f)

    return empty_db
