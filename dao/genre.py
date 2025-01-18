from constants import COUNT_VIEW
from dao.model.genre import Genre

# CRUD
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, director_id):
        return self.session.get(Genre, director_id)

    def get_page(self, page: int):
        return self.session.query(Genre).limit(COUNT_VIEW).offset(page)

    def create(self, data: dict):
        pass

    def update(self, data: dict):
        pass

    def delete(self,data):
        pass