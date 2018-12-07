

class Film(object):
    def __init__(self, title, duration, genres, rating=None):
        self.title = title
        self.duration = duration
        self.genres = set(genres)
        self.rating = rating


def create_database():
    return []


def store_film(db, film):
    db.append(film)


def get_film_by_title(db, title):
    for film in db:
        if film.title == title:
            return film


def save_database(db, filename):
    pass


def restore_database(filename):
    return []
