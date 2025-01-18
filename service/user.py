import hashlib

from constants import PWD_HASH_SALT, PWD_HASH_ITERATION
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create(self, data: dict):
        data["password"] = self.create_hash(data["password"])
        self.dao.create(data)

    def get_by_email(self, email: str):
        return self.dao.get_by_email(email)

    def create_hash(self, password: str):
        return hashlib.pbkdf2_hmac(
            "sha-256",
            password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATION
        ).decode("utf-8", "ignore")

    def get_all(self):
        return self.dao.get_all()

    def update(self, data: dict):
        self.dao.update(data)

    def delete(self):
        pass