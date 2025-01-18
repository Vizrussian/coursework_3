from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from dao.movies import MovieDAO
from dao.user import UserDAO
from service.auth import AuthService
from service.directors import DirectorService
from service.genres import GenreService
from service.movies import MovieService
from service.user import UserService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
