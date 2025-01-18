from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from decorators import admin_required, auth_required
from implemented import genre_service

genre_ns = Namespace("genres")
movie_schema = GenreSchema()
movies_schema = GenreSchema(many=True)


@genre_ns.route('/')
class MoviesView(Resource):
    """The MoviesView class handles GET requests for the route /movies/"""

    #@auth_required
    def get(self):
        page = request.args.get('page')
        if page:
            genre = genre_service.get_page(page)
        genre = genre_service.get_all()
        return movies_schema.dump(genre), 200


@genre_ns.route("/<int:movie_id>")
class MovieView(Resource):
    """The MovieView class handles GET requests for the route /movies/<int:movie_id>"""

    # @auth_required
    def get(self, movie_id: int):
        genre = genre_service.get_one(movie_id)
        return movie_schema.dump(genre), 200
