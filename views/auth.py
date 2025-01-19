from flask import request, jsonify
from flask_restx import Namespace, Resource

from decorators import admin_required, auth_required
from implemented import auth_service, user_service

auth_ns = Namespace("auth")


@auth_ns.route('/register')
class AuthRegisterView(Resource):
    """The AuthRegisterView class handles GET requests for the route /auth/register"""

    def post(self):
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)
        role = data.get("role", "user")
        if None in [email, password]:
            return jsonify({"error": "Missing required fields"}), 400
        user_data = {
            "email": email,
            "password": password,
            "role": role
        }
        user_service.create(data)
        tokens = auth_service.generate_tokens(user_data)
        return tokens

@auth_ns.route('/login')
class AuthLoginView(Resource):
    """The AuthLoginView class handles GET requests for the route /auth/login"""

    def post(self):
        try:
            data = request.json
            email = data.get("email", None)
            password = data.get("password", None)
            if None in [email, password]:
                return "", 400
            # не работает сравнение паролей
            if auth_service.log_in(email, password):
                return "Log in success", 200
            else:
                return "email or password incorrect", 404
        except Exception as e:
            return f"Erorr: {e}", 400

    def put(self):
        tokens = request.json
        access = tokens.get("access_token", None)
        refresh = tokens.get("refresh_token", None)
        if None in [access, refresh]:
            return "", 400

        new_tokens = auth_service.approve_refresh_token()
        return new_tokens
