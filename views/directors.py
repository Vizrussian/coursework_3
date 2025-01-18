from flask_restx import Resource, Namespace
from flask import request, jsonify

from constants import COUNT_VIEW
from dao.model.director import DirectorSchema
from decorators import admin_required, auth_required
from implemented import director_service

director_ns = Namespace("directors")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    """The DirectorsView class handles GET requests for the route /diretors/"""

   # @auth_required
    def get(self):
        page = request.args.get("page")
        try:
            if page:
                page = (int(page) - 1) * COUNT_VIEW
                directors = director_service.get_page(page)
                return directors_schema.dump(directors), 200
            else:
                directors = director_service.get_all()
                return directors_schema.dump(directors), 200
        except:
            return "", 404


@director_ns.route("/<int:director_id>")
class DirectorView(Resource):
    """The DirectorView class handles GET requests for the route /directors/<int:director_id>"""

    # @auth_required
    def get(self, director_id: int):
        try:
            directors = director_service.get_one(director_id)
            return director_schema.dump(directors), 200
        except:
            return "", 404
