from typing import List

from dao.genre import GenreDAO
from dao.model.genre import Genre


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, genre_id: int) -> List[Genre]:
        return self.dao.get_one(genre_id)

    def get_all(self) -> List[Genre]:
        return self.dao.get_all()

    def get_page(self, page: int) -> List[Genre]:
        return self.dao.get_page(page)
