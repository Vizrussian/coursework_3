from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object: Config = None) -> Flask:
    """Function for creating a Flask application"""
    application = Flask(__name__)
    if config_object:
        application.config.from_object(config_object)
    else:
        application.config.from_object(Config())
    with application.app_context():
        configure_app(application)
    return application


def configure_app(application: Flask) -> None:
    """Function for creating configurations for a Flask application"""
    db.init_app(application)
    api = Api(application)
    migrate = Migrate(application, db, render_as_batch=True)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)


if __name__ == '__main__':
    app = create_app()
    app.run()
