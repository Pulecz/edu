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


def create_database():
    return []


def store_film(db, film):
    db.append(film)


def get_film_by_title(db, title):
    for film in db:
        if film.title == title:
            return film


def save_database(db, filename):
    db_of_dicts = [f.to_dict() for f in db]
    with open(filename, "w") as save_file:
        json.dump(db_of_dicts, save_file)
    pass


def restore_database(filename):
    with open(filename, "r") as restore_file:
        db_of_dicts = json.load(restore_file)
    db = [Film.from_dict(d) for d in db_of_dicts]
    return db
