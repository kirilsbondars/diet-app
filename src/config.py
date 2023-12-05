import os

SECRET_KEY = 'giiwch9xG1HZ4HHGLYI0OD7GAazeaWZL'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:dietapp1-@localhost/diet_app'

SQLALCHEMY_TRACK_MODIFICATIONS = False