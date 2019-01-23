import sqlalchemy as sqla
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqla.db', echo=True)

Base = declarative_base()


class Film(Base):
    __tablename__ = 'films'

    title = sqla.Column(sqla.String, primary_key=True)
    genres = sqla.Column(sqla.String)
    duration = sqla.Column(sqla.Integer)
    rating = sqla.Column(sqla.Float)


Base.metadata.create_all(engine)

film = Film(title="Fantomas", genres="action,comedy", duration=120)
print(film.title)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()
session.add(film)
session.commit()
