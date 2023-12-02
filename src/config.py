import os

SECRET_KEY = 'abc'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

SQLALCHEMY_TRACK_MODIFICATIONS = False