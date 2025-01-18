import os


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.dirname(__file__), 'movies.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
