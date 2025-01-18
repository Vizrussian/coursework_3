from constants import COUNT_VIEW
from dao.model.director import Director


# CRUD
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, director_id):
        return self.session.get(Director, director_id)

    def get_page(self, page: int):
        return self.session.query(Director).limit(COUNT_VIEW).offset(page)
