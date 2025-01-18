import jwt
from constants import SECRET, ALGORITHM
from flask import request, abort


def auth_required(func):
    """Decorator for authorization verification"""

    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers["Authorization"]
        tokens = data.split("Bearer ")[-1]
        try:
            res = jwt.decode(tokens, SECRET, algorithms=[ALGORITHM])
            print(res)
        except Exception as e:
            print("Some decode error", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """Decorator for authorization and user role verification"""

    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers["Authorization"]
        tokens = data.split("Bearer ")[-1]
        role = None
        try:
            user = jwt.decode(tokens, SECRET, algorithms=[ALGORITHM])
            role = user.get("role", "user")
            print(user)
            print(role)
        except Exception as e:
            print("Some decode error", e)
            abort(401)

        if role != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
