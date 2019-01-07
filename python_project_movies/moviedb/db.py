import json


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
    def __init__(self, filename):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def store(self, film):
        self._database.append(film)

    def get_by_title(self, title):
        for film in self._database:
            if film.title == title:
                return film


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
