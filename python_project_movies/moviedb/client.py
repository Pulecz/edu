import argparse

import db


def parse_arguments():
    parser = argparse.ArgumentParser(description="Movie DB CLI client")
    parser.add_argument("command", choices=["list"], help="What to do with the database.")
    parser.add_argument("filename")

    args = parser.parse_args()

    return args


args = parse_arguments()

if args.command == "list":
    print("<list of films in {fname}>".format(fname=args.filename))
