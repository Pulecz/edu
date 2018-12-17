import moviedb.db


def test_film():
    film = moviedb.db.Film("Fantomas", 120, ["action"])
    assert film.title == "Fantomas"


def test_db():
    db = moviedb.db.create_database()
    store_fantomas_to_db(db)

    assert fantomas_in_db(db)
    assert moviedb.db.get_film_by_title(db, "Franta") is None


def store_fantomas_to_db(db):
    film = moviedb.db.Film("Fantomas", 120, ["action"])
    moviedb.db.store_film(db, film)


def fantomas_in_db(db):
    film = moviedb.db.get_film_by_title(db, "Fantomas")
    return film.title == "Fantomas"


def test_film_comparison():
    film1 = moviedb.db.Film("Fantomas", 120, ["action"])
    film2 = moviedb.db.Film("Fantomas", 120, ["action"])
    assert film1 == film2
    assert film1.__eq__(film2)


def test_film_save_and_restore_as_dict():
    film = moviedb.db.Film("Fantomas", 120, ["action"])
    film_as_dict = film.to_dict()
    film_from_dict = moviedb.db.Film.from_dict(film_as_dict)
    assert film == film_from_dict


def test_save_and_restore():
    db = moviedb.db.create_database()
    store_fantomas_to_db(db)

    film = moviedb.db.Film("Fantomas 2", 120, ["action"])
    moviedb.db.store_film(db, film)

    moviedb.db.save_database(db, "dbfile")
    db2 = moviedb.db.restore_database("dbfile")

    assert fantomas_in_db(db2)

    film = moviedb.db.get_film_by_title(db, "Fantomas 2")
    return film.title == "Fantomas 2"



