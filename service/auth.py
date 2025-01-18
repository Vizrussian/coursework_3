import calendar
import datetime

import jwt

from constants import SECRET, ALGORITHM
from flask import request, abort
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        users = self.user_service.get_by_name(username)
        right_user = None
        for user in users:
            if self.user_service.compare_password(user.password, password):
                right_user = user
                break

        if right_user is None:
            raise abort(404)

        # user = self.user_service.get_by_name(username)
        # if user is None or len(user) > 2:
        #     raise abort(400)
        #
        # if not self.user_service.compare_password(user[0].password, password):
        #     abort(400)

        data = {
            "username": username,
            "password": password,
            "role": right_user.role
        }

        # 30 minutes for access token
        min30 = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)

        # 180 days for refresh_token
        days_180 = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=180)
        data["exp"] = calendar.timegm(days_180.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)

        return {
            "access token":access_token,
            "refresh token": refresh_token
            }

    def approve_refresh_token(self, token):
        data = jwt.decode(jwt=token, key=SECRET, algorithms=[ALGORITHM])
        username = data.get("username")
        password = data.get("password")
        return self.generate_tokens(username, password, is_refresh=True)