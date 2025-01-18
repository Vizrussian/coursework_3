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

    # @auth_required
    def get(self):
        try:
            status = request.args.get("status")
            page = request.args.get("page")
            if status:
                movies = movie_service.get_status(status)
            if page:
                if int(page) >= 1:
                    movies = movie_service.get_page(int(page))
            else:
                movies = movie_service.get_all()
            return movies_schema.dump(movies), 200
        except:
            return 'not found', 404


@movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    """The MovieView class handles GET requests for the route /movies/<int:movie_id>"""

    # @auth_required
    def get(self, movie_id: int):
        try:
            movie = movie_service.get_one(movie_id)
            return movie_schema.dump(movie), 200
        except:
            return "", 404
