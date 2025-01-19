import calendar
import datetime
import hashlib

import jwt

from constants import SECRET, ALGORITHM, PWD_HASH_SALT, PWD_HASH_ITERATION
from flask import abort

from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    # def create(self, data: dict):
    #     data["password"] = self.user_service.create_hash(data["password"])
    #     self.user_service.create(data)

    def generate_tokens(self, user_data: dict):

        # 30 minutes for access token
        min30 = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
        user_data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(user_data, SECRET, algorithm=ALGORITHM)

        # 180 days for refresh_token
        days_180 = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=180)
        user_data["exp"] = calendar.timegm(days_180.timetuple())
        refresh_token = jwt.encode(user_data, SECRET, algorithm=ALGORITHM)

        return {
            "access token": access_token,
            "refresh token": refresh_token
        }

    def get_by_email(self,emai: str):
        return self.user_service.get_by_email(emai)

    def log_in(self, email: str, password: str):
        user = self.user_service.get_by_email(email)
        # if not user:
        #     raise abort(404)
        #
        if self.compare_password(password, user.password):
            return True
        else:
            return False

        # token = compare_password(user.password, password)

    def compare_password(self, password_from_user, password):
        password_from_user = self.user_service.create_hash(password_from_user)
        return password_from_user == password

    def approve_refresh_token(self, token):
        data = jwt.decode(jwt=token, key=SECRET, algorithms=[ALGORITHM])
        username = data.get("username")
        password = data.get("password")
        return self.generate_tokens(username, password, is_refresh=True)
