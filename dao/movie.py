from typing import List
from dao.model.movie import Movie
from sqlalchemy import desc

from constants import COUNT_VIEW


# CRUD
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self) -> List[Movie]:
        return self.session.query(Movie).all()

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def get_status(self):
        movies = self.session.query(Movie).order_by(desc(Movie.year))
        return movies.all()

    def get_page(self, page: int):
        movies = self.session.query(Movie).limit(COUNT_VIEW).offset(page * COUNT_VIEW)
        return movies.all()

    def create(self, data: dict):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()
        return movie

    def update(self, data: dict):
        movie = self.get_one(data.get("id"))
        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]

        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def delete(self, movie_id: int):
        movie = self.get_one(movie_id)

        self.session.delete(movie)
        self.session.commit()
        self.session.close()
