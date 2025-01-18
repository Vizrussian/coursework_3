from flask_restx import Resource, Namespace
from flask import request

from constants import COUNT_VIEW
from dao.model.genre import GenreSchema
from decorators import admin_required, auth_required
from implemented import genre_service

genre_ns = Namespace("genres")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    """The GenresView class handles GET requests for the route /genres/"""

    #@auth_required
    def get(self):
        page = request.args.get('page')
        try:
            if page:
                page = (int(page) - 1) * COUNT_VIEW
                genre = genre_service.get_page(page)
                return genres_schema.dump(genre), 200
            else:
                genre = genre_service.get_all()
                return genres_schema.dump(genre), 200
        except:
            return "", 404


@genre_ns.route("/<int:genre_id>")
class GenreView(Resource):
    """The GenreView class handles GET requests for the route /genres/<int:genre_id>"""

    # @auth_required
    def get(self, genre_id: int):
        try:
            genre = genre_service.get_one(genre_id)
            return genre_schema.dump(genre), 200
        except:
            return "", 404
