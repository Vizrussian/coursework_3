from flask_restx import Resource, Namespace
from flask import request, jsonify
from dao.model.movie import MovieSchema
from decorators import admin_required, auth_required
from implemented import movie_service

movie_ns = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """The MoviesView class handles GET requests for the route /movies/"""

    @auth_required
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "status": status,
            "page": page,
        }
        movies = movie_service.get_all(filters)
        return movies_schema.dump(movies), 200


@movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    """The MovieView class handles GET requests for the route /movies/<int:movie_id>"""

    # @auth_required
    def get(self, movie_id: int):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200
