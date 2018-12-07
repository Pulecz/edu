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


def test_save_and_restore():
    db = moviedb.db.create_database()
    store_fantomas_to_db(db)

    moviedb.db.save_database(db, "dbfile")
    db2 = moviedb.db.restore_database("dbfile")

    assert fantomas_in_db(db2)



