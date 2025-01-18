from typing import List

from dao.director import DirectorDAO
from dao.model.director import Director


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, genre_id: int) -> List[Director]:
        return self.dao.get_one(genre_id)

    def get_all(self) -> List[Director]:
        return self.dao.get_all()

    def get_page(self, page: int) -> List[Director]:
        return self.dao.get_page(page)
