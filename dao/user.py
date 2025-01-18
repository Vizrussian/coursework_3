from dao.model.user import User


# CRUD
class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        pass

    def get_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).all()

    def update(self, data):
        pass

    def create(self, data: dict):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def delete(self):
        pass
