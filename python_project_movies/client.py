import argparse

from moviedb import db, sqla


def parse_arguments():
    parser = argparse.ArgumentParser(description="Movie DB CLI client")
    parser.add_argument("filename")

    subparsers = parser.add_subparsers(help='operation')

    # create the parser for the "a" command
    parser_add = subparsers.add_parser('add', help='add a new film entry')
    parser_add.add_argument(
        'title', help='Film title')
    parser_add.add_argument(
        'duration', type=int, help='Film duration [min].')
    parser_add.add_argument(
        'genres', type=str,
        help='Comma-separated list of genres.')
    parser_add.add_argument(
        'rating', type=float, nargs="?",
        help='Film Rating [0-5]')
    parser_add.set_defaults(func=add_film)

    parser_list = subparsers.add_parser('list', help='list films by title')
    parser_list.add_argument(
        'title', nargs="?", help="Filter by title.")
    parser_list.set_defaults(func=list_films)

    args = parser.parse_args()
    return args


def add_film(database, args):
    genres = args.genres.split(",")
    film_to_add = db.Film(args.title, args.duration, genres, args.rating)
    database.store(film_to_add)


def list_films(database, args):
    pass


args = parse_arguments()

# taken from test_db.py
backend = f"sqlite:///{args.filename}"
database = sqla.SqlAlchemyFilmStorage(backend)

args.func(database, args)

"""
if args.command == "list":
    print("<list of films in {fname}>".format(fname=args.filename))
    empty_db = db.MemoryFilmStorage()
    populated_db = db.restore_database(empty_db, args.filename)

    for film in populated_db:
        print(film.to_dict())
"""
