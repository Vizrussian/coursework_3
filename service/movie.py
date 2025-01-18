from typing import List

from dao.model.movie import Movie
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, movie_id: int) -> List[Movie]:
        return self.dao.get_one(movie_id)

    def get_all(self):
        movies = self.dao.get_all()
        print(movies)
        if len(movies):
            return movies

    def get_status(self, status: str):
        if status == "new":
            return self.dao.get_status()
        else:
            raise ValueError

    def get_page(self, page: int):
        page = page - 1
        return self.dao.get_page(page)

    def create(self, data: dict):
        self.dao.create(data)

    def update(self, data: dict):
        self.dao.update(data)
        return self.dao

    def delete(self, movie_id: int):
        self.dao.delete(movie_id)
